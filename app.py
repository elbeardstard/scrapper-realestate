from flask import Flask, jsonify
from realtor_scraper import fetch_listings

app = Flask(__name__)

@app.route("/listings.json")
def listings():
    data = fetch_listings()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=10000)
