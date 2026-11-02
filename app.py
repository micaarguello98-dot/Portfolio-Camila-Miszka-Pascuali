import os
from flask import Flask, render_template, send_from_directory

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PUBLIC_STATIC_DIR = os.path.join(BASE_DIR, 'public', 'static')
STATIC_DIR = PUBLIC_STATIC_DIR if os.path.exists(PUBLIC_STATIC_DIR) else os.path.join(BASE_DIR, 'static')

app = Flask(
    __name__,
    static_folder=STATIC_DIR,
    static_url_path='/static'
)

@app.route('/static/<path:filename>')
def serve_static(filename):
    if os.path.exists(os.path.join(PUBLIC_STATIC_DIR, filename)):
        return send_from_directory(PUBLIC_STATIC_DIR, filename)
    fallback_dir = os.path.join(BASE_DIR, 'static')
    return send_from_directory(fallback_dir, filename)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)

