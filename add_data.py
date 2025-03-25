from models import db, Article, app

with app.app_context():
    article1 = Article(title="عشق دیرآشنای مولانا", content="این کتاب درباره عشق درونی و معنوی مولاناست.")
    article2 = Article(title="مولانا و شمس", content="داستان آشنایی مولانا با شمس تبریزی و تأثیر آن بر اشعار او.")

    db.session.add(article1)
    db.session.add(article2)
    db.session.commit()

    print("✅ داده‌های تستی با موفقیت اضافه شدند!")