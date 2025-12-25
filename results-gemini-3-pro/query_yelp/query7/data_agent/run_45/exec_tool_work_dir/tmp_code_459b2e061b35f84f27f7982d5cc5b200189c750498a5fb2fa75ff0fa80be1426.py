code = """import json
import re
import pandas as pd

# Load previous results
reviews_data = locals()['var_function-call-11270356130647268502']
# reviews_data is a list of dicts: [{'business_ref': '...', 'review_count': ...}, ...]

business_file_path = locals()['var_function-call-13597253066142582915']
with open(business_file_path, 'r') as f:
    business_data = json.load(f)

# Helper to extract categories from description
def extract_categories(desc):
    # Normalize
    text = desc.strip()
    
    # Patterns
    markers = [
        "providing a range of services in ",
        "including ",
        "destination for ",
        "categories of ",
        "category of ",
        "selection of ",
        "array of dishes in "
    ]
    
    cat_string = ""
    for marker in markers:
        if marker in text:
            parts = text.split(marker)
            if len(parts) > 1:
                cat_string = parts[-1]
                break
    
    if not cat_string:
        return []

    if cat_string.endswith('.'):
        cat_string = cat_string[:-1]
    
    if "seeking " in cat_string:
         cat_string = cat_string.split("seeking ")[-1]

    if " to meet all your" in cat_string:
        cat_string = cat_string.split(" to meet all your")[0]
        
    if " for all your" in cat_string:
        cat_string = cat_string.split(" for all your")[0]

    if "'" in cat_string:
        matches = re.findall(r"'(.*?)'", cat_string)
        if matches:
            cat_string = ", ".join(matches)
            
    items = [x.strip() for x in cat_string.split(',')]
    
    final_cats = []
    for i, item in enumerate(items):
        if item.startswith("and "):
            item = item[4:]
        
        if item:
            final_cats.append(item)
            
    return final_cats

# Process businesses
business_cat_map = {}
for b in business_data:
    b_id = b['business_id']
    desc = b.get('description', '')
    cats = extract_categories(desc)
    ref_id = b_id.replace('businessid_', 'businessref_')
    business_cat_map[ref_id] = cats

# Aggregate reviews
category_counts = {}

for record in reviews_data:
    ref = record['business_ref']
    count = int(record['review_count']) # Convert to int
    
    cats = business_cat_map.get(ref, [])
    
    for cat in cats:
        category_counts[cat] = category_counts.get(cat, 0) + count

# Sort and get top 5
sorted_cats = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)
top_5 = sorted_cats[:5]

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-8990874986253942495': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-14162911161076251475': [{'user_id': 'userid_286', 'name': 'Todd', 'review_count': '376', 'yelping_since': '15 Jan 2009, 16:40', 'useful': '1373', 'funny': '723', 'cool': '639', 'elite': '2010,2011,2012,2013,2014'}], 'var_function-call-16765445317971873260': [{'review_id': 'reviewid_135', 'user_id': 'userid_548', 'business_ref': 'businessref_34', 'rating': '2', 'useful': '0', 'funny': '0', 'cool': '0', 'text': "Sure, it's cheap, but there isn't much to see. I think you'd have to have a big interest in the topic to find it exciting, and kids would be bored. I think it only lasted maybe 10-15 minutes. Our tour person was somewhat knowledgeable and seemed into it, but he didn't give us much time to read the information on each level. I had to take photos of the plaques to read later, and half of them need replacing, as they are so sun-bleached they're virtually unreadable (tour guide said they're being replaced soon and that the other half were already replaced). I really thought it needed to be higher up to give a good view. The Lewis and Clark State Historic Site just down the road was more interesting and free. If you live around here like I do and have nothing better to do, you might want to give it a go if the topic interests you, but if you're a tourist, this is not something you should waste your time on.", 'date': 'August 01, 2016 at 03:44 AM'}], 'var_function-call-11270356130647268502': [{'business_ref': 'businessref_79', 'review_count': '4'}, {'business_ref': 'businessref_13', 'review_count': '2'}, {'business_ref': 'businessref_44', 'review_count': '3'}, {'business_ref': 'businessref_9', 'review_count': '2'}, {'business_ref': 'businessref_25', 'review_count': '1'}, {'business_ref': 'businessref_29', 'review_count': '1'}, {'business_ref': 'businessref_39', 'review_count': '1'}, {'business_ref': 'businessref_6', 'review_count': '2'}, {'business_ref': 'businessref_71', 'review_count': '1'}, {'business_ref': 'businessref_91', 'review_count': '1'}, {'business_ref': 'businessref_16', 'review_count': '1'}, {'business_ref': 'businessref_55', 'review_count': '1'}, {'business_ref': 'businessref_67', 'review_count': '3'}, {'business_ref': 'businessref_15', 'review_count': '2'}, {'business_ref': 'businessref_12', 'review_count': '1'}, {'business_ref': 'businessref_60', 'review_count': '2'}, {'business_ref': 'businessref_51', 'review_count': '1'}, {'business_ref': 'businessref_37', 'review_count': '2'}, {'business_ref': 'businessref_57', 'review_count': '2'}, {'business_ref': 'businessref_8', 'review_count': '1'}, {'business_ref': 'businessref_62', 'review_count': '1'}, {'business_ref': 'businessref_86', 'review_count': '1'}, {'business_ref': 'businessref_85', 'review_count': '1'}, {'business_ref': 'businessref_42', 'review_count': '1'}, {'business_ref': 'businessref_40', 'review_count': '3'}, {'business_ref': 'businessref_61', 'review_count': '1'}, {'business_ref': 'businessref_21', 'review_count': '4'}, {'business_ref': 'businessref_4', 'review_count': '1'}, {'business_ref': 'businessref_88', 'review_count': '2'}, {'business_ref': 'businessref_26', 'review_count': '1'}, {'business_ref': 'businessref_82', 'review_count': '2'}, {'business_ref': 'businessref_45', 'review_count': '1'}, {'business_ref': 'businessref_76', 'review_count': '1'}, {'business_ref': 'businessref_14', 'review_count': '2'}, {'business_ref': 'businessref_3', 'review_count': '2'}, {'business_ref': 'businessref_96', 'review_count': '2'}], 'var_function-call-12285340326297499937': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-11689952881762285706': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-13597253066142582915': 'file_storage/function-call-13597253066142582915.json'}

exec(code, env_args)
