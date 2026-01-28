code = """import json

# Get the full business data from the file
business_data_file = locals()['var_functions.query_db:6']
if isinstance(business_data_file, str) and business_data_file.endswith('.json'):
    with open(business_data_file, 'r') as f:
        business_data = json.load(f)
else:
    business_data = business_data_file

print(f"Total businesses in sample: {len(business_data)}")

# Function to extract categories from description
def extract_categories(description):
    if not description or description == "None" or description == "None":
        return []
    
    categories = []
    desc_lower = description.lower()
    
    # Look for the phrase "services in" or "services including" or "category of"
    if "services in" in desc_lower:
        parts = desc_lower.split("services in")
        if len(parts) > 1:
            cat_text = parts[1].strip(" .'")
            # Extract comma-separated categories
            cats = [c.strip().capitalize() for c in cat_text.split(",")]
            categories.extend(cats)
    elif "services including" in desc_lower:
        parts = desc_lower.split("services including")
        if len(parts) > 1:
            cat_text = parts[1].strip(" .'")
            cats = [c.strip().capitalize() for c in cat_text.split(",")]
            categories.extend(cats)
    elif "category of" in desc_lower:
        parts = desc_lower.split("category of")
        if len(parts) > 1:
            cat_text = parts[1].strip(" .'")
            cats = [c.strip().capitalize() for c in cat_text.split(",")]
            categories.extend(cats)
    elif "offers a" in desc_lower and "range of" in desc_lower:
        # Extract after "range of"
        parts = desc_lower.split("range of")
        if len(parts) > 1:
            cat_text = parts[1].split(".")[0].strip()
            if "services" in cat_text:
                cat_text = cat_text.split("services")[1].strip()
            cats = [c.strip().capitalize() for c in cat_text.split(",")]
            categories.extend(cats)
    elif "offers" in desc_lower:
        # More general pattern
        parts = desc_lower.split("offers")
        if len(parts) > 1:
            cat_text = parts[1].split(".")[0].strip()
            if "services" in cat_text:
                cat_text = cat_text.split("services")[1].strip()
            cats = [c.strip().capitalize() for c in cat_text.split(",")]
            categories.extend(cats)
    
    # Clean up
    categories = [c for c in categories if c and c not in ['', 'None', 'And', 'making', 'to', 'a']]
    return categories

# Process businesses
category_counts = {}
category_businesses = {}  # Store unique business IDs per category

for biz in business_data:
    # Check if business accepts credit cards
    accepts_credit = False
    if biz.get('attributes') and biz['attributes'] != 'None' and biz['attributes'] != 'None':
        attrs = biz['attributes']
        if isinstance(attrs, dict) and 'BusinessAcceptsCreditCards' in attrs:
            accepts_credit = attrs['BusinessAcceptsCreditCards'] == 'True'
    
    if accepts_credit:
        # Extract categories
        description = biz.get('description', '')
        categories = extract_categories(description)
        
        business_id = biz['business_id']
        
        for cat in categories:
            clean_cat = cat.strip()
            if clean_cat:
                if clean_cat not in category_counts:
                    category_counts[clean_cat] = 0
                    category_businesses[clean_cat] = set()
                
                category_counts[clean_cat] += 1
                category_businesses[clean_cat].add(business_id)

# Sort categories by count
sorted_categories = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)

print('__RESULT__:')
print(json.dumps({
    'total_businesses_accepting_credit': len(business_data),
    'category_summary': sorted_categories[:10],  # Top 10
    'category_businesses_sample': {cat: list(biz_ids) for cat, biz_ids in list(category_businesses.items())[:5]}
}))"""

env_args = {'var_functions.list_db:0': ['checkin', 'business'], 'var_functions.query_db:2': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'attributes': 'None'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'attributes': 'None', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.execute_python:8': {'top_category': 'Beauty & spas', 'business_count': 4, 'category_business_ids': ['businessid_47', 'businessid_33', 'businessid_33', 'businessid_33']}, 'var_functions.list_db:10': ['review', 'tip', 'user'], 'var_functions.execute_python:12': ['businessref_47', 'businessref_33', 'businessref_33', 'businessref_33'], 'var_functions.execute_python:14': ['businessref_47', 'businessref_33'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
