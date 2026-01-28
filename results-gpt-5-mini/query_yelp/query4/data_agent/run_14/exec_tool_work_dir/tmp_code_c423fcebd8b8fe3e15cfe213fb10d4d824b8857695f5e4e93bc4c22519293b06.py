code = """import json, re, ast
from collections import defaultdict

biz_path = var_call_xQTpFtpR13zpzNbkcqvFFafi
rev_path = var_call_qlkHo3dF8SjDijFURBwJADSJ

with open(biz_path, 'r') as f:
    businesses = json.load(f)
with open(rev_path, 'r') as f:
    reviews = json.load(f)

# parse attributes helper
def parse_attributes(attr):
    if attr is None:
        return {}
    if isinstance(attr, dict):
        return attr
    if isinstance(attr, str):
        s = attr.strip()
        if s.lower() == 'none' or s == '':
            return {}
        try:
            parsed = ast.literal_eval(s)
            if isinstance(parsed, dict):
                return parsed
            else:
                return {}
        except Exception:
            return {}
    return {}

# function to extract categories from description
def extract_categories_from_description(desc):
    if not desc or not isinstance(desc, str):
        return []
    # Work with original casing but search lowercase for positions
    lower = desc.lower()
    # Look for key patterns in order
    patterns = [
        'in the categories of',
        'in the category of',
        'in the fields of',
        'in the field of',
        'offers a diverse range of services and products in',
        'offers a diverse range of services in',
        'offers a diverse selection of',
        'offers a range of services and products in',
        'offers a range of services in',
        'offers a range of services including',
        'offers a range of services',
        'offers a wide range of services, including',
        'offers a wide range of services including',
        'offers a wide range of services',
        'offers a variety of services including',
        'offers a variety of services',
        'offers a delightful array of options ranging from',
        'offers a delightful array of options ranging from',
        'offers a delightful array of options ranging from',
        'offers a delightful array of options ranging from',
        'offers a delightful array of options ranging from',
        'offers a delightful array of options ranging from',
        'offers a delightful array of',
        'offers a delightful array of options',
        'offers a delightful array of dishes in the category of',
        'in the category of',
        'including',
        'including a range of',
        'including the categories of'
    ]
    found = None
    for p in patterns:
        idx = lower.find(p)
        if idx != -1:
            found = (p, idx)
            break
    segment = None
    if found:
        p, idx = found
        # Get substring after pattern
        start = idx + len(p)
        segment = desc[start:]
    else:
        # fallback: try to find 'offers' then take what follows
        idx = lower.find('offers')
        if idx != -1:
            # take substring after 'offers'
            start = idx + len('offers')
            # if 'in' shortly after, skip to 'in'
            seg = desc[start:]
            m = re.search(r'\bin\b', seg, flags=re.IGNORECASE)
            if m:
                segment = seg[m.end():]
            else:
                segment = seg
        else:
            # fallback: try last 'in ' occurrence after the address phrase 'Located at'
            idx_loc = lower.find('located at')
            if idx_loc != -1:
                # take substring after the comma that follows the address
                # find the first ')' or second comma after 'located at'? Simpler: find 'this' after address
                idx_this = lower.find('this', idx_loc)
                if idx_this != -1:
                    seg = desc[idx_this:]
                    m = re.search(r'\bin\b', seg, flags=re.IGNORECASE)
                    if m:
                        segment = seg[m.end():]
            if segment is None:
                # ultimate fallback: take last 200 chars
                segment = desc[-200:]
    # Clean segment
    if not segment:
        return []
    # remove trailing sentence fragments after a period
    segment = segment.split('.')
    segment = segment[0]
    # Now split by commas and ' and '
    # Replace ' & ' with comma
    seg = segment.replace(' & ', ', ').replace(';', ',')
    # Remove words like 'and', 'to', 'ranging from'
    # We'll split on commas first
    parts = [p.strip() for p in seg.split(',') if p.strip()]
    # Further split parts that contain ' and ' into subparts
    final = []
    for part in parts:
        # remove leading connecting words
        part = re.sub(r'^(the |a |of |in the |in |the categories of |the category of )', '', part, flags=re.IGNORECASE).strip()
        # split by ' and '
        sub = re.split(r'\band\b|\bto\b|/|\bvs\b', part, flags=re.IGNORECASE)
        for s in sub:
            s2 = s.strip().strip(' .')
            if s2:
                # remove leading words like 'services', 'products'
                s2 = re.sub(r'^(services|products|options|fields|fields of)\b', '', s2, flags=re.IGNORECASE).strip()
                if s2:
                    final.append(s2)
    # normalize: remove duplicates, preserve order
    seen = set()
    out = []
    for f in final:
        # Remove trailing phrases like 'and', 'including'
        f = f.strip().strip(',')
        if not f:
            continue
        if f.lower() in seen:
            continue
        seen.add(f.lower())
        out.append(f)
    return out

# Build mapping
bizref_to_categories = {}
category_to_businesses = defaultdict(set)
for b in businesses:
    bid = b.get('business_id')
    if not bid:
        continue
    attrs = parse_attributes(b.get('attributes'))
    val = attrs.get('BusinessAcceptsCreditCards')
    accepts = False
    if isinstance(val, bool):
        accepts = val
    elif isinstance(val, str) and val.strip().lower() == 'true':
        accepts = True
    if not accepts:
        continue
    # attempt to get categories
    cats = b.get('categories')
    cat_list = []
    if cats and isinstance(cats, list):
        cat_list = [c.strip() for c in cats if c and c.strip()]
    elif cats and isinstance(cats, str) and cats.strip().lower() != 'none':
        cat_list = [c.strip() for c in cats.split(',') if c.strip()]
    if not cat_list:
        # try parse from description
        desc = b.get('description')
        cat_list = extract_categories_from_description(desc)
    if not cat_list:
        continue
    bref = bid.replace('businessid_', 'businessref_')
    bizref_to_categories[bref] = cat_list
    for c in cat_list:
        category_to_businesses[c].add(bref)

# Load reviews into mapping business_ref -> list of ratings
biz_reviews = defaultdict(list)
for r in reviews:
    bref = r.get('business_ref')
    rating_raw = r.get('rating')
    try:
        rating = float(rating_raw)
    except Exception:
        continue
    biz_reviews[bref].append(rating)

# compute for each category
category_stats = []
for c, bizset in category_to_businesses.items():
    count = len(bizset)
    # gather ratings for all reviews whose business_ref in bizset
    ratings = []
    for bref in bizset:
        ratings.extend(biz_reviews.get(bref, []))
    avg = None
    if ratings:
        avg = sum(ratings)/len(ratings)
    category_stats.append({'category': c, 'business_count': count, 'average_rating': round(avg,2) if avg is not None else None, 'num_ratings': len(ratings)})

# find max
if not category_stats:
    result = {'category': None, 'business_count': 0, 'average_rating': None}
else:
    max_count = max(cs['business_count'] for cs in category_stats)
    candidates = [cs for cs in category_stats if cs['business_count']==max_count]
    # if multiple pick highest average_rating, treating None as -inf
    def avg_key(x):
        return x['average_rating'] if x['average_rating'] is not None else -999
    candidates_sorted = sorted(candidates, key=lambda x: (-avg_key(x), x['category']))
    top = candidates_sorted[0]
    result = {'category': top['category'], 'business_count': top['business_count'], 'average_rating': top['average_rating'], 'num_ratings': top['num_ratings']}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_0QTDBTRd8H2RpxhSyMvftFu1': ['checkin', 'business'], 'var_call_VJcMYyiV5SnGv91Ebp3eBv6h': ['review', 'tip', 'user'], 'var_call_zenaF9gAgfmTXB50cZZX9sgh': 'file_storage/call_zenaF9gAgfmTXB50cZZX9sgh.json', 'var_call_qlkHo3dF8SjDijFURBwJADSJ': 'file_storage/call_qlkHo3dF8SjDijFURBwJADSJ.json', 'var_call_nEII5g43LY0Blwe2Q4EG9evd': {'category': None, 'business_count': 0, 'average_rating': None}, 'var_call_h66gNLc8vDGPJMwQcm4Ffwlo': {'total_businesses': 100, 'with_categories_count': 0, 'sample_accepts_credit_cards': [{'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'categories': None, 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}}, {'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'categories': None, 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'business_id': 'businessid_88', 'name': 'Impact Guns', 'categories': None, 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}}, {'business_id': 'businessid_33', 'name': 'J&Q Nails', 'categories': None, 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}}, {'business_id': 'businessid_92', 'name': 'Luminosity', 'categories': None, 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'True', 'NoiseLevel': "u'quiet'", 'WiFi': "u'no'"}}, {'business_id': 'businessid_64', 'name': 'Nail Care Salon', 'categories': None, 'attributes': {'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': True, 'valet': False}", 'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'True', 'WiFi': "u'free'"}}, {'business_id': 'businessid_52', 'name': 'Architectural Antiques of Indianapolis', 'categories': None, 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'BikeParking': 'True'}}, {'business_id': 'businessid_29', 'name': "Aster's Floral Shop", 'categories': None, 'attributes': {'BikeParking': 'True', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsPriceRange2': '2', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsDelivery': 'None'}}, {'business_id': 'businessid_10', 'name': 'China Wok', 'categories': None, 'attributes': {'RestaurantsGoodForGroups': 'True', 'RestaurantsDelivery': 'False', 'RestaurantsTakeOut': 'True', 'HasTV': 'True', 'BusinessAcceptsCreditCards': 'True', 'Ambience': "{'touristy': False, 'hipster': False, 'romantic': False, 'divey': False, 'intimate': False, 'trendy': False, 'upscale': False, 'classy': False, 'casual': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': False, 'brunch': False, 'breakfast': False}", 'BusinessParking': "{u'valet': False, u'garage': False, u'street': False, u'lot': True, u'validated': False}"}}, {'business_id': 'businessid_61', 'name': 'Brandon Family Medical Care', 'categories': None, 'attributes': {'ByAppointmentOnly': 'True', 'BusinessAcceptsCreditCards': 'True'}}]}, 'var_call_xQTpFtpR13zpzNbkcqvFFafi': 'file_storage/call_xQTpFtpR13zpzNbkcqvFFafi.json'}

exec(code, env_args)
