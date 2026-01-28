code = """import json, re
from collections import defaultdict

# Gather all storage variables that start with var_call_
storage_vars = {k: v for k, v in globals().items() if k.startswith('var_call_')}

# reviews aggregation from earlier SQL
reviews = storage_vars.get('var_call_GVD5X3CHVSQoYi8Fb6SeyNGz')

# Build business_id -> categories mapping
biz_cat = {}

def clean(s):
    return s.strip().rstrip('. ')

for name, val in storage_vars.items():
    # val can be a list of dicts or a filepath string to a JSON file
    docs = None
    if isinstance(val, str) and val.endswith('.json'):
        try:
            with open(val, 'r', encoding='utf-8') as f:
                docs = json.load(f)
        except Exception:
            docs = None
    elif isinstance(val, list):
        docs = val
    else:
        continue
    if not docs:
        continue
    for d in docs:
        if not isinstance(d, dict):
            continue
        bid = d.get('business_id')
        if not bid:
            continue
        cats = []
        if 'categories' in d and d.get('categories'):
            c = d.get('categories')
            if isinstance(c, list):
                cats = [clean(str(x)) for x in c if str(x).strip()]
            else:
                cats = [clean(x) for x in str(c).split(',') if x.strip()]
        if not cats and d.get('description'):
            desc = d.get('description')
            desc = desc.replace('\n', ' ')
            low = desc.lower()
            # try to find 'categories of' or 'offers' patterns
            candidate = None
            m = re.search(r'categories? of\s*(.*)', desc, flags=re.IGNORECASE)
            if m:
                candidate = m.group(1)
            else:
                m2 = re.search(r'offers[\w\s,]*?(?:in|including|the categories of)\s+(.*)', desc, flags=re.IGNORECASE)
                if m2:
                    candidate = m2.group(1)
            if not candidate:
                parts = desc.split(',')
                if len(parts) > 2:
                    candidate = ','.join(parts[2:])
                else:
                    candidate = desc
            candidate = candidate.split('.')[0]
            candidate = re.sub(r'\band\b', ',', candidate, flags=re.IGNORECASE)
            parts = re.split(r',|/', candidate)
            for p in parts:
                p = p.strip()
                if not p:
                    continue
                p_low = p.lower()
                if p_low.startswith('a range of services in'):
                    p = p[len('a range of services in'):]
                if p_low.startswith('including'):
                    p = p[len('including'):]
                p = clean(p)
                if p:
                    cats.append(p)
        # split on '&' and ' and '
        final = []
        for c in cats:
            for sub in re.split(r'&| and ', c):
                ssub = clean(sub)
                if ssub:
                    final.append(ssub)
        # dedupe preserving order
        seen = set()
        out = []
        for c in final:
            if c not in seen:
                seen.add(c)
                out.append(c)
        if out:
            biz_cat[bid] = out

# Aggregate review counts by category
cat_counts = defaultdict(int)
if not reviews:
    reviews = []
for rec in reviews:
    bref = rec.get('business_ref')
    try:
        rc = int(rec.get('review_count'))
    except Exception:
        try:
            rc = int(str(rec.get('review_count')))
        except Exception:
            rc = 0
    bid = None
    if isinstance(bref, str) and bref.startswith('businessref_'):
        bid = 'businessid_' + bref.split('_', 1)[1]
    else:
        bid = bref
    cats = biz_cat.get(bid)
    if not cats:
        continue
    for c in cats:
        cat_counts[c] += rc

sorted_cats = sorted(cat_counts.items(), key=lambda x: x[1], reverse=True)
result = [{"category": k, "total_reviews_from_2016_users": v} for k, v in sorted_cats[:5]]

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_P65b3Ebh5RGjST8CC3Qa8RlV': ['business', 'checkin'], 'var_call_s4IXnZ3il1F6TSw32HiFhRYB': ['review', 'tip', 'user'], 'var_call_KtKiT0Ihn7XbBKhltcRL89fC': 'file_storage/call_KtKiT0Ihn7XbBKhltcRL89fC.json', 'var_call_LqHtbfyUfFa1y7ZszRlV9kuj': [{'user_id': 'userid_746'}, {'user_id': 'userid_1109'}, {'user_id': 'userid_1950'}, {'user_id': 'userid_1316'}, {'user_id': 'userid_1182'}, {'user_id': 'userid_151'}, {'user_id': 'userid_1158'}, {'user_id': 'userid_508'}, {'user_id': 'userid_435'}, {'user_id': 'userid_958'}, {'user_id': 'userid_1879'}, {'user_id': 'userid_308'}, {'user_id': 'userid_1179'}, {'user_id': 'userid_324'}, {'user_id': 'userid_863'}, {'user_id': 'userid_100'}, {'user_id': 'userid_1333'}, {'user_id': 'userid_1636'}, {'user_id': 'userid_1850'}, {'user_id': 'userid_711'}, {'user_id': 'userid_729'}, {'user_id': 'userid_1505'}, {'user_id': 'userid_1315'}, {'user_id': 'userid_1708'}, {'user_id': 'userid_1661'}, {'user_id': 'userid_850'}, {'user_id': 'userid_1675'}, {'user_id': 'userid_227'}, {'user_id': 'userid_577'}, {'user_id': 'userid_257'}, {'user_id': 'userid_598'}, {'user_id': 'userid_847'}, {'user_id': 'userid_673'}, {'user_id': 'userid_1856'}, {'user_id': 'userid_384'}, {'user_id': 'userid_935'}, {'user_id': 'userid_210'}, {'user_id': 'userid_1101'}, {'user_id': 'userid_945'}, {'user_id': 'userid_842'}, {'user_id': 'userid_1351'}, {'user_id': 'userid_230'}, {'user_id': 'userid_593'}, {'user_id': 'userid_1431'}, {'user_id': 'userid_686'}, {'user_id': 'userid_527'}, {'user_id': 'userid_244'}, {'user_id': 'userid_393'}, {'user_id': 'userid_1178'}, {'user_id': 'userid_526'}, {'user_id': 'userid_90'}, {'user_id': 'userid_238'}, {'user_id': 'userid_1105'}], 'var_call_GVD5X3CHVSQoYi8Fb6SeyNGz': [{'business_ref': 'businessref_45', 'review_count': '3'}, {'business_ref': 'businessref_57', 'review_count': '2'}, {'business_ref': 'businessref_74', 'review_count': '2'}, {'business_ref': 'businessref_66', 'review_count': '2'}, {'business_ref': 'businessref_92', 'review_count': '2'}, {'business_ref': 'businessref_36', 'review_count': '2'}, {'business_ref': 'businessref_60', 'review_count': '2'}, {'business_ref': 'businessref_33', 'review_count': '2'}, {'business_ref': 'businessref_96', 'review_count': '2'}, {'business_ref': 'businessref_86', 'review_count': '1'}, {'business_ref': 'businessref_31', 'review_count': '1'}, {'business_ref': 'businessref_53', 'review_count': '1'}, {'business_ref': 'businessref_98', 'review_count': '1'}, {'business_ref': 'businessref_12', 'review_count': '1'}, {'business_ref': 'businessref_13', 'review_count': '1'}, {'business_ref': 'businessref_79', 'review_count': '1'}, {'business_ref': 'businessref_14', 'review_count': '1'}, {'business_ref': 'businessref_20', 'review_count': '1'}, {'business_ref': 'businessref_6', 'review_count': '1'}, {'business_ref': 'businessref_15', 'review_count': '1'}, {'business_ref': 'businessref_62', 'review_count': '1'}, {'business_ref': 'businessref_26', 'review_count': '1'}, {'business_ref': 'businessref_68', 'review_count': '1'}, {'business_ref': 'businessref_41', 'review_count': '1'}, {'business_ref': 'businessref_37', 'review_count': '1'}, {'business_ref': 'businessref_10', 'review_count': '1'}], 'var_call_clJV8Te4XGi71giVQcmDVCrU': [{'_id': '6859a000fe8b31cd7362e2db', 'business_id': 'businessid_45', 'name': 'The Fresh Market', 'description': 'Located at 2900 4th St N in St. Petersburg, FL, this establishment offers a diverse range of products and services in the categories of Food, Grocery, Shopping.'}], 'var_call_IvcTCA0MHNU8XrPSlydeOdIF': [{'_id': '6859a000fe8b31cd7362e2cd', 'business_id': 'businessid_57', 'name': 'Big Boys Moving And Storage', 'description': 'Located at 13605 W Hillsborough Ave in Tampa, FL, this versatile establishment offers a range of services and dining options, including Movers, American (New), Landscape Architects, Food, Home Services, Self Storage, Local Services, Restaurants.'}], 'var_call_2jms4G3HYyBdrwJl20zP9ssx': [{'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'name': 'Candy Barrel', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}], 'var_call_zyf7GkotB21MDfb2YOTPpYFJ': [{'_id': '6859a000fe8b31cd7362e2e1', 'business_id': 'businessid_66', 'name': 'Panda Express', 'description': 'Located at 3849 State St. Space I-58 in Santa Barbara, CA, this establishment offers a variety of quick and delicious options in the categories of Fast Food, Chinese, Restaurants.'}], 'var_call_D5ak6HJftnl0JNR8kVVePZZb': [{'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'name': 'Luminosity', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}], 'var_call_LKTPptwQyqaQaA08Se1Y8rJH': [{'_id': '6859a000fe8b31cd7362e308', 'business_id': 'businessid_36', 'name': 'Pho & Beyond', 'description': "Located at 47 Easton Rd in Willow Grove, PA, this inviting establishment offers a delightful menu featuring authentic flavors in the categories of 'Restaurants, Vietnamese'."}], 'var_call_pKU1DAqUAgRyOwIkWwbJgmgh': [{'_id': '6859a000fe8b31cd7362e302', 'business_id': 'businessid_60', 'name': 'Walmart', 'description': 'Located at 8101 W Judge Perez Dr in Chalmette, LA, this versatile establishment offers a wide range of options for customers, including Food, Shopping, Fashion, Discount Store, Grocery, Electronics, Drugstores, Department Stores, ensuring that visitors can find everything they need in one convenient location.'}], 'var_call_NusBJkqNcqZE0HIuctvGzzZ0': [{'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_5nebBMIGLbriIiQn8zGvH4LY': [{'_id': '6859a000fe8b31cd7362e2e6', 'business_id': 'businessid_96', 'name': 'Farmhaus Restaurant', 'description': 'Located at 3257 Ivanhoe Ave in Saint Louis, MO, this establishment offers a vibrant atmosphere perfect for enjoying a diverse selection of experiences, including Wine Bars, American (New), Cocktail Bars, Restaurants, American (Traditional), Nightlife, and Bars.'}], 'var_call_9B826t7lJVnsN1X63QwUjO8T': [{'_id': '6859a000fe8b31cd7362e2ed', 'business_id': 'businessid_86', 'name': "Humpty's Dumplings", 'description': 'Located at 705 East Passyunk Ave in Philadelphia, PA, this vibrant eatery offers a diverse menu featuring American (New), Restaurants, American (Traditional), Asian Fusion, Noodles, Dim Sum, Fast Food, Chinese, catering to a variety of tastes and preferences.'}], 'var_call_2f2SqAQAl1caIuyOUvoZcA5H': [{'_id': '6859a000fe8b31cd7362e2fb', 'business_id': 'businessid_31', 'name': 'Island Way Car Wash', 'description': 'Located at 1234 Pasadena Ave S in South Pasadena, FL, this business specializes in Automotive services, offering a comprehensive Car Wash and professional Auto Detailing to keep your vehicle looking its best.'}], 'var_call_veehpx24n3YL1hXAR7sh3Vmx': [{'_id': '6859a000fe8b31cd7362e2ee', 'business_id': 'businessid_53', 'name': 'Samwich', 'description': 'Located at 1040 N American St, Ste 1101 in Philadelphia, PA, this eatery offers a diverse menu featuring Salad, Sandwiches, Restaurants, and Burgers.'}], 'var_call_8yYw590aIqggc3pcP6MmFBle': [{'_id': '6859a000fe8b31cd7362e304', 'business_id': 'businessid_98', 'name': 'Brookmont Apartment Homes', 'description': 'Situated at 600 Red Lion Rd in Philadelphia, PA, this establishment offers a range of services in Real Estate, Apartments, and Home Services.'}], 'var_call_R2zaSfzWqLZJGIIcPIonUbZH': [{'_id': '6859a000fe8b31cd7362e300', 'business_id': 'businessid_12', 'name': 'Atlantic Trap & Gill Pub', 'description': 'Located at 7704 Calgary Trail S in Edmonton, AB, this vibrant spot offers a diverse experience with options for Pubs, Restaurants, Nightlife, Burgers, Seafood, and Bars.'}], 'var_call_4E3bNDMu40GCsFwjkhqPigTj': [{'_id': '6859a000fe8b31cd7362e30d', 'business_id': 'businessid_13', 'name': 'Avian Glen Winery', 'description': 'Located at 3545 Almaville Rd in Smyrna, TN, this establishment offers a delightful experience encompassing Food, Arts & Entertainment, Wineries, and a Wine Tasting Room.'}], 'var_call_4P66tsnJqMN1kgXqtBwQp3T1': [{'_id': '6859a000fe8b31cd7362e2e0', 'business_id': 'businessid_79', 'name': 'Pit Stop HQ', 'description': 'Located at 838-842 Christian St in Philadelphia, PA, this establishment offers a wide range of services including Pet Groomers, Pet Stores, Pet Training, Dog Walkers, Pet Services, Pets, and Pet Sitting.'}], 'var_call_vze43BhWc1T5TOS5awSiC6Gf': [{'_id': '6859a000fe8b31cd7362e2c9', 'business_id': 'businessid_14', 'name': 'Ross Dress for Less', 'description': "Located at 7055 Marketplace Dr in Goleta, CA, this store offers a diverse selection of products across various categories, including Women's Clothing, Fashion, Department Stores, Home Decor, Home & Garden, Shopping, Men's Clothing, and Discount Store."}], 'var_call_zcPZ0DM13M6Ee57MFKnbSIz9': [{'_id': '6859a000fe8b31cd7362e2f4', 'business_id': 'businessid_20', 'name': 'Chick-fil-A', 'description': 'Located at 9040 State Road 54 in Trinity, FL, this establishment offers a diverse array of options, including Restaurants, American (New), Caterers, Fast Food, Chicken Shop, Event Planning & Services, and American (Traditional).'}], 'var_call_Tj66bpNA0dLAmXN4pN4dLmZL': [{'_id': '6859a000fe8b31cd7362e2dd', 'business_id': 'businessid_6', 'name': 'The Jungle', 'description': 'Located at 246 W 1st St in Reno, NV, this vibrant destination offers a delightful mix of Restaurants, Breakfast & Brunch, Bars, Wine Bars, Coffee & Tea, Food, Cafes, Sandwiches, and Nightlife, making it an ideal spot for any meal or occasion.'}], 'var_call_6tAJcRFnnCnYWS6nqv3SxazX': [{'_id': '6859a000fe8b31cd7362e2e5', 'business_id': 'businessid_15', 'name': 'Take 5 Oil Change', 'description': 'Located at 3803 Gen Degaulle Dr in New Orleans, LA, this establishment specializes in Automotive, Oil Change Stations, providing efficient service for all your vehicle maintenance needs.'}], 'var_call_QlujvlKG0fNsvVkSEJPvZlti': [{'_id': '6859a000fe8b31cd7362e2f7', 'business_id': 'businessid_62', 'name': 'Winn Dixie', 'description': 'Located at 8424 Sheldon Rd in Tampa, FL, this establishment offers a diverse range of products and services, including Photography Stores & Services, Shopping, Grocery, and Food.'}], 'var_call_1JnGv2lfztuzs1zOi1H3aA1T': [{'_id': '6859a000fe8b31cd7362e2c1', 'business_id': 'businessid_26', 'name': "McDonald's", 'description': 'Located at 7003 Seminole Blvd in Seminole, FL, this establishment specializes in a variety of offerings, including Fast Food, Restaurants, Coffee & Tea, Food, and Burgers, making it a convenient stop for a quick meal or a refreshing beverage.'}], 'var_call_AQTTfjolQIFHzaDrmz6luF5z': [{'_id': '6859a000fe8b31cd7362e2dc', 'business_id': 'businessid_68', 'name': 'Brow Art', 'description': 'Located at 593 Brandon Town Ctr in Brandon, FL, this establishment offers a range of services in the categories of Beauty & Spas, Hair Removal, and Eyebrow Services.'}], 'var_call_6nE8H2YLFa1yeeVjyst4Oo3l': [{'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}], 'var_call_RZVCQqHfLz6aiu7uJDMUPdYm': [{'_id': '6859a000fe8b31cd7362e2f5', 'business_id': 'businessid_37', 'name': 'Orangetheory Fitness Carrollwood', 'description': 'Located at 13122 N Dale Mabry Hwy in Tampa, FL, this facility offers a comprehensive range of services in Fitness & Instruction, Gyms, Boot Camps, Trainers, Active Life, and Interval Training Gyms.'}], 'var_call_ie5Dd13IqoTmabzyMyI7rsSz': [{'_id': '6859a000fe8b31cd7362e2b5', 'business_id': 'businessid_10', 'name': 'China Wok', 'description': "Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of 'Restaurants, Chinese'."}]}

exec(code, env_args)
