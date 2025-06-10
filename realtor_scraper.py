import requests
from urllib.parse import urlencode

# Realtor.ca API endpoint for map search
API_URL = "https://api2.realtor.ca/Listing.svc/PropertySearch_Post"

HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0"
}

def fetch_listings():
    payload = {
        "CultureId": 1,
        "ApplicationId": 1,
        "RecordsPerPage": 10,
        "MaximumResults": 10,
        "PropertySearchTypeId": 1,
        "TransactionTypeId": 2,
        "SortOrder": "A",
        "SortBy": "6",
        "IndividualId": 1967088,  # <-- Replace with agent ID
        "Version": "7.0"
    }

    response = requests.post(API_URL, json=payload, headers=HEADERS)
    data = response.json()

    listings = []

    for listing in data.get("Results", []):
        listings.append({
            "id": listing.get("MlsNumber"),
            "address": listing.get("Property", {}).get("Address", {}).get("AddressText", "N/A"),
            "city": listing.get("Property", {}).get("Address", {}).get("City", "N/A"),
            "slug": listing.get("MlsNumber"),
            "image_urls": listing.get("Property", {}).get("PhotoUrls", [])
        })

    return listings
