code = """import json
import re
import collections

filename = locals()['var_function-call-19678560926327217']
with open(filename, 'r') as f:
    businesses = json.load(f)

category_counts = collections.defaultdict(int)
category_businesses = collections.defaultdict(list)

def extract_categories(description):
    if not description:
        return []
    
    # Regex pattern
    # Use \\s for \s in JSON
    pattern = re.compile(r"(?:services in|including|fields of|destination for|selection of|category of|categories of|variety of services including)\s+(.*)", re.IGNORECASE)
    match = pattern.search(description)
    
    if not match:
        return []
        
    list_str = match.group(1)
    
    end_markers = [" to meet all your", " for all your"]
    for marker in end_markers:
        idx = list_str.find(marker)
        if idx != -1:
            list_str = list_str[:idx]
            
    # Clean up quotes and periods
    # list_str = list_str.replace('"', '').replace("'", "").strip(".")
    # In JSON:
    list_str = list_str.replace('"', '').replace("'", "").strip(".")
    
    # Split
    parts = re.split(r",| and | & ", list_str)
    
    cleaned_categories = []
    for part in parts:
        c = part.strip()
        if c:
            cleaned_categories.append(c)
            
    return cleaned_categories

for b in businesses:
    desc = b.get('description', '')
    cats = extract_categories(desc)
    bid = b.get('business_id')
    
    for cat in cats:
        category_counts[cat] += 1
        category_businesses[cat].append(bid)

if category_counts:
    top_category = max(category_counts, key=category_counts.get)
    count = category_counts[top_category]
    top_business_ids = category_businesses[top_category]
else:
    top_category = None
    count = 0
    top_business_ids = []

business_refs = [bid.replace("businessid_", "businessref_") for bid in top_business_ids]

print("__RESULT__:")
print(json.dumps({
    "top_category": top_category,
    "count": count,
    "business_refs": business_refs
}))"""

env_args = {'var_function-call-17856246893402406059': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-2693524415427068630': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'name': 'Luminosity', 'review_count': '39', 'is_open': '1', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'True', 'NoiseLevel': "u'quiet'", 'WiFi': "u'no'"}, 'hours': {'Monday': '10:0-21:0', 'Tuesday': '10:0-21:0', 'Wednesday': '10:0-21:0', 'Thursday': '10:0-21:0', 'Friday': '10:0-21:0', 'Saturday': '10:0-21:0', 'Sunday': '11:0-18:0'}, 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}], 'var_function-call-8092589546513333020': {'top_category': 'Beauty & Spas', 'count': 3, 'top_business_ids_count': 3, 'sample_ids': ['businessid_47', 'businessid_33', 'businessid_92']}, 'var_function-call-19678560926327217': 'file_storage/function-call-19678560926327217.json'}

exec(code, env_args)
