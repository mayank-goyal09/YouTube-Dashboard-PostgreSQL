# 📺✨ YOUTUBE ANALYTICS DASHBOARD 2.0 ✨📺

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=25&duration=3000&pause=1000&color=FF0000&center=true&vCenter=true&width=1000&lines=Real-Time+Channel+Analytics;AI-Powered+Content+Insights;SQLite+Architecture+Migration;Streamlit+Interactive+Dashboard)](https://git.io/typing-svg)

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite&logoColor=white)
![YouTube API](https://img.shields.io/badge/API-YouTube_Data_v3-FF0000?logo=youtube&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-Visuals-3F4F75?logo=plotly&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Streamlit-FF4B4B?style=for-the-badge)](https://youtube-dashboard-appql-w6tacoledpx4fgpmkdtth4.streamlit.app/)
[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github)](https://github.com/mayank-goyal09/youtube-analytics-dashboard)

---

## 🌟 **PROJECT OVERVIEW** 🌟

### **"Data is clarity; analytics is action."**

This **YouTube Analytics Dashboard 2.0** is a comprehensive tool designed to empower content creators with real-time insights, AI-driven recommendations, and deep performance analysis. Unlike standard analytics, this dashboard focuses on **actionable intelligence**—telling you not just *what* happened, but *why* and *what to do next*.

---

## 🏗️ **ARCHITECTURAL DECISION: The PostgreSQL vs. SQLite Story** 🏗️

### **The Journey: From Cloud to Local**

**"Why I chose SQLite over PostgreSQL for this Open-Source Release"**

Initially, I built this application using **PostgreSQL hosted on Neon DB**. This setup was robust, scalable, and production-ready, connecting a live cloud database to my application. I successfully implemented the full pipeline:
- ✅ **Connected via `psycopg2`**
- ✅ **Managed credentials securely**
- ✅ **Handled cloud latency and connection pooling**

**However, when preparing to open-source this project for the community and recruiters, I faced a critical decision:**

1.  **Security Risks**: Distributing a project dependent on a private cloud database requires handling sensitive connection strings and passwords. Even with environment variables, it adds a layer of "setup friction" for anyone trying to run the code.
2.  **Complexity for Users**: I wanted this tool to be **instantly usable**. Requiring users to set up a Neon account, configure a Postgres instance, and manage network rules creates a barrier to entry.
3.  **Portability**: A self-contained application is far superior for a portfolio showcase.

### **The Solution: Strategically Migrating to SQLite**

I refactored the backend to use **SQLite**, an embedded database engine.

**Why SQLite was the smarter choice here:**
*   **Zero Configuration**: The database is a single file (`youtube_data.db`). No servers, no ports, no user management.
*   **Instant Deployment**: Users can clone the repo and run it immediately.
*   **Data Privacy**: All analytics data stays on the user's local machine—crucial for personal channel data.
*   **Simplicity**: It proves that **I can choose the right tool for the job**, prioritizing user experience and portability over unnecessary complexity.

> *I have the skills to build enterprise-grade PostgreSQL systems, but I have the wisdom to use SQLite when it serves the user best.*

---

# 🔥 **KEY FEATURES** 🔥

### 1. 📊 **Real-Time Analytics**
*   **Live Dashboard**: Auto-refreshes every 60 seconds to fetch the latest view counts, likes, and comments.
*   **KPI Cards**: Instant view of Subscribers, Total Views, Avg Engagement, and more.

### 2. 🧠 **AI & Smart Insights (New!)**
*   **Video Performance Scores**: Every video gets a grade (A+, B, C...) based on a weighted algorithm of views, likes, and comments.
*   **Growth Velocity**: Tracks if your channel momentum is "Growing", "Good", or "Excellent".
*   **Actionable Recommendations**: AI-logic suggests specific actions (e.g., "Boost Engagement", "Improve Thumbnails") based on your metrics.

### 3. 🎨 **Premium UI/UX**
*   **Dual Theme Support**: Seamlessly switch between **Dark Mode** (Cyberpunk/Midnight) and **Light Mode** (Clean/Minimal) with dynamic text contrast adjustments.
*   **Interactive Charts**: Beautiful Plotly visualizations for subscriber growth, engagement rates, and content performance.

---

## 🛠️ **TECH STACK** 🛠️

| **Category** | **Technologies** |
|--------------|------------------|
| 🐍 **Language** | Python 3.9+ |
| 🖥️ **Frontend** | Streamlit |
| 💾 **Database** | SQLite (Migrated from PostgreSQL) |
| 🔌 **API** | YouTube Data API v3 |
| 📊 **Visualization** | Plotly Express |
| 🐼 **Data Processing** | Pandas, SQLAlchemy |

---

## 📂 **PROJECT STRUCTURE** 📂

```
youtube-analytics-dashboard/
│
├── 🐍 youtube_dashboard.py    # Main Application (UI & Logic)
├── 🔌 youtube_fetch.py        # API Data Fetcher & ETL Script
├── 🧪 init_demo_data.py       # Demo Data Generator (for testing)
├── 💾 youtube_data.db         # SQLite Database (Local)
├── 📋 requirements.txt        # Project Dependencies
├── 🔒 .env.example            # API Key Configuration Template
└── 📖 README.md               # Documentation
```

---

## 🚀 **QUICK START** 🚀

### **Step 1: Clone the Repository**
```bash
git clone https://github.com/mayank-goyal09/youtube-analytics-dashboard.git
cd youtube-analytics-dashboard
```

### **Step 2: Install Dependencies**
```bash
pip install -r requirements.txt
```

### **Step 3: Run with Demo Data (Instant Test)**
Want to see it in action without an API key?
```bash
python init_demo_data.py
streamlit run youtube_dashboard.py
```

### **Step 4: Use Your Own Data (Optional)**
1.  Get a **YouTube Data API Key** from Google Cloud Console.
2.  Create a `.env` file and add your key:
    ```env
    YOUTUBE_API_KEY=your_api_key_here
    YOUTUBE_CHANNEL_ID=your_channel_id_here
    ```
3.  Run the fetcher:
    ```bash
    python youtube_fetch.py
    ```

---

## 👨‍💻 **CONNECT WITH ME** 👨‍💻

[![GitHub](https://img.shields.io/badge/GitHub-mayank--goyal09-181717?style=for-the-badge&logo=github)](https://github.com/mayank-goyal09)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Mayank_Goyal-0077B5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/mayank-goyal-mg09/)
[![Portfolio](https://img.shields.io/badge/Portfolio-mayank--goyal09-00C853?style=for-the-badge&logo=googlechrome&logoColor=white)](https://mayank-goyal09.github.io/)
[![YouTube](https://img.shields.io/badge/YouTube-@maygal_memer-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](http://www.youtube.com/@maygal_memer)

**Mayank Goyal**
*Data Analyst | Python Developer | Open Source Enthusiast*

---

![Footer](https://capsule-render.vercel.app/api?type=waving&color=gradient&height=100&section=footer)
