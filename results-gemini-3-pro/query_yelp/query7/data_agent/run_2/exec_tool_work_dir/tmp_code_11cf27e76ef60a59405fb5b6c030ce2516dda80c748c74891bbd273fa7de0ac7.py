code = """import json
import re

with open(locals()['var_function-call-13067069964491135469'], 'r') as f:
    businesses = json.load(f)
reviews = locals()['var_function-call-7414676008247388085']

biz_review_counts = {}
for r in reviews:
    bid = r['business_ref'].replace('businessref_', 'businessid_')
    count = int(r['review_cnt'])
    biz_review_counts[bid] = count

start_keywords = ["seeking ", "services in ", "including ", "destination for ", "categories of ", "category of ", "ranging from ", "featuring ", "mix of ", "specializes in ", "products in ", "offerings within the ", "offerings, including "]
stop_pattern = re.compile(r"(, making it|, perfect for|, along with| to meet| enthusiasts| options| needs| offering| and products|\.$| with a )")

category_counts = {}

for b in businesses:
    bid = b['business_id']
    if bid not in biz_review_counts: continue
    desc = b.get('description', '')
    if not desc: continue

    found_idx = -1
    used_kw = ""
    for kw in start_keywords:
        idx = desc.rfind(kw)
        if idx != -1:
            if idx > found_idx:
                found_idx = idx
                used_kw = kw
    
    if found_idx == -1:
        kw = "selection of "
        idx = desc.rfind(kw)
        if idx != -1:
            if idx > found_idx:
                found_idx = idx
                used_kw = kw
    
    if found_idx == -1: continue

    content = desc[found_idx + len(used_kw):]
    match = stop_pattern.search(content)
    if match: content = content[:match.start()]
    content = content.replace("'", "").replace("category of ", "").replace("categories of ", "")
    
    raw_cats = content.split(',')
    final_cats = []
    for c in raw_cats:
        c = c.strip()
        if c.lower().startswith('and '): c = c[4:].strip()
        if " to " in c:
            parts = c.split(' to ')
            for p in parts:
                if p.strip(): final_cats.append(p.strip())
            continue
        if c: final_cats.append(c)
    
    cnt = biz_review_counts[bid]
    for cat in final_cats:
        cat = cat.strip('.').strip()
        if not cat: continue
        if "range" in cat.lower() or "selection" in cat.lower(): continue
        category_counts[cat] = category_counts.get(cat, 0) + cnt

sorted_cats = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)
print("__RESULT__:")
print(json.dumps(sorted_cats[:10]))"""

env_args = {'var_function-call-14315717405031266805': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-16510140419764474466': [{'user_id': 'userid_286', 'name': 'Todd', 'review_count': '376', 'yelping_since': '15 Jan 2009, 16:40', 'useful': '1373', 'funny': '723', 'cool': '639', 'elite': '2010,2011,2012,2013,2014'}], 'var_function-call-7414676008247388085': [{'business_ref': 'businessref_79', 'review_cnt': '4'}, {'business_ref': 'businessref_13', 'review_cnt': '2'}, {'business_ref': 'businessref_44', 'review_cnt': '3'}, {'business_ref': 'businessref_6', 'review_cnt': '2'}, {'business_ref': 'businessref_71', 'review_cnt': '1'}, {'business_ref': 'businessref_91', 'review_cnt': '1'}, {'business_ref': 'businessref_16', 'review_cnt': '1'}, {'business_ref': 'businessref_55', 'review_cnt': '1'}, {'business_ref': 'businessref_9', 'review_cnt': '2'}, {'business_ref': 'businessref_25', 'review_cnt': '1'}, {'business_ref': 'businessref_29', 'review_cnt': '1'}, {'business_ref': 'businessref_39', 'review_cnt': '1'}, {'business_ref': 'businessref_67', 'review_cnt': '3'}, {'business_ref': 'businessref_15', 'review_cnt': '2'}, {'business_ref': 'businessref_12', 'review_cnt': '1'}, {'business_ref': 'businessref_60', 'review_cnt': '2'}, {'business_ref': 'businessref_51', 'review_cnt': '1'}, {'business_ref': 'businessref_37', 'review_cnt': '2'}, {'business_ref': 'businessref_57', 'review_cnt': '2'}, {'business_ref': 'businessref_8', 'review_cnt': '1'}, {'business_ref': 'businessref_62', 'review_cnt': '1'}, {'business_ref': 'businessref_86', 'review_cnt': '1'}, {'business_ref': 'businessref_85', 'review_cnt': '1'}, {'business_ref': 'businessref_42', 'review_cnt': '1'}, {'business_ref': 'businessref_40', 'review_cnt': '3'}, {'business_ref': 'businessref_61', 'review_cnt': '1'}, {'business_ref': 'businessref_82', 'review_cnt': '2'}, {'business_ref': 'businessref_45', 'review_cnt': '1'}, {'business_ref': 'businessref_21', 'review_cnt': '4'}, {'business_ref': 'businessref_4', 'review_cnt': '1'}, {'business_ref': 'businessref_88', 'review_cnt': '2'}, {'business_ref': 'businessref_26', 'review_cnt': '1'}, {'business_ref': 'businessref_76', 'review_cnt': '1'}, {'business_ref': 'businessref_14', 'review_cnt': '2'}, {'business_ref': 'businessref_3', 'review_cnt': '2'}, {'business_ref': 'businessref_96', 'review_cnt': '2'}], 'var_function-call-4578890131057548585': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-13067069964491135469': 'file_storage/function-call-13067069964491135469.json', 'var_function-call-16268181922780412941': [['Restaurants', 21], ['Food', 15], ['Breakfast & Brunch', 11], ['American (New)', 11], ['Automotive', 9]]}

exec(code, env_args)
