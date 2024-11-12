import requests
import json


def get_location_from_wifi(mac_address, api_key):
    url = "https://www.googleapis.com/geolocation/v1/geolocate?key=" + api_key

    # Wi-Fi network data
    wifi_data = {
        "wifiAccessPoints": [
            {
                "macAddress": mac_address,
                "signalStrength": -65,
                "signalToNoiseRatio": 40
            }
        ]
    }

    # Make a POST request to the Google Geolocation API
    try:
        response = requests.post(url, json=wifi_data)

        # Check if the request was successful
        if response.status_code == 200:
            location_data = response.json()
            if "location" in location_data:
                latitude = location_data["location"]["lat"]
                longitude = location_data["location"]["lng"]
                accuracy = location_data["accuracy"]
                print(f"Latitude: {latitude}, Longitude: {longitude}")
                print(f"Accuracy: {accuracy} meters")
            else:
                print("Error: Location not found in the response.")
        else:
            print(f"Error: Unable to get location. HTTP Status Code: {response.status_code}")
            print("Response:", response.text)

    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    # Replace with your Google Maps API key
    api_key = "TOKEN"

    # Example MAC address (BSSID)
    mac_address = "13-12-41-5h-h5-77"

    # Get location for the Wi-Fi MAC address
    get_location_from_wifi(mac_address, api_key)
