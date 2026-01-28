code = """import json, re
with open(var_call_cKAUvs32jTulvBxlVKm3UG9A, 'r') as f:
    businesses = json.load(f)
with open(var_call_HqfVjLmSpm2LUwUZsWZG8Qg2, 'r') as f:
    reviews = json.load(f)

US_STATES = set(['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY','DC'])

# map reviews to business_ref
ratings_by_ref = {}
for r in reviews:
    br = r.get('business_ref')
    try:
        rating = float(r.get('rating'))
    except Exception:
        continue
    ratings_by_ref.setdefault(br, []).append(rating)

# wifi detection
def has_wifi(attrs):
    if not isinstance(attrs, dict):
        return False
    for k, v in attrs.items():
        if not k:
            continue
        key = str(k).lower()
        if 'wifi' in key or 'wi-fi' in key:
            if v is None:
                return False
            sval = str(v).lower()
            # strip punctuation
            sval_clean = re.sub(r"[^a-z0-9]", "", sval)
            if sval_clean in ('no','none','false','0'):
                return False
            return True
    return False

# extract state from description robustly
def extract_state(desc):
    if not desc:
        return None
    # 1) look for ' in City, ST' pattern
    m = re.search(r'in [^,]+,\s*([A-Za-z]{2})\b', desc)
    if m:
        st = m.group(1).upper()
        if st in US_STATES:
            return st
    # 2) split by commas and find a part that's exactly a state code after stripping
    parts = [p.strip() for p in desc.split(',')]
    for p in parts:
        p2 = re.sub(r"[^A-Za-z]", "", p).upper()
        if p2 in US_STATES and len(p2) == 2:
            return p2
    # 3) find last occurrence of ', ST' where ST uppercase
    m2 = re.search(r',\s*([A-Z]{2})\b', desc)
    if m2 and m2.group(1) in US_STATES:
        return m2.group(1)
    return None

from collections import defaultdict
state_business_refs = defaultdict(set)
for b in businesses:
    attrs = b.get('attributes')
    if not attrs or not has_wifi(attrs):
        continue
    desc = b.get('description') or ''
    st = extract_state(desc)
    if not st:
        continue
    bid = b.get('business_id')
    if not bid:
        continue
    bref = bid.replace('businessid_', 'businessref_')
    state_business_refs[st].add(bref)

# compute stats
state_stats = []
for st, bref_set in state_business_refs.items():
    count = len(bref_set)
    total = 0.0
    cnt = 0
    for bref in bref_set:
        rlist = ratings_by_ref.get(bref, [])
        total += sum(rlist)
        cnt += len(rlist)
    avg = None
    if cnt > 0:
        avg = round(total / cnt, 2)
    state_stats.append({'state': st, 'wifi_business_count': count, 'ratings_count': cnt, 'average_rating': avg})

if not state_stats:
    out = {'error': 'No WiFi businesses with US states found.'}
else:
    top = sorted(state_stats, key=lambda x: (-x['wifi_business_count'], x['state']))[0]
    out = top

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_cKAUvs32jTulvBxlVKm3UG9A': 'file_storage/call_cKAUvs32jTulvBxlVKm3UG9A.json', 'var_call_HqfVjLmSpm2LUwUZsWZG8Qg2': 'file_storage/call_HqfVjLmSpm2LUwUZsWZG8Qg2.json', 'var_call_YQstDHrjxqbZGF1nEQksbPZw': {'error': 'No results'}, 'var_call_CV7owKU3aXGXXwrUax5RU3wj': {'total_businesses': 91, 'with_attributes': 91, 'wifi_key_count': 35, 'samples': [{'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'wifi_key': 'WiFi', 'wifi_val': "u'no'", 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_92', 'name': 'Luminosity', 'wifi_key': 'WiFi', 'wifi_val': "u'no'", 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'business_id': 'businessid_64', 'name': 'Nail Care Salon', 'wifi_key': 'WiFi', 'wifi_val': "u'free'", 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.'}, {'business_id': 'businessid_54', 'name': '7-Eleven', 'wifi_key': 'WiFi', 'wifi_val': "u'free'", 'description': 'Located at 13151 Race Track Rd in Tampa, FL, this establishment offers a variety of services including Service Stations, Coffee & Tea, Gas Stations, Automotive, Gas Stations, Food, and Convenience Stores.'}, {'business_id': 'businessid_91', 'name': 'Cafe Porche and snowbar', 'wifi_key': 'WiFi', 'wifi_val': "u'free'", 'description': 'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning, Comfort Food, Cafes, Restaurants, to Event Planning & Services, making it a perfect spot for any occasion.'}, {'business_id': 'businessid_93', 'name': "Callahan's Corner", 'wifi_key': 'WiFi', 'wifi_val': "u'free'", 'description': 'Located at 914 Edwardsville Rd in Troy, IL, this vibrant spot offers a diverse menu featuring American (New) cuisine, along with a lively atmosphere perfect for nightlife, bars, restaurants, and sports bars.'}, {'business_id': 'businessid_24', 'name': 'FroYo Frozen Yogurt', 'wifi_key': 'WiFi', 'wifi_val': "u'no'", 'description': 'Located at 4663 Maryland Ave in Saint Louis, MO, this delightful spot offers a tempting selection of treats in the categories of Food, Ice Cream & Frozen Yogurt.'}, {'business_id': 'businessid_26', 'name': "McDonald's", 'wifi_key': 'WiFi', 'wifi_val': "u'free'", 'description': 'Located at 7003 Seminole Blvd in Seminole, FL, this establishment specializes in a variety of offerings, including Fast Food, Restaurants, Coffee & Tea, Food, and Burgers, making it a convenient stop for a quick meal or a refreshing beverage.'}, {'business_id': 'businessid_89', 'name': 'King of Prussia Laundromat', 'wifi_key': 'WiFi', 'wifi_val': "u'free'", 'description': 'Located at 540 Shoemaker Rd in King of Prussia, PA, this establishment offers a range of services including Dry Cleaning & Laundry, Laundromat, Local Services, and Laundry Services.'}, {'business_id': 'businessid_32', 'name': 'The Recovery Room Bar & Grill', 'wifi_key': 'WiFi', 'wifi_val': "u'no'", 'description': 'Located at 1715 Jefferson Hwy in New Orleans, LA, this lively establishment offers a great atmosphere for enjoying Bars, Dive Bars, Burgers, Nightlife, and Restaurants.'}, {'business_id': 'businessid_97', 'name': 'Executive Auto Body', 'wifi_key': 'WiFi', 'wifi_val': "u'free'", 'description': 'Located at 560 Cottman Ave in Cheltenham, PA, this establishment specializes in Body Shops, Automotive services to meet all your vehicle repair needs.'}, {'business_id': 'businessid_27', 'name': 'Egg Roll King Two', 'wifi_key': 'WiFi', 'wifi_val': "u'no'", 'description': 'Located at 2253 Oddie Blvd in Sparks, NV, this establishment offers a delightful dining experience featuring a diverse menu in the category of Restaurants, Chinese.'}, {'business_id': 'businessid_67', 'name': "Hanoi's Pho", 'wifi_key': 'WiFi', 'wifi_val': "u'free'", 'description': 'Located at 1501 W Chester Pike in Havertown, PA, this eatery specializes in Vietnamese, Soup, Restaurants, Noodles, offering a delightful array of flavorful dishes.'}, {'business_id': 'businessid_7', 'name': 'Eagle Luxe Reel Theatre', 'wifi_key': 'WiFi', 'wifi_val': "u'no'", 'description': 'Located at 170 E Eagles Gate Dr in Eagle, ID, this establishment offers a vibrant experience in the realm of Cinema, Arts & Entertainment.'}, {'business_id': 'businessid_51', 'name': "Gram's Place", 'wifi_key': 'WiFi', 'wifi_val': "u'free'", 'description': 'Situated at 3109 N Ola Ave in Tampa, FL, this establishment offers a range of services in the hospitality sector, including Hotels & Travel, Hostels, Bed & Breakfast, Hotels, and Event Planning & Services.'}, {'business_id': 'businessid_5', 'name': 'Simply Done Cafe', 'wifi_key': 'WiFi', 'wifi_val': "'no'", 'description': 'Located at 10728 124 Street in Edmonton, AB, this inviting spot offers a delightful menu perfect for anyone looking to enjoy a satisfying meal, specializing in Breakfast & Brunch, Restaurants.'}, {'business_id': 'businessid_6', 'name': 'The Jungle', 'wifi_key': 'WiFi', 'wifi_val': "'free'", 'description': 'Located at 246 W 1st St in Reno, NV, this vibrant destination offers a delightful mix of Restaurants, Breakfast & Brunch, Bars, Wine Bars, Coffee & Tea, Food, Cafes, Sandwiches, and Nightlife, making it an ideal spot for any meal or occasion.'}, {'business_id': 'businessid_87', 'name': 'Jordans Fish and Chicken', 'wifi_key': 'WiFi', 'wifi_val': "u'no'", 'description': 'Located at 6416 W Washington St in Indianapolis, IN, this establishment offers a delightful menu featuring Restaurants, Chicken Wings, Fish & Chips, and American (Traditional) cuisine.'}, {'business_id': 'businessid_55', 'name': 'Uptown Snoballs and Ice Cream', 'wifi_key': 'WiFi', 'wifi_val': "u'free'", 'description': 'Located at 1003 4th St N in St. Petersburg, FL, this delightful spot offers a variety of treats including Ice Cream & Frozen Yogurt, Shaved Ice, Food, and Desserts.'}, {'business_id': 'businessid_96', 'name': 'Farmhaus Restaurant', 'wifi_key': 'WiFi', 'wifi_val': "u'no'", 'description': 'Located at 3257 Ivanhoe Ave in Saint Louis, MO, this establishment offers a vibrant atmosphere perfect for enjoying a diverse selection of experiences, including Wine Bars, American (New), Cocktail Bars, Restaurants, American (Traditional), Nightlife, and Bars.'}]}, 'var_call_K0IFZc91jCDLAWFBONzRvYdR': {'error': 'No WiFi businesses with US state found.'}, 'var_call_4ILenEOABk9kvQEcyy5Q0Bwr': {'error': 'No WiFi businesses with US states found.'}, 'var_call_OLM4oeEVgr7v9Kn8mfG4rYF0': 'file_storage/call_OLM4oeEVgr7v9Kn8mfG4rYF0.json'}

exec(code, env_args)
