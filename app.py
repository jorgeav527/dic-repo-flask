from flask import Flask, render_template
import sqlite3

def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)

@app.route("/", methods=["GET"])
def root():
    return render_template('index.html')

@app.route("/base", methods=["GET"])
def base():
    return render_template('base.html')

@app.route("/home", methods=["GET"])
def home():
    return render_template('home.html')

@app.route("/about", methods=["GET"])
def about():
    return render_template('about.html')

@app.route("/post", methods=["GET"])
def get_all_posts():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('post/posts.html', posts=posts)

@app.route("/post/<int:post_id>", methods=["GET"])
def get_one_posts(post_id: int):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    conn.close()
    return render_template('post/post.html', post=post)


# Iniciar el servidor
if __name__ == '__main__':
    app.run(debug=True, port=5000)
