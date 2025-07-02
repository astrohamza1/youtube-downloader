from flask import Flask, request, render_template, send_file
from pytube import YouTube
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    video_url = request.form['url']
    yt = YouTube(video_url)
    stream = yt.streams.get_highest_resolution()
    path = stream.download()
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
