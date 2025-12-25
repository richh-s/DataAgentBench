code = """import json
import pandas as pd
import re

# Load businesses
businesses = locals()['var_function-call-5541482877209134776']

# Load reviews
with open(locals()['var_function-call-8166027884678298734'], 'r') as f:
    reviews = json.load(f)

# Convert to DataFrames
df_bus = pd.DataFrame(businesses)
df_rev = pd.DataFrame(reviews)

# Function to extract categories
def extract_categories(desc):
    if not desc:
        return []
    
    # Patterns to look for start of categories
    patterns = [
        r"services in (.*)",
        r"services, including (.*)",
        r"services including (.*)",
        r"destination for (.*)",
        r"products in the fields of (.*)"
    ]
    
    categories_str = ""
    for pat in patterns:
        match = re.search(pat, desc, re.IGNORECASE)
        if match:
            categories_str = match.group(1)
            break
            
    if not categories_str:
        return []
        
    # Remove trailing period
    categories_str = categories_str.rstrip('.')
    
    # Split by ',' and ' and '
    # Replace ' and ' with ',' for easier splitting
    categories_str = categories_str.replace(" and ", ", ")
    cats = [c.strip() for c in categories_str.split(',') if c.strip()]
    return cats

# Apply extraction
df_bus['categories'] = df_bus['description'].apply(extract_categories)

# Explode categories
df_exploded = df_bus.explode('categories')

# Filter out rows with no categories
df_exploded = df_exploded[df_exploded['categories'].notna()]
df_exploded = df_exploded[df_exploded['categories'] != ""]

# Count unique businesses per category
cat_counts = df_exploded.groupby('categories')['business_id'].nunique().sort_values(ascending=False)

# Get top category
if cat_counts.empty:
    print("__RESULT__:")
    print(json.dumps({"error": "No categories found"}))
else:
    top_category = cat_counts.index[0]
    top_count = int(cat_counts.iloc[0])
    
    # Get businesses in top category
    top_bus_ids = df_exploded[df_exploded['categories'] == top_category]['business_id'].unique()
    
    # Convert business_id to business_ref format for joining
    # businessid_X -> businessref_X
    top_bus_refs = [bid.replace("businessid_", "businessref_") for bid in top_bus_ids]
    
    # Filter reviews for these businesses
    # Ensure rating is numeric
    df_rev['rating'] = pd.to_numeric(df_rev['rating'], errors='coerce')
    relevant_reviews = df_rev[df_rev['business_ref'].isin(top_bus_refs)]
    
    # Calculate average rating
    avg_rating = relevant_reviews['rating'].mean()
    
    result = {
        "top_category": top_category,
        "business_count": top_count,
        "average_rating": avg_rating
    }
    
    print("__RESULT__:")
    print(json.dumps(result))"""

env_args = {'var_function-call-18061789272839501609': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-5541482877209134776': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}], 'var_function-call-8166027884678298734': 'file_storage/function-call-8166027884678298734.json'}

exec(code, env_args)
