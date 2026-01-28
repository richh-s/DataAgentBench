code = """import json
import pandas as pd
import re

# Load data from storage
businesses_data = locals()['var_functions.query_db:2']
reviews_file_path = locals()['var_functions.query_db:4']

# Load reviews data from file
with open(reviews_file_path, 'r') as f:
    reviews_data = json.load(f)

# Create DataFrames
df_businesses = pd.DataFrame(businesses_data)
df_reviews = pd.DataFrame(reviews_data)

# Extract business ID numbers
df_businesses['business_id_num'] = df_businesses['business_id'].str.replace('businessid_', '').astype(int)
df_reviews['business_id_num'] = df_reviews['business_ref'].str.replace('businessref_', '').astype(int)

# Show summary statistics
print("Data Summary:")
print(f"Total businesses accepting credit cards: {len(df_businesses)}")
print(f"Total review records: {len(df_reviews)}")

# Extract categories from descriptions
def extract_categories(description):
    """Extract categories from description field"""
    if pd.isna(description) or description == "":
        return []
    
    # Look for patterns like "services in X, Y, and Z" or "fields of X, Y"
    patterns = [
        r"services in ([^\.]+)",
        r"fields of ([^\.]+)",
        r"range of services including ([^\.]+)"
    ]
    
    for pattern in patterns:
        match = re.search(pattern, description, re.IGNORECASE)
        if match:
            text = match.group(1)
            # Split by comma or 'and' to get individual categories
            categories = [cat.strip() for cat in re.split(r',|and', text) if cat.strip()]
            return categories
    
    return []

# Apply category extraction
df_businesses['categories'] = df_businesses['description'].apply(extract_categories)

# Expand categories and count
all_categories = []
for cats in df_businesses['categories']:
    all_categories.extend(cats)

from collections import Counter
category_counts = Counter(all_categories)

print("\nTop 10 Categories:")
for cat, count in category_counts.most_common(10):
    print(f"  {cat}: {count}")

# Find the most common category
top_category = category_counts.most_common(1)[0] if category_counts else (None, 0)

# Filter to businesses in this category
target_category = top_category[0]
businesses_in_top_cat = []

for idx, row in df_businesses.iterrows():
    if target_category and target_category in row['categories']:
        businesses_in_top_cat.append(row['business_id_num'])

# Get ratings for these businesses
target_ratings = df_reviews[df_reviews['business_id_num'].isin(businesses_in_top_cat)]['rating']

# Calculate average rating
average_rating = target_ratings.astype(float).mean() if not target_ratings.empty else 0

result = {
    "category": target_category,
    "business_count": len(businesses_in_top_cat),
    "rating_count": len(target_ratings),
    "average_rating": round(average_rating, 2)
}

print("\n__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_functions.query_db:2': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'name': 'Luminosity', 'review_count': '39', 'is_open': '1', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'True', 'NoiseLevel': "u'quiet'", 'WiFi': "u'no'"}, 'hours': {'Monday': '10:0-21:0', 'Tuesday': '10:0-21:0', 'Wednesday': '10:0-21:0', 'Thursday': '10:0-21:0', 'Friday': '10:0-21:0', 'Saturday': '10:0-21:0', 'Sunday': '11:0-18:0'}, 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
