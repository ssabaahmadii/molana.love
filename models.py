from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# تنظیمات پایگاه داده (SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# مدل مقالات
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    print("✅ دیتابیس با موفقیت ساخته شد!")