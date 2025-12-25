code = """import json
import re

# Load data
review_counts_data = locals()['var_function-call-3593452875317703037']
business_file = locals()['var_function-call-13352177957018971692']

with open(business_file, 'r') as f:
    businesses_data = json.load(f)

# Process review counts
biz_review_map = {}
for item in review_counts_data:
    ref = item['business_ref']
    count = int(item['review_cnt'])
    if '_' in ref:
        id_part = ref.split('_')[1]
        biz_review_map[id_part] = count

category_totals = {}

# Keywords to find start of categories
start_phrases = [
    "category of ", "categories of ", "fields of ", 
    "services in ", "including ", "destination for ", 
    "seeking ", "selection of "
]

# Phrases to remove from end
end_phrases = [
    " for all your", " to meet all your", " making it a must-visit"
]

for biz in businesses_data:
    if 'business_id' not in biz or 'description' not in biz:
        continue
    
    bid_str = biz['business_id']
    if '_' in bid_str:
        id_part = bid_str.split('_')[1]
    else:
        continue
        
    count = biz_review_map.get(id_part, 0)
    if count == 0:
        continue

    desc = biz['description']
    
    # Identify the start of the category list
    # We pick the start_phrase that appears latest in the description
    # but before the actual list
    best_start_idx = -1
    best_phrase_len = 0
    
    for phrase in start_phrases:
        idx = desc.rfind(phrase)
        if idx != -1:
            # Check if this index is 'better'
            # We want the rightmost trigger
            if idx > best_start_idx:
                best_start_idx = idx
                best_phrase_len = len(phrase)
    
    if best_start_idx != -1:
        cat_str = desc[best_start_idx + best_phrase_len:]
    else:
        # Fallback: maybe the description IS the list? Unlikely.
        # Or maybe "offers X, Y, Z".
        # Check for "offers "
        idx = desc.rfind("offers ")
        if idx != -1:
            cat_str = desc[idx + 7:]
        else:
            continue

    # Cleanup end
    for end_p in end_phrases:
        if end_p in cat_str:
            cat_str = cat_str.split(end_p)[0]
    
    # Remove trailing period
    cat_str = cat_str.strip().rstrip('.')
    # Remove quotes
    cat_str = cat_str.replace("'", "").replace('"', "")
    
    # Split
    # Handle " and "
    # "A, B, and C" -> "A, B, C"
    # "A and B" -> "A, B"
    # But "Bed and Breakfast" shouldn't be split.
    # Standard Yelp categories don't usually start with "and ".
    # The list is usually comma separated.
    # The last item might be preceded by "and".
    
    # Regex split by comma
    parts = cat_str.split(',')
    
    parsed_cats = []
    for p in parts:
        p = p.strip()
        if p.startswith('and '):
            p = p[4:].strip()
        
        # Verify it looks like a category (Capitalized)
        if p and p[0].isupper():
            parsed_cats.append(p)
    
    for c in parsed_cats:
        category_totals[c] = category_totals.get(c, 0) + count

# Sort
sorted_cats = sorted(category_totals.items(), key=lambda x: x[1], reverse=True)
top_5 = sorted_cats[:5]

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-6189912303136514232': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-14488034719695753707': [{'yelping_since': '15 Jan 2009, 16:40'}, {'yelping_since': '13 Jul 2010, 15:42'}, {'yelping_since': '2010-09-07 23:24:36'}, {'yelping_since': 'October 23, 2011 at 07:47 PM'}, {'yelping_since': '2011-08-30 13:46:26'}], 'var_function-call-3593452875317703037': [{'business_ref': 'businessref_79', 'review_cnt': '8'}, {'business_ref': 'businessref_44', 'review_cnt': '4'}, {'business_ref': 'businessref_13', 'review_cnt': '3'}, {'business_ref': 'businessref_6', 'review_cnt': '4'}, {'business_ref': 'businessref_71', 'review_cnt': '1'}, {'business_ref': 'businessref_91', 'review_cnt': '2'}, {'business_ref': 'businessref_46', 'review_cnt': '1'}, {'business_ref': 'businessref_1', 'review_cnt': '1'}, {'business_ref': 'businessref_47', 'review_cnt': '1'}, {'business_ref': 'businessref_16', 'review_cnt': '1'}, {'business_ref': 'businessref_55', 'review_cnt': '1'}, {'business_ref': 'businessref_29', 'review_cnt': '1'}, {'business_ref': 'businessref_39', 'review_cnt': '1'}, {'business_ref': 'businessref_67', 'review_cnt': '5'}, {'business_ref': 'businessref_15', 'review_cnt': '3'}, {'business_ref': 'businessref_33', 'review_cnt': '5'}, {'business_ref': 'businessref_81', 'review_cnt': '1'}, {'business_ref': 'businessref_36', 'review_cnt': '3'}, {'business_ref': 'businessref_12', 'review_cnt': '4'}, {'business_ref': 'businessref_60', 'review_cnt': '4'}, {'business_ref': 'businessref_89', 'review_cnt': '3'}, {'business_ref': 'businessref_17', 'review_cnt': '1'}, {'business_ref': 'businessref_43', 'review_cnt': '3'}, {'business_ref': 'businessref_31', 'review_cnt': '1'}, {'business_ref': 'businessref_99', 'review_cnt': '1'}, {'business_ref': 'businessref_9', 'review_cnt': '3'}, {'business_ref': 'businessref_74', 'review_cnt': '2'}, {'business_ref': 'businessref_25', 'review_cnt': '1'}, {'business_ref': 'businessref_66', 'review_cnt': '2'}, {'business_ref': 'businessref_53', 'review_cnt': '1'}, {'business_ref': 'businessref_51', 'review_cnt': '3'}, {'business_ref': 'businessref_40', 'review_cnt': '3'}, {'business_ref': 'businessref_7', 'review_cnt': '2'}, {'business_ref': 'businessref_92', 'review_cnt': '2'}, {'business_ref': 'businessref_61', 'review_cnt': '1'}, {'business_ref': 'businessref_37', 'review_cnt': '6'}, {'business_ref': 'businessref_57', 'review_cnt': '7'}, {'business_ref': 'businessref_8', 'review_cnt': '4'}, {'business_ref': 'businessref_56', 'review_cnt': '1'}, {'business_ref': 'businessref_62', 'review_cnt': '2'}, {'business_ref': 'businessref_86', 'review_cnt': '4'}, {'business_ref': 'businessref_97', 'review_cnt': '1'}, {'business_ref': 'businessref_72', 'review_cnt': '1'}, {'business_ref': 'businessref_85', 'review_cnt': '1'}, {'business_ref': 'businessref_42', 'review_cnt': '1'}, {'business_ref': 'businessref_88', 'review_cnt': '4'}, {'business_ref': 'businessref_21', 'review_cnt': '4'}, {'business_ref': 'businessref_26', 'review_cnt': '4'}, {'business_ref': 'businessref_68', 'review_cnt': '1'}, {'business_ref': 'businessref_4', 'review_cnt': '1'}, {'business_ref': 'businessref_23', 'review_cnt': '1'}, {'business_ref': 'businessref_41', 'review_cnt': '1'}, {'business_ref': 'businessref_10', 'review_cnt': '1'}, {'business_ref': 'businessref_45', 'review_cnt': '5'}, {'business_ref': 'businessref_82', 'review_cnt': '2'}, {'business_ref': 'businessref_76', 'review_cnt': '1'}, {'business_ref': 'businessref_14', 'review_cnt': '3'}, {'business_ref': 'businessref_3', 'review_cnt': '2'}, {'business_ref': 'businessref_96', 'review_cnt': '4'}, {'business_ref': 'businessref_98', 'review_cnt': '3'}, {'business_ref': 'businessref_22', 'review_cnt': '1'}, {'business_ref': 'businessref_20', 'review_cnt': '1'}], 'var_function-call-14503387314847266168': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-9144042560795515851': [['Beauty & Spas', 6], ['Nail Salons', 5], ['Hair Removal', 5], ['Waxing', 5], ['Gun/Rifle Ranges', 4]], 'var_function-call-13905227478667609543': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-13352177957018971692': 'file_storage/function-call-13352177957018971692.json'}

exec(code, env_args)
