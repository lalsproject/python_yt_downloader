from quart import Quart, render_template, request, jsonify
from pytube import YouTube

app = Quart(__name__)

@app.route('/')
async def index():
    return await render_template('index.html')

async def fetch_video_info(video_url):
    try:
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        video_title = yt.title
        video_url = stream.url
        video_id = yt.video_id
        thumbnail_url = f'https://img.youtube.com/vi/{video_id}/0.jpg'
        return {'title': video_title, 'url': video_url, 'thumbnail': thumbnail_url}
    except Exception as e:
        return {'error': str(e)}

@app.route('/download', methods=['POST'])
async def download():
    data = await request.form
    video_url = data['url']
    response = await fetch_video_info(video_url)
    return jsonify(response)

if __name__ == '__main__':
    app.run('0.0.0.0',debug=True)
