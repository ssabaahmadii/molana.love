from flask import Flask, render_template, url_for

app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/poems')
def poems():
    return render_template('poems.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/molana')
def molana():
    return render_template('molana.html')

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template
from models import db, Article


# تنظیمات پایگاه داده
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# مسیرهای سایت
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/poems')
def poems():
    return render_template('poems.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/molana')
def molana():
    return render_template('molana.html')
@app.route('/articles')
def articles():
    return render_template('articles.html')

@app.route('/articles')
def articles():
    articles = Article.query.all()  # گرفتن همه مقالات از پایگاه داده
    return render_template('articles.html', articles=articles)

if __name__ == '__main__':  # اصلاح شد
    app.run(debug=True)
from flask import Flask, render_template
from models import db, Article, app

@app.route("/article/<int:article_id>")
def article_detail(article_id):
    article = Article.query.get_or_404(article_id)  # پیدا کردن مقاله بر اساس ID
    return render_template("article_detail.html", article=article)
from flask import Flask, render_template
from models import db, Article, app

@app.route("/articles")
def articles():
    all_articles = Article.query.all()  # گرفتن همه مقالات
    return render_template("articles.html", articles=all_articles)

if __name__ == "__main__":
    app.run(debug=True)