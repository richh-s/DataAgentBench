code = """import json

# Read the business data
business_data = locals()['var_functions.query_db:6']

# Function to extract categories from description
def extract_categories(description):
    if not description or description == "None":
        return []
    
    categories = []
    desc_lower = description.lower()
    
    # Look for common patterns
    if "category of" in desc_lower:
        # Extract text after "category of"
        parts = desc_lower.split("category of")
        if len(parts) > 1:
            cat_text = parts[1].strip(" .'")
            # Extract comma-separated categories
            cats = [c.strip().capitalize() for c in cat_text.split(",")]
            categories.extend(cats)
    
    if "services in" in desc_lower and "range of services" in desc_lower:
        # Extract text after "services in"
        parts = desc_lower.split("services in")
        if len(parts) > 1:
            cat_text = parts[1].strip(" .'")
            # Extract comma-separated categories
            cats = [c.strip().capitalize() for c in cat_text.split(",")]
            categories.extend(cats)
    
    if "services including" in desc_lower:
        # Extract text after "services including"
        parts = desc_lower.split("services including")
        if len(parts) > 1:
            cat_text = parts[1].strip(" .'")
            # Extract comma-separated categories
            cats = [c.strip().capitalize() for c in cat_text.split(",")]
            categories.extend(cats)
    
    if "offers" in desc_lower and "services" in desc_lower:
        # More complex pattern
        if "offers a" in desc_lower:
            parts = desc_lower.split("offers a")
            if len(parts) > 1:
                cat_text = parts[1].split(".")[0].strip()
                if "range of" in cat_text:
                    cat_text = cat_text.split("range of")[1].strip()
                if "services" in cat_text:
                    cat_text = cat_text.split("services")[1].strip()
                cat_text = cat_text.strip(" inincludingfor .'")
                cats = [c.strip().capitalize() for c in cat_text.split(",")]
                categories.extend(cats)
    
    # Clean up
    categories = [c for c in categories if c and c not in ['', 'None', 'And']]
    return categories

# Process all businesses
businesses_with_categories = []
for biz in business_data:
    # Check if accepts credit cards
    accepts_credit = False
    if biz.get('attributes') and biz['attributes'] != 'None':
        attrs = biz['attributes']
        if isinstance(attrs, dict) and 'BusinessAcceptsCreditCards' in attrs:
            accepts_credit = attrs['BusinessAcceptsCreditCards'] == 'True'
    
    # Extract categories
    description = biz.get('description', '')
    categories = extract_categories(description)
    
    businesses_with_categories.append({
        'business_id': biz['business_id'],
        'accepts_credit_cards': accepts_credit,
        'categories': categories
    })

# Count businesses by category that accept credit cards
from collections import defaultdict
category_counts = defaultdict(int)
category_business_ids = defaultdict(list)

for biz in businesses_with_categories:
    if biz['accepts_credit_cards']:
        for cat in biz['categories']:
            # Clean up category names
            clean_cat = cat.strip()
            if clean_cat:
                category_counts[clean_cat] += 1
                category_business_ids[clean_cat].append(biz['business_id'])

# Find top category
if category_counts:
    top_category = max(category_counts.items(), key=lambda x: x[1])
    print('__RESULT__:')
    print(json.dumps({
        'top_category': top_category[0],
        'business_count': top_category[1],
        'category_business_ids': category_business_ids[top_category[0]]
    }))
else:
    print('__RESULT__:')
    print(json.dumps({'error': 'No categories found'}))"""

env_args = {'var_functions.list_db:0': ['checkin', 'business'], 'var_functions.query_db:2': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'attributes': 'None'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'attributes': 'None', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}]}

exec(code, env_args)
