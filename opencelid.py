import requests
import xml.etree.ElementTree as ET

# OpenCellID API key
API_KEY = 'API_TOKEN_opencellid'

# Function to get the geolocation from OpenCellID
def get_geolocation(mcc, mnc, lac, cell_id):
    # OpenCellID API URL to get geolocation by cell parameters
    url = "https://opencellid.org/cell/get"

    # Parameters for the API request
    params = {
        'mcc': mcc,          # Mobile Country Code
        'mnc': mnc,          # Mobile Network Code
        'lac': lac,          # Location Area Code
        'cellid': cell_id,   # Cell ID (mCi)
        'key': API_KEY       # Your OpenCellID API key
    }

    try:
        # Sending GET request to the API
        response = requests.get(url, params=params, verify=False)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Print the raw XML response to see what we're getting from the API
            print(f"Raw Response: {response.text}")

            # Parse the XML response
            try:
                # Parse the XML into an ElementTree object
                root = ET.fromstring(response.text)

                # Check the status in the XML response
                status = root.get('stat')
                if status == 'fail':
                    print(f"Error: {root.find('err').attrib['info']}")
                    return

                # Extract the 'cell' tag
                cell = root.find('cell')

                if cell is not None:
                    # Extract latitude and longitude from the cell attributes
                    latitude = cell.get('lat')
                    longitude = cell.get('lon')

                    if latitude and longitude:
                        print(f"Latitude , Longitude : {latitude},{longitude}")
                    else:
                        print("No geolocation data found for the given parameters.")
                else:
                    print("Cell information not found in the response.")
            except Exception as e:
                print(f"Error parsing XML response: {e}")
        else:
            print(f"Failed to fetch data from OpenCellID. Status code: {response.status_code}")
            print(f"Response Text: {response.text}")  # Print the response text for further debugging

    except Exception as e:
        print(f"Error: {str(e)}")

# Main method to run the script
def main():
    # Parameters (from your request)
    mcc = 311       # Mobile Country Code (USA)
    mnc = 480       # Mobile Network Code (T-Mobile USA)
    lac = 64781     # Location Area Code
    cell_id = 64907024  # Cell ID (mCi)

    # Call the function to get geolocation
    get_geolocation(mcc, mnc, lac, cell_id)

# Ensure the script runs only if it's executed directly (not imported)
if __name__ == "__main__":
    main()
