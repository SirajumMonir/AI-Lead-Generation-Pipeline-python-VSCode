import requests
import os
import pandas as pd
import time
from dotenv import load_dotenv

print("\n🚀 Starting The Ultimate Lead Generation Pipeline...")

# --- Step 1: Read the Input CSV File ---
print("📂 Reading 'input_leads.csv'...")
try:
    # Pandas দিয়ে ইনপুট ফাইল পড়া হচ্ছে
    input_df = pd.read_csv("input_leads.csv")
    businesses_list = input_df["BusinessName"].tolist()
    print(f"✅ Found {len(businesses_list)} businesses to process.\n")
except FileNotFoundError:
    print("❌ Error: 'input_leads.csv' file not found! Please create it.")
    exit()

load_dotenv()
api_key = os.getenv("SERPAPI_KEY")
url = "https://serpapi.com/search"

# --- Step 2: Loop through the list ---
for business_name in businesses_list:
    
    search_query = f"{business_name} official contact info"
    params = {"engine": "google", "q": search_query, "api_key": api_key}

    print(f"⏳ Searching for: {business_name}...")
    response = requests.get(url, params=params)
    data = response.json()

    # --- Step 3: Extract Data ---
    try:
        contact_info = data["answer_box"]["answer"]
    except KeyError:
        try:
            contact_info = data["organic_results"][0]["snippet"]
        except (KeyError, IndexError):
            contact_info = "N/A (Data not found)"

    print(f"   🎯 Found: {contact_info}")

    # --- Step 4: Save to Database ---
    lead_data = {"Business Name": [business_name], "Contact Info": [contact_info]}
    df = pd.DataFrame(lead_data)

    # File Append Logic
    file_exists = os.path.isfile("leads_database.csv")
    df.to_csv("leads_database.csv", mode='a', index=False, header=not file_exists)
    
    time.sleep(2) # Anti-ban sleep (গুগল যেন ব্লক না করে)

print("\n🎉 Pipeline Complete! Check 'leads_database.csv' for results.")