code = """import json, re
# Load data from storage variables
reviews_path = var_call_gcYSEQo3o3olHVVUQtU02ohC
businesses_path = var_call_fzkfmJ9i9wLBCNcqqIyR2U5e
users = var_call_YS8M0IXsz6wEKAKHB31nsIGb

# read files
with open(reviews_path, 'r') as f:
    reviews = json.load(f)
with open(businesses_path, 'r') as f:
    businesses = json.load(f)

# build user set
user_set = set(r['user_id'] for r in users)

# helper to extract year from date string
def extract_year(date_str):
    if not date_str:
        return None
    m = re.search(r"(19|20)\d{2}", date_str)
    if m:
        try:
            return int(m.group(0))
        except:
            return None
    return None

# build business_id -> description mapping
biz_map = {}
for b in businesses:
    bid = b.get('business_id')
    desc = b.get('description') or ''
    name = b.get('name') or ''
    biz_map[bid] = {'description': desc, 'name': name}

# category extraction heuristic
lead_phrases = [r"offers.*? in ", r"providing .*? in ", r"in the category of ", r"categories? of ", r"including ", r"offers a diverse range.*? in ", r"falls into ", r"offers a range of services in "]

def extract_categories_from_description(desc):
    if not desc:
        return []
    parts = [p.strip() for p in re.split(r'[\.\n]', desc) if p.strip()]
    last = parts[-1] if parts else desc
    s = last
    for lp in lead_phrases:
        m = re.search(lp, desc, flags=re.IGNORECASE)
        if m:
            s = desc[m.end():]
            s = s.split('.')[-1]
            break
    tokens = re.split(r',|\band\b', s)
    cats = []
    for t in tokens:
        tt = t.strip()
        tt = re.sub(r'^(a |the |this |offers |establishment |business |facility |provides |providing |offering |offering a |a range of services in |offers a range of services in )', '', tt, flags=re.IGNORECASE)
        if re.search(r'\d', tt):
            continue
        if re.search(r'\b(Rd|St|Ave|Blvd|Dr|Ste|Court|Ct|Way|Ln|Pl|Suite|PO Box)\b', tt, flags=re.IGNORECASE):
            continue
        tt = tt.strip(' .;:')
        if not tt:
            continue
        if len(tt) < 2:
            continue
        if re.search(r'[A-Za-z]', tt):
            cats.append(tt)
    final = []
    for c in cats:
        parts = [p.strip() for p in re.split(r'/|–', c) if p.strip()]
        final.extend(parts)
    norm = []
    for c in final:
        cc = re.sub(r'\s+', ' ', c).strip()
        norm.append(cc)
    seen = set()
    out = []
    for c in norm:
        key = c.lower()
        if key not in seen:
            seen.add(key)
            out.append(c)
    return out

# build business categories mapping
biz_cats = {}
for bid, info in biz_map.items():
    desc = info.get('description','')
    cats = extract_categories_from_description(desc)
    if not cats and info.get('name'):
        name = info.get('name')
        tokens = re.split(r'[-:|,]', name)
        cand = []
        for t in tokens:
            t = t.strip()
            if len(t) > 1 and re.search(r'[A-Za-z]', t):
                cand.append(t)
        if cand:
            cats = cand
    biz_cats[bid] = cats

# iterate reviews, filter by user and year>=2016
counts = {}
for r in reviews:
    uid = r.get('user_id')
    if uid not in user_set:
        continue
    year = extract_year(r.get('date',''))
    if year is None or year < 2016:
        continue
    bref = r.get('business_ref')
    if not bref:
        continue
    bid = bref.replace('businessref_', 'businessid_')
    cats = biz_cats.get(bid, [])
    if not cats:
        continue
    for c in cats:
        key = c
        counts[key] = counts.get(key, 0) + 1

# get top 5
sorted_cats = sorted(counts.items(), key=lambda x: x[1], reverse=True)
top5 = sorted_cats[:5]
result = []
for cat, cnt in top5:
    result.append({'category': cat, 'review_count': cnt})

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_S0ONr6sEOdbxZHPmMDm4OoIC': ['review', 'tip', 'user'], 'var_call_dLpxQLRTCJFkOsBaE7AEhwEc': ['business', 'checkin'], 'var_call_I5QmavlzrVx07PR7BlFjiCzk': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'name': 'Candy Barrel', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'name': 'Luminosity', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'_id': '6859a000fe8b31cd7362e2b2', 'business_id': 'businessid_64', 'name': 'Nail Care Salon', 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.'}, {'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52', 'name': 'Architectural Antiques of Indianapolis', 'description': 'Located at 5000 W 96th St in Indianapolis, IN, this establishment offers a diverse selection of Antiques, Shopping, Home Services, and Lighting Fixtures & Equipment for all your home and decorative needs.'}, {'_id': '6859a000fe8b31cd7362e2b4', 'business_id': 'businessid_29', 'name': "Aster's Floral Shop", 'description': 'Located at 41 Haddon Ave in Collingswood, NJ, this versatile establishment offers a range of services including Wedding Planning, Flowers & Gifts, Event Planning & Services, Financial Services, Shopping, and Florists.'}, {'_id': '6859a000fe8b31cd7362e2b5', 'business_id': 'businessid_10', 'name': 'China Wok', 'description': "Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of 'Restaurants, Chinese'."}, {'_id': '6859a000fe8b31cd7362e2b6', 'business_id': 'businessid_61', 'name': 'Brandon Family Medical Care', 'description': 'Located at 1218 Millennium Pkwy in Brandon, FL, this facility provides essential services in the categories of Medical Centers, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2b7', 'business_id': 'businessid_54', 'name': '7-Eleven', 'description': 'Located at 13151 Race Track Rd in Tampa, FL, this establishment offers a variety of services including Service Stations, Coffee & Tea, Gas Stations, Automotive, Gas Stations, Food, and Convenience Stores.'}, {'_id': '6859a000fe8b31cd7362e2b8', 'business_id': 'businessid_8', 'name': 'Uber', 'description': 'This Philadelphia, PA location offers a range of services including Hotels & Travel, Taxis, Transportation, Local Services, and Automotive to meet all your travel and transportation needs.'}, {'_id': '6859a000fe8b31cd7362e2b9', 'business_id': 'businessid_59', 'name': 'Chestnut St. Cafe', 'description': 'Located at 4403 Chestnut St in Philadelphia, PA, this vibrant spot offers a delightful mix of Food, Bubble Tea, Restaurants, Sandwiches, Vietnamese, Cafes, perfect for a casual meal or a refreshing drink.'}, {'_id': '6859a000fe8b31cd7362e2ba', 'business_id': 'businessid_91', 'name': 'Cafe Porche and snowbar', 'description': 'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning, Comfort Food, Cafes, Restaurants, to Event Planning & Services, making it a perfect spot for any occasion.'}, {'_id': '6859a000fe8b31cd7362e2bb', 'business_id': 'businessid_83', 'name': 'Eyeglass World', 'description': 'Located at 13002 Seminole Blvd, Ste 10-11 in Largo, FL, this business specializes in Optometrists, Health & Medical, Eyewear & Opticians, Ophthalmologists, Doctors, Shopping, offering a range of eye care services and products.'}, {'_id': '6859a000fe8b31cd7362e2bc', 'business_id': 'businessid_93', 'name': "Callahan's Corner", 'description': 'Located at 914 Edwardsville Rd in Troy, IL, this vibrant spot offers a diverse menu featuring American (New) cuisine, along with a lively atmosphere perfect for nightlife, bars, restaurants, and sports bars.'}, {'_id': '6859a000fe8b31cd7362e2bd', 'business_id': 'businessid_1', 'name': 'Spa Guy Dave', 'description': 'Located in Pennsauken, NJ, this business specializes in Home Services, Pool & Hot Tub Service, providing expert care for all your residential maintenance needs.'}, {'_id': '6859a000fe8b31cd7362e2be', 'business_id': 'businessid_24', 'name': 'FroYo Frozen Yogurt', 'description': 'Located at 4663 Maryland Ave in Saint Louis, MO, this delightful spot offers a tempting selection of treats in the categories of Food, Ice Cream & Frozen Yogurt.'}], 'var_call_dxRe7fxS97xJlgHxJEdlzCO5': [{'user_id': 'userid_286', 'name': 'Todd', 'yelping_since': '15 Jan 2009, 16:40'}, {'user_id': 'userid_1331', 'name': 'Patt', 'yelping_since': '13 Jul 2010, 15:42'}, {'user_id': 'userid_1880', 'name': 'Norma', 'yelping_since': '2010-09-07 23:24:36'}, {'user_id': 'userid_271', 'name': 'Antony', 'yelping_since': 'October 23, 2011 at 07:47 PM'}, {'user_id': 'userid_534', 'name': 'Mandy', 'yelping_since': '2011-08-30 13:46:26'}, {'user_id': 'userid_1997', 'name': 'Francesca', 'yelping_since': '2009-12-02 18:54:31'}, {'user_id': 'userid_1386', 'name': 'Michael', 'yelping_since': '2009-04-15 12:46:06'}, {'user_id': 'userid_237', 'name': 'Jason', 'yelping_since': 'October 04, 2009 at 05:59 PM'}, {'user_id': 'userid_596', 'name': 'Andy', 'yelping_since': '20 Apr 2008, 16:55'}, {'user_id': 'userid_948', 'name': 'Lisa', 'yelping_since': '2007-07-28 22:22:09'}, {'user_id': 'userid_42', 'name': 'Jen', 'yelping_since': 'January 14, 2009 at 06:31 PM'}, {'user_id': 'userid_604', 'name': 'Eric', 'yelping_since': 'October 10, 2009 at 01:37 AM'}, {'user_id': 'userid_1291', 'name': 'Katrina', 'yelping_since': '17 Nov 2008, 02:26'}, {'user_id': 'userid_995', 'name': 'Aimee', 'yelping_since': '2010-04-29 14:32:53'}, {'user_id': 'userid_1630', 'name': 'Steven', 'yelping_since': '26 Sep 2009, 02:31'}, {'user_id': 'userid_1857', 'name': 'Brooke', 'yelping_since': 'May 03, 2009 at 08:19 PM'}, {'user_id': 'userid_1936', 'name': 'Ryan', 'yelping_since': 'July 21, 2008 at 06:04 PM'}, {'user_id': 'userid_288', 'name': 'Seth', 'yelping_since': 'August 13, 2009 at 01:09 PM'}, {'user_id': 'userid_1956', 'name': 'Bodie', 'yelping_since': '2011-08-19 18:09:41'}, {'user_id': 'userid_529', 'name': 'Irene', 'yelping_since': '2009-12-14 01:40:43'}], 'var_call_5pIPhcX1lanZOtfPneqbWBAX': [], 'var_call_YS8M0IXsz6wEKAKHB31nsIGb': [{'user_id': 'userid_1231'}, {'user_id': 'userid_343'}, {'user_id': 'userid_746'}, {'user_id': 'userid_505'}, {'user_id': 'userid_898'}, {'user_id': 'userid_144'}, {'user_id': 'userid_1927'}, {'user_id': 'userid_1109'}, {'user_id': 'userid_1950'}, {'user_id': 'userid_1316'}, {'user_id': 'userid_805'}, {'user_id': 'userid_1182'}, {'user_id': 'userid_431'}, {'user_id': 'userid_1287'}, {'user_id': 'userid_151'}, {'user_id': 'userid_1274'}, {'user_id': 'userid_1158'}, {'user_id': 'userid_643'}, {'user_id': 'userid_1558'}, {'user_id': 'userid_1542'}, {'user_id': 'userid_508'}, {'user_id': 'userid_435'}, {'user_id': 'userid_1398'}, {'user_id': 'userid_958'}, {'user_id': 'userid_68'}, {'user_id': 'userid_145'}, {'user_id': 'userid_518'}, {'user_id': 'userid_1879'}, {'user_id': 'userid_1981'}, {'user_id': 'userid_64'}, {'user_id': 'userid_211'}, {'user_id': 'userid_308'}, {'user_id': 'userid_1444'}, {'user_id': 'userid_1179'}, {'user_id': 'userid_677'}, {'user_id': 'userid_537'}, {'user_id': 'userid_208'}, {'user_id': 'userid_1397'}, {'user_id': 'userid_324'}, {'user_id': 'userid_795'}, {'user_id': 'userid_863'}, {'user_id': 'userid_100'}, {'user_id': 'userid_1333'}, {'user_id': 'userid_1636'}, {'user_id': 'userid_38'}, {'user_id': 'userid_1850'}, {'user_id': 'userid_401'}, {'user_id': 'userid_711'}, {'user_id': 'userid_729'}, {'user_id': 'userid_1505'}, {'user_id': 'userid_374'}, {'user_id': 'userid_1315'}, {'user_id': 'userid_597'}, {'user_id': 'userid_386'}, {'user_id': 'userid_1978'}, {'user_id': 'userid_862'}, {'user_id': 'userid_1068'}, {'user_id': 'userid_1708'}, {'user_id': 'userid_522'}, {'user_id': 'userid_1246'}, {'user_id': 'userid_339'}, {'user_id': 'userid_1786'}, {'user_id': 'userid_1661'}, {'user_id': 'userid_152'}, {'user_id': 'userid_1376'}, {'user_id': 'userid_851'}, {'user_id': 'userid_1940'}, {'user_id': 'userid_216'}, {'user_id': 'userid_39'}, {'user_id': 'userid_850'}, {'user_id': 'userid_1419'}, {'user_id': 'userid_425'}, {'user_id': 'userid_582'}, {'user_id': 'userid_333'}, {'user_id': 'userid_1288'}, {'user_id': 'userid_252'}, {'user_id': 'userid_676'}, {'user_id': 'userid_361'}, {'user_id': 'userid_1675'}, {'user_id': 'userid_1490'}, {'user_id': 'userid_123'}, {'user_id': 'userid_227'}, {'user_id': 'userid_510'}, {'user_id': 'userid_577'}, {'user_id': 'userid_242'}, {'user_id': 'userid_771'}, {'user_id': 'userid_1350'}, {'user_id': 'userid_1077'}, {'user_id': 'userid_1013'}, {'user_id': 'userid_1030'}, {'user_id': 'userid_1902'}, {'user_id': 'userid_367'}, {'user_id': 'userid_257'}, {'user_id': 'userid_598'}, {'user_id': 'userid_847'}, {'user_id': 'userid_1343'}, {'user_id': 'userid_792'}, {'user_id': 'userid_673'}, {'user_id': 'userid_243'}, {'user_id': 'userid_1072'}, {'user_id': 'userid_369'}, {'user_id': 'userid_622'}, {'user_id': 'userid_1758'}, {'user_id': 'userid_1856'}, {'user_id': 'userid_384'}, {'user_id': 'userid_1533'}, {'user_id': 'userid_1736'}, {'user_id': 'userid_1161'}, {'user_id': 'userid_359'}, {'user_id': 'userid_318'}, {'user_id': 'userid_1871'}, {'user_id': 'userid_655'}, {'user_id': 'userid_108'}, {'user_id': 'userid_131'}, {'user_id': 'userid_1760'}, {'user_id': 'userid_935'}, {'user_id': 'userid_1139'}, {'user_id': 'userid_210'}, {'user_id': 'userid_70'}, {'user_id': 'userid_25'}, {'user_id': 'userid_1101'}, {'user_id': 'userid_97'}, {'user_id': 'userid_1624'}, {'user_id': 'userid_1739'}, {'user_id': 'userid_942'}, {'user_id': 'userid_945'}, {'user_id': 'userid_842'}, {'user_id': 'userid_986'}, {'user_id': 'userid_1717'}, {'user_id': 'userid_1351'}, {'user_id': 'userid_406'}, {'user_id': 'userid_230'}, {'user_id': 'userid_914'}, {'user_id': 'userid_593'}, {'user_id': 'userid_1083'}, {'user_id': 'userid_742'}, {'user_id': 'userid_1938'}, {'user_id': 'userid_356'}, {'user_id': 'userid_876'}, {'user_id': 'userid_1431'}, {'user_id': 'userid_424'}, {'user_id': 'userid_686'}, {'user_id': 'userid_527'}, {'user_id': 'userid_641'}, {'user_id': 'userid_1346'}, {'user_id': 'userid_1766'}, {'user_id': 'userid_207'}, {'user_id': 'userid_1070'}, {'user_id': 'userid_989'}, {'user_id': 'userid_927'}, {'user_id': 'userid_244'}, {'user_id': 'userid_1816'}, {'user_id': 'userid_1756'}, {'user_id': 'userid_393'}, {'user_id': 'userid_1409'}, {'user_id': 'userid_197'}, {'user_id': 'userid_1178'}, {'user_id': 'userid_526'}, {'user_id': 'userid_90'}, {'user_id': 'userid_661'}, {'user_id': 'userid_238'}, {'user_id': 'userid_1897'}, {'user_id': 'userid_241'}, {'user_id': 'userid_1262'}, {'user_id': 'userid_1727'}, {'user_id': 'userid_1105'}, {'user_id': 'userid_744'}, {'user_id': 'userid_1263'}], 'var_call_fzkfmJ9i9wLBCNcqqIyR2U5e': 'file_storage/call_fzkfmJ9i9wLBCNcqqIyR2U5e.json', 'var_call_gcYSEQo3o3olHVVUQtU02ohC': 'file_storage/call_gcYSEQo3o3olHVVUQtU02ohC.json'}

exec(code, env_args)
