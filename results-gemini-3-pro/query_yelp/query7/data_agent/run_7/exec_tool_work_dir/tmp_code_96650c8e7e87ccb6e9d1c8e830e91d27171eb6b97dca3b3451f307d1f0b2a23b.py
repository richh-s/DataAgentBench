code = """import json
import re

# Load data
sql_results = json.loads(r'''[{"business_ref": "businessref_45", "count": 3}, {"business_ref": "businessref_74", "count": 2}, {"business_ref": "businessref_66", "count": 2}, {"business_ref": "businessref_33", "count": 2}, {"business_ref": "businessref_36", "count": 2}, {"business_ref": "businessref_60", "count": 2}, {"business_ref": "businessref_57", "count": 2}, {"business_ref": "businessref_92", "count": 2}, {"business_ref": "businessref_96", "count": 2}, {"business_ref": "businessref_13", "count": 1}, {"business_ref": "businessref_79", "count": 1}, {"business_ref": "businessref_15", "count": 1}, {"business_ref": "businessref_12", "count": 1}, {"business_ref": "businessref_31", "count": 1}, {"business_ref": "businessref_53", "count": 1}, {"business_ref": "businessref_86", "count": 1}, {"business_ref": "businessref_62", "count": 1}, {"business_ref": "businessref_37", "count": 1}, {"business_ref": "businessref_26", "count": 1}, {"business_ref": "businessref_68", "count": 1}, {"business_ref": "businessref_98", "count": 1}, {"business_ref": "businessref_14", "count": 1}, {"business_ref": "businessref_20", "count": 1}, {"business_ref": "businessref_6", "count": 1}, {"business_ref": "businessref_41", "count": 1}, {"business_ref": "businessref_10", "count": 1}]''')
mongo_file = locals()['var_function-call-13515998265298002616'] # Using file path if large, but here it's result list? Wait, the tool result says "The result is stored under key". If it's small, it's in the key directly? 
# The variable `var_function-call-...` usually holds the JSON object/list directly if it's small. If it was a file path, the preview would say so. 
# Looking at previous output: "The result is: [...]". It seems to be the list itself.
# But wait, the prompt says "If a tool result is large... the storage entry will be the .json file path".
# I'll check if it's a list or string.
mongo_results = mongo_file # Assuming it's the list.

# Map business_id to count
# Normalize business_ref to business_id
# businessref_45 -> businessid_45
count_map = {}
for item in sql_results:
    bid = item['business_ref'].replace('businessref_', 'businessid_')
    count_map[bid] = item['count']

# Process categories
category_counts = {}

def parse_categories(desc):
    # Patterns to look for
    patterns = [
        r"category of\s*['\"]([^'\"]+)['\"]",
        r"fields of\s*(.+?)(?:\.|$)",
        r"services in\s*(.+?)(?:\.|$)",
        r"including\s*(.+?)(?:\.|$)",
        r"destination for\s*(.+?)(?:\.|$)",
        r"seeking\s*(.+?)(?:\.|$)"
    ]
    
    text_to_parse = desc
    
    # Try each pattern
    for pat in patterns:
        match = re.search(pat, desc, re.IGNORECASE)
        if match:
            # If match found, this is likely the category part.
            # However, some descriptions might have multiple keywords. 
            # We want the one closest to the end or the most relevant.
            # But usually the structure is consistent.
            # Let's verify with the captured group.
            content = match.group(1)
            # Remove trailing dot if captured
            if content.endswith('.'):
                content = content[:-1]
            return content
    return ""

def clean_categories(cat_str):
    if not cat_str:
        return []
    # Split by comma and " and "
    # Replace " and " with "," first?
    # "Cosmetics & Beauty Supply" should be kept together.
    # "Hair Salons, Beauty & Spas, ... and Waxing"
    # "and" usually precedes the last item.
    s = cat_str.replace(" and ", ", ") # Careful with "Bed and Breakfast"
    # Wait, "Bed and Breakfast" is a category. replacing " and " might break it?
    # Usually list is: "A, B, C, and D".
    # Regex replace ",? and " with ", " might be safer.
    s = re.sub(r",?\s+and\s+", ", ", cat_str)
    
    parts = s.split(',')
    cats = [p.strip() for p in parts if p.strip()]
    return cats

# Debug: Print parsing results
debug_list = []

if isinstance(mongo_results, str):
    # If it's a file path
    import os
    if os.path.exists(mongo_results):
        with open(mongo_results, 'r') as f:
            mongo_results = json.load(f)
    else:
        # It's probably the string representation of the list if it's not a valid path? 
        # But previous tool execution output showed the list directly.
        pass

for biz in mongo_results:
    bid = biz['business_id']
    if bid in count_map:
        count = count_map[bid]
        desc = biz.get('description', '')
        cat_str = parse_categories(desc)
        cats = clean_categories(cat_str)
        
        debug_list.append(f"{bid}: {desc[:50]}... -> {cats}")
        
        for cat in cats:
            # Handle quotes if remained
            cat = cat.strip("'\"")
            category_counts[cat] = category_counts.get(cat, 0) + count

sorted_cats = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)

print("__RESULT__:")
print(json.dumps({"sorted_cats": sorted_cats, "debug": debug_list}))"""

env_args = {'var_function-call-17842901698263806162': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-17411742535346701157': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-3649926715728267985': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-14509043132087738444': [{'business_ref': 'businessref_45', 'count': '3'}, {'business_ref': 'businessref_74', 'count': '2'}, {'business_ref': 'businessref_66', 'count': '2'}, {'business_ref': 'businessref_33', 'count': '2'}, {'business_ref': 'businessref_36', 'count': '2'}, {'business_ref': 'businessref_60', 'count': '2'}, {'business_ref': 'businessref_57', 'count': '2'}, {'business_ref': 'businessref_92', 'count': '2'}, {'business_ref': 'businessref_96', 'count': '2'}, {'business_ref': 'businessref_13', 'count': '1'}, {'business_ref': 'businessref_79', 'count': '1'}, {'business_ref': 'businessref_15', 'count': '1'}, {'business_ref': 'businessref_12', 'count': '1'}, {'business_ref': 'businessref_31', 'count': '1'}, {'business_ref': 'businessref_53', 'count': '1'}, {'business_ref': 'businessref_86', 'count': '1'}, {'business_ref': 'businessref_62', 'count': '1'}, {'business_ref': 'businessref_37', 'count': '1'}, {'business_ref': 'businessref_26', 'count': '1'}, {'business_ref': 'businessref_68', 'count': '1'}, {'business_ref': 'businessref_98', 'count': '1'}, {'business_ref': 'businessref_14', 'count': '1'}, {'business_ref': 'businessref_20', 'count': '1'}, {'business_ref': 'businessref_6', 'count': '1'}, {'business_ref': 'businessref_41', 'count': '1'}, {'business_ref': 'businessref_10', 'count': '1'}], 'var_function-call-6884879533053385404': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-13515998265298002616': [{'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'name': 'Candy Barrel', 'review_count': '7', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '4', 'BikeParking': 'False'}, 'hours': 'None', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'name': 'Luminosity', 'review_count': '39', 'is_open': '1', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'True', 'NoiseLevel': "u'quiet'", 'WiFi': "u'no'"}, 'hours': {'Monday': '10:0-21:0', 'Tuesday': '10:0-21:0', 'Wednesday': '10:0-21:0', 'Thursday': '10:0-21:0', 'Friday': '10:0-21:0', 'Saturday': '10:0-21:0', 'Sunday': '11:0-18:0'}, 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'_id': '6859a000fe8b31cd7362e2b5', 'business_id': 'businessid_10', 'name': 'China Wok', 'review_count': '20', 'is_open': '1', 'attributes': {'RestaurantsGoodForGroups': 'True', 'RestaurantsDelivery': 'False', 'RestaurantsTakeOut': 'True', 'HasTV': 'True', 'BusinessAcceptsCreditCards': 'True', 'Ambience': "{'touristy': False, 'hipster': False, 'romantic': False, 'divey': False, 'intimate': False, 'trendy': False, 'upscale': False, 'classy': False, 'casual': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': False, 'brunch': False, 'breakfast': False}", 'BusinessParking': "{u'valet': False, u'garage': False, u'street': False, u'lot': True, u'validated': False}"}, 'hours': 'None', 'description': "Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of 'Restaurants, Chinese'."}]}

exec(code, env_args)
