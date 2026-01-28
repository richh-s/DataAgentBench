code = """import json
import pandas as pd

# load previous tool results from storage variables
businesses_path = var_call_M98bV3EvapcWojYZWNiswD97  # path to large JSON file
reviews_records = var_call_Mb63Mqav5dOgJqAJwwve1XgS

# load full businesses data
with open(businesses_path, 'r', encoding='utf-8') as f:
    businesses = json.load(f)

# build mapping business_id -> categories (list)
import re

def extract_categories(desc):
    if not desc or not isinstance(desc, str):
        return []
    s = desc
    s = s.replace('\n', ' ').strip()
    # common markers
    markers = [' including ', ' in the category of ', ' offers a range of services in ', ' offers a wide range of services in ', ' offers a range of services, including ', ' offers a wide range of services, including ', ' offers a wide range of services, ', ' offers a range of services, ', ' offers a range of services ', ' offers a wide range of services ', ' offers a diverse range of services and products in ', ' offers a diverse range of services and products in the fields of ', ' offers a diverse selection of ', 'offers a range of services in ', 'offers a wide range of services in ', 'offers a range of services, including ', 'located at']
    piece = None
    for m in markers:
        idx = s.lower().find(m.strip())
        if idx != -1:
            # find the marker case-insensitively by using regex
            m_re = re.compile(re.escape(m), re.IGNORECASE)
            m_match = m_re.search(s)
            if m_match:
                piece = s[m_match.end():]
                break
    if piece is None:
        # try splitting on ' in ' occurrences but avoid matches like 'Located at ... in City'
        # find ' in ' followed by capitalized word and commas - heuristic
        m = re.search(r' in (the fields of |the category of )?', s, flags=re.IGNORECASE)
        if m:
            piece = s[m.end():]
    if piece is None:
        # fallback: take substring after last comma
        if ',' in s:
            piece = s.split(',')[-3:]  # last up to 3 segments
            piece = ','.join(piece)
        else:
            piece = s
    # remove trailing sentences about location (like 'Located at ...') if present at start
    # remove sentences that start with location info e.g., 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers ...'
    # If 'this' or 'offers' appear, try to cut before them
    if ' this ' in piece.lower():
        # keep substring after 'this' if it leads to categories
        pass
    # cleanup
    piece = re.sub(r"\b(and|and/or)\b", ',', piece, flags=re.IGNORECASE)
    piece = piece.replace(' & ', ',')
    piece = piece.replace(';', ',')
    # remove content in parentheses or quotes
    piece = re.sub(r"\(.*?\)", '', piece)
    piece = re.sub(r"\'.*?\'", '', piece)
    piece = re.sub(r'\".*?\"', '', piece)
    # split by commas
    parts = [p.strip() for p in piece.split(',') if p.strip()]
    # further split on ' and ' fragments
    final = []
    for p in parts:
        sub = [sp.strip() for sp in re.split(r'\band\b', p, flags=re.IGNORECASE) if sp.strip()]
        for sss in sub:
            # remove trailing words like 'services' or 'products' or 'for all your needs'
            sss = re.sub(r"(services|service|products|facility|establishment|businesses|business)\b.*$", '', sss, flags=re.IGNORECASE).strip(' ,.-')
            if sss:
                final.append(sss)
    # deduplicate while preserving order
    seen = set()
    out = []
    for f in final:
        ff = f.strip()
        if ff and ff.lower() not in seen:
            seen.add(ff.lower())
            out.append(ff)
    return out

# create mapping
biz_cat_map = {}
for b in businesses:
    bid = b.get('business_id')
    desc = b.get('description')
    cats = extract_categories(desc)
    biz_cat_map[bid] = cats

# aggregate reviews per category
from collections import defaultdict
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

# prepare sorted top 5
items = sorted(cat_counts.items(), key=lambda x: x[1], reverse=True)
top5 = [{'category': k, 'reviews': v} for k, v in items[:5]]

# If some businesses had no categories extracted, they will be in missed; we could try fallback using 'name' or other fields, but skip

import json as _json
print("__RESULT__:")
print(_json.dumps(top5))"""

env_args = {'var_call_hxlTPUlKf10eGQD9MWWL3vty': ['business', 'checkin'], 'var_call_vJpbhhgSMWYvahvuxsXHzAN9': ['review', 'tip', 'user'], 'var_call_vdOGCO3lPNfGG8nhDfMWheJC': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_Mb63Mqav5dOgJqAJwwve1XgS': [{'business_ref': 'businessref_45', 'reviews_count': '3'}, {'business_ref': 'businessref_92', 'reviews_count': '2'}, {'business_ref': 'businessref_57', 'reviews_count': '2'}, {'business_ref': 'businessref_36', 'reviews_count': '2'}, {'business_ref': 'businessref_60', 'reviews_count': '2'}, {'business_ref': 'businessref_74', 'reviews_count': '2'}, {'business_ref': 'businessref_96', 'reviews_count': '2'}, {'business_ref': 'businessref_66', 'reviews_count': '2'}, {'business_ref': 'businessref_33', 'reviews_count': '2'}, {'business_ref': 'businessref_13', 'reviews_count': '1'}, {'business_ref': 'businessref_20', 'reviews_count': '1'}, {'business_ref': 'businessref_37', 'reviews_count': '1'}, {'business_ref': 'businessref_53', 'reviews_count': '1'}, {'business_ref': 'businessref_79', 'reviews_count': '1'}, {'business_ref': 'businessref_6', 'reviews_count': '1'}, {'business_ref': 'businessref_31', 'reviews_count': '1'}, {'business_ref': 'businessref_10', 'reviews_count': '1'}, {'business_ref': 'businessref_15', 'reviews_count': '1'}, {'business_ref': 'businessref_86', 'reviews_count': '1'}, {'business_ref': 'businessref_14', 'reviews_count': '1'}, {'business_ref': 'businessref_68', 'reviews_count': '1'}, {'business_ref': 'businessref_98', 'reviews_count': '1'}, {'business_ref': 'businessref_62', 'reviews_count': '1'}, {'business_ref': 'businessref_12', 'reviews_count': '1'}, {'business_ref': 'businessref_26', 'reviews_count': '1'}, {'business_ref': 'businessref_41', 'reviews_count': '1'}], 'var_call_M98bV3EvapcWojYZWNiswD97': 'file_storage/call_M98bV3EvapcWojYZWNiswD97.json'}

exec(code, env_args)
