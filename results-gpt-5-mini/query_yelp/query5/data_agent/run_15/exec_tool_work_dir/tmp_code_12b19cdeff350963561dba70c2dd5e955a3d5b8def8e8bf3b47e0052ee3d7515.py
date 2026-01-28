code = """import json, re
with open(var_call_cKAUvs32jTulvBxlVKm3UG9A, 'r') as f:
    businesses = json.load(f)

US_STATES = set(['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY','DC'])

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
            sval = re.sub(r"[^a-z0-9]", "", sval)
            if sval in ("no", "none", "false", "0"):
                return False
            return True
    return False

rows = []
for b in businesses:
    attrs = b.get('attributes')
    if not attrs:
        continue
    # find wifi key
    found_k = None
    for k in attrs.keys():
        if k and ('wifi' in str(k).lower() or 'wi-fi' in str(k).lower()):
            found_k = k
            break
    if not found_k:
        continue
    desc = b.get('description') or ''
    # find all two-letter uppercase tokens and all occurrences after commas
    cand_states = re.findall(r'\b([A-Z]{2})\b', desc)
    cand_after_comma = re.findall(r',\s*([^,]+)', desc)
    rows.append({'business_id': b.get('business_id'), 'name': b.get('name'), 'wifi_key': found_k, 'wifi_val': attrs.get(found_k), 'description': desc, 'cand_states': cand_states, 'cand_after_comma': cand_after_comma[:5]})

print('__RESULT__:')
print(json.dumps(rows))"""

env_args = {'var_call_cKAUvs32jTulvBxlVKm3UG9A': 'file_storage/call_cKAUvs32jTulvBxlVKm3UG9A.json', 'var_call_HqfVjLmSpm2LUwUZsWZG8Qg2': 'file_storage/call_HqfVjLmSpm2LUwUZsWZG8Qg2.json', 'var_call_YQstDHrjxqbZGF1nEQksbPZw': {'error': 'No results'}, 'var_call_CV7owKU3aXGXXwrUax5RU3wj': {'total_businesses': 91, 'with_attributes': 91, 'wifi_key_count': 35, 'samples': [{'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'wifi_key': 'WiFi', 'wifi_val': "u'no'", 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_92', 'name': 'Luminosity', 'wifi_key': 'WiFi', 'wifi_val': "u'no'", 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'business_id': 'businessid_64', 'name': 'Nail Care Salon', 'wifi_key': 'WiFi', 'wifi_val': "u'free'", 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.'}, {'business_id': 'businessid_54', 'name': '7-Eleven', 'wifi_key': 'WiFi', 'wifi_val': "u'free'", 'description': 'Located at 13151 Race Track Rd in Tampa, FL, this establishment offers a variety of services including Service Stations, Coffee & Tea, Gas Stations, Automotive, Gas Stations, Food, and Convenience Stores.'}, {'business_id': 'businessid_91', 'name': 'Cafe Porche and snowbar', 'wifi_key': 'WiFi', 'wifi_val': "u'free'", 'description': 'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning, Comfort Food, Cafes, Restaurants, to Event Planning & Services, making it a perfect spot for any occasion.'}, {'business_id': 'businessid_93', 'name': "Callahan's Corner", 'wifi_key': 'WiFi', 'wifi_val': "u'free'", 'description': 'Located at 914 Edwardsville Rd in Troy, IL, this vibrant spot offers a diverse menu featuring American (New) cuisine, along with a lively atmosphere perfect for nightlife, bars, restaurants, and sports bars.'}, {'business_id': 'businessid_24', 'name': 'FroYo Frozen Yogurt', 'wifi_key': 'WiFi', 'wifi_val': "u'no'", 'description': 'Located at 4663 Maryland Ave in Saint Louis, MO, this delightful spot offers a tempting selection of treats in the categories of Food, Ice Cream & Frozen Yogurt.'}, {'business_id': 'businessid_26', 'name': "McDonald's", 'wifi_key': 'WiFi', 'wifi_val': "u'free'", 'description': 'Located at 7003 Seminole Blvd in Seminole, FL, this establishment specializes in a variety of offerings, including Fast Food, Restaurants, Coffee & Tea, Food, and Burgers, making it a convenient stop for a quick meal or a refreshing beverage.'}, {'business_id': 'businessid_89', 'name': 'King of Prussia Laundromat', 'wifi_key': 'WiFi', 'wifi_val': "u'free'", 'description': 'Located at 540 Shoemaker Rd in King of Prussia, PA, this establishment offers a range of services including Dry Cleaning & Laundry, Laundromat, Local Services, and Laundry Services.'}, {'business_id': 'businessid_32', 'name': 'The Recovery Room Bar & Grill', 'wifi_key': 'WiFi', 'wifi_val': "u'no'", 'description': 'Located at 1715 Jefferson Hwy in New Orleans, LA, this lively establishment offers a great atmosphere for enjoying Bars, Dive Bars, Burgers, Nightlife, and Restaurants.'}, {'business_id': 'businessid_97', 'name': 'Executive Auto Body', 'wifi_key': 'WiFi', 'wifi_val': "u'free'", 'description': 'Located at 560 Cottman Ave in Cheltenham, PA, this establishment specializes in Body Shops, Automotive services to meet all your vehicle repair needs.'}, {'business_id': 'businessid_27', 'name': 'Egg Roll King Two', 'wifi_key': 'WiFi', 'wifi_val': "u'no'", 'description': 'Located at 2253 Oddie Blvd in Sparks, NV, this establishment offers a delightful dining experience featuring a diverse menu in the category of Restaurants, Chinese.'}, {'business_id': 'businessid_67', 'name': "Hanoi's Pho", 'wifi_key': 'WiFi', 'wifi_val': "u'free'", 'description': 'Located at 1501 W Chester Pike in Havertown, PA, this eatery specializes in Vietnamese, Soup, Restaurants, Noodles, offering a delightful array of flavorful dishes.'}, {'business_id': 'businessid_7', 'name': 'Eagle Luxe Reel Theatre', 'wifi_key': 'WiFi', 'wifi_val': "u'no'", 'description': 'Located at 170 E Eagles Gate Dr in Eagle, ID, this establishment offers a vibrant experience in the realm of Cinema, Arts & Entertainment.'}, {'business_id': 'businessid_51', 'name': "Gram's Place", 'wifi_key': 'WiFi', 'wifi_val': "u'free'", 'description': 'Situated at 3109 N Ola Ave in Tampa, FL, this establishment offers a range of services in the hospitality sector, including Hotels & Travel, Hostels, Bed & Breakfast, Hotels, and Event Planning & Services.'}, {'business_id': 'businessid_5', 'name': 'Simply Done Cafe', 'wifi_key': 'WiFi', 'wifi_val': "'no'", 'description': 'Located at 10728 124 Street in Edmonton, AB, this inviting spot offers a delightful menu perfect for anyone looking to enjoy a satisfying meal, specializing in Breakfast & Brunch, Restaurants.'}, {'business_id': 'businessid_6', 'name': 'The Jungle', 'wifi_key': 'WiFi', 'wifi_val': "'free'", 'description': 'Located at 246 W 1st St in Reno, NV, this vibrant destination offers a delightful mix of Restaurants, Breakfast & Brunch, Bars, Wine Bars, Coffee & Tea, Food, Cafes, Sandwiches, and Nightlife, making it an ideal spot for any meal or occasion.'}, {'business_id': 'businessid_87', 'name': 'Jordans Fish and Chicken', 'wifi_key': 'WiFi', 'wifi_val': "u'no'", 'description': 'Located at 6416 W Washington St in Indianapolis, IN, this establishment offers a delightful menu featuring Restaurants, Chicken Wings, Fish & Chips, and American (Traditional) cuisine.'}, {'business_id': 'businessid_55', 'name': 'Uptown Snoballs and Ice Cream', 'wifi_key': 'WiFi', 'wifi_val': "u'free'", 'description': 'Located at 1003 4th St N in St. Petersburg, FL, this delightful spot offers a variety of treats including Ice Cream & Frozen Yogurt, Shaved Ice, Food, and Desserts.'}, {'business_id': 'businessid_96', 'name': 'Farmhaus Restaurant', 'wifi_key': 'WiFi', 'wifi_val': "u'no'", 'description': 'Located at 3257 Ivanhoe Ave in Saint Louis, MO, this establishment offers a vibrant atmosphere perfect for enjoying a diverse selection of experiences, including Wine Bars, American (New), Cocktail Bars, Restaurants, American (Traditional), Nightlife, and Bars.'}]}, 'var_call_K0IFZc91jCDLAWFBONzRvYdR': {'error': 'No WiFi businesses with US state found.'}, 'var_call_4ILenEOABk9kvQEcyy5Q0Bwr': {'error': 'No WiFi businesses with US states found.'}}

exec(code, env_args)
