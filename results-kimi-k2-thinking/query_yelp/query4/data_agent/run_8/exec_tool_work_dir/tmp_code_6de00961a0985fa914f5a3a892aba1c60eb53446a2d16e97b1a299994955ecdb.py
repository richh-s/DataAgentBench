code = """import json
import re

# Read the full result from the file
file_path = var_functions.query_db:5
with open(file_path, 'r') as f:
    credit_card_businesses = json.load(f)

# Function to extract categories from description
def extract_categories(description):
    """Extract business categories from description field."""
    if not description:
        return []
    
    # Look for patterns like "in the fields of X, Y, and Z" or "in the categories of X, Y, Z"
    # or "services in X, Y, Z" or just lists at the end
    
    # Try to find patterns that list categories
    patterns = [
        r'fields of ([^\.]+)',  # "fields of Cosmetics & Beauty Supply, Cosmetic Dentists..."
        r'categories of ([^\.]+)',  # "categories of Medical Centers, Health & Medical"
        r'services in ([^\.]+)',  # "services in Education, Elementary Schools..."
        r'range of services including ([^\.]+)',  # "services including Nail Salons, Hair Removal..."
        r'offers a ([^\.,]+)',  # general capture
        r'array of ([^\.]+)',  # "array of dishes in the category of 'Restaurants, Chinese'"
        r'category of \'([^\']+)\''  # "category of 'Restaurants, Chinese'"
    ]
    
    categories = []
    for pattern in patterns:
        matches = re.findall(pattern, description, re.IGNORECASE)
        for match in matches:
            # Split by commas and clean up each category
            parts = match.split(',')
            for part in parts:
                # Remove "and" from the last item if present
                part = part.strip()
                if part.startswith('and '):
                    part = part[4:].strip()
                
                # Clean up the category name
                part = part.replace('"', '').replace("'", "").strip()
                
                # Skip empty or generic phrases
                if part and len(part) > 2 and not part.lower().startswith('including'):
                    # Further split by "and" if there are multiple categories joined by "and"
                    if ' and ' in part:
                        subparts = part.split(' and ')
                        for subpart in subparts:
                            subpart = subpart.strip()
                            if subpart and len(subpart) > 2:
                                categories.append(subpart)
                    else:
                        categories.append(part)
    
    return categories

# Extract business_id and categories for businesses that accept credit cards
business_data = []
for business in credit_card_businesses:
    business_id = business.get('business_id', '')
    description = business.get('description', '')
    
    # Extract the numeric ID for joining later
    numeric_id = business_id.replace('businessid_', '') if business_id else ''
    
    categories = extract_categories(description)
    
    # If no categories extracted, try a simpler approach - look for patterns at end of description
    if not categories and description:
        # Look for patterns like "X, Y, and Z." at the end
        desc_lower = description.lower()
        if 'services' in desc_lower or 'categories' in desc_lower or 'fields' in desc_lower:
            # Try to extract everything after certain keywords
            for keyword in ['services in ', 'services including ', 'fields of ', 'categories of ']:
                if keyword in desc_lower:
                    start_idx = desc_lower.rfind(keyword) + len(keyword)
                    end_idx = description.find('.', start_idx)
                    if end_idx == -1:
                        end_idx = len(description)
                    
                    category_text = description[start_idx:end_idx].strip()
                    
                    # Split by commas
                    parts = category_text.split(',')
                    for part in parts:
                        part = part.strip()
                        if part.startswith('and '):
                            part = part[4:].strip()
                        
                        # Clean up
                        part = part.replace('"', '').replace("'", "").strip()
                        
                        if part and len(part) > 2:
                            if ' and ' in part:
                                subparts = part.split(' and ')
                                for subpart in subparts:
                                    subpart = subpart.strip()
                                    if subpart and len(subpart) > 2:
                                        categories.append(subpart)
                            else:
                                categories.append(part)
                    break
    
    business_data.append({
        'business_id': business_id,
        'numeric_id': numeric_id,
        'name': business.get('name', ''),
        'categories': categories,
        'description': description
    })

# Count businesses per category
category_counts = {}
category_businesses = {}  # Track which businesses belong to each category

for business in business_data:
    for category in business['categories']:
        category_counts[category] = category_counts.get(category, 0) + 1
        if category not in category_businesses:
            category_businesses[category] = []
        category_businesses[category].append(business['numeric_id'])

# Sort categories by count
sorted_categories = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)

# Print top categories
print('__RESULT__:')
print(json.dumps({
    'top_categories': sorted_categories[:10],
    'total_businesses': len(business_data),
    'distinct_categories': len(category_counts)
}))"""

env_args = {'var_functions.query_db:0': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.query_db:2': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'name': 'Luminosity', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'True', 'NoiseLevel': "u'quiet'", 'WiFi': "u'no'"}, 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
