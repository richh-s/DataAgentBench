code = """import json
from collections import defaultdict

# load businesses subset file
biz_path = var_call_S8OX3aIp5GBOxbxgtBqbdRut
with open(biz_path, 'r', encoding='utf-8') as f:
    businesses = json.load(f)

reviews_records = var_call_Mb63Mqav5dOgJqAJwwve1XgS

# simple extraction using 'categories' present in description after keywords or listed separated by commas
import re

def simple_extract(desc):
    if not desc or not isinstance(desc, str):
        return []
    s = desc
    # try to find 'categories of' or 'categories' or 'in the category of' etc
    m = re.search(r'categories? (of|in) (.+)', s, flags=re.IGNORECASE)
    if m:
        piece = m.group(2)
    else:
        m2 = re.search(r'category of (.+)', s, flags=re.IGNORECASE)
        if m2:
            piece = m2.group(1)
        else:
            # find 'including' or 'offers a range of' occurrences
            m3 = re.search(r'including (.+)', s, flags=re.IGNORECASE)
            if m3:
                piece = m3.group(1)
            else:
                m4 = re.search(r'offers a range of services in (.+)', s, flags=re.IGNORECASE)
                if m4:
                    piece = m4.group(1)
                else:
                    m5 = re.search(r'offers a wide range of services in (.+)', s, flags=re.IGNORECASE)
                    if m5:
                        piece = m5.group(1)
                    else:
                        piece = None
    if not piece:
        # fallback: use last 80 chars
        piece = s[-120:]
    # cleanup
    piece = re.sub(r"\(.*?\)", '', piece)
    piece = re.sub(r"\'.*?\'", '', piece)
    piece = piece.replace('&', ',')
    piece = re.sub(r'\s+and\s+', ',', piece)
    parts = [p.strip() for p in re.split('[,;]', piece) if p.strip()]
    # filter out fragments that look like locations (contain 'in ' followed by two-letter state) or addresses
    cats = []
    for p in parts:
        if re.search(r'\b(in\s+[A-Za-z]{2}\b)', p):
            continue
        if re.search(r'\d', p):
            continue
        if len(p) < 2:
            continue
        cats.append(p)
    return cats

biz_cat_map = {}
for b in businesses:
    bid = b.get('business_id')
    desc = b.get('description')
    cats = simple_extract(desc)
    # if empty, try some known fields in description like 'Restaurants' or 'Food' etc by searching
    if not cats and desc:
        # find capitalized words with ampersands or & in fragment
        caps = re.findall(r"([A-Z][A-Za-z '&]+)", desc)
        # filter
        caps = [c.strip() for c in caps if len(c.strip())>2]
        if caps:
            cats = caps[:3]
    biz_cat_map[bid] = cats

# aggregate
cat_counts = defaultdict(int)
for rec in reviews_records:
    bref = rec.get('business_ref')
    if not bref:
        continue
    bid = bref.replace('businessref_', 'businessid_')
    try:
        count = int(rec.get('reviews_count', 0))
    except:
        count = 0
    cats = biz_cat_map.get(bid, [])
    if not cats:
        # try to find biz in full businesses set (not in subset) - but we only loaded subset
        continue
    for c in cats:
        cat_counts[c] += count

items = sorted(cat_counts.items(), key=lambda x: x[1], reverse=True)
top5 = [{'category': k, 'reviews': v} for k,v in items[:5]]

print('__RESULT__:')
print(json.dumps(top5))"""

env_args = {'var_call_hxlTPUlKf10eGQD9MWWL3vty': ['business', 'checkin'], 'var_call_vJpbhhgSMWYvahvuxsXHzAN9': ['review', 'tip', 'user'], 'var_call_vdOGCO3lPNfGG8nhDfMWheJC': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_Mb63Mqav5dOgJqAJwwve1XgS': [{'business_ref': 'businessref_45', 'reviews_count': '3'}, {'business_ref': 'businessref_92', 'reviews_count': '2'}, {'business_ref': 'businessref_57', 'reviews_count': '2'}, {'business_ref': 'businessref_36', 'reviews_count': '2'}, {'business_ref': 'businessref_60', 'reviews_count': '2'}, {'business_ref': 'businessref_74', 'reviews_count': '2'}, {'business_ref': 'businessref_96', 'reviews_count': '2'}, {'business_ref': 'businessref_66', 'reviews_count': '2'}, {'business_ref': 'businessref_33', 'reviews_count': '2'}, {'business_ref': 'businessref_13', 'reviews_count': '1'}, {'business_ref': 'businessref_20', 'reviews_count': '1'}, {'business_ref': 'businessref_37', 'reviews_count': '1'}, {'business_ref': 'businessref_53', 'reviews_count': '1'}, {'business_ref': 'businessref_79', 'reviews_count': '1'}, {'business_ref': 'businessref_6', 'reviews_count': '1'}, {'business_ref': 'businessref_31', 'reviews_count': '1'}, {'business_ref': 'businessref_10', 'reviews_count': '1'}, {'business_ref': 'businessref_15', 'reviews_count': '1'}, {'business_ref': 'businessref_86', 'reviews_count': '1'}, {'business_ref': 'businessref_14', 'reviews_count': '1'}, {'business_ref': 'businessref_68', 'reviews_count': '1'}, {'business_ref': 'businessref_98', 'reviews_count': '1'}, {'business_ref': 'businessref_62', 'reviews_count': '1'}, {'business_ref': 'businessref_12', 'reviews_count': '1'}, {'business_ref': 'businessref_26', 'reviews_count': '1'}, {'business_ref': 'businessref_41', 'reviews_count': '1'}], 'var_call_M98bV3EvapcWojYZWNiswD97': 'file_storage/call_M98bV3EvapcWojYZWNiswD97.json', 'var_call_S8OX3aIp5GBOxbxgtBqbdRut': 'file_storage/call_S8OX3aIp5GBOxbxgtBqbdRut.json'}

exec(code, env_args)
