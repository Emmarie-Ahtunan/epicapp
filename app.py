import streamlit as st
import requests
import io
import os
from dotenv import load_dotenv
import secrets

load_dotenv()

MY_EPIC_API_KEY = os.getenv("NASA_API_KEY")

class EPICConnection:
    def __init__(self, api_key):
        self.api_key = api_key

    def fetch_epic_data(self, date=None):
        base_url = "https://epic.gsfc.nasa.gov/api/natural"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        if date:
            url = f"{base_url}/data/{date}"
        else:
            url = f"{base_url}/data/latest"
            
def main():
    st.title("EPIC Daily 'Blue Marble' API Streamlit App")
    api_key = MY_EPIC_API_KEY

    epic_connection = EPICConnection(api_key)

    # Fetch the most recent EPIC data
    epic_data = epic_connection.fetch_epic_data()
    if epic_data:
        st.image(epic_data['image_url'], caption="EPIC Earth Image", use_column_width=True)
        st.write("Date:", epic_data['date'])
        st.write("Enhanced Color:", epic_data['enhanced'])
        st.write("Natural Color:", epic_data['natural'])
    else:
        st.error("Failed to fetch data from EPIC API.")

        response = requests.get("https://api.nasa.gov/EPIC/api/natural/images?api_key=DEMO_KEY", headers=headers)
        print("API Response:", response.status_code)
        print("API Response:", response.json())
        
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return None



if __name__ == "__main__":
    main()
