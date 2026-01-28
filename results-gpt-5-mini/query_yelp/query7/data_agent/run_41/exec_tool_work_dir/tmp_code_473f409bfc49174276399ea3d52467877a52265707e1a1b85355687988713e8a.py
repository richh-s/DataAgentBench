code = """import json
import re
from collections import defaultdict

# var_call_vye... and var_call_jsWw... are available
reviews = var_call_vyeLE0Nj2E6SmzjvQ2riAPoQ
biz_file = var_call_jsWw0y3YO7IOLGzEkApV8RC7

# Load business data from file
with open(biz_file, 'r') as f:
    bizs = json.load(f)

# Build business_id -> business entry map
biz_map = {b.get('business_id'): b for b in bizs}

# Build ref -> count
ref_counts = {}
for r in reviews:
    ref = r.get('business_ref')
    try:
        cnt = int(r.get('review_cnt'))
    except:
        try:
            cnt = int(r.get('review_cnt', 0))
        except:
            cnt = 0
    ref_counts[ref] = cnt

# Helper to extract categories from description
keywords = ['offers a diverse range of services and products in', 'offers a diverse range of services in', 'offers a range of services in',
            'offers a range of services, including', 'offers a range of services', 'offers a range of', 'this establishment offers', 'this business offers',
            'this facility offers', 'this spot offers', 'this location offers', 'offers', 'in the category of', 'in the categories of', 'in the category',
            'includes', 'specializes in', 'offers a diverse range of', 'offers a range', 'the category of']

filler_patterns = [r"making it a.*$", r"to meet all your.*$", r"perfect for.*$", r"to meet.*$", r"offering.*$", r"providing.*$"]

def extract_categories(desc):
    if not desc:
        return []
    d = desc.strip()
    low = d.lower()
    idxs = []
    for kw in keywords:
        i = low.find(kw)
        if i!=-1:
            idxs.append(i)
    if idxs:
        i = min(idxs)
        s = d[i:]
    else:
        # fallback: try to find first dash or 'this' occurrence after location
        s = d
    # cut at first period
    if '.' in s:
        s = s.split('.')[0]
    # remove introductory phrases upto 'in' or 'offers'
    # remove known starting phrases
    for kw in keywords:
        pat = re.compile(re.escape(kw), re.IGNORECASE)
        s = pat.sub('', s)
    # remove filler trailing phrases
    for pat in filler_patterns:
        s = re.sub(pat, '', s, flags=re.IGNORECASE)
    # replace conjunctions with commas
    s = re.sub(r'\sand\s', ',', s, flags=re.IGNORECASE)
    s = s.replace(' & ', ',')
    s = s.replace('/', ',')
    # split by comma
    parts = [p.strip() for p in re.split(r',', s) if p.strip()]
    # filter out noise
    cats = []
    for p in parts:
        # remove leading words like 'including', 'such as', 'offers'
        p = re.sub(r'^(including|such as|offer(s)?|provides|providing)\s+', '', p, flags=re.IGNORECASE).strip()
        # drop small noise tokens
        if len(p) < 2:
            continue
        # drop tokens that are clearly not categories
        lowp = p.lower()
        if lowp.startswith('located at') or 'located at' in lowp:
            continue
        if any(phrase in lowp for phrase in ['located', 'this', 'offers', 'perfect for', 'making it', 'to meet', 'provides', 'offering']):
            continue
        # normalize spacing
        p = re.sub(r'\s+', ' ', p)
        cats.append(p)
    # further split long tokens that contain 'and'
    final = []
    for c in cats:
        if ' and ' in c.lower():
            for sub in re.split(r'\band\b', c, flags=re.IGNORECASE):
                sub = sub.strip()
                if sub:
                    final.append(sub)
        else:
            final.append(c)
    # deduplicate preserving order
    seen=set()
    out=[]
    for c in final:
        if c not in seen:
            seen.add(c)
            out.append(c)
    return out

# Aggregate counts per category
cat_counts = defaultdict(int)
missing = []
for ref, cnt in ref_counts.items():
    bid = ref.replace('businessref_', 'businessid_')
    biz = biz_map.get(bid)
    if not biz:
        missing.append(bid)
        continue
    desc = biz.get('description') or biz.get('name') or ''
    cats = extract_categories(desc)
    if not cats:
        # fallback: use name as category
        cats = [biz.get('name')]
    for c in cats:
        cat_counts[c] += cnt

# Prepare sorted results
sorted_cats = sorted(cat_counts.items(), key=lambda x: x[1], reverse=True)
top5 = [{'category': c, 'review_count': v} for c,v in sorted_cats[:5]]

import json
print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_ACswXX5GHOerjUebc14RqUxD': ['checkin', 'business'], 'var_call_LxMOlI11lTc5xawrWI39FZm5': ['review', 'tip', 'user'], 'var_call_a7eSQqF8xqduK1E3MxdeKHBr': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'name': 'Candy Barrel', 'review_count': '7', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '4', 'BikeParking': 'False'}, 'hours': 'None', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'name': 'Luminosity', 'review_count': '39', 'is_open': '1', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'True', 'NoiseLevel': "u'quiet'", 'WiFi': "u'no'"}, 'hours': {'Monday': '10:0-21:0', 'Tuesday': '10:0-21:0', 'Wednesday': '10:0-21:0', 'Thursday': '10:0-21:0', 'Friday': '10:0-21:0', 'Saturday': '10:0-21:0', 'Sunday': '11:0-18:0'}, 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'_id': '6859a000fe8b31cd7362e2b2', 'business_id': 'businessid_64', 'name': 'Nail Care Salon', 'review_count': '6', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': True, 'valet': False}", 'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'True', 'WiFi': "u'free'"}, 'hours': {'Monday': '10:0-20:0', 'Tuesday': '10:0-20:0', 'Wednesday': '10:0-20:0', 'Thursday': '10:0-20:0', 'Friday': '10:0-20:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.'}, {'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52', 'name': 'Architectural Antiques of Indianapolis', 'review_count': '6', 'is_open': '1', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-17:0', 'Tuesday': '10:0-17:0', 'Wednesday': '10:0-17:0', 'Thursday': '10:0-17:0', 'Friday': '10:0-17:0', 'Saturday': '10:0-17:0'}, 'description': 'Located at 5000 W 96th St in Indianapolis, IN, this establishment offers a diverse selection of Antiques, Shopping, Home Services, and Lighting Fixtures & Equipment for all your home and decorative needs.'}, {'_id': '6859a000fe8b31cd7362e2b4', 'business_id': 'businessid_29', 'name': "Aster's Floral Shop", 'review_count': '25', 'is_open': '1', 'attributes': {'BikeParking': 'True', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsPriceRange2': '2', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsDelivery': 'None'}, 'hours': {'Monday': '9:0-18:0', 'Tuesday': '9:0-18:0', 'Wednesday': '9:0-18:0', 'Thursday': '9:0-18:0', 'Friday': '9:0-18:0', 'Saturday': '9:0-18:0'}, 'description': 'Located at 41 Haddon Ave in Collingswood, NJ, this versatile establishment offers a range of services including Wedding Planning, Flowers & Gifts, Event Planning & Services, Financial Services, Shopping, and Florists.'}], 'var_call_DdQ6gIQRpvUIezn1IHJ8viSX': [{'user_id': 'userid_746', 'yelping_since': '2016-06-23 01:59:28'}, {'user_id': 'userid_1109', 'yelping_since': '2016-10-16 18:32:25'}, {'user_id': 'userid_1950', 'yelping_since': '2016-04-16 03:42:28'}, {'user_id': 'userid_1316', 'yelping_since': '2016-12-29 21:32:44'}, {'user_id': 'userid_1182', 'yelping_since': '2016-03-20 18:41:14'}, {'user_id': 'userid_151', 'yelping_since': '2016-11-07 18:40:10'}, {'user_id': 'userid_1158', 'yelping_since': '2016-01-31 16:25:04'}, {'user_id': 'userid_508', 'yelping_since': '2016-07-08 22:37:42'}, {'user_id': 'userid_435', 'yelping_since': '2016-10-31 09:46:54'}, {'user_id': 'userid_958', 'yelping_since': '2016-03-23 20:55:45'}, {'user_id': 'userid_1879', 'yelping_since': '2016-07-08 17:56:11'}, {'user_id': 'userid_308', 'yelping_since': '2016-07-02 23:48:36'}, {'user_id': 'userid_1179', 'yelping_since': '2016-12-18 17:31:52'}, {'user_id': 'userid_324', 'yelping_since': '2016-10-10 22:09:08'}, {'user_id': 'userid_863', 'yelping_since': '2016-01-16 00:45:41'}, {'user_id': 'userid_100', 'yelping_since': '2016-08-18 11:39:42'}, {'user_id': 'userid_1333', 'yelping_since': '2016-12-07 14:57:41'}, {'user_id': 'userid_1636', 'yelping_since': '2016-02-14 23:51:28'}, {'user_id': 'userid_1850', 'yelping_since': '2016-07-22 19:26:01'}, {'user_id': 'userid_711', 'yelping_since': '2016-07-07 22:59:48'}, {'user_id': 'userid_729', 'yelping_since': '2016-02-06 00:41:18'}, {'user_id': 'userid_1505', 'yelping_since': '2016-07-14 00:26:46'}, {'user_id': 'userid_1315', 'yelping_since': '2016-03-07 02:47:32'}, {'user_id': 'userid_1708', 'yelping_since': '2016-03-06 20:06:53'}, {'user_id': 'userid_1661', 'yelping_since': '2016-06-13 00:48:17'}, {'user_id': 'userid_850', 'yelping_since': '2016-04-05 22:20:15'}, {'user_id': 'userid_1675', 'yelping_since': '2016-02-13 20:18:19'}, {'user_id': 'userid_227', 'yelping_since': '2016-01-16 01:12:00'}, {'user_id': 'userid_577', 'yelping_since': '2016-08-05 21:32:23'}, {'user_id': 'userid_257', 'yelping_since': '2016-10-19 21:58:32'}, {'user_id': 'userid_598', 'yelping_since': '2016-07-24 20:27:40'}, {'user_id': 'userid_847', 'yelping_since': '2016-08-04 20:28:55'}, {'user_id': 'userid_673', 'yelping_since': '2016-09-29 14:11:39'}, {'user_id': 'userid_1856', 'yelping_since': '2016-11-19 23:19:11'}, {'user_id': 'userid_384', 'yelping_since': '2016-04-21 20:00:19'}, {'user_id': 'userid_935', 'yelping_since': '2016-03-04 03:53:07'}, {'user_id': 'userid_210', 'yelping_since': '2016-06-24 03:16:47'}, {'user_id': 'userid_1101', 'yelping_since': '2016-06-13 19:58:37'}, {'user_id': 'userid_945', 'yelping_since': '2016-05-08 04:31:48'}, {'user_id': 'userid_842', 'yelping_since': '2016-02-21 19:02:44'}, {'user_id': 'userid_1351', 'yelping_since': '2016-03-30 02:56:55'}, {'user_id': 'userid_230', 'yelping_since': '2016-09-28 21:47:27'}, {'user_id': 'userid_593', 'yelping_since': '2016-11-18 05:33:16'}, {'user_id': 'userid_1431', 'yelping_since': '2016-01-06 23:48:07'}, {'user_id': 'userid_686', 'yelping_since': '2016-02-20 02:24:38'}, {'user_id': 'userid_527', 'yelping_since': '2016-06-26 04:19:08'}, {'user_id': 'userid_244', 'yelping_since': '2016-02-06 05:06:29'}, {'user_id': 'userid_393', 'yelping_since': '2016-08-16 18:42:51'}, {'user_id': 'userid_1178', 'yelping_since': '2016-05-05 18:04:24'}, {'user_id': 'userid_526', 'yelping_since': '2016-12-16 00:17:31'}, {'user_id': 'userid_90', 'yelping_since': '2016-07-14 00:52:49'}, {'user_id': 'userid_238', 'yelping_since': '2016-12-29 01:41:33'}, {'user_id': 'userid_1105', 'yelping_since': '2016-03-15 21:53:34'}], 'var_call_vyeLE0Nj2E6SmzjvQ2riAPoQ': [{'business_ref': 'businessref_13', 'review_cnt': '1'}, {'business_ref': 'businessref_79', 'review_cnt': '1'}, {'business_ref': 'businessref_74', 'review_cnt': '2'}, {'business_ref': 'businessref_66', 'review_cnt': '2'}, {'business_ref': 'businessref_15', 'review_cnt': '1'}, {'business_ref': 'businessref_33', 'review_cnt': '2'}, {'business_ref': 'businessref_36', 'review_cnt': '2'}, {'business_ref': 'businessref_60', 'review_cnt': '2'}, {'business_ref': 'businessref_12', 'review_cnt': '1'}, {'business_ref': 'businessref_6', 'review_cnt': '1'}, {'business_ref': 'businessref_31', 'review_cnt': '1'}, {'business_ref': 'businessref_57', 'review_cnt': '2'}, {'business_ref': 'businessref_86', 'review_cnt': '1'}, {'business_ref': 'businessref_62', 'review_cnt': '1'}, {'business_ref': 'businessref_37', 'review_cnt': '1'}, {'business_ref': 'businessref_53', 'review_cnt': '1'}, {'business_ref': 'businessref_92', 'review_cnt': '2'}, {'business_ref': 'businessref_26', 'review_cnt': '1'}, {'business_ref': 'businessref_68', 'review_cnt': '1'}, {'business_ref': 'businessref_41', 'review_cnt': '1'}, {'business_ref': 'businessref_10', 'review_cnt': '1'}, {'business_ref': 'businessref_45', 'review_cnt': '3'}, {'business_ref': 'businessref_96', 'review_cnt': '2'}, {'business_ref': 'businessref_98', 'review_cnt': '1'}, {'business_ref': 'businessref_14', 'review_cnt': '1'}, {'business_ref': 'businessref_20', 'review_cnt': '1'}], 'var_call_jsWw0y3YO7IOLGzEkApV8RC7': 'file_storage/call_jsWw0y3YO7IOLGzEkApV8RC7.json'}

exec(code, env_args)
