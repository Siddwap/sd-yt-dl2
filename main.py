from flask import Flask, render_template, request, send_file

from pytube import YouTube

import os

app = Flask(__name__)

@app.route('/')

def index():

    return render_template('index.html')

@app.route('/download', methods=['POST'])

def download():

    video_url = request.form['video_url']

    yt = YouTube(video_url)

    video = yt.streams.first()

    video.download()

    return send_file(f'{video.default_filename}', as_attachment=True, cache_timeout=0)

if __name__ == '__main__':

    app.run(debug=True)

