from flask import Flask, jsonify, request,render_template
from flask_cors import CORS
from modules.nhentai import get

app = Flask(__name__)
CORS(app)

@app.route('/get')
def nhentai():
    page = request.args.get('page')
    query = request.args.get('query')
    return get(query,page)

if __name__ == "__main__":
    app.run(debug=True)