code = """import json
from collections import defaultdict

reviews_2016_users = locals()['var_function-call-6873826044148845602']
business_info = locals()['var_function-call-3176026539170776166']

business_id_to_categories = {}
for business in business_info:
    business_id = business['business_id']
    description = business['description']
    categories = []

    # Attempt to extract categories from description
    if 'services in ' in description:
        start_index = description.find('services in ') + len('services in ')
        end_index = description.find('.', start_index)
        if end_index != -1:
            category_string = description[start_index:end_index]
            categories.extend([cat.strip() for cat in category_string.split(',')])
    elif 'services including ' in description:
        start_index = description.find('services including ') + len('services including ')
        end_index = description.find('.', start_index)
        if end_index != -1:
            category_string = description[start_index:end_index]
            categories.extend([cat.strip() for cat in category_string.split(',')])
    elif 'in the category of ' in description:
        start_index = description.find('in the category of ') + len('in the category of ')
        end_index = description.find('.', start_index)
        if end_index != -1:
            category_string = description[start_index:end_index].strip("'") # remove surrounding quotes
            categories.extend([cat.strip() for cat in category_string.split(',')])

    business_id_to_categories[business_id] = categories


category_review_counts = defaultdict(int)

for review in reviews_2016_users:
    business_ref = review['business_ref']
    business_id = business_ref.replace('businessref_', 'businessid_')

    if business_id in business_id_to_categories:
        categories = business_id_to_categories[business_id]
        for category in categories:
            if category:
                category_review_counts[category] += 1

sorted_categories = sorted(category_review_counts.items(), key=lambda item: item[1], reverse=True)
top_5_categories = sorted_categories[:5]

print("__RESULT__:")
print(json.dumps(top_5_categories))"""

env_args = {'var_function-call-15071328952853740136': [{'user_id': 'userid_746'}, {'user_id': 'userid_1109'}, {'user_id': 'userid_1950'}, {'user_id': 'userid_1316'}, {'user_id': 'userid_1182'}, {'user_id': 'userid_151'}, {'user_id': 'userid_1158'}, {'user_id': 'userid_508'}, {'user_id': 'userid_435'}, {'user_id': 'userid_958'}, {'user_id': 'userid_1879'}, {'user_id': 'userid_308'}, {'user_id': 'userid_1179'}, {'user_id': 'userid_324'}, {'user_id': 'userid_863'}, {'user_id': 'userid_100'}, {'user_id': 'userid_1333'}, {'user_id': 'userid_1636'}, {'user_id': 'userid_1850'}, {'user_id': 'userid_711'}, {'user_id': 'userid_729'}, {'user_id': 'userid_1505'}, {'user_id': 'userid_1315'}, {'user_id': 'userid_1708'}, {'user_id': 'userid_1661'}, {'user_id': 'userid_850'}, {'user_id': 'userid_1675'}, {'user_id': 'userid_227'}, {'user_id': 'userid_577'}, {'user_id': 'userid_257'}, {'user_id': 'userid_598'}, {'user_id': 'userid_847'}, {'user_id': 'userid_673'}, {'user_id': 'userid_1856'}, {'user_id': 'userid_384'}, {'user_id': 'userid_935'}, {'user_id': 'userid_210'}, {'user_id': 'userid_1101'}, {'user_id': 'userid_945'}, {'user_id': 'userid_842'}, {'user_id': 'userid_1351'}, {'user_id': 'userid_230'}, {'user_id': 'userid_593'}, {'user_id': 'userid_1431'}, {'user_id': 'userid_686'}, {'user_id': 'userid_527'}, {'user_id': 'userid_244'}, {'user_id': 'userid_393'}, {'user_id': 'userid_1178'}, {'user_id': 'userid_526'}, {'user_id': 'userid_90'}, {'user_id': 'userid_238'}, {'user_id': 'userid_1105'}], 'var_function-call-6873826044148845602': [{'business_ref': 'businessref_74', 'date': '2021-07-16 17:24:00'}, {'business_ref': 'businessref_57', 'date': 'September 04, 2017 at 08:57 PM'}, {'business_ref': 'businessref_96', 'date': 'August 06, 2016 at 02:19 AM'}, {'business_ref': 'businessref_45', 'date': 'August 10, 2016 at 04:36 AM'}, {'business_ref': 'businessref_74', 'date': 'April 17, 2016 at 12:00 AM'}, {'business_ref': 'businessref_53', 'date': '25 Nov 2016, 20:04'}, {'business_ref': 'businessref_41', 'date': 'December 12, 2017 at 02:27 AM'}, {'business_ref': 'businessref_96', 'date': '2017-01-06 11:15:06'}, {'business_ref': 'businessref_10', 'date': '2021-11-28 23:56:00'}, {'business_ref': 'businessref_66', 'date': 'November 10, 2021 at 06:40 AM'}, {'business_ref': 'businessref_31', 'date': '24 Jan 2017, 19:28'}, {'business_ref': 'businessref_92', 'date': '2019-11-14 17:06:00'}, {'business_ref': 'businessref_26', 'date': '2018-07-23 06:45:43'}, {'business_ref': 'businessref_98', 'date': '2017-11-17 16:06:00'}, {'business_ref': 'businessref_45', 'date': 'February 06, 2018 at 07:29 PM'}, {'business_ref': 'businessref_45', 'date': 'October 28, 2016 at 03:54 PM'}, {'business_ref': 'businessref_36', 'date': '2018-05-21 17:51:00'}, {'business_ref': 'businessref_14', 'date': 'May 04, 2017 at 11:25 PM'}, {'business_ref': 'businessref_86', 'date': '2019-04-14 23:08:41'}, {'business_ref': 'businessref_57', 'date': 'October 30, 2018 at 01:06 PM'}, {'business_ref': 'businessref_13', 'date': 'August 22, 2021 at 12:11 AM'}, {'business_ref': 'businessref_68', 'date': 'October 14, 2018 at 04:06 PM'}, {'business_ref': 'businessref_36', 'date': '2016-12-02 00:06:00'}, {'business_ref': 'businessref_60', 'date': '2017-03-24 23:59:00'}, {'business_ref': 'businessref_20', 'date': '27 May 2017, 00:50'}, {'business_ref': 'businessref_15', 'date': 'June 20, 2018 at 02:12 PM'}, {'business_ref': 'businessref_62', 'date': '2018-04-01 10:52:37'}, {'business_ref': 'businessref_33', 'date': 'August 18, 2016 at 11:57 AM'}, {'business_ref': 'businessref_37', 'date': '2016-07-24 20:27:00'}, {'business_ref': 'businessref_92', 'date': '30 Dec 2018, 18:49'}, {'business_ref': 'businessref_66', 'date': 'June 21, 2020 at 07:59 PM'}, {'business_ref': 'businessref_33', 'date': 'August 30, 2019 at 06:15 PM'}, {'business_ref': 'businessref_6', 'date': '30 Jun 2017, 04:44'}, {'business_ref': 'businessref_12', 'date': 'October 26, 2017 at 11:10 PM'}, {'business_ref': 'businessref_79', 'date': '30 Oct 2017, 01:27'}, {'business_ref': 'businessref_60', 'date': '2019-05-29 19:46:00'}], 'var_function-call-17517535313902130297': ['business', 'checkin'], 'var_function-call-4816535974244241166': ['businessid_14', 'businessid_45', 'businessid_98', 'businessid_53', 'businessid_36', 'businessid_62', 'businessid_86', 'businessid_96', 'businessid_41', 'businessid_15', 'businessid_26', 'businessid_60', 'businessid_68', 'businessid_13', 'businessid_37', 'businessid_92', 'businessid_66', 'businessid_74', 'businessid_31', 'businessid_6', 'businessid_12', 'businessid_57', 'businessid_79', 'businessid_10', 'businessid_33', 'businessid_20'], 'var_function-call-3176026539170776166': [{'business_id': 'businessid_41', 'attributes': 'None', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'business_id': 'businessid_74', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '4', 'BikeParking': 'False'}, 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}, {'business_id': 'businessid_92', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'True', 'NoiseLevel': "u'quiet'", 'WiFi': "u'no'"}, 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'business_id': 'businessid_10', 'attributes': {'RestaurantsGoodForGroups': 'True', 'RestaurantsDelivery': 'False', 'RestaurantsTakeOut': 'True', 'HasTV': 'True', 'BusinessAcceptsCreditCards': 'True', 'Ambience': "{'touristy': False, 'hipster': False, 'romantic': False, 'divey': False, 'intimate': False, 'trendy': False, 'upscale': False, 'classy': False, 'casual': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': False, 'brunch': False, 'breakfast': False}", 'BusinessParking': "{u'valet': False, u'garage': False, u'street': False, u'lot': True, u'validated': False}"}, 'description': "Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of 'Restaurants, Chinese'."}]}

exec(code, env_args)
