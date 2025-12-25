code = """import json
import re

# Load SQL result
sql_result = locals()['var_function-call-3569218054206668481']
# Load Mongo result (full list)
# The previous tool call result is a list, so I can access it directly if it's in locals.
# Wait, the system prompt says "The result is stored under key... The next message will include both the result... and the storage key name."
# If the result is large, it's a file path. If it's small, it's the object.
# The previous message showed a list, but it might have been truncated in display.
# I should check the type of locals()['var_function-call-1532397386858049905'].
# If it's a string ending in .json, I load it. If it's a list, I use it.

mongo_data = locals()['var_function-call-1532397386858049905']
if isinstance(mongo_data, str) and mongo_data.endswith('.json'):
    with open(mongo_data, 'r') as f:
        businesses = json.load(f)
else:
    businesses = mongo_data

# Create a map of business_id -> count
business_counts = {}
for row in sql_result:
    ref = row['business_ref']
    bid = ref.replace('businessref_', 'businessid_')
    count = int(row['cnt'])
    business_counts[bid] = count

# Category counts
category_counts = {}

def extract_categories(description):
    # Patterns to look for start of categories
    # "services in "
    # "including "
    # "seeking "
    # "fields of "
    # "category of "
    
    # Simple heuristic: Split by common introductory phrases and take the last part.
    phrases = [
        "services in ",
        "including ",
        "seeking ",
        "fields of ",
        "category of "
    ]
    
    cats_str = None
    for phrase in phrases:
        if phrase in description:
            # Split and take the part after the phrase
            # Handle multiple occurrences? Usually just one description.
            # Take the last split just in case?
            parts = description.split(phrase)
            if len(parts) > 1:
                cats_str = parts[-1]
                break # Found one
    
    if not cats_str:
        return []
    
    # Cleanup cats_str
    # It might end with a period.
    cats_str = cats_str.strip()
    if cats_str.endswith('.'):
        cats_str = cats_str[:-1]
    
    # Remove quotes if present (e.g. 'Restaurants, Chinese')
    cats_str = cats_str.strip("'")
    
    # Remove "and " before the last item if present
    # But "and" can be part of a category name? Usually in lists it is "A, B, and C".
    # I'll rely on splitting by ",".
    
    # Split by comma
    items = [x.strip() for x in cats_str.split(',')]
    
    final_cats = []
    for item in items:
        # Check for "and " at the start of the item (for the last item in a list)
        if item.startswith('and '):
            item = item[4:]
        
        # Clean up
        item = item.strip()
        if item:
            final_cats.append(item)
            
    return final_cats

debug_info = []

for biz in businesses:
    bid = biz['business_id']
    desc = biz.get('description', '')
    
    cats = extract_categories(desc)
    
    # Get review count for this business
    count = business_counts.get(bid, 0)
    
    debug_info.append({'bid': bid, 'cats': cats, 'count': count, 'desc': desc})
    
    for cat in cats:
        category_counts[cat] = category_counts.get(cat, 0) + count

# Sort categories by count desc
sorted_cats = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)
top_5 = sorted_cats[:5]

print("__RESULT__:")
print(json.dumps({"top_5": top_5, "debug": debug_info}))"""

env_args = {'var_function-call-16297084049708208247': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-3569218054206668481': [{'business_ref': 'businessref_13', 'cnt': '1'}, {'business_ref': 'businessref_79', 'cnt': '1'}, {'business_ref': 'businessref_74', 'cnt': '2'}, {'business_ref': 'businessref_66', 'cnt': '2'}, {'business_ref': 'businessref_15', 'cnt': '1'}, {'business_ref': 'businessref_33', 'cnt': '2'}, {'business_ref': 'businessref_36', 'cnt': '2'}, {'business_ref': 'businessref_60', 'cnt': '2'}, {'business_ref': 'businessref_12', 'cnt': '1'}, {'business_ref': 'businessref_31', 'cnt': '1'}, {'business_ref': 'businessref_53', 'cnt': '1'}, {'business_ref': 'businessref_92', 'cnt': '2'}, {'business_ref': 'businessref_26', 'cnt': '1'}, {'business_ref': 'businessref_68', 'cnt': '1'}, {'business_ref': 'businessref_41', 'cnt': '1'}, {'business_ref': 'businessref_10', 'cnt': '1'}, {'business_ref': 'businessref_45', 'cnt': '3'}, {'business_ref': 'businessref_96', 'cnt': '2'}, {'business_ref': 'businessref_98', 'cnt': '1'}, {'business_ref': 'businessref_14', 'cnt': '1'}, {'business_ref': 'businessref_20', 'cnt': '1'}, {'business_ref': 'businessref_6', 'cnt': '1'}, {'business_ref': 'businessref_57', 'cnt': '2'}, {'business_ref': 'businessref_86', 'cnt': '1'}, {'business_ref': 'businessref_62', 'cnt': '1'}, {'business_ref': 'businessref_37', 'cnt': '1'}], 'var_function-call-13561583767062779772': ['businessid_13', 'businessid_79', 'businessid_74', 'businessid_66', 'businessid_15', 'businessid_33', 'businessid_36', 'businessid_60', 'businessid_12', 'businessid_31', 'businessid_53', 'businessid_92', 'businessid_26', 'businessid_68', 'businessid_41', 'businessid_10', 'businessid_45', 'businessid_96', 'businessid_98', 'businessid_14', 'businessid_20', 'businessid_6', 'businessid_57', 'businessid_86', 'businessid_62', 'businessid_37'], 'var_function-call-1532397386858049905': [{'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'name': 'Candy Barrel', 'review_count': '7', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '4', 'BikeParking': 'False'}, 'hours': 'None', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'name': 'Luminosity', 'review_count': '39', 'is_open': '1', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'True', 'NoiseLevel': "u'quiet'", 'WiFi': "u'no'"}, 'hours': {'Monday': '10:0-21:0', 'Tuesday': '10:0-21:0', 'Wednesday': '10:0-21:0', 'Thursday': '10:0-21:0', 'Friday': '10:0-21:0', 'Saturday': '10:0-21:0', 'Sunday': '11:0-18:0'}, 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'_id': '6859a000fe8b31cd7362e2b5', 'business_id': 'businessid_10', 'name': 'China Wok', 'review_count': '20', 'is_open': '1', 'attributes': {'RestaurantsGoodForGroups': 'True', 'RestaurantsDelivery': 'False', 'RestaurantsTakeOut': 'True', 'HasTV': 'True', 'BusinessAcceptsCreditCards': 'True', 'Ambience': "{'touristy': False, 'hipster': False, 'romantic': False, 'divey': False, 'intimate': False, 'trendy': False, 'upscale': False, 'classy': False, 'casual': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': False, 'brunch': False, 'breakfast': False}", 'BusinessParking': "{u'valet': False, u'garage': False, u'street': False, u'lot': True, u'validated': False}"}, 'hours': 'None', 'description': "Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of 'Restaurants, Chinese'."}]}

exec(code, env_args)
