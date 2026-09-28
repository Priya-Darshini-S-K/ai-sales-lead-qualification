# 🤖 AI Sales Lead Qualification Agent

An AI-powered application that analyses sales leads from a CSV file and helps sales teams identify which leads need attention first.

## 🎯 Project Overview

The system processes sales lead data, calculates a qualification score out of **100**, assigns a priority status, and generates an AI-based summary with a suggested next action.

### 🔄 Workflow

```text
CSV Upload
    ↓
Data Analysis
    ↓
Qualification Score
    ↓
Ready / Interested / Later
    ↓
AI Summary
    ↓
Next Action
    ↓
Dashboard
```

## ⚙️ Qualification Criteria

| Criteria       |   Score |
| -------------- | ------: |
| Budget Fit     |      25 |
| Timeline       |      20 |
| Need Fit       |      20 |
| Decision Maker |      15 |
| Engagement     |      10 |
| Company Fit    |      10 |
| **Total**      | **100** |

### 📌 Status

* 🟢 **Ready:** 75–100
* 🟡 **Interested:** 50–74
* ⚪ **Later:** 0–49

## 🚀 Features

* Upload CSV sales leads
* Analyse multiple leads
* Calculate qualification scores
* Classify lead status
* Generate AI summaries
* Suggest next sales actions
* Interactive Streamlit dashboard

## 🛠️ Tech Stack

**Python • Pandas • Streamlit • LLM API • CSV • GitHub**

## 📂 Dataset

The project uses `realistic_100_sales_leads.csv` containing **100 sample sales leads**.

## 💻 Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 🎯 Goal

To build a practical AI-based solution that combines **data processing, business logic, and LLM capabilities** to support sales lead qualification and prioritization.

## 👩‍💻 Author

**Priyadarshini.S**
Final year B.Com Information Technology Student
AI • Agentic AI • LLM Applications • Web Development
