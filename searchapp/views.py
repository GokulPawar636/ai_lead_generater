import requests
import re
import csv
from django.shortcuts import render
from django.http import HttpResponse


# =========================
# 📧 Extract Email
# =========================
def extract_email_from_website(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}

        res = requests.get(url, headers=headers, timeout=5)
        emails = re.findall(r"[\w\.-]+@[\w\.-]+", res.text)

        # Try contact page if not found
        if not emails:
            contact_url = url.rstrip("/") + "/contact"
            res = requests.get(contact_url, headers=headers, timeout=5)
            emails = re.findall(r"[\w\.-]+@[\w\.-]+", res.text)

        return emails[0] if emails else "Not Available"

    except:
        return "Not Available"


# =========================
# 🔍 Main Search View
# =========================
def search_view(request):
    query = request.GET.get('query')
    export = request.GET.get('export')
    results = []

    if query:
        api_key = "4208e37182f77817183a43202820dd060342f210ac4378c62f06f374a7b7bc1c"

        search_query = f"{query} suppliers near me"

        start = 0

        # 🔥 Fetch until we get at least 20 valid leads
        while len(results) < 20:

            params = {
                "engine": "google_maps",
                "q": search_query,
                "api_key": api_key,
                "start": start,
                "hl": "en",
                "gl": "in"
            }

            try:
                response = requests.get(
                    "https://serpapi.com/search.json",
                    params=params,
                    timeout=10
                )

                print("STATUS:", response.status_code)

                data = response.json()

            except Exception as e:
                print("ERROR:", e)
                break

            local_results = data.get("local_results", [])

            # ❌ Stop if no more data
            if not local_results:
                break

            for place in local_results:

                # Skip incomplete data
                if not place.get("phone") or not place.get("title"):
                    continue

                website = place.get("website", "")
                email = extract_email_from_website(website) if website else "Not Available"

                rating = place.get("rating", 0)
                reviews = place.get("reviews", 0)

                # Lead Quality Score
                import math

                score = (
                    (rating or 0) * 2 +
                    math.log((reviews or 1), 10) +
                    (2 if email != "Not Available" else 0) +
                    (1 if website else 0)
                )

                results.append({
                    "name": place.get("title"),
                    "address": place.get("address"),
                    "phone": place.get("phone"),
                    "email": email,
                    "website": website,
                    "score": round(score, 1),
                })

            start += 10

            # ⚠️ Safety limit (avoid too many API calls)
            if start >= 50:
                break

        # =========================
        # 🔁 Remove duplicates
        # =========================
        unique_results = []
        seen = set()

        for r in results:
            if r["name"] not in seen:
                unique_results.append(r)
                seen.add(r["name"])

        # Sort best leads first
        results = sorted(unique_results, key=lambda x: x["score"], reverse=True)

    # =========================
    # 📥 EXPORT CSV
    # =========================
    if export == "csv" and results:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="leads.csv"'

        writer = csv.writer(response)
        writer.writerow(["Company", "Phone", "Email", "Location", "Website", "Score"])

        for r in results:
            writer.writerow([
                r["name"],
                r["phone"],
                r["email"],
                r["address"],
                r["website"],
                r["score"]
            ])

        return response

    # =========================
    # 📥 EXPORT EXCEL
    # =========================
    if export == "excel" and results:
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="leads.xls"'

        writer = csv.writer(response)
        writer.writerow(["Company", "Phone", "Email", "Location", "Website", "Score"])

        for r in results:
            writer.writerow([
                r["name"],
                r["phone"],
                r["email"],
                r["address"],
                r["website"],
                r["score"]
            ])

        return response

    # =========================
    # 🎨 Render Page
    # =========================
    return render(request, "index.html", {
        "results": results,
        "query": query
    })