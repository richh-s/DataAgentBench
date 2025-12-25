code = """import json
import re

# Load data
review_counts_data = locals()['var_function-call-3593452875317703037']
businesses_data = locals()['var_function-call-14503387314847266168']

# Process review counts into a dict: business_id_suffix -> count
# business_ref format: "businessref_X" -> X
biz_review_map = {}
for item in review_counts_data:
    ref = item['business_ref']
    count = int(item['review_cnt'])
    # Extract ID part
    if '_' in ref:
        id_part = ref.split('_')[1]
        biz_review_map[id_part] = count

# Process businesses and aggregate categories
category_totals = {}

keywords = ["services in ", "including ", "destination for "]

for biz in businesses_data:
    if 'business_id' not in biz or 'description' not in biz:
        continue
    
    bid_str = biz['business_id']
    # business_id format: "businessid_X" -> X
    if '_' in bid_str:
        id_part = bid_str.split('_')[1]
    else:
        continue
        
    # Get review count for this business
    count = biz_review_map.get(id_part, 0)
    
    if count == 0:
        continue

    desc = biz['description']
    # Extract categories
    # Find the start of the category list
    categories_str = None
    for kw in keywords:
        if kw in desc:
            # We assume the last occurrence or the one introducing the list is what we want.
            # descriptions seem to have only one such phrase usually.
            parts = desc.split(kw)
            if len(parts) > 1:
                categories_str = parts[-1]
                break
    
    if categories_str:
        # Clean up the string
        # Remove trailing period
        categories_str = categories_str.strip().rstrip('.')
        
        # Split by comma and 'and'
        # Example: "A, B, and C" -> ["A", "B", "and C"] -> handle "and"
        # Replace " and " with "," to make splitting easier? 
        # But be careful about "Bed and Breakfast".
        # Usually the list is "A, B, ..., and Z". The oxford comma might be there or not.
        # "X, Y and Z"
        
        # Simple approach: split by ',' first.
        segments = categories_str.split(',')
        cleaned_cats = []
        for seg in segments:
            seg = seg.strip()
            if seg.startswith('and '):
                seg = seg[4:].strip()
            if seg:
                cleaned_cats.append(seg)
        
        # Add count to totals
        for cat in cleaned_cats:
            category_totals[cat] = category_totals.get(cat, 0) + count

# Sort and get top 5
sorted_cats = sorted(category_totals.items(), key=lambda x: x[1], reverse=True)
top_5 = sorted_cats[:5]

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-6189912303136514232': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-14488034719695753707': [{'yelping_since': '15 Jan 2009, 16:40'}, {'yelping_since': '13 Jul 2010, 15:42'}, {'yelping_since': '2010-09-07 23:24:36'}, {'yelping_since': 'October 23, 2011 at 07:47 PM'}, {'yelping_since': '2011-08-30 13:46:26'}], 'var_function-call-3593452875317703037': [{'business_ref': 'businessref_79', 'review_cnt': '8'}, {'business_ref': 'businessref_44', 'review_cnt': '4'}, {'business_ref': 'businessref_13', 'review_cnt': '3'}, {'business_ref': 'businessref_6', 'review_cnt': '4'}, {'business_ref': 'businessref_71', 'review_cnt': '1'}, {'business_ref': 'businessref_91', 'review_cnt': '2'}, {'business_ref': 'businessref_46', 'review_cnt': '1'}, {'business_ref': 'businessref_1', 'review_cnt': '1'}, {'business_ref': 'businessref_47', 'review_cnt': '1'}, {'business_ref': 'businessref_16', 'review_cnt': '1'}, {'business_ref': 'businessref_55', 'review_cnt': '1'}, {'business_ref': 'businessref_29', 'review_cnt': '1'}, {'business_ref': 'businessref_39', 'review_cnt': '1'}, {'business_ref': 'businessref_67', 'review_cnt': '5'}, {'business_ref': 'businessref_15', 'review_cnt': '3'}, {'business_ref': 'businessref_33', 'review_cnt': '5'}, {'business_ref': 'businessref_81', 'review_cnt': '1'}, {'business_ref': 'businessref_36', 'review_cnt': '3'}, {'business_ref': 'businessref_12', 'review_cnt': '4'}, {'business_ref': 'businessref_60', 'review_cnt': '4'}, {'business_ref': 'businessref_89', 'review_cnt': '3'}, {'business_ref': 'businessref_17', 'review_cnt': '1'}, {'business_ref': 'businessref_43', 'review_cnt': '3'}, {'business_ref': 'businessref_31', 'review_cnt': '1'}, {'business_ref': 'businessref_99', 'review_cnt': '1'}, {'business_ref': 'businessref_9', 'review_cnt': '3'}, {'business_ref': 'businessref_74', 'review_cnt': '2'}, {'business_ref': 'businessref_25', 'review_cnt': '1'}, {'business_ref': 'businessref_66', 'review_cnt': '2'}, {'business_ref': 'businessref_53', 'review_cnt': '1'}, {'business_ref': 'businessref_51', 'review_cnt': '3'}, {'business_ref': 'businessref_40', 'review_cnt': '3'}, {'business_ref': 'businessref_7', 'review_cnt': '2'}, {'business_ref': 'businessref_92', 'review_cnt': '2'}, {'business_ref': 'businessref_61', 'review_cnt': '1'}, {'business_ref': 'businessref_37', 'review_cnt': '6'}, {'business_ref': 'businessref_57', 'review_cnt': '7'}, {'business_ref': 'businessref_8', 'review_cnt': '4'}, {'business_ref': 'businessref_56', 'review_cnt': '1'}, {'business_ref': 'businessref_62', 'review_cnt': '2'}, {'business_ref': 'businessref_86', 'review_cnt': '4'}, {'business_ref': 'businessref_97', 'review_cnt': '1'}, {'business_ref': 'businessref_72', 'review_cnt': '1'}, {'business_ref': 'businessref_85', 'review_cnt': '1'}, {'business_ref': 'businessref_42', 'review_cnt': '1'}, {'business_ref': 'businessref_88', 'review_cnt': '4'}, {'business_ref': 'businessref_21', 'review_cnt': '4'}, {'business_ref': 'businessref_26', 'review_cnt': '4'}, {'business_ref': 'businessref_68', 'review_cnt': '1'}, {'business_ref': 'businessref_4', 'review_cnt': '1'}, {'business_ref': 'businessref_23', 'review_cnt': '1'}, {'business_ref': 'businessref_41', 'review_cnt': '1'}, {'business_ref': 'businessref_10', 'review_cnt': '1'}, {'business_ref': 'businessref_45', 'review_cnt': '5'}, {'business_ref': 'businessref_82', 'review_cnt': '2'}, {'business_ref': 'businessref_76', 'review_cnt': '1'}, {'business_ref': 'businessref_14', 'review_cnt': '3'}, {'business_ref': 'businessref_3', 'review_cnt': '2'}, {'business_ref': 'businessref_96', 'review_cnt': '4'}, {'business_ref': 'businessref_98', 'review_cnt': '3'}, {'business_ref': 'businessref_22', 'review_cnt': '1'}, {'business_ref': 'businessref_20', 'review_cnt': '1'}], 'var_function-call-14503387314847266168': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}]}

exec(code, env_args)
