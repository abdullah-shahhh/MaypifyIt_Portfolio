from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

GH_API_KEY = "684e71fd-c7c3-4bf9-a13a-cc0b99419efd" 
GH_BASE_URL = "https://graphhopper.com/api/1/route"

@app.route("/route")
def route():
    start = request.args.get("start")  
    end = request.args.get("end")     
    
    if not start or not end:
        return jsonify({"error": "start and end parameters required"}), 400
    
    start_lat, start_lng = start.split(",")
    end_lat, end_lng = end.split(",")
    
    params = {
        "point": [f"{start_lat},{start_lng}", f"{end_lat},{end_lng}"],
        "vehicle": "car",
        "locale": "en",
        "points_encoded": "false",
        "key": GH_API_KEY
    }
    
    r = requests.get(GH_BASE_URL, params=params)
    
    if r.status_code != 200:
        return jsonify({"error": r.json()}), r.status_code
    
    return jsonify(r.json())

if __name__ == "__main__":
    app.run(debug=True, port=5003)
