code = """import json
from collections import defaultdict

# load the small query result from storage
reviews = var_call_Hc49ZhC22GCBqN7V3mB7Fk87

# load the full business collection JSON from file path variable
businesses_file = var_call_XVCjqhkXqdqnBGj7nGobEdQT
with open(businesses_file, 'r') as f:
    businesses = json.load(f)

# build mapping from business_id to business doc
biz_map = {b.get('business_id'): b for b in businesses}

# helper to extract categories from description or categories field
import re

def extract_categories(biz):
    cats = []
    if not biz:
        return cats
    # prefer explicit 'categories' field if present and non-empty
    if 'categories' in biz and biz['categories']:
        if isinstance(biz['categories'], list):
            return [c.strip() for c in biz['categories'] if isinstance(c, str) and c.strip()]
        elif isinstance(biz['categories'], str):
            return [c.strip() for c in biz['categories'].split(',') if c.strip()]
    desc = biz.get('description') or ''
    desc = desc.strip()
    if not desc:
        return cats
    # try several patterns to capture categories segment before a period
    patterns = [
        r'(?:in the categories of|in the category of|categories of|category of|offers a range of services in|offers a diverse range of services and products in|offers a diverse range of products and services in|offers a range of services including|offers a range of services, including|including the categories of|including)([^\.]+)\.',
        r'([^\.]+)\.'
    ]
    segment = None
    for pat in patterns:
        m = re.search(pat, desc, flags=re.IGNORECASE)
        if m:
            segment = m.group(1)
            break
    if not segment:
        segment = desc
    # split segment by commas and 'and'
    parts = re.split(r',| and | & ', segment)
    # clean and filter
    for p in parts:
        p = p.strip()
        # remove leading phrases like 'this facility offers' etc
        p = re.sub(r'^(offers a (?:diverse )?(?:range of )?(?:products and services )?in|this (?:facility|establishment) (?:offers|specializes in)|located at .* this .* offers|located at .* this location offers|this .* offers a range of services in)\s*', '', p, flags=re.IGNORECASE)
        # remove trailing words like 'services', 'products', 'and' etc
        p = re.sub(r'\b(?:services|products)\b', '', p, flags=re.IGNORECASE).strip()
        # remove stray words 'Food' 'Shopping' with punctuation
        if p:
            # avoid numeric addresses
            if re.search(r'\d', p):
                continue
            cats.append(p)
    # final cleanup: split any elements that still contain slashes
    final = []
    for c in cats:
        for sub in re.split(r'/|\\', c):
            s = sub.strip().strip(',').strip()
            if s:
                final.append(s)
    # deduplicate while preserving order
    seen = set()
    out = []
    for c in final:
        lc = c.lower()
        if lc not in seen:
            seen.add(lc)
            out.append(c)
    return out

# aggregate counts per category
cat_counts = defaultdict(int)
missing = []
for rec in reviews:
    business_ref = rec.get('business_ref')
    count = int(rec.get('reviews_count') or 0)
    if not business_ref:
        continue
    # convert businessref_N to businessid_N
    biz_id = business_ref.replace('businessref_', 'businessid_')
    biz = biz_map.get(biz_id)
    cats = extract_categories(biz)
    if not cats:
        # fallback: use business name as a single category to not lose count
        name = biz.get('name') if biz else None
        if name:
            cats = [name]
        else:
            missing.append(biz_id)
            cats = ['Unknown']
    for c in cats:
        cat_counts[c] += count

# prepare top 5 categories
sorted_cats = sorted(cat_counts.items(), key=lambda x: x[1], reverse=True)
top5 = [{'category': c, 'total_reviews': v} for c, v in sorted_cats[:5]]

import json
print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_jyzmTegughRmR0QoCmwUii7m': ['checkin', 'business'], 'var_call_unlczDxFIfk3XGj4JB7w40GZ': ['review', 'tip', 'user'], 'var_call_FFXE02a1BXsLtYiBkUzW1fey': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_Hc49ZhC22GCBqN7V3mB7Fk87': [{'business_ref': 'businessref_45', 'reviews_count': '3'}, {'business_ref': 'businessref_57', 'reviews_count': '2'}, {'business_ref': 'businessref_33', 'reviews_count': '2'}, {'business_ref': 'businessref_66', 'reviews_count': '2'}, {'business_ref': 'businessref_74', 'reviews_count': '2'}, {'business_ref': 'businessref_92', 'reviews_count': '2'}, {'business_ref': 'businessref_96', 'reviews_count': '2'}, {'business_ref': 'businessref_60', 'reviews_count': '2'}, {'business_ref': 'businessref_36', 'reviews_count': '2'}, {'business_ref': 'businessref_79', 'reviews_count': '1'}, {'business_ref': 'businessref_37', 'reviews_count': '1'}, {'business_ref': 'businessref_13', 'reviews_count': '1'}, {'business_ref': 'businessref_12', 'reviews_count': '1'}, {'business_ref': 'businessref_86', 'reviews_count': '1'}, {'business_ref': 'businessref_26', 'reviews_count': '1'}, {'business_ref': 'businessref_98', 'reviews_count': '1'}, {'business_ref': 'businessref_15', 'reviews_count': '1'}, {'business_ref': 'businessref_6', 'reviews_count': '1'}, {'business_ref': 'businessref_53', 'reviews_count': '1'}, {'business_ref': 'businessref_31', 'reviews_count': '1'}, {'business_ref': 'businessref_41', 'reviews_count': '1'}, {'business_ref': 'businessref_62', 'reviews_count': '1'}, {'business_ref': 'businessref_68', 'reviews_count': '1'}, {'business_ref': 'businessref_10', 'reviews_count': '1'}, {'business_ref': 'businessref_20', 'reviews_count': '1'}, {'business_ref': 'businessref_14', 'reviews_count': '1'}], 'var_call_QDdfYDRQTZiPpgjhk5Dhqdvn': [{'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails'}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'name': 'Candy Barrel'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'name': 'Luminosity'}, {'_id': '6859a000fe8b31cd7362e2cd', 'business_id': 'businessid_57', 'name': 'Big Boys Moving And Storage'}, {'_id': '6859a000fe8b31cd7362e2db', 'business_id': 'businessid_45', 'name': 'The Fresh Market'}, {'_id': '6859a000fe8b31cd7362e2e0', 'business_id': 'businessid_79', 'name': 'Pit Stop HQ'}, {'_id': '6859a000fe8b31cd7362e2e1', 'business_id': 'businessid_66', 'name': 'Panda Express'}, {'_id': '6859a000fe8b31cd7362e2e6', 'business_id': 'businessid_96', 'name': 'Farmhaus Restaurant'}, {'_id': '6859a000fe8b31cd7362e2f5', 'business_id': 'businessid_37', 'name': 'Orangetheory Fitness Carrollwood'}, {'_id': '6859a000fe8b31cd7362e300', 'business_id': 'businessid_12', 'name': 'Atlantic Trap & Gill Pub'}, {'_id': '6859a000fe8b31cd7362e302', 'business_id': 'businessid_60', 'name': 'Walmart'}, {'_id': '6859a000fe8b31cd7362e308', 'business_id': 'businessid_36', 'name': 'Pho & Beyond'}, {'_id': '6859a000fe8b31cd7362e30d', 'business_id': 'businessid_13', 'name': 'Avian Glen Winery'}], 'var_call_XVCjqhkXqdqnBGj7nGobEdQT': 'file_storage/call_XVCjqhkXqdqnBGj7nGobEdQT.json', 'var_call_NmQBgKBvlQQTvEOzBr70os0t': [{'_id': '6859a000fe8b31cd7362e2db', 'business_id': 'businessid_45', 'name': 'The Fresh Market', 'description': 'Located at 2900 4th St N in St. Petersburg, FL, this establishment offers a diverse range of products and services in the categories of Food, Grocery, Shopping.'}]}

exec(code, env_args)
