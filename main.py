from flask import Flask, request, render_template_string
from pytube import YouTube
import os

app = Flask(__name__)

HTML_TEMPLATE = """
<!doctype html>
<title>YouTube Downloader</title>
<h1>YouTube Video Downloader</h1>
<form action="/" method="post">
  <input type="text" name="url" placeholder="Enter YouTube URL">
  <input type="submit" value="Download">
</form>
{% if message %}
<p>{{ message }}</p>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        url = request.form.get("url")
        try:
            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution()
            stream.download()
            message = "✅ Download successful!"
        except Exception as e:
            message = f"❌ Error: {e}"
    return render_template_string(HTML_TEMPLATE, message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
