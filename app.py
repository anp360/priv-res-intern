from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow frontend to access this API

@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.get_json()
    print("Received data:", data)
    
    # Save to a file or DB (currently just simulating)
    with open("data_log.txt", "a") as f:
        f.write(str(data) + "\n")

    return jsonify({"message": "Data received successfully!"})

if __name__ == '__main__':
    app.run(debug=True)

