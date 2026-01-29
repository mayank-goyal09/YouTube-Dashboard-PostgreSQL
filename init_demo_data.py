"""
Initialize Demo Data for YouTube Analytics Dashboard
Run this script to populate the database with sample data for testing.
This allows users to see the dashboard working without a YouTube API key.
"""

                subscribers INTEGER,
                total_views INTEGER,
                total_videos INTEGER,
                dislikes INTEGER DEFAULT 0,
                fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """))
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS video_stats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                video_id TEXT,
                title TEXT,
                published_at TIMESTAMP,
                views INTEGER,
                likes INTEGER,
                dislikes INTEGER DEFAULT 0,
                comments INTEGER,
                fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """))
        conn.commit()

def generate_demo_data():
    """Generate realistic demo data"""
    
    # Clear existing data
    with engine.connect() as conn:
        conn.execute(text("DELETE FROM channel_stats"))
        conn.execute(text("DELETE FROM video_stats"))
        conn.commit()
    
    print("🧹 Cleared existing data")
    
    # Generate channel stats history (simulating growth over 30 days)
    base_subs = 5000
    base_views = 150000
    channel_history = []
    
    for i in range(30):
        date = datetime.now() - timedelta(days=30-i)
        growth = i * random.randint(50, 150)
        channel_history.append({
            "channel_name": "Demo Channel",
            "subscribers": base_subs + growth,
            "total_views": base_views + (growth * 30),
            "total_videos": 25 + (i // 5),
            "dislikes": random.randint(0, 50),
            "fetched_at": date
        })
    
    df_channel = pd.DataFrame(channel_history)
    df_channel.to_sql("channel_stats", engine, if_exists="append", index=False)
    print(f"✅ Inserted {len(channel_history)} channel stat records")
    
    # Generate video stats
    video_titles = [
        "🚀 Getting Started with Python - Complete Tutorial",
        "🔥 Top 10 VS Code Extensions You NEED",
        "💡 Machine Learning for Beginners",
        "🎯 How I Built My First App in 24 Hours",
        "⚡ JavaScript Tips That Will Blow Your Mind",
        "🌟 The Future of AI - What You Need to Know",
        "🔧 Docker Tutorial for Beginners",
        "📊 Data Visualization with Python",
        "🎨 CSS Tricks for Modern Websites",
        "🛠️ Git & GitHub Crash Course",
        "🤖 Building a Chatbot from Scratch",
        "📱 React Native vs Flutter - Which is Better?",
        "🔐 Web Security Best Practices",
        "☁️ AWS for Beginners - Cloud Computing 101",
        "🎬 Video Editing with Python"
    ]
    
    videos = []
    for i, title in enumerate(video_titles):
        published = datetime.now() - timedelta(days=random.randint(1, 90))
        views = random.randint(500, 50000)
        
    print(f"\n📁 Demo data saved to: {DB_PATH}")
    print("\n🎉 You can now run the dashboard:")
    print("   streamlit run youtube_dashboard.py")

if __name__ == "__main__":
    print("🎬 YouTube Analytics Dashboard - Demo Data Generator")
    print("=" * 50)
    init_database()
    generate_demo_data()

