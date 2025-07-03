from flask import Flask, request, render_template_string
from pytube import YouTube
import os

app = Flask(__name__)

# قالب HTML بسيط لواجهة المستخدم
HTML_TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>YouTube Downloader</title>
</head>
<body>
    <h1>🧲 YouTube Video Downloader</h1>
    <form method="post">
        <input type="text" name="url" placeholder="أدخل رابط فيديو اليوتيوب" required style="width:300px;">
        <input type="submit" value="تحميل">
    </form>
    {% if message %}
        <p>{{ message }}</p>
   

