code = """import json, re
p = var_call_dTdMzELB4RK2SW9tG9NA5SiF
with open(p, 'r', encoding='utf-8') as f:
    data = json.load(f)
US_STATES = set(["AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"])

def offers_wifi(val):
    if val is None:
        return False
    s = str(val).lower()
    # remove non-alphanumeric
    s_clean = re.sub(r"[^a-z0-9]","", s)
    if s_clean in ('none','null','nan',''):
        return False
    if s_clean.startswith('no'):
        return False
    if any(k in s_clean for k in ('free','paid','yes','limited','signal','true')):
        return True
    # default: if not explicitly no, assume True
    return True

state_to_brefs = {}
for rec in data:
    attrs = rec.get('attributes')
    wifi_val = None
    if isinstance(attrs, dict):
        wifi_val = attrs.get('WiFi')
    else:
        wifi_val = None
    if not offers_wifi(wifi_val):
        continue
    desc = rec.get('description','') or ''
    # try to find 'in City, ST' pattern
    m = re.search(r'in [^,]+,\s*([A-Z]{2})\b', desc)
    if not m:
        # fallback: find last occurrence of comma + space + 2 uppercase letters
        m = re.search(r',\s*([A-Z]{2})\b', desc)
    if not m:
        continue
    state = m.group(1)
    if state not in US_STATES:
        continue
    bid = rec.get('business_id')
    if not bid:
        continue
    bref = bid.replace('businessid_','businessref_')
    state_to_brefs.setdefault(state, []).append(bref)

# compute top state
if not state_to_brefs:
    out = {"top_state": None, "count": 0, "business_refs": []}
else:
    counts = {s: len(set(brefs)) for s,brefs in state_to_brefs.items()}
    max_count = max(counts.values())
    top_states = [s for s,c in counts.items() if c==max_count]
    top_state = sorted(top_states)[0]
    brefs = sorted(list(set(state_to_brefs[top_state])))
    out = {"top_state": top_state, "count": max_count, "business_refs": brefs}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_ZESpVOW8rLKXaIlEar1igsb3': ['business', 'checkin'], 'var_call_BkALsWIa0Flqm7nUNmc0QjvX': ['review', 'tip', 'user'], 'var_call_M0ZKJDSbejRHfgoAjAgTh3bp': 'file_storage/call_M0ZKJDSbejRHfgoAjAgTh3bp.json', 'var_call_dTdMzELB4RK2SW9tG9NA5SiF': 'file_storage/call_dTdMzELB4RK2SW9tG9NA5SiF.json', 'var_call_MB1DQMPUGde9BdwSfFxfMM1s': {'business_refs': [], 'ref_to_state': {}}, 'var_call_wg9CJtLCyfqCnKQzlIYXGU94': [{'business_id': 'businessid_49', 'WiFi': "u'no'", 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_92', 'WiFi': "u'no'", 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'business_id': 'businessid_64', 'WiFi': "u'free'", 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.'}, {'business_id': 'businessid_54', 'WiFi': "u'free'", 'description': 'Located at 13151 Race Track Rd in Tampa, FL, this establishment offers a variety of services including Service Stations, Coffee & Tea, Gas Stations, Automotive, Gas Stations, Food, and Convenience Stores.'}, {'business_id': 'businessid_91', 'WiFi': "u'free'", 'description': 'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning, Comfort Food, Cafes, Restaurants, to Event Planning & Services, making it a perfect spot for any occasion.'}, {'business_id': 'businessid_93', 'WiFi': "u'free'", 'description': 'Located at 914 Edwardsville Rd in Troy, IL, this vibrant spot offers a diverse menu featuring American (New) cuisine, along with a lively atmosphere perfect for nightlife, bars, restaurants, and sports bars.'}, {'business_id': 'businessid_24', 'WiFi': "u'no'", 'description': 'Located at 4663 Maryland Ave in Saint Louis, MO, this delightful spot offers a tempting selection of treats in the categories of Food, Ice Cream & Frozen Yogurt.'}, {'business_id': 'businessid_26', 'WiFi': "u'free'", 'description': 'Located at 7003 Seminole Blvd in Seminole, FL, this establishment specializes in a variety of offerings, including Fast Food, Restaurants, Coffee & Tea, Food, and Burgers, making it a convenient stop for a quick meal or a refreshing beverage.'}, {'business_id': 'businessid_89', 'WiFi': "u'free'", 'description': 'Located at 540 Shoemaker Rd in King of Prussia, PA, this establishment offers a range of services including Dry Cleaning & Laundry, Laundromat, Local Services, and Laundry Services.'}, {'business_id': 'businessid_32', 'WiFi': "u'no'", 'description': 'Located at 1715 Jefferson Hwy in New Orleans, LA, this lively establishment offers a great atmosphere for enjoying Bars, Dive Bars, Burgers, Nightlife, and Restaurants.'}, {'business_id': 'businessid_97', 'WiFi': "u'free'", 'description': 'Located at 560 Cottman Ave in Cheltenham, PA, this establishment specializes in Body Shops, Automotive services to meet all your vehicle repair needs.'}, {'business_id': 'businessid_27', 'WiFi': "u'no'", 'description': 'Located at 2253 Oddie Blvd in Sparks, NV, this establishment offers a delightful dining experience featuring a diverse menu in the category of Restaurants, Chinese.'}, {'business_id': 'businessid_67', 'WiFi': "u'free'", 'description': 'Located at 1501 W Chester Pike in Havertown, PA, this eatery specializes in Vietnamese, Soup, Restaurants, Noodles, offering a delightful array of flavorful dishes.'}, {'business_id': 'businessid_7', 'WiFi': "u'no'", 'description': 'Located at 170 E Eagles Gate Dr in Eagle, ID, this establishment offers a vibrant experience in the realm of Cinema, Arts & Entertainment.'}, {'business_id': 'businessid_51', 'WiFi': "u'free'", 'description': 'Situated at 3109 N Ola Ave in Tampa, FL, this establishment offers a range of services in the hospitality sector, including Hotels & Travel, Hostels, Bed & Breakfast, Hotels, and Event Planning & Services.'}, {'business_id': 'businessid_5', 'WiFi': "'no'", 'description': 'Located at 10728 124 Street in Edmonton, AB, this inviting spot offers a delightful menu perfect for anyone looking to enjoy a satisfying meal, specializing in Breakfast & Brunch, Restaurants.'}, {'business_id': 'businessid_6', 'WiFi': "'free'", 'description': 'Located at 246 W 1st St in Reno, NV, this vibrant destination offers a delightful mix of Restaurants, Breakfast & Brunch, Bars, Wine Bars, Coffee & Tea, Food, Cafes, Sandwiches, and Nightlife, making it an ideal spot for any meal or occasion.'}, {'business_id': 'businessid_87', 'WiFi': "u'no'", 'description': 'Located at 6416 W Washington St in Indianapolis, IN, this establishment offers a delightful menu featuring Restaurants, Chicken Wings, Fish & Chips, and American (Traditional) cuisine.'}, {'business_id': 'businessid_55', 'WiFi': "u'free'", 'description': 'Located at 1003 4th St N in St. Petersburg, FL, this delightful spot offers a variety of treats including Ice Cream & Frozen Yogurt, Shaved Ice, Food, and Desserts.'}, {'business_id': 'businessid_96', 'WiFi': "u'no'", 'description': 'Located at 3257 Ivanhoe Ave in Saint Louis, MO, this establishment offers a vibrant atmosphere perfect for enjoying a diverse selection of experiences, including Wine Bars, American (New), Cocktail Bars, Restaurants, American (Traditional), Nightlife, and Bars.'}, {'business_id': 'businessid_77', 'WiFi': "u'free'", 'description': 'Located at 900 Packer Ave in Philadelphia, PA, this establishment offers a range of services in Hotels & Travel, Venues & Event Spaces, Hotels, and Event Planning & Services, making it an ideal choice for travelers and event organizers alike.'}, {'business_id': 'businessid_86', 'WiFi': "u'free'", 'description': 'Located at 705 East Passyunk Ave in Philadelphia, PA, this vibrant eatery offers a diverse menu featuring American (New), Restaurants, American (Traditional), Asian Fusion, Noodles, Dim Sum, Fast Food, Chinese, catering to a variety of tastes and preferences.'}, {'business_id': 'businessid_40', 'WiFi': "u'free'", 'description': 'Located at 4457 Main St in Philadelphia, PA, this establishment specializes in Venues & Event Spaces, Event Planning & Services, making it an ideal choice for hosting memorable gatherings and celebrations.'}, {'business_id': 'businessid_44', 'WiFi': "u'free'", 'description': 'Located at 2424 E York St in Philadelphia, PA, this vibrant establishment offers a delightful array of options, including Restaurants, Diners, Breakfast & Brunch, American (New), American (Traditional), Burgers, making it a perfect spot for any meal of the day.'}, {'business_id': 'businessid_43', 'WiFi': "'free'", 'description': 'Located at 11425 Allisonville Road in Fishers, IN, this vibrant eatery offers a delightful menu featuring Tex-Mex, Tacos, Restaurants, Breakfast & Brunch, Sandwiches, Mexican, Fast Food, perfect for satisfying any craving at any time of day.'}, {'business_id': 'businessid_9', 'WiFi': "u'no'", 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}, {'business_id': 'businessid_20', 'WiFi': "'free'", 'description': 'Located at 9040 State Road 54 in Trinity, FL, this establishment offers a diverse array of options, including Restaurants, American (New), Caterers, Fast Food, Chicken Shop, Event Planning & Services, and American (Traditional).'}, {'business_id': 'businessid_94', 'WiFi': "u'no'", 'description': 'Located at 4320 W 96th St in Indianapolis, IN, this inviting establishment offers a diverse menu that showcases a delightful fusion of flavors across categories such as Food, Specialty Food, Ethnic Food, Modern European, Restaurants.'}, {'business_id': 'businessid_85', 'WiFi': "'no'", 'description': 'Located at 3417 Spruce St in Philadelphia, PA, this delightful spot offers a tempting selection of treats, including Ice Cream & Frozen Yogurt, Food, Food Delivery Services, Bakeries, and Desserts.'}, {'business_id': 'businessid_25', 'WiFi': "u'free'", 'description': 'Located at 5608 W Fairview Ave in Boise, ID, this charming establishment offers a delightful array of options in the categories of Food, Restaurants, Sandwiches, Breakfast & Brunch, and Bakeries.'}]}

exec(code, env_args)
