from flask import Flask, jsonify, request,render_template
from flask_cors import CORS
from modules.nhentai import search,getBookById

app = Flask(__name__)
CORS(app)

@app.route('/search')
def searchBooks():
    page = request.args.get('page')
    query = request.args.get('query')
    return search(query,page)

@app.route('/book')
def getBook():
    _id = request.args.get('id')
    return getBookById(_id)

if __name__ == "__main__":
    app.run(debug=True)