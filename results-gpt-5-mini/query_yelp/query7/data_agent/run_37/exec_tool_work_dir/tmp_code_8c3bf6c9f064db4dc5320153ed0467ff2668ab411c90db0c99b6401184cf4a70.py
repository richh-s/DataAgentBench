code = """import json
import pandas as pd
import re

# Load data from storage file paths
with open(var_call_RYsEyFp03zPEyXDygxM7Pp4g, 'r') as f:
    reviews = json.load(f)
with open(var_call_09LN6K9IBFSMo4gfEYYOghMC, 'r') as f:
    businesses = json.load(f)

# Create dataframes
df_reviews = pd.DataFrame(reviews)
df_business = pd.DataFrame(businesses)

# Parse dates and filter reviews since 2016-01-01
df_reviews['parsed_date'] = pd.to_datetime(df_reviews['date'], errors='coerce')
# Some dates are like 'May 07, 2016 at 03:17 PM' which pandas can parse; others may parse to NaT
# Keep only dates in 2016 or later
df_reviews = df_reviews[df_reviews['parsed_date'] >= pd.Timestamp('2016-01-01')].copy()

# Map business_ref -> business_id (businessref_# -> businessid_#)
if 'business_ref' in df_reviews.columns:
    df_reviews['business_id'] = df_reviews['business_ref'].str.replace('businessref_', 'businessid_')
else:
    df_reviews['business_id'] = None

# Build business_id -> description mapping
biz_desc = df_business.set_index('business_id')['description'].to_dict()

# Function to extract categories from description
kw_regex = re.compile(r"(?:including|providing a range of services in|offers a range of services in|offers a range of services|offers a variety of services including|offers a variety of services|offers a variety of|specializes in|this establishment offers|this facility offers|provides a range of services in|provides a range of services|provides|offering|offers)[:\s]*(.*)", flags=re.IGNORECASE)

split_pattern = re.compile(r",|\band\b|&")

def extract_categories(desc):
    if not isinstance(desc, str):
        return []
    # Try keyword-based extraction
    m = kw_regex.search(desc)
    text = None
    if m:
        text = m.group(1)
    else:
        # fallback: try to take the portion after the last comma (likely categories at end)
        parts = desc.split(',')
        if len(parts) > 1:
            text = ','.join(parts[-3:])  # take last few parts
        else:
            text = desc
    # Remove location/address patterns (drop content before first occurrence of capitalized category words?)
    # Now split into tokens
    tokens = [t.strip() for t in split_pattern.split(text) if t and t.strip()]
    # Clean tokens: remove trailing periods and leading words like 'this', 'the'
    clean = []
    for tok in tokens:
        tok = re.sub(r"\.$", "", tok).strip()
        # remove leading phrases that are not categories
        tok = re.sub(r"^(this|the|offers|provides|including)\s+", "", tok, flags=re.IGNORECASE).strip()
        # Discard very short tokens or tokens that look like address fragments (contain digits)
        if len(tok) < 2:
            continue
        if re.search(r"\d", tok):
            continue
        clean.append(tok)
    # Further split tokens that contain '/' or ' and '
    final = []
    for c in clean:
        parts = re.split(r"/|-", c)
        for p in parts:
            p = p.strip()
            if p:
                final.append(p)
    # Normalize spaces
    final = [re.sub(r"\s+", ' ', f) for f in final]
    # Deduplicate while preserving order
    seen = set()
    out = []
    for f in final:
        if f.lower() not in seen:
            seen.add(f.lower())
            out.append(f)
    return out

# Build mapping for businesses
biz_cats = {}
for bid, desc in biz_desc.items():
    biz_cats[bid] = extract_categories(desc)

# Map categories to reviews
df_reviews['categories'] = df_reviews['business_id'].map(biz_cats)
# Drop reviews with no categories
df_reviews = df_reviews[df_reviews['categories'].map(lambda x: bool(x) if isinstance(x, list) else False)]

# Explode categories and count
df_exploded = df_reviews.explode('categories')
# Clean category strings
df_exploded['categories'] = df_exploded['categories'].astype(str).str.strip()

counts = df_exploded.groupby('categories').size().reset_index(name='review_count')
counts = counts.sort_values('review_count', ascending=False)

# Get top 5
top5 = counts.head(5)

result = []
for _, row in top5.iterrows():
    result.append({"category": row['categories'], "review_count": int(row['review_count'])})

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_BWl6sHAf8J0BznA3h3xYq6Hf': ['checkin', 'business'], 'var_call_suvycklpHfKr6oshNJM0GpLC': ['review', 'tip', 'user'], 'var_call_E5E6QLsA2JlrJlfZuHMyvGUm': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_CqzljAKq5WvcSmqgmb4W5WND': [{'user_id': 'userid_286', 'yelping_since': '15 Jan 2009, 16:40'}, {'user_id': 'userid_1331', 'yelping_since': '13 Jul 2010, 15:42'}, {'user_id': 'userid_1880', 'yelping_since': '2010-09-07 23:24:36'}, {'user_id': 'userid_271', 'yelping_since': 'October 23, 2011 at 07:47 PM'}, {'user_id': 'userid_534', 'yelping_since': '2011-08-30 13:46:26'}, {'user_id': 'userid_1997', 'yelping_since': '2009-12-02 18:54:31'}, {'user_id': 'userid_1386', 'yelping_since': '2009-04-15 12:46:06'}, {'user_id': 'userid_237', 'yelping_since': 'October 04, 2009 at 05:59 PM'}, {'user_id': 'userid_596', 'yelping_since': '20 Apr 2008, 16:55'}, {'user_id': 'userid_948', 'yelping_since': '2007-07-28 22:22:09'}], 'var_call_8GNTqFagJclbpXCetAcOYZxx': 'file_storage/call_8GNTqFagJclbpXCetAcOYZxx.json', 'var_call_RYsEyFp03zPEyXDygxM7Pp4g': 'file_storage/call_RYsEyFp03zPEyXDygxM7Pp4g.json', 'var_call_09LN6K9IBFSMo4gfEYYOghMC': 'file_storage/call_09LN6K9IBFSMo4gfEYYOghMC.json'}

exec(code, env_args)
