from flask import Flask, request, jsonify

app= Flask(__name__)

@app.route('/products', methods=['GET, POST'])
def products():
    if request.method == 'POST':
        data = request.json