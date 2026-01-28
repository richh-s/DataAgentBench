code = """import json
import pandas as pd
import re
from collections import defaultdict

# Read the full result file
file_path = locals()['var_functions.query_db:4']
with open(file_path, 'r') as file:
    businesses = json.load(file)

# Create DataFrame
import pandas as pd
df_business = pd.DataFrame(businesses)

# Check for credit card acceptance and extract categories from description
credit_card_businesses = []

for i, row in df_business.iterrows():
    # Check if accepts credit cards
    accepts_cc = False
    if pd.notna(row['attributes']):
        if isinstance(row['attributes'], dict):
            cc_value = row['attributes'].get('BusinessAcceptsCreditCards')
        else:
            # Handle string representation
            attr_str = str(row['attributes'])
            cc_value = None
        
        if cc_value == 'True' or cc_value == True or (isinstance(row['attributes'], dict) and str(row['attributes'].get('BusinessAcceptsCreditCards')).lower() == 'true'):
            accepts_cc = True
    
    # If accepts credit cards, extract categories
    if accepts_cc:
        categories = []
        if pd.notna(row['description']):
            desc = row['description']
            # Extract categories from description
            if 'category of' in desc:
                parts = desc.split('category of')
                if len(parts) > 1:
                    cat_part = parts[1].strip().rstrip('.')
                    # Clean up categories
                    cat_part = cat_part.replace("'", "").strip()
                    if cat_part.startswith('\\"') and cat_part.endswith('\\"'):
                        cat_part = cat_part[2:-2]
                    
                    # Split by comma
                    if ',' in cat_part:
                        cats = [c.strip() for c in cat_part.split(',')]
                        categories.extend(cats)
                    else:
                        categories.append(cat_part)

        credit_card_businesses.append({
            'business_id': row['business_id'],
            'name': row['name'],
            'accepts_cc': True,
            'categories': categories,
            'review_count': row.get('review_count', 0) if row.get('review_count') != 'None' else 0
        })

# Calculate category counts
category_counts = defaultdict(int)
businesses_by_category = defaultdict(list)

for biz in credit_card_businesses:
    if biz['categories']:
        for cat in biz['categories']:
            if cat:  # Skip empty categories
                category_counts[cat] += 1
                businesses_by_category[cat].append(biz)

# Sort by count
top_categories = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)

print('__RESULT__:')
print({
    'total_businesses_with_cc': len(credit_card_businesses),
    'top_categories': top_categories[:10],
    'sample_business': credit_card_businesses[0] if credit_card_businesses else None
})"""

env_args = {'var_functions.list_db:0': ['business', 'checkin'], 'var_functions.query_db:2': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'name': 'Candy Barrel', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '4', 'BikeParking': 'False'}}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'name': 'Luminosity', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'True', 'NoiseLevel': "u'quiet'", 'WiFi': "u'no'"}}, {'_id': '6859a000fe8b31cd7362e2b2', 'business_id': 'businessid_64', 'name': 'Nail Care Salon', 'attributes': {'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': True, 'valet': False}", 'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'True', 'WiFi': "u'free'"}}, {'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52', 'name': 'Architectural Antiques of Indianapolis', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'BikeParking': 'True'}}, {'_id': '6859a000fe8b31cd7362e2b4', 'business_id': 'businessid_29', 'name': "Aster's Floral Shop", 'attributes': {'BikeParking': 'True', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsPriceRange2': '2', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsDelivery': 'None'}}, {'_id': '6859a000fe8b31cd7362e2b5', 'business_id': 'businessid_10', 'name': 'China Wok', 'attributes': {'RestaurantsGoodForGroups': 'True', 'RestaurantsDelivery': 'False', 'RestaurantsTakeOut': 'True', 'HasTV': 'True', 'BusinessAcceptsCreditCards': 'True', 'Ambience': "{'touristy': False, 'hipster': False, 'romantic': False, 'divey': False, 'intimate': False, 'trendy': False, 'upscale': False, 'classy': False, 'casual': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': False, 'brunch': False, 'breakfast': False}", 'BusinessParking': "{u'valet': False, u'garage': False, u'street': False, u'lot': True, u'validated': False}"}}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
