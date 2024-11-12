import requests
import json


def get_location_by_mac(api_key, mac_address, signal_strength=-65, snr=40):
    # API endpoint for Google Geolocation
    url = 'https://www.googleapis.com/geolocation/v1/geolocate?key=' + api_key

    # List of Wi-Fi access points (BSSIDs)
    wifi_access_points = [{
        "macAddress": mac_address,  # The MAC address (BSSID)
        "signalStrength": signal_strength,  # Signal strength in dBm (default: -65)
        "signalToNoiseRatio": snr  # Signal-to-noise ratio (default: 40)
    }]

    # Prepare payload for POST request
    payload = {
        "wifiAccessPoints": wifi_access_points
    }

    # Send request to Google Geolocation API
    response = requests.post(url, json=payload)

    # Check if the response is successful
    if response.status_code == 200:
        location_data = response.json()

        # Check if location data is available in the response
        if 'location' in location_data:
            latitude = location_data['location']['lat']
            longitude = location_data['location']['lng']
            accuracy = location_data['accuracy']
            print(
                f"MAC Address {mac_address} is located at:Latitude: {latitude},{longitude}\nAccuracy: {accuracy} meters.")
        else:
            print(f"No location data found for MAC Address {mac_address}.")
    else:
        print(f"Error: Unable to retrieve location. HTTP Status code: {response.status_code}")
        print("Response:", response.text)


if __name__ == "__main__":
    # Replace with your actual Google API key
    api_key = "TOKEN"  # Replace with your actual API key

    # MAC address you want to check (example MAC address)
    mac_address = "13-12-41-5h-h5-77"  # Replace with the MAC address you want to check

    # Get location based on MAC address (BSSID)
    get_location_by_mac(api_key, mac_address)
