from models import db, Article, app

with app.app_context():
    all_articles = Article.query.all()
    if all_articles:
        print("✅ مقالات ثبت‌شده در دیتابیس:")
        for article in all_articles:
            print(f"{article.id}: {article.title} - {article.content}")
    else:
        print("❌ دیتابیس خالیه! باید دوباره add_data.py رو اجرا کنی.")