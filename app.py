from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from datetime import datetime

app = Flask(__name__, static_folder="static", template_folder="templates")

posts = [
    {
        "id": 1,
        "author": "Teacher",
        "time": "Start of Class",
        "content": "Welcome to ClassBook! Post an update or reply to a classmate below.",
        "likes": 1,
        "comments": []
    }
]


@app.route("/manifest.json")
def manifest():
    return send_from_directory(app.static_folder, "manifest.json", mimetype="application/manifest+json")


@app.route("/sw.js")
def service_worker():
    return send_from_directory(app.static_folder, "sw.js", mimetype="application/javascript")


@app.route("/")
def home():
    return render_template("index.html", posts=posts)


@app.route("/post", methods=["POST"])
def add_post():
    author = request.form.get("author")
    content = request.form.get("content")
    if author and content:
        posts.insert(0, {
            "id": len(posts) + 1,
            "author": author,
            "time": datetime.now().strftime("%I:%M %p"),
            "content": content,
            "likes": 0,
            "comments": []
        })
    return redirect(url_for("home"))


@app.route("/like/<int:post_id>", methods=["POST"])
def like_post(post_id):
    for post in posts:
        if post["id"] == post_id:
            post["likes"] += 1
            break
    return redirect(url_for("home"))


@app.route("/comment/<int:post_id>", methods=["POST"])
def add_comment(post_id):
    author = request.form.get("author")
    text = request.form.get("text")
    for post in posts:
        if post["id"] == post_id and author and text:
            post["comments"].append({"author": author, "text": text})
            break
    return redirect(url_for("home"))


@app.route("/clear", methods=["POST"])
def clear_posts():
    posts.clear()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
