code = """import json

# Read the full business data from file
file_path = var_functions.query_db:8
with open(file_path, 'r') as f:
    businesses = json.load(f)

# Filter businesses that accept credit cards
credit_card_businesses = []
for business in businesses:
    if 'attributes' in business and business['attributes'] != 'None' and business['attributes'] is not None:
        attributes = business['attributes']
        if isinstance(attributes, dict) and 'BusinessAcceptsCreditCards' in attributes:
            if attributes['BusinessAcceptsCreditCards'] == 'True':
                credit_card_businesses.append(business)

# Debug: Check total count and first few records
print('Total credit card businesses:', len(credit_card_businesses))
print('First 3:', credit_card_businesses[:3])

# Extract categories from descriptions
from collections import defaultdict
category_count = defaultdict(int)
business_ids_by_category = defaultdict(list)

for business in credit_card_businesses:
    if 'description' in business and business['description']:
        # Categories are typically listed after "services in" or similar patterns
        desc = business['description'].lower()
        
        # Simple extraction: look for comma-separated lists or key phrases
        # Common patterns: "in the category of", "in the fields of", "offers a range of services in", "makes it a must-visit for"
        import re
        
        patterns = [
            r'fields of ([^\n\.]+)',
            r'category of [\'"]([^\'"]+)[\'"]',
            r'services in ([^\n\.]+)',
            r'offers a range of services including ([^\n\.]+)',
            r'for anyone seeking ([^\n\.]+)'
        ]
        
        categories = []
        for pattern in patterns:
            matches = re.findall(pattern, desc, re.IGNORECASE)
            for match in matches:
                # Split by comma or and
                cats = re.split(r',|\band\b|&', match)
                for cat in cats:
                    cat = cat.strip()
                    if cat:
                        # Remove common stop words at start
                        cat = re.sub(r'^\s*(in|of|for|and|or)\s+', '', cat, flags=re.IGNORECASE)
                        categories.append(cat)
        
        # If no pattern found, look for explicit category listings at end of description
        if not categories and ("'" in desc or '"' in desc):
            # Try to extract quoted categories
            quoted = re.findall(r"[\'\"]([^\'\"]+)[\'\"]", desc)
            if quoted:
                for q in quoted:
                    if len(q.split(',')) > 2:  # Multiple categories
                        cats = q.split(',')
                        categories.extend([c.strip().lower() for c in cats if c.strip()])
        
        # If still no categories, try to extract simple comma-separated lists
        if not categories:
            # Look for patterns like "Restaurants, Chinese" or "Education, Elementary Schools"
            end_part = desc.split('.')[-1]
            comma_separated = re.findall(r'([A-Z][a-z]+(?:\s+&\s+)?[A-Z][a-z]+(?:,\s*[A-Z][a-z]+)+)', business['description'])
            if comma_separated:
                for cs in comma_separated:
                    cats = cs.split(',')
                    categories.extend([c.strip() for c in cats if c.strip()])
        
        # Normalize category names and count
        for cat in categories:
            cat = cat.strip()
            if cat and len(cat) > 2:  # Filter out very short strings
                category_count[cat] += 1
                business_ids_by_category[cat].append(business['business_id'])
        
        # Also store the extracted categories with the business
        business['extracted_categories'] = categories

# Find top category
top_category = max(category_count.items(), key=lambda x: x[1]) if category_count else (None, 0)

print('Top category:', top_category)
print('Total unique categories:', len(category_count))

# Store results
result = {
    'credit_card_businesses': credit_card_businesses,
    'category_count': dict(category_count),
    'top_category_name': top_category[0],
    'top_category_count': top_category[1],
    'business_ids_by_category': dict(business_ids_by_category)
}

print('__RESULT__:')
print(json.dumps(result, default=str))"""

env_args = {'var_functions.list_db:0': ['checkin', 'business'], 'var_functions.query_db:2': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['review', 'tip', 'user'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
