code = """import json
from collections import defaultdict

businesses_path = var_call_M98bV3EvapcWojYZWNiswD97
reviews_records = var_call_Mb63Mqav5dOgJqAJwwve1XgS

with open(businesses_path, 'r', encoding='utf-8') as f:
    businesses = json.load(f)

# build id->record map
biz_map = {b.get('business_id'): b for b in businesses if b.get('business_id')}

def remove_parentheses(s):
    # remove content inside parentheses
    out = ''
    skip = 0
    for ch in s:
        if ch == '(':
            skip += 1
        elif ch == ')':
            if skip > 0:
                skip -= 1
        elif skip == 0:
            out += ch
    return out

def extract_categories_simple(desc):
    if not desc or not isinstance(desc, str):
        return []
    s = desc.replace('\n', ' ').strip()
    s_low = s.lower()
    piece = None
    # prefer substring after 'offers'
    idx = s_low.find('offers')
    if idx != -1:
        piece = s[idx+len('offers'):]
    else:
        # try after 'in the category' or 'in the fields of'
        for marker in ['in the category', 'in the fields of', 'the category of']:
            idx = s_low.find(marker)
            if idx != -1:
                piece = s[idx+len(marker):]
                break
    if piece is None:
        # fallback: take last 120 chars after last comma
        if ',' in s:
            parts = s.split(',')
            piece = ','.join(parts[-3:])
        else:
            piece = s
    piece = remove_parentheses(piece)
    # normalize separators
    piece = piece.replace('&', ',')
    piece = piece.replace('/', ',')
    piece = piece.replace(';', ',')
    piece = piece.replace(' and ', ',')
    # split
    tokens = [t.strip() for t in piece.split(',') if t.strip()]
    clean = []
    for t in tokens:
        # remove trailing generic words
        for word in ['services', 'service', 'products', 'facility', 'establishment', 'businesses', 'business', 'offers', 'including', 'including the', 'in the', 'in']:
            if t.lower().endswith(' ' + word) or t.lower().endswith(word):
                # strip the word
                idxw = t.lower().rfind(word)
                if idxw > 0:
                    t = t[:idxw].strip(' -,:;.')
                else:
                    t = ''
        # filter out tokens that look like addresses or start with 'located'
        if not t:
            continue
        if any(ch.isdigit() for ch in t):
            continue
        if t.lower().startswith('located') or t.lower().startswith('this') or t.lower().startswith('offers'):
            continue
        if len(t) < 2:
            continue
        clean.append(t)
    # dedupe preserving order
    seen = set()
    out = []
    for c in clean:
        k = c.lower()
        if k not in seen:
            seen.add(k)
            out.append(c)
    return out

# Build business_id -> categories mapping
biz_cat_map = {}
for bid, brec in biz_map.items():
    desc = brec.get('description')
    cats = extract_categories_simple(desc)
    # if no cats, try to extract from name by splitting on ':' or '-' or ' - '
    if not cats:
        name = brec.get('name') or ''
        # split name on common separators
        parts = [p.strip() for p in name.replace('-', ',').replace(':', ',').split(',') if p.strip()]
        cats = parts
    biz_cat_map[bid] = cats

cat_counts = defaultdict(int)
missed = []
for rec in reviews_records:
    bref = rec.get('business_ref')
    try:
        count = int(rec.get('reviews_count', 0))
    except:
        try:
            count = int(float(rec.get('reviews_count', 0)))
        except:
            count = 0
    if not bref:
        continue
    bid = bref.replace('businessref_', 'businessid_')
    cats = biz_cat_map.get(bid)
    if not cats:
        missed.append(bid)
        continue
    for c in cats:
        cat_counts[c] += count

items = sorted(cat_counts.items(), key=lambda x: x[1], reverse=True)

top5 = [{'category': k, 'reviews': v} for k, v in items[:5]]

print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_hxlTPUlKf10eGQD9MWWL3vty': ['business', 'checkin'], 'var_call_vJpbhhgSMWYvahvuxsXHzAN9': ['review', 'tip', 'user'], 'var_call_vdOGCO3lPNfGG8nhDfMWheJC': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_Mb63Mqav5dOgJqAJwwve1XgS': [{'business_ref': 'businessref_45', 'reviews_count': '3'}, {'business_ref': 'businessref_92', 'reviews_count': '2'}, {'business_ref': 'businessref_57', 'reviews_count': '2'}, {'business_ref': 'businessref_36', 'reviews_count': '2'}, {'business_ref': 'businessref_60', 'reviews_count': '2'}, {'business_ref': 'businessref_74', 'reviews_count': '2'}, {'business_ref': 'businessref_96', 'reviews_count': '2'}, {'business_ref': 'businessref_66', 'reviews_count': '2'}, {'business_ref': 'businessref_33', 'reviews_count': '2'}, {'business_ref': 'businessref_13', 'reviews_count': '1'}, {'business_ref': 'businessref_20', 'reviews_count': '1'}, {'business_ref': 'businessref_37', 'reviews_count': '1'}, {'business_ref': 'businessref_53', 'reviews_count': '1'}, {'business_ref': 'businessref_79', 'reviews_count': '1'}, {'business_ref': 'businessref_6', 'reviews_count': '1'}, {'business_ref': 'businessref_31', 'reviews_count': '1'}, {'business_ref': 'businessref_10', 'reviews_count': '1'}, {'business_ref': 'businessref_15', 'reviews_count': '1'}, {'business_ref': 'businessref_86', 'reviews_count': '1'}, {'business_ref': 'businessref_14', 'reviews_count': '1'}, {'business_ref': 'businessref_68', 'reviews_count': '1'}, {'business_ref': 'businessref_98', 'reviews_count': '1'}, {'business_ref': 'businessref_62', 'reviews_count': '1'}, {'business_ref': 'businessref_12', 'reviews_count': '1'}, {'business_ref': 'businessref_26', 'reviews_count': '1'}, {'business_ref': 'businessref_41', 'reviews_count': '1'}], 'var_call_M98bV3EvapcWojYZWNiswD97': 'file_storage/call_M98bV3EvapcWojYZWNiswD97.json'}

exec(code, env_args)
