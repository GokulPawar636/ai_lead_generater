# 🤖 AI Lead Generator (Django + SerpAPI)

## 📌 Overview

AI Lead Generator is a web-based application that helps users **find business leads** based on a product or service keyword (e.g., *TDS Meter, Mobile Shop, Water Purifier*).

The system uses **Google Maps data via SerpAPI** and applies **intelligent filtering + scoring** to generate high-quality leads including:

* Company Name
* Phone Number
* Email Address
* Location (with Google Maps link)
* Website
* Lead Quality Score

---

## 🚀 Features

### 🔍 Smart Lead Search

* Converts user input into **business-focused queries**
* Example:
  `TDS Meter → TDS Meter suppliers near me`

---

### 📊 Lead Data Extraction

* Fetches real-time business data using **SerpAPI (Google Maps)**
* Extracts:

  * Company Name
  * Phone Number
  * Address
  * Website

---

### 📧 Email Extraction

* Scrapes business websites
* Automatically checks:

  * Homepage
  * `/contact` page

---

### 🧠 Lead Quality Scoring

Each lead is ranked using a scoring system:

```
Score = (Rating × 2) + log10(Reviews) + Email Bonus + Website Bonus
```

✔ Helps prioritize **high-value leads**
✔ Avoids bias from very large review counts

---

### 📈 Pagination Handling (Unlimited Fetch)

* Fetches multiple pages using `start` parameter
* Continues until:

  * Minimum leads achieved (≥20)
  * OR no more data available
* Removes duplicates automatically

---

### 📥 Export Functionality

* Download leads as:

  * CSV file
  * Excel (.xls) file

---

### 🎨 Modern UI/UX

* Glassmorphism design
* Background image with overlay
* Responsive layout (4 cards per row)
* Clean professional structure
* Google Maps clickable locations

---

## 🏗️ Tech Stack

| Technology  | Usage                |
| ----------- | -------------------- |
| Django      | Backend framework    |
| Python      | Logic & API handling |
| SerpAPI     | Google Maps data     |
| HTML5       | Structure            |
| CSS3        | Styling              |
| Bootstrap 5 | Responsive layout    |
| JavaScript  | UI interactivity     |
| Requests    | API calls            |
| Regex       | Email extraction     |

---

## 🔄 Application Flow

1. User enters product keyword
2. Query is transformed into business search
3. SerpAPI fetches Google Maps results
4. System loops through multiple pages
5. Filters valid businesses
6. Extracts emails from websites
7. Calculates Lead Quality Score
8. Removes duplicates
9. Displays results in UI
10. User can export leads

---

## 🧠 Lead Quality Score Logic

| Factor              | Purpose           |
| ------------------- | ----------------- |
| Rating              | Business quality  |
| Reviews (log scale) | Popularity        |
| Email presence      | Contact readiness |
| Website presence    | Professionalism   |

---

## ✅ Advantages

✔ Generates **real business leads automatically**
✔ Works with **any product/service keyword**
✔ Intelligent ranking (AI-like behavior)
✔ Export-ready data (CSV/Excel)
✔ Clean and responsive UI
✔ Uses real-time Google Maps data
✔ Email extraction adds extra value

---

## ⚠️ Limitations

❌ Depends on **SerpAPI limits (free tier restrictions)**
❌ Some businesses may not have:

* Website
* Email
* Phone number

❌ Email scraping may fail due to:

* Dynamic websites
* Hidden emails

❌ Not truly AI (rule-based scoring system)
❌ Slower performance due to sequential API calls

---

## 🔧 Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/your-username/ai-lead-generator.git
cd ai-lead-generator
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add SerpAPI Key

In `views.py`:

```python
api_key = "YOUR_SERPAPI_KEY"
```

### 4. Run Server

```bash
python manage.py runserver
```

### 5. Open Browser

```
http://127.0.0.1:8000/
```

---

## 📌 Example Searches

* `Mobile shop`
* `Water purifier suppliers`
* `Electronics store`
* `Steel suppliers`
* `Construction companies`

---

## 🚀 Future Improvements

* 📍 City-based search filter
* 📊 Dashboard with analytics
* ⚡ Faster scraping (async/multithreading)
* 🤖 ML-based lead scoring
* 🔐 User login system
* 📧 Email verification system
* 🌐 Deployment (Render / AWS / Hostinger)

---

## 👨‍💻 Author

Developed as part of an **AI Lead Generator MVP assignment**
Focused on combining:

* Web scraping
* API integration
* Data filtering
* UI/UX design

---

## ⭐ Conclusion

This project demonstrates how to build a **real-world lead generation system** using:

* API integration
* Data processing
* Smart ranking
* Clean UI

It can be extended into a **full SaaS product** for B2B lead generation.

---
