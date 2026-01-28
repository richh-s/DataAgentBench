code = """import json
import pandas as pd
import re
from collections import Counter

# Load all businesses accepting credit cards
businesses_path = locals()['var_functions.query_db:14']
with open(businesses_path, 'r') as f:
    businesses = json.load(f)

# Load all reviews
reviews_path = locals()['var_functions.query_db:4']
with open(reviews_path, 'r') as f:
    reviews = json.load(f)

print(f"Total businesses accepting credit cards: {len(businesses)}")
print(f"Total reviews: {len(reviews)}")

# Create DataFrames
df_businesses = pd.DataFrame(businesses)
df_reviews = pd.DataFrame(reviews)

# Extract numeric business IDs
df_businesses['business_id_num'] = df_businesses['business_id'].str.replace('businessid_', '').astype(int)
df_reviews['business_id_num'] = df_reviews['business_ref'].str.replace('businessref_', '').astype(int)

# Function to extract categories from description
def extract_categories(description):
    categories = []
    if pd.isna(description):
        return categories
    
    # Look for "services in" or "fields of" patterns
    patterns = [
        r'(?:services in|fields of|services including) ([^\.]+)',
        r'(?:category of|categories of) [\'"]([^\'"]+)[\'"]',
        r'range of services including ([^\.]+)'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, description, re.IGNORECASE)
        if match:
            text = match.group(1)
            # Split by comma or 'and' to get individual categories
            parts = re.split(r',|\band\b', text)
            for part in parts:
                cat = part.strip()
                # Clean up category names
                cat = re.sub(r'\s+$', '', cat)
                cat = re.sub(r'^\s+', '', cat)
                if cat and len(cat) > 2:  # Filter out very short entries
                    categories.append(cat)
            break
    
    return categories

# Extract categories for each business
df_businesses['categories'] = df_businesses['description'].apply(extract_categories)

# Count all categories across all businesses
all_categories = []
for cats in df_businesses['categories']:
    all_categories.extend(cats)

category_counts = Counter(all_categories)

# Get top 10 categories for reference
print("\nTop 10 categories by business count:")
for cat, count in category_counts.most_common(10):
    print(f"  {cat}: {count} businesses")

# Find the category with most businesses
top_category, top_business_count = category_counts.most_common(1)[0]
print(f"\nTop category: '{top_category}' with {top_business_count} businesses")

# Get business IDs for the top category
business_ids_in_top_cat = []
for idx, row in df_businesses.iterrows():
    if top_category in row['categories']:
        business_ids_in_top_cat.append(row['business_id_num'])

print(f"Number of business IDs in top category: {len(business_ids_in_top_cat)}")

# Get ratings for businesses in the top category
top_cat_ratings = df_reviews[df_reviews['business_id_num'].isin(business_ids_in_top_cat)]['rating']
print(f"Number of ratings found: {len(top_cat_ratings)}")

# Calculate average rating
if not top_cat_ratings.empty:
    avg_rating = top_cat_ratings.astype(float).mean()
    print(f"Average rating: {avg_rating}")
else:
    avg_rating = 0.0

# Create final result
result = {
    'category': top_category,
    'business_count': len(business_ids_in_top_cat),
    'review_count': len(top_cat_ratings),
    'average_rating': round(avg_rating, 2)
}

print("\n__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_functions.query_db:2': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'name': 'Luminosity', 'review_count': '39', 'is_open': '1', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'True', 'NoiseLevel': "u'quiet'", 'WiFi': "u'no'"}, 'hours': {'Monday': '10:0-21:0', 'Tuesday': '10:0-21:0', 'Wednesday': '10:0-21:0', 'Thursday': '10:0-21:0', 'Friday': '10:0-21:0', 'Saturday': '10:0-21:0', 'Sunday': '11:0-18:0'}, 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:12': {'category': 'Education', 'business_count': 1, 'total_reviews': 6, 'average_rating': 4.17}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
