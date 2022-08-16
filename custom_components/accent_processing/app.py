from flask import Flask, jsonify, request
from restore_accents import DiacriticsRestorer

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

restorer = DiacriticsRestorer('ckpt_blog_td2')


@app.route('/restore', methods=['POST'])
def samplefunction():
    # text = request.args['text']  # This is for GET method
    text = request.form.get('text', default="xin chao ban than men", type=str)  # body's 'text' is in forms
    result = restorer.add_diacritics(text)
    data = {"text": result}
    return jsonify(data)


@app.route('/hello', methods=['GET'])
def hello():
    return "hello"


if __name__ == '__main__':
    port = 5351  # the custom port you want
    app.run(host='0.0.0.0', port=port)
