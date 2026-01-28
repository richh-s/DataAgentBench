code = """import json
reviews = var_call_r5UYUPfPbLUYW4A8NeluTRws
bus_a = var_call_vxwFcdb32uPnzeuXZqpwSly4
bus_b = var_call_2GSaXvJXfXhEKP4ZP6m641By
bus_c = var_call_LXqxjG1N9PGhTymVx2KErtGW
bus_d = var_call_Kb90ZYuUSJrEMpq1jTGKchFc
all_list = []
all_list.extend(bus_a)
all_list.extend(bus_b)
all_list.extend(bus_c)
all_list.extend(bus_d)
biz_map = {}
for b in all_list:
    bid = b.get('business_id')
    if bid:
        biz_map[bid] = b

def extract(desc):
    if not desc or not isinstance(desc, str):
        return []
    s = desc
    keys = ["including", "includes", "in the categories of", "in the category of", "services in", "offers a range of services including", "offers a range of services in", "offers services in", "offers a range of services", "offers"]
    tail = None
    lower = s.lower()
    for k in keys:
        idx = lower.find(k)
        if idx != -1:
            tail = s[idx + len(k):]
            break
    if tail is None:
        # fallback: take substring after second comma if exists
        parts = s.split(',')
        if len(parts) > 2:
            tail = ','.join(parts[2:])
        else:
            tail = s
    # replace periods with commas to help split
    tail = tail.replace('.', ',')
    parts = [p.strip() for p in tail.split(',') if p.strip()]
    out = []
    for p in parts:
        if any(ch.isdigit() for ch in p):
            continue
        if 'located' in p.lower():
            continue
        # remove leading words like 'this facility offers' if present
        lowp = p.lower()
        for phrase in ['this facility offers', 'this establishment offers', 'this facility', 'this establishment', 'this shop offers']:
            if lowp.startswith(phrase):
                p = p[len(phrase):].strip()
                break
        if len(p) >= 2:
            out.append(p)
    # further split on ampersand and slash and the word ' and '
    final = []
    for item in out:
        temp = item.replace('/', ',')
        temp = temp.replace('&', ',')
        parts2 = [t.strip() for t in temp.split(',') if t.strip()]
        for t in parts2:
            if t not in final:
                final.append(t)
    return final

from collections import defaultdict
counts = defaultdict(int)
for r in reviews:
    bref = r.get('business_ref')
    if not bref:
        continue
    bid = bref.replace('businessref_', 'businessid_')
    b = biz_map.get(bid)
    if not b:
        continue
    cats = extract(b.get('description', ''))
    for c in cats:
        counts[c] += 1
items = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
top5 = items[:5]
output = [{'category': c, 'review_count': n} for c,n in top5]
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_U0HmSTFnVQBog50Q5X3uurvL': [{'user_id': 'userid_746'}, {'user_id': 'userid_1109'}, {'user_id': 'userid_1950'}, {'user_id': 'userid_1316'}, {'user_id': 'userid_1182'}, {'user_id': 'userid_151'}, {'user_id': 'userid_1158'}, {'user_id': 'userid_508'}, {'user_id': 'userid_435'}, {'user_id': 'userid_958'}, {'user_id': 'userid_1879'}, {'user_id': 'userid_308'}, {'user_id': 'userid_1179'}, {'user_id': 'userid_324'}, {'user_id': 'userid_863'}, {'user_id': 'userid_100'}, {'user_id': 'userid_1333'}, {'user_id': 'userid_1636'}, {'user_id': 'userid_1850'}, {'user_id': 'userid_711'}, {'user_id': 'userid_729'}, {'user_id': 'userid_1505'}, {'user_id': 'userid_1315'}, {'user_id': 'userid_1708'}, {'user_id': 'userid_1661'}, {'user_id': 'userid_850'}, {'user_id': 'userid_1675'}, {'user_id': 'userid_227'}, {'user_id': 'userid_577'}, {'user_id': 'userid_257'}, {'user_id': 'userid_598'}, {'user_id': 'userid_847'}, {'user_id': 'userid_673'}, {'user_id': 'userid_1856'}, {'user_id': 'userid_384'}, {'user_id': 'userid_935'}, {'user_id': 'userid_210'}, {'user_id': 'userid_1101'}, {'user_id': 'userid_945'}, {'user_id': 'userid_842'}, {'user_id': 'userid_1351'}, {'user_id': 'userid_230'}, {'user_id': 'userid_593'}, {'user_id': 'userid_1431'}, {'user_id': 'userid_686'}, {'user_id': 'userid_527'}, {'user_id': 'userid_244'}, {'user_id': 'userid_393'}, {'user_id': 'userid_1178'}, {'user_id': 'userid_526'}, {'user_id': 'userid_90'}, {'user_id': 'userid_238'}, {'user_id': 'userid_1105'}], 'var_call_fE0PfI7WooPL23b7izwchMWH': ['checkin', 'business'], 'var_call_vxwFcdb32uPnzeuXZqpwSly4': [{'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'name': 'Impact Guns', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'attributes': 'None', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'name': 'J&Q Nails', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_r5UYUPfPbLUYW4A8NeluTRws': [{'review_id': 'reviewid_318', 'user_id': 'userid_1101', 'business_ref': 'businessref_74', 'date': '2021-07-16 17:24:00'}, {'review_id': 'reviewid_1049', 'user_id': 'userid_1105', 'business_ref': 'businessref_57', 'date': 'September 04, 2017 at 08:57 PM'}, {'review_id': 'reviewid_454', 'user_id': 'userid_863', 'business_ref': 'businessref_96', 'date': 'August 06, 2016 at 02:19 AM'}, {'review_id': 'reviewid_1065', 'user_id': 'userid_308', 'business_ref': 'businessref_45', 'date': 'August 10, 2016 at 04:36 AM'}, {'review_id': 'reviewid_704', 'user_id': 'userid_729', 'business_ref': 'businessref_74', 'date': 'April 17, 2016 at 12:00 AM'}, {'review_id': 'reviewid_84', 'user_id': 'userid_935', 'business_ref': 'businessref_53', 'date': '25 Nov 2016, 20:04'}, {'review_id': 'reviewid_1110', 'user_id': 'userid_1856', 'business_ref': 'businessref_41', 'date': 'December 12, 2017 at 02:27 AM'}, {'review_id': 'reviewid_655', 'user_id': 'userid_435', 'business_ref': 'businessref_96', 'date': '2017-01-06 11:15:06'}, {'review_id': 'reviewid_1239', 'user_id': 'userid_1178', 'business_ref': 'businessref_10', 'date': '2021-11-28 23:56:00'}, {'review_id': 'reviewid_515', 'user_id': 'userid_1109', 'business_ref': 'businessref_66', 'date': 'November 10, 2021 at 06:40 AM'}, {'review_id': 'reviewid_44', 'user_id': 'userid_593', 'business_ref': 'businessref_31', 'date': '24 Jan 2017, 19:28'}, {'review_id': 'reviewid_65', 'user_id': 'userid_1182', 'business_ref': 'businessref_92', 'date': '2019-11-14 17:06:00'}, {'review_id': 'reviewid_1216', 'user_id': 'userid_230', 'business_ref': 'businessref_26', 'date': '2018-07-23 06:45:43'}, {'review_id': 'reviewid_781', 'user_id': 'userid_244', 'business_ref': 'businessref_98', 'date': '2017-11-17 16:06:00'}, {'review_id': 'reviewid_334', 'user_id': 'userid_1316', 'business_ref': 'businessref_45', 'date': 'February 06, 2018 at 07:29 PM'}, {'review_id': 'reviewid_124', 'user_id': 'userid_324', 'business_ref': 'businessref_45', 'date': 'October 28, 2016 at 03:54 PM'}, {'review_id': 'reviewid_957', 'user_id': 'userid_1850', 'business_ref': 'businessref_36', 'date': '2018-05-21 17:51:00'}, {'review_id': 'reviewid_1174', 'user_id': 'userid_686', 'business_ref': 'businessref_14', 'date': 'May 04, 2017 at 11:25 PM'}, {'review_id': 'reviewid_1502', 'user_id': 'userid_1950', 'business_ref': 'businessref_86', 'date': '2019-04-14 23:08:41'}, {'review_id': 'reviewid_919', 'user_id': 'userid_945', 'business_ref': 'businessref_57', 'date': 'October 30, 2018 at 01:06 PM'}, {'review_id': 'reviewid_926', 'user_id': 'userid_1179', 'business_ref': 'businessref_13', 'date': 'August 22, 2021 at 12:11 AM'}, {'review_id': 'reviewid_1457', 'user_id': 'userid_1879', 'business_ref': 'businessref_68', 'date': 'October 14, 2018 at 04:06 PM'}, {'review_id': 'reviewid_1576', 'user_id': 'userid_850', 'business_ref': 'businessref_36', 'date': '2016-12-02 00:06:00'}, {'review_id': 'reviewid_1677', 'user_id': 'userid_958', 'business_ref': 'businessref_60', 'date': '2017-03-24 23:59:00'}, {'review_id': 'reviewid_160', 'user_id': 'userid_1661', 'business_ref': 'businessref_20', 'date': '27 May 2017, 00:50'}, {'review_id': 'reviewid_1207', 'user_id': 'userid_210', 'business_ref': 'businessref_15', 'date': 'June 20, 2018 at 02:12 PM'}, {'review_id': 'reviewid_1635', 'user_id': 'userid_151', 'business_ref': 'businessref_62', 'date': '2018-04-01 10:52:37'}, {'review_id': 'reviewid_1966', 'user_id': 'userid_100', 'business_ref': 'businessref_33', 'date': 'August 18, 2016 at 11:57 AM'}, {'review_id': 'reviewid_1791', 'user_id': 'userid_598', 'business_ref': 'businessref_37', 'date': '2016-07-24 20:27:00'}, {'review_id': 'reviewid_1986', 'user_id': 'userid_746', 'business_ref': 'businessref_92', 'date': '30 Dec 2018, 18:49'}, {'review_id': 'reviewid_1137', 'user_id': 'userid_1675', 'business_ref': 'businessref_66', 'date': 'June 21, 2020 at 07:59 PM'}, {'review_id': 'reviewid_1555', 'user_id': 'userid_1505', 'business_ref': 'businessref_33', 'date': 'August 30, 2019 at 06:15 PM'}, {'review_id': 'reviewid_1408', 'user_id': 'userid_842', 'business_ref': 'businessref_6', 'date': '30 Jun 2017, 04:44'}, {'review_id': 'reviewid_1388', 'user_id': 'userid_257', 'business_ref': 'businessref_12', 'date': 'October 26, 2017 at 11:10 PM'}, {'review_id': 'reviewid_62', 'user_id': 'userid_1333', 'business_ref': 'businessref_79', 'date': '30 Oct 2017, 01:27'}, {'review_id': 'reviewid_280', 'user_id': 'userid_711', 'business_ref': 'businessref_60', 'date': '2019-05-29 19:46:00'}], 'var_call_p5ZlJ3hvGMFixkwM6Q25bssC': ['businessid_10', 'businessid_12', 'businessid_13', 'businessid_14', 'businessid_15', 'businessid_20', 'businessid_26', 'businessid_31', 'businessid_33', 'businessid_36', 'businessid_37', 'businessid_41', 'businessid_45', 'businessid_53', 'businessid_57', 'businessid_6', 'businessid_60', 'businessid_62', 'businessid_66', 'businessid_68', 'businessid_74', 'businessid_79', 'businessid_86', 'businessid_92', 'businessid_96', 'businessid_98'], 'var_call_2GSaXvJXfXhEKP4ZP6m641By': [{'business_id': 'businessid_33', 'name': 'J&Q Nails', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'business_id': 'businessid_10', 'name': 'China Wok', 'description': "Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of 'Restaurants, Chinese'."}, {'business_id': 'businessid_26', 'name': "McDonald's", 'description': 'Located at 7003 Seminole Blvd in Seminole, FL, this establishment specializes in a variety of offerings, including Fast Food, Restaurants, Coffee & Tea, Food, and Burgers, making it a convenient stop for a quick meal or a refreshing beverage.'}, {'business_id': 'businessid_14', 'name': 'Ross Dress for Less', 'description': "Located at 7055 Marketplace Dr in Goleta, CA, this store offers a diverse selection of products across various categories, including Women's Clothing, Fashion, Department Stores, Home Decor, Home & Garden, Shopping, Men's Clothing, and Discount Store."}, {'business_id': 'businessid_15', 'name': 'Take 5 Oil Change', 'description': 'Located at 3803 Gen Degaulle Dr in New Orleans, LA, this establishment specializes in Automotive, Oil Change Stations, providing efficient service for all your vehicle maintenance needs.'}], 'var_call_LXqxjG1N9PGhTymVx2KErtGW': [{'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_57', 'name': 'Big Boys Moving And Storage', 'description': 'Located at 13605 W Hillsborough Ave in Tampa, FL, this versatile establishment offers a range of services and dining options, including Movers, American (New), Landscape Architects, Food, Home Services, Self Storage, Local Services, Restaurants.'}, {'business_id': 'businessid_45', 'name': 'The Fresh Market', 'description': 'Located at 2900 4th St N in St. Petersburg, FL, this establishment offers a diverse range of products and services in the categories of Food, Grocery, Shopping.'}, {'business_id': 'businessid_6', 'name': 'The Jungle', 'description': 'Located at 246 W 1st St in Reno, NV, this vibrant destination offers a delightful mix of Restaurants, Breakfast & Brunch, Bars, Wine Bars, Coffee & Tea, Food, Cafes, Sandwiches, and Nightlife, making it an ideal spot for any meal or occasion.'}, {'business_id': 'businessid_53', 'name': 'Samwich', 'description': 'Located at 1040 N American St, Ste 1101 in Philadelphia, PA, this eatery offers a diverse menu featuring Salad, Sandwiches, Restaurants, and Burgers.'}], 'var_call_Kb90ZYuUSJrEMpq1jTGKchFc': [{'business_id': 'businessid_74', 'name': 'Candy Barrel', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}, {'business_id': 'businessid_92', 'name': 'Luminosity', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'business_id': 'businessid_68', 'name': 'Brow Art', 'description': 'Located at 593 Brandon Town Ctr in Brandon, FL, this establishment offers a range of services in the categories of Beauty & Spas, Hair Removal, and Eyebrow Services.'}, {'business_id': 'businessid_79', 'name': 'Pit Stop HQ', 'description': 'Located at 838-842 Christian St in Philadelphia, PA, this establishment offers a wide range of services including Pet Groomers, Pet Stores, Pet Training, Dog Walkers, Pet Services, Pets, and Pet Sitting.'}, {'business_id': 'businessid_66', 'name': 'Panda Express', 'description': 'Located at 3849 State St. Space I-58 in Santa Barbara, CA, this establishment offers a variety of quick and delicious options in the categories of Fast Food, Chinese, Restaurants.'}]}

exec(code, env_args)
