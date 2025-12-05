from flask import Flask, request, jsonify
import pandas as pd

df = pd.read_csv("Coord2.csv")

app = Flask(__name__)

# Geocoding
@app.route("/search")
def search():
    query = request.args.get("q", "").lower()
    results = df[df["name"].str.lower().str.contains(query)]
    return jsonify(results.to_dict(orient="records"))

# Reverse geocoding
@app.route("/reverse")
def reverse():
    lat = float(request.args.get("lat"))
    lon = float(request.args.get("lon"))
    
    df["dist"] = ((df["lat"] - lat)**2 + (df["lon"] - lon)**2)**0.5
    nearest = df.loc[df["dist"].idxmin()]
    return jsonify({"name": nearest["name"], "lat": nearest["lat"], "lon": nearest["lon"]})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
