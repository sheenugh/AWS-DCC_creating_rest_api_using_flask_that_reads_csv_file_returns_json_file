from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Read data from CSV file
data = pd.read_csv('programming_languages.csv')

# Convert the data to a JSON response
json_data = data.to_json(orient='records')

# Write JSON data to a file
with open('data.json', 'w') as json_file:
    json_file.write(json_data)

@app.route('/')
def home():
    return "Welcome to my REST API!"

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(json_data)

if __name__ == '__main__':
    app.run(debug=True)
