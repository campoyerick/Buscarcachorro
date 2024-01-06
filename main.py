from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/breeds', methods=['GET'])
def breeds():
    api_url = 'http://dog.ceo/api/breeds/list/all'
    response = requests.get(api_url)
    data = response.json()
    breeds = list(data['message'].keys())
    return jsonify({'breeds': breeds})

@app.route('/breeds/<breed>/images', methods=['GET'])
def breeds_images(breed):
    api_url = f'http://dog.ceo/api/breed/{breed}/images'
    response = requests.get(api_url)
    data = response.json()
    images = data['message']
    return jsonify({'breed': breed, 'images': images})

if __name__ == '__main__':
    app.run(debug=True)