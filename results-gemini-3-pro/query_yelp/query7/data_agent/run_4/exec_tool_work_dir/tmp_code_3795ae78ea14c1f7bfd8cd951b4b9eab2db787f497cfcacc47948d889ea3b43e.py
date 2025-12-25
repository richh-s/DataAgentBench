code = """import json
import re

# Load data
review_counts_list = locals()['var_function-call-6746499127763040595']
business_details_list = locals()['var_function-call-15041652997040794365']

# Map business_ref to count
# business_ref needs to be converted to business_id for matching
# map business_id -> count
count_map = {}
for item in review_counts_list:
    bid = item['business_ref'].replace('businessref_', 'businessid_')
    count_map[bid] = int(item['review_count'])

# Category tally
category_totals = {}

def parse_categories(description):
    # Normalize
    desc = description.strip()
    if desc.endswith('.'):
        desc = desc[:-1]
    
    # List of markers that precede the category list
    markers = [
        "services in ",
        "services including ",
        " including ",
        "seeking ",
        "fields of ",
        "category of ",
        "destination for "
    ]
    
    # Find the last marker that exists in the string
    found_marker = None
    last_pos = -1
    for m in markers:
        pos = desc.rfind(m)
        if pos > last_pos:
            last_pos = pos
            found_marker = m
            
    if found_marker:
        # Extract the part after the marker
        content = desc[last_pos + len(found_marker):]
        # Clean up quotes if any (e.g. 'Restaurants, Chinese')
        content = content.replace("'", "").replace('"', "")
        
        # Split by commas and 'and'
        # Replace ' and ' with ',' to simplify
        content = content.replace(", and ", ",").replace(" and ", ",")
        
        cats = [c.strip() for c in content.split(',') if c.strip()]
        return cats
    else:
        # Fallback: looks like categories are just at the end?
        # Maybe return empty list or try to guess
        return []

# Process
debug_info = []
for bus in business_details_list:
    bid = bus['business_id']
    desc = bus['description']
    count = count_map.get(bid, 0)
    
    if count > 0:
        cats = parse_categories(desc)
        debug_info.append(f"{bid}: {cats} (from '{desc}')")
        for c in cats:
            category_totals[c] = category_totals.get(c, 0) + count

# Sort categories
sorted_cats = sorted(category_totals.items(), key=lambda x: x[1], reverse=True)

print("__RESULT__:")
print(json.dumps({
    "top_categories": sorted_cats[:5],
    "debug_parsed": debug_info[:5] # Check parsing quality
}))"""

env_args = {'var_function-call-2111835342666136229': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-11772285770280701237': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}], 'var_function-call-6746499127763040595': [{'business_ref': 'businessref_45', 'review_count': '3'}, {'business_ref': 'businessref_33', 'review_count': '3'}, {'business_ref': 'businessref_92', 'review_count': '2'}, {'business_ref': 'businessref_74', 'review_count': '2'}, {'business_ref': 'businessref_66', 'review_count': '2'}, {'business_ref': 'businessref_36', 'review_count': '2'}, {'business_ref': 'businessref_60', 'review_count': '2'}, {'business_ref': 'businessref_96', 'review_count': '2'}, {'business_ref': 'businessref_6', 'review_count': '2'}, {'business_ref': 'businessref_57', 'review_count': '2'}, {'business_ref': 'businessref_51', 'review_count': '2'}, {'business_ref': 'businessref_41', 'review_count': '1'}, {'business_ref': 'businessref_9', 'review_count': '1'}, {'business_ref': 'businessref_8', 'review_count': '1'}, {'business_ref': 'businessref_98', 'review_count': '1'}, {'business_ref': 'businessref_86', 'review_count': '1'}, {'business_ref': 'businessref_15', 'review_count': '1'}, {'business_ref': 'businessref_53', 'review_count': '1'}, {'business_ref': 'businessref_97', 'review_count': '1'}, {'business_ref': 'businessref_12', 'review_count': '1'}, {'business_ref': 'businessref_62', 'review_count': '1'}, {'business_ref': 'businessref_14', 'review_count': '1'}, {'business_ref': 'businessref_20', 'review_count': '1'}, {'business_ref': 'businessref_10', 'review_count': '1'}, {'business_ref': 'businessref_26', 'review_count': '1'}, {'business_ref': 'businessref_72', 'review_count': '1'}, {'business_ref': 'businessref_37', 'review_count': '1'}, {'business_ref': 'businessref_31', 'review_count': '1'}, {'business_ref': 'businessref_68', 'review_count': '1'}, {'business_ref': 'businessref_13', 'review_count': '1'}, {'business_ref': 'businessref_79', 'review_count': '1'}], 'var_function-call-14542254514785404118': {'collection': 'business', 'filter': {'business_id': {'$in': ['businessid_45', 'businessid_33', 'businessid_92', 'businessid_74', 'businessid_66', 'businessid_36', 'businessid_60', 'businessid_96', 'businessid_6', 'businessid_57', 'businessid_51', 'businessid_41', 'businessid_9', 'businessid_8', 'businessid_98', 'businessid_86', 'businessid_15', 'businessid_53', 'businessid_97', 'businessid_12', 'businessid_62', 'businessid_14', 'businessid_20', 'businessid_10', 'businessid_26', 'businessid_72', 'businessid_37', 'businessid_31', 'businessid_68', 'businessid_13', 'businessid_79']}}, 'projection': {'business_id': 1, 'description': 1, '_id': 0}}, 'var_function-call-15041652997040794365': [{'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'business_id': 'businessid_74', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}, {'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'business_id': 'businessid_10', 'description': "Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of 'Restaurants, Chinese'."}]}

exec(code, env_args)
