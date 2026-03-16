from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    url = 'https://jsonplaceholder.typicode.com/users/1'  # Sample API
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
        else:
            data = {'error': 'Unable to fetch data'}
    except Exception as e:
        data = {'error': str(e)}
    
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)