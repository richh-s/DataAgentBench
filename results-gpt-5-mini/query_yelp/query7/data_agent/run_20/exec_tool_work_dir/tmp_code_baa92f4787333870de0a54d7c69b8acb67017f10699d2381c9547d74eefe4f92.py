code = """import json
from collections import defaultdict

reviews = var_call_Hc49ZhC22GCBqN7V3mB7Fk87
businesses_file = var_call_XVCjqhkXqdqnBGj7nGobEdQT
with open(businesses_file, 'r') as f:
    businesses = json.load(f)

biz_map = {b.get('business_id'): b for b in businesses}

def extract_categories_simple(biz):
    if not biz:
        return []
    # prefer explicit categories field
    if 'categories' in biz and biz['categories']:
        c = biz['categories']
        if isinstance(c, list):
            return [x.strip() for x in c if isinstance(x, str) and x.strip()]
        if isinstance(c, str):
            return [x.strip() for x in c.split(',') if x.strip()]
    desc = (biz.get('description') or '').strip()
    if not desc:
        return []
    lower = desc.lower()
    keys = ['in the categories of', 'in the category of', 'categories of', 'category of', 'offers a range of services in', 'offers a diverse range of products and services in', 'offers a diverse range of services and products in', 'offers a range of services including', 'offers a range of services, including', 'including the categories of', 'including']
    start = None
    for k in keys:
        idx = lower.find(k)
        if idx != -1:
            start = idx + len(k)
            break
    segment = desc[start:].strip() if start is not None else desc
    # if there's a period, take up to first period
    if '.' in segment:
        segment = segment.split('.', 1)[0]
    # split by common delimiters
    parts = []
    for part in segment.replace('&', ',').replace('/', ',').split(','):
        for sub in part.split(' and '):
            p = sub.strip()
            if not p:
                continue
            # drop trailing generic words
            for suffix in ['services', 'products']:
                if p.lower().endswith(suffix):
                    p = p[: -len(suffix)].strip()
            # remove stray leading words
            if p:
                parts.append(p)
    # filter out parts that look like addresses (contain digits)
    parts = [p for p in parts if not any(ch.isdigit() for ch in p)]
    # dedup preserving order
    seen = set()
    out = []
    for p in parts:
        key = p.lower()
        if key not in seen:
            seen.add(key)
            out.append(p)
    return out

cat_counts = defaultdict(int)
for rec in reviews:
    business_ref = rec.get('business_ref')
    cnt = int(rec.get('reviews_count') or 0)
    if not business_ref:
        continue
    biz_id = business_ref.replace('businessref_', 'businessid_')
    biz = biz_map.get(biz_id)
    cats = extract_categories_simple(biz)
    if not cats:
        # fallback to business name
        if biz and biz.get('name'):
            cats = [biz.get('name')]
        else:
            cats = ['Unknown']
    for c in cats:
        cat_counts[c] += cnt

sorted_cats = sorted(cat_counts.items(), key=lambda x: x[1], reverse=True)
top5 = [{'category': c, 'total_reviews': v} for c, v in sorted_cats[:5]]

print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_jyzmTegughRmR0QoCmwUii7m': ['checkin', 'business'], 'var_call_unlczDxFIfk3XGj4JB7w40GZ': ['review', 'tip', 'user'], 'var_call_FFXE02a1BXsLtYiBkUzW1fey': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_Hc49ZhC22GCBqN7V3mB7Fk87': [{'business_ref': 'businessref_45', 'reviews_count': '3'}, {'business_ref': 'businessref_57', 'reviews_count': '2'}, {'business_ref': 'businessref_33', 'reviews_count': '2'}, {'business_ref': 'businessref_66', 'reviews_count': '2'}, {'business_ref': 'businessref_74', 'reviews_count': '2'}, {'business_ref': 'businessref_92', 'reviews_count': '2'}, {'business_ref': 'businessref_96', 'reviews_count': '2'}, {'business_ref': 'businessref_60', 'reviews_count': '2'}, {'business_ref': 'businessref_36', 'reviews_count': '2'}, {'business_ref': 'businessref_79', 'reviews_count': '1'}, {'business_ref': 'businessref_37', 'reviews_count': '1'}, {'business_ref': 'businessref_13', 'reviews_count': '1'}, {'business_ref': 'businessref_12', 'reviews_count': '1'}, {'business_ref': 'businessref_86', 'reviews_count': '1'}, {'business_ref': 'businessref_26', 'reviews_count': '1'}, {'business_ref': 'businessref_98', 'reviews_count': '1'}, {'business_ref': 'businessref_15', 'reviews_count': '1'}, {'business_ref': 'businessref_6', 'reviews_count': '1'}, {'business_ref': 'businessref_53', 'reviews_count': '1'}, {'business_ref': 'businessref_31', 'reviews_count': '1'}, {'business_ref': 'businessref_41', 'reviews_count': '1'}, {'business_ref': 'businessref_62', 'reviews_count': '1'}, {'business_ref': 'businessref_68', 'reviews_count': '1'}, {'business_ref': 'businessref_10', 'reviews_count': '1'}, {'business_ref': 'businessref_20', 'reviews_count': '1'}, {'business_ref': 'businessref_14', 'reviews_count': '1'}], 'var_call_QDdfYDRQTZiPpgjhk5Dhqdvn': [{'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails'}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'name': 'Candy Barrel'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'name': 'Luminosity'}, {'_id': '6859a000fe8b31cd7362e2cd', 'business_id': 'businessid_57', 'name': 'Big Boys Moving And Storage'}, {'_id': '6859a000fe8b31cd7362e2db', 'business_id': 'businessid_45', 'name': 'The Fresh Market'}, {'_id': '6859a000fe8b31cd7362e2e0', 'business_id': 'businessid_79', 'name': 'Pit Stop HQ'}, {'_id': '6859a000fe8b31cd7362e2e1', 'business_id': 'businessid_66', 'name': 'Panda Express'}, {'_id': '6859a000fe8b31cd7362e2e6', 'business_id': 'businessid_96', 'name': 'Farmhaus Restaurant'}, {'_id': '6859a000fe8b31cd7362e2f5', 'business_id': 'businessid_37', 'name': 'Orangetheory Fitness Carrollwood'}, {'_id': '6859a000fe8b31cd7362e300', 'business_id': 'businessid_12', 'name': 'Atlantic Trap & Gill Pub'}, {'_id': '6859a000fe8b31cd7362e302', 'business_id': 'businessid_60', 'name': 'Walmart'}, {'_id': '6859a000fe8b31cd7362e308', 'business_id': 'businessid_36', 'name': 'Pho & Beyond'}, {'_id': '6859a000fe8b31cd7362e30d', 'business_id': 'businessid_13', 'name': 'Avian Glen Winery'}], 'var_call_XVCjqhkXqdqnBGj7nGobEdQT': 'file_storage/call_XVCjqhkXqdqnBGj7nGobEdQT.json', 'var_call_NmQBgKBvlQQTvEOzBr70os0t': [{'_id': '6859a000fe8b31cd7362e2db', 'business_id': 'businessid_45', 'name': 'The Fresh Market', 'description': 'Located at 2900 4th St N in St. Petersburg, FL, this establishment offers a diverse range of products and services in the categories of Food, Grocery, Shopping.'}]}

exec(code, env_args)
