code = """import json
reviews = var_call_qEAZPzCuBNoketItF6ikTU75
vars_list = [
 'var_call_60kMH9XgNWm43CjZ41ESHNIF','var_call_e1qKFXbc01Qbl7sjhUtJ9m0b','var_call_1kMSYNmDoqxMrOqmAIC36JMc',
 'var_call_Yy3Mdcxl3Y0f6P5hxpw7ndRF','var_call_cG48pCnpsdkNXWHcWugF8swy','var_call_krTbaeGlIcn9hjqxEKjwHIOo',
 'var_call_qQVCifbyYBz2NiwUDCVBKjss','var_call_NkzqA8jXjljlCaTnao7nX7Yb','var_call_TWNvZ5K9R7Yb3nW2enLPyPeW',
 'var_call_b8zNoMrlTbgs1VAfFhSPX8TO','var_call_1AmnuZL3ttmIGM12fK31K7ky','var_call_wQVij58hV207yeDJryC2Gt6E',
 'var_call_jnRiMwRY1cXB1ULcaFfeIB60','var_call_wGSigq1uXCWvxCB4wNrmy1kt','var_call_oETuCplRW2vxzANyePcCiRA6',
 'var_call_jP90brw0N1MMLnURMrjWMMDB','var_call_PtqnBiQlHFjXhFxFbqeNcnzb','var_call_wGB0f4jk7NIolo43ccMjZqJU',
 'var_call_3mGizG1CDVHwH6ih9HoadPD5','var_call_n5HtPZr98ZU1LqOLWazeA6IY','var_call_ggrgrlLTJ3ApDHT5gKSgBD88',
 'var_call_XCQQ8AYrUNzdXUtenB6xyr52','var_call_Q1lP6WBY8IF0hITwkAmgoqqz','var_call_lHGvVWJ4oI8hJjJIaPYUsKRL',
 'var_call_ukdQXFcgNklQWYB3F6DXxObY','var_call_bb2vdU4q2MVrAJs0GRRIHAXg'
]
# build mapping
biz_desc = {}
for name in vars_list:
    v = globals().get(name)
    if not v:
        continue
    if isinstance(v, list) and len(v)>0 and isinstance(v[0], dict):
        d = v[0]
        bid = d.get('business_id')
        desc = d.get('description','')
        if bid:
            biz_desc[bid] = desc
# simple extractor
def extract_categories(desc):
    if not desc:
        return []
    s = desc
    s_low = s.lower()
    markers = ['in the categories of','in the fields of','in the categories','in the fields','including','offers a range of products and services in','offers a diverse range of products and services in','offers a range of services in','offers a variety of options for customers, including','offers a range of services including']
    idx = -1; found = None
    for m in markers:
        i = s_low.rfind(m)
        if i > idx:
            idx = i; found = m
    tail = ''
    if idx != -1:
        tail = s[idx+len(found):]
    else:
        parts = s.split(',')
        if len(parts) > 1:
            tail = ','.join(parts[-3:])
        else:
            tail = s
    tail = tail.strip().strip('.')
    # replace common connectors with a comma
    for sep in [' and ', ' & ', '/', ';']:
        tail = tail.replace(sep, ',')
    items = [it.strip().strip('.\'"') for it in tail.split(',') if it.strip()]
    # filter out "located at" and long fragments
    cats = []
    for it in items:
        low = it.lower()
        if low.startswith('located at'):
            continue
        if len(it.split()) > 6:
            continue
        # remove leading words
        for lead in ['including','the','offers a range of','offering a range of','offering a','offers a','offering']:
            if it.lower().startswith(lead):
                it = it[len(lead):].strip()
        it = it.strip("'\" ")
        if it:
            cats.append(it)
    # dedupe preserve order
    out=[]; seen=set()
    for c in cats:
        if c not in seen:
            seen.add(c); out.append(c)
    return out

from collections import defaultdict
cat_counts = defaultdict(int)
for r in reviews:
    bre = r.get('business_ref')
    cnt = int(r.get('review_count') or 0)
    if not bre:
        continue
    bid = bre.replace('businessref_','businessid_')
    desc = biz_desc.get(bid,'')
    cats = extract_categories(desc)
    if not cats:
        # fallback: take last segment after last comma
        parts = desc.split(',')
        if parts:
            candidate = parts[-1].strip()
            if candidate:
                cats = [candidate]
    for c in cats:
        cat_counts[c] += cnt
sorted_cats = sorted(cat_counts.items(), key=lambda x: x[1], reverse=True)
result = [{'category': c, 'review_count': v} for c,v in sorted_cats[:5]]
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_4ocbBnMRWQc17OUgcsL18Eir': ['checkin', 'business'], 'var_call_jQi2xsOt90t0LPdCE7wwQ4e3': ['review', 'tip', 'user'], 'var_call_N093Wqdr4h5cu0qKEKD9PHbA': [{'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'name': 'Impact Guns', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'attributes': 'None', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'name': 'J&Q Nails', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_vaCwhyHYB1tdO8pjPp3Zw5jo': [{'user_id': 'userid_746', 'yelping_since': '2016-06-23 01:59:28'}, {'user_id': 'userid_1109', 'yelping_since': '2016-10-16 18:32:25'}, {'user_id': 'userid_1950', 'yelping_since': '2016-04-16 03:42:28'}, {'user_id': 'userid_1316', 'yelping_since': '2016-12-29 21:32:44'}, {'user_id': 'userid_1182', 'yelping_since': '2016-03-20 18:41:14'}, {'user_id': 'userid_151', 'yelping_since': '2016-11-07 18:40:10'}, {'user_id': 'userid_1158', 'yelping_since': '2016-01-31 16:25:04'}, {'user_id': 'userid_508', 'yelping_since': '2016-07-08 22:37:42'}, {'user_id': 'userid_435', 'yelping_since': '2016-10-31 09:46:54'}, {'user_id': 'userid_958', 'yelping_since': '2016-03-23 20:55:45'}, {'user_id': 'userid_1879', 'yelping_since': '2016-07-08 17:56:11'}, {'user_id': 'userid_308', 'yelping_since': '2016-07-02 23:48:36'}, {'user_id': 'userid_1179', 'yelping_since': '2016-12-18 17:31:52'}, {'user_id': 'userid_324', 'yelping_since': '2016-10-10 22:09:08'}, {'user_id': 'userid_863', 'yelping_since': '2016-01-16 00:45:41'}, {'user_id': 'userid_100', 'yelping_since': '2016-08-18 11:39:42'}, {'user_id': 'userid_1333', 'yelping_since': '2016-12-07 14:57:41'}, {'user_id': 'userid_1636', 'yelping_since': '2016-02-14 23:51:28'}, {'user_id': 'userid_1850', 'yelping_since': '2016-07-22 19:26:01'}, {'user_id': 'userid_711', 'yelping_since': '2016-07-07 22:59:48'}, {'user_id': 'userid_729', 'yelping_since': '2016-02-06 00:41:18'}, {'user_id': 'userid_1505', 'yelping_since': '2016-07-14 00:26:46'}, {'user_id': 'userid_1315', 'yelping_since': '2016-03-07 02:47:32'}, {'user_id': 'userid_1708', 'yelping_since': '2016-03-06 20:06:53'}, {'user_id': 'userid_1661', 'yelping_since': '2016-06-13 00:48:17'}, {'user_id': 'userid_850', 'yelping_since': '2016-04-05 22:20:15'}, {'user_id': 'userid_1675', 'yelping_since': '2016-02-13 20:18:19'}, {'user_id': 'userid_227', 'yelping_since': '2016-01-16 01:12:00'}, {'user_id': 'userid_577', 'yelping_since': '2016-08-05 21:32:23'}, {'user_id': 'userid_257', 'yelping_since': '2016-10-19 21:58:32'}, {'user_id': 'userid_598', 'yelping_since': '2016-07-24 20:27:40'}, {'user_id': 'userid_847', 'yelping_since': '2016-08-04 20:28:55'}, {'user_id': 'userid_673', 'yelping_since': '2016-09-29 14:11:39'}, {'user_id': 'userid_1856', 'yelping_since': '2016-11-19 23:19:11'}, {'user_id': 'userid_384', 'yelping_since': '2016-04-21 20:00:19'}, {'user_id': 'userid_935', 'yelping_since': '2016-03-04 03:53:07'}, {'user_id': 'userid_210', 'yelping_since': '2016-06-24 03:16:47'}, {'user_id': 'userid_1101', 'yelping_since': '2016-06-13 19:58:37'}, {'user_id': 'userid_945', 'yelping_since': '2016-05-08 04:31:48'}, {'user_id': 'userid_842', 'yelping_since': '2016-02-21 19:02:44'}, {'user_id': 'userid_1351', 'yelping_since': '2016-03-30 02:56:55'}, {'user_id': 'userid_230', 'yelping_since': '2016-09-28 21:47:27'}, {'user_id': 'userid_593', 'yelping_since': '2016-11-18 05:33:16'}, {'user_id': 'userid_1431', 'yelping_since': '2016-01-06 23:48:07'}, {'user_id': 'userid_686', 'yelping_since': '2016-02-20 02:24:38'}, {'user_id': 'userid_527', 'yelping_since': '2016-06-26 04:19:08'}, {'user_id': 'userid_244', 'yelping_since': '2016-02-06 05:06:29'}, {'user_id': 'userid_393', 'yelping_since': '2016-08-16 18:42:51'}, {'user_id': 'userid_1178', 'yelping_since': '2016-05-05 18:04:24'}, {'user_id': 'userid_526', 'yelping_since': '2016-12-16 00:17:31'}, {'user_id': 'userid_90', 'yelping_since': '2016-07-14 00:52:49'}, {'user_id': 'userid_238', 'yelping_since': '2016-12-29 01:41:33'}, {'user_id': 'userid_1105', 'yelping_since': '2016-03-15 21:53:34'}], 'var_call_qEAZPzCuBNoketItF6ikTU75': [{'business_ref': 'businessref_45', 'review_count': '3'}, {'business_ref': 'businessref_60', 'review_count': '2'}, {'business_ref': 'businessref_66', 'review_count': '2'}, {'business_ref': 'businessref_74', 'review_count': '2'}, {'business_ref': 'businessref_92', 'review_count': '2'}, {'business_ref': 'businessref_33', 'review_count': '2'}, {'business_ref': 'businessref_96', 'review_count': '2'}, {'business_ref': 'businessref_36', 'review_count': '2'}, {'business_ref': 'businessref_57', 'review_count': '2'}, {'business_ref': 'businessref_26', 'review_count': '1'}, {'business_ref': 'businessref_14', 'review_count': '1'}, {'business_ref': 'businessref_68', 'review_count': '1'}, {'business_ref': 'businessref_98', 'review_count': '1'}, {'business_ref': 'businessref_6', 'review_count': '1'}, {'business_ref': 'businessref_15', 'review_count': '1'}, {'business_ref': 'businessref_53', 'review_count': '1'}, {'business_ref': 'businessref_10', 'review_count': '1'}, {'business_ref': 'businessref_37', 'review_count': '1'}, {'business_ref': 'businessref_86', 'review_count': '1'}, {'business_ref': 'businessref_13', 'review_count': '1'}, {'business_ref': 'businessref_31', 'review_count': '1'}, {'business_ref': 'businessref_20', 'review_count': '1'}, {'business_ref': 'businessref_62', 'review_count': '1'}, {'business_ref': 'businessref_12', 'review_count': '1'}, {'business_ref': 'businessref_79', 'review_count': '1'}, {'business_ref': 'businessref_41', 'review_count': '1'}], 'var_call_60kMH9XgNWm43CjZ41ESHNIF': [{'business_id': 'businessid_45', 'description': 'Located at 2900 4th St N in St. Petersburg, FL, this establishment offers a diverse range of products and services in the categories of Food, Grocery, Shopping.'}], 'var_call_e1qKFXbc01Qbl7sjhUtJ9m0b': [{'business_id': 'businessid_60', 'description': 'Located at 8101 W Judge Perez Dr in Chalmette, LA, this versatile establishment offers a wide range of options for customers, including Food, Shopping, Fashion, Discount Store, Grocery, Electronics, Drugstores, Department Stores, ensuring that visitors can find everything they need in one convenient location.'}], 'var_call_1kMSYNmDoqxMrOqmAIC36JMc': [{'business_id': 'businessid_66', 'description': 'Located at 3849 State St. Space I-58 in Santa Barbara, CA, this establishment offers a variety of quick and delicious options in the categories of Fast Food, Chinese, Restaurants.'}], 'var_call_Yy3Mdcxl3Y0f6P5hxpw7ndRF': [{'business_id': 'businessid_74', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}], 'var_call_cG48pCnpsdkNXWHcWugF8swy': [{'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}], 'var_call_krTbaeGlIcn9hjqxEKjwHIOo': [{'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_qQVCifbyYBz2NiwUDCVBKjss': [{'business_id': 'businessid_96', 'description': 'Located at 3257 Ivanhoe Ave in Saint Louis, MO, this establishment offers a vibrant atmosphere perfect for enjoying a diverse selection of experiences, including Wine Bars, American (New), Cocktail Bars, Restaurants, American (Traditional), Nightlife, and Bars.'}], 'var_call_NkzqA8jXjljlCaTnao7nX7Yb': [{'business_id': 'businessid_36', 'description': "Located at 47 Easton Rd in Willow Grove, PA, this inviting establishment offers a delightful menu featuring authentic flavors in the categories of 'Restaurants, Vietnamese'."}], 'var_call_TWNvZ5K9R7Yb3nW2enLPyPeW': [{'business_id': 'businessid_57', 'description': 'Located at 13605 W Hillsborough Ave in Tampa, FL, this versatile establishment offers a range of services and dining options, including Movers, American (New), Landscape Architects, Food, Home Services, Self Storage, Local Services, Restaurants.'}], 'var_call_b8zNoMrlTbgs1VAfFhSPX8TO': [{'business_id': 'businessid_26', 'description': 'Located at 7003 Seminole Blvd in Seminole, FL, this establishment specializes in a variety of offerings, including Fast Food, Restaurants, Coffee & Tea, Food, and Burgers, making it a convenient stop for a quick meal or a refreshing beverage.'}], 'var_call_1AmnuZL3ttmIGM12fK31K7ky': [{'business_id': 'businessid_14', 'description': "Located at 7055 Marketplace Dr in Goleta, CA, this store offers a diverse selection of products across various categories, including Women's Clothing, Fashion, Department Stores, Home Decor, Home & Garden, Shopping, Men's Clothing, and Discount Store."}], 'var_call_wQVij58hV207yeDJryC2Gt6E': [{'business_id': 'businessid_68', 'description': 'Located at 593 Brandon Town Ctr in Brandon, FL, this establishment offers a range of services in the categories of Beauty & Spas, Hair Removal, and Eyebrow Services.'}], 'var_call_jnRiMwRY1cXB1ULcaFfeIB60': [{'business_id': 'businessid_98', 'description': 'Situated at 600 Red Lion Rd in Philadelphia, PA, this establishment offers a range of services in Real Estate, Apartments, and Home Services.'}], 'var_call_wGSigq1uXCWvxCB4wNrmy1kt': [{'business_id': 'businessid_6', 'description': 'Located at 246 W 1st St in Reno, NV, this vibrant destination offers a delightful mix of Restaurants, Breakfast & Brunch, Bars, Wine Bars, Coffee & Tea, Food, Cafes, Sandwiches, and Nightlife, making it an ideal spot for any meal or occasion.'}], 'var_call_oETuCplRW2vxzANyePcCiRA6': [{'business_id': 'businessid_15', 'description': 'Located at 3803 Gen Degaulle Dr in New Orleans, LA, this establishment specializes in Automotive, Oil Change Stations, providing efficient service for all your vehicle maintenance needs.'}], 'var_call_jP90brw0N1MMLnURMrjWMMDB': [{'business_id': 'businessid_53', 'description': 'Located at 1040 N American St, Ste 1101 in Philadelphia, PA, this eatery offers a diverse menu featuring Salad, Sandwiches, Restaurants, and Burgers.'}], 'var_call_PtqnBiQlHFjXhFxFbqeNcnzb': [{'business_id': 'businessid_10', 'description': "Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of 'Restaurants, Chinese'."}], 'var_call_wGB0f4jk7NIolo43ccMjZqJU': [{'business_id': 'businessid_37', 'description': 'Located at 13122 N Dale Mabry Hwy in Tampa, FL, this facility offers a comprehensive range of services in Fitness & Instruction, Gyms, Boot Camps, Trainers, Active Life, and Interval Training Gyms.'}], 'var_call_3mGizG1CDVHwH6ih9HoadPD5': [{'business_id': 'businessid_86', 'description': 'Located at 705 East Passyunk Ave in Philadelphia, PA, this vibrant eatery offers a diverse menu featuring American (New), Restaurants, American (Traditional), Asian Fusion, Noodles, Dim Sum, Fast Food, Chinese, catering to a variety of tastes and preferences.'}], 'var_call_n5HtPZr98ZU1LqOLWazeA6IY': [{'business_id': 'businessid_13', 'description': 'Located at 3545 Almaville Rd in Smyrna, TN, this establishment offers a delightful experience encompassing Food, Arts & Entertainment, Wineries, and a Wine Tasting Room.'}], 'var_call_ggrgrlLTJ3ApDHT5gKSgBD88': [{'business_id': 'businessid_31', 'description': 'Located at 1234 Pasadena Ave S in South Pasadena, FL, this business specializes in Automotive services, offering a comprehensive Car Wash and professional Auto Detailing to keep your vehicle looking its best.'}], 'var_call_XCQQ8AYrUNzdXUtenB6xyr52': [{'business_id': 'businessid_20', 'description': 'Located at 9040 State Road 54 in Trinity, FL, this establishment offers a diverse array of options, including Restaurants, American (New), Caterers, Fast Food, Chicken Shop, Event Planning & Services, and American (Traditional).'}], 'var_call_Q1lP6WBY8IF0hITwkAmgoqqz': [{'business_id': 'businessid_62', 'description': 'Located at 8424 Sheldon Rd in Tampa, FL, this establishment offers a diverse range of products and services, including Photography Stores & Services, Shopping, Grocery, and Food.'}], 'var_call_lHGvVWJ4oI8hJjJIaPYUsKRL': [{'business_id': 'businessid_12', 'description': 'Located at 7704 Calgary Trail S in Edmonton, AB, this vibrant spot offers a diverse experience with options for Pubs, Restaurants, Nightlife, Burgers, Seafood, and Bars.'}], 'var_call_ukdQXFcgNklQWYB3F6DXxObY': [{'business_id': 'businessid_79', 'description': 'Located at 838-842 Christian St in Philadelphia, PA, this establishment offers a wide range of services including Pet Groomers, Pet Stores, Pet Training, Dog Walkers, Pet Services, Pets, and Pet Sitting.'}], 'var_call_bb2vdU4q2MVrAJs0GRRIHAXg': [{'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}]}

exec(code, env_args)
