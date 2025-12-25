code = """import pandas as pd
import json

reviews_data = locals()['var_function-call-68412389071058765']
business_info = locals()['var_function-call-1993038310780031126']

df_reviews = pd.DataFrame(reviews_data)
df_business = pd.DataFrame(business_info)

# Clean business_id to match business_ref for merging
df_business['business_ref'] = df_business['business_id'].str.replace('businessid_', 'businessref_')

# Merge reviews with business info
df_merged = pd.merge(df_reviews, df_business, on='business_ref', how='left')

# Extract categories from description. Split by comma and clean up.
# Some descriptions are like '...offers a range of services in Internal Medicine, Doctors, Health & Medical.'
# Some are like '...a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'
# I will try to find keywords indicating the start of categories such as 'in the fields of', 'including', 'offers a range of services in', 'seeking'.
# For simplicity, I will extract text after the last occurrence of such keywords, or just split the whole description.

def extract_categories(description):
    if not isinstance(description, str):
        return []

    # Keywords to look for indicating the start of a category list
    keywords = ['in the fields of ', 'including ', 'offers a range of services in ', 'seeking ']
    start_index = -1
    for keyword in keywords:
        if keyword in description:
            start_index = description.rfind(keyword) + len(keyword)
            break

    if start_index != -1:
        category_str = description[start_index:]
    else:
        # Fallback if no keyword is found, take the last part of the sentence after a common separator
        if ',' in description:
            category_str = description.split(',')[-1] # Take the last segment
        else:
            return [] # No clear categories
    
    # Further refinement: remove location parts at the beginning like 'Located at X in Y, this...' or 'this facility'
    # Simple heuristic: remove text before the first category word that is typically not a location or introductory phrase
    category_str = category_str.lower().replace(' and ', ',').replace(' or ', ',')
    categories = [cat.strip() for cat in category_str.split(',') if cat.strip()]

    return categories


all_categories = []
for _, row in df_merged.iterrows():
    categories = extract_categories(row['description'])
    all_categories.extend([(cat, row['review_id']) for cat in categories])

df_categories_reviews = pd.DataFrame(all_categories, columns=['category', 'review_id'])

# Count reviews per category
category_review_counts = df_categories_reviews.groupby('category')['review_id'].count().reset_index()
category_review_counts.columns = ['category', 'total_reviews']

# Get top 5 categories
top_5_categories = category_review_counts.sort_values(by='total_reviews', ascending=False).head(5)


print("__RESULT__:")
print(top_5_categories.to_json(orient='records'))"""

env_args = {'var_function-call-16171340445905463813': [{'user_id': 'userid_746'}, {'user_id': 'userid_1109'}, {'user_id': 'userid_1950'}, {'user_id': 'userid_1316'}, {'user_id': 'userid_1182'}, {'user_id': 'userid_151'}, {'user_id': 'userid_1158'}, {'user_id': 'userid_508'}, {'user_id': 'userid_435'}, {'user_id': 'userid_958'}, {'user_id': 'userid_1879'}, {'user_id': 'userid_308'}, {'user_id': 'userid_1179'}, {'user_id': 'userid_324'}, {'user_id': 'userid_863'}, {'user_id': 'userid_100'}, {'user_id': 'userid_1333'}, {'user_id': 'userid_1636'}, {'user_id': 'userid_1850'}, {'user_id': 'userid_711'}, {'user_id': 'userid_729'}, {'user_id': 'userid_1505'}, {'user_id': 'userid_1315'}, {'user_id': 'userid_1708'}, {'user_id': 'userid_1661'}, {'user_id': 'userid_850'}, {'user_id': 'userid_1675'}, {'user_id': 'userid_227'}, {'user_id': 'userid_577'}, {'user_id': 'userid_257'}, {'user_id': 'userid_598'}, {'user_id': 'userid_847'}, {'user_id': 'userid_673'}, {'user_id': 'userid_1856'}, {'user_id': 'userid_384'}, {'user_id': 'userid_935'}, {'user_id': 'userid_210'}, {'user_id': 'userid_1101'}, {'user_id': 'userid_945'}, {'user_id': 'userid_842'}, {'user_id': 'userid_1351'}, {'user_id': 'userid_230'}, {'user_id': 'userid_593'}, {'user_id': 'userid_1431'}, {'user_id': 'userid_686'}, {'user_id': 'userid_527'}, {'user_id': 'userid_244'}, {'user_id': 'userid_393'}, {'user_id': 'userid_1178'}, {'user_id': 'userid_526'}, {'user_id': 'userid_90'}, {'user_id': 'userid_238'}, {'user_id': 'userid_1105'}], 'var_function-call-68412389071058765': [{'business_ref': 'businessref_74', 'review_id': 'reviewid_318', 'date': '2021-07-16 17:24:00'}, {'business_ref': 'businessref_57', 'review_id': 'reviewid_1049', 'date': 'September 04, 2017 at 08:57 PM'}, {'business_ref': 'businessref_96', 'review_id': 'reviewid_454', 'date': 'August 06, 2016 at 02:19 AM'}, {'business_ref': 'businessref_45', 'review_id': 'reviewid_1065', 'date': 'August 10, 2016 at 04:36 AM'}, {'business_ref': 'businessref_74', 'review_id': 'reviewid_704', 'date': 'April 17, 2016 at 12:00 AM'}, {'business_ref': 'businessref_53', 'review_id': 'reviewid_84', 'date': '25 Nov 2016, 20:04'}, {'business_ref': 'businessref_41', 'review_id': 'reviewid_1110', 'date': 'December 12, 2017 at 02:27 AM'}, {'business_ref': 'businessref_96', 'review_id': 'reviewid_655', 'date': '2017-01-06 11:15:06'}, {'business_ref': 'businessref_10', 'review_id': 'reviewid_1239', 'date': '2021-11-28 23:56:00'}, {'business_ref': 'businessref_66', 'review_id': 'reviewid_515', 'date': 'November 10, 2021 at 06:40 AM'}, {'business_ref': 'businessref_31', 'review_id': 'reviewid_44', 'date': '24 Jan 2017, 19:28'}, {'business_ref': 'businessref_92', 'review_id': 'reviewid_65', 'date': '2019-11-14 17:06:00'}, {'business_ref': 'businessref_26', 'review_id': 'reviewid_1216', 'date': '2018-07-23 06:45:43'}, {'business_ref': 'businessref_98', 'review_id': 'reviewid_781', 'date': '2017-11-17 16:06:00'}, {'business_ref': 'businessref_45', 'review_id': 'reviewid_334', 'date': 'February 06, 2018 at 07:29 PM'}, {'business_ref': 'businessref_45', 'review_id': 'reviewid_124', 'date': 'October 28, 2016 at 03:54 PM'}, {'business_ref': 'businessref_36', 'review_id': 'reviewid_957', 'date': '2018-05-21 17:51:00'}, {'business_ref': 'businessref_14', 'review_id': 'reviewid_1174', 'date': 'May 04, 2017 at 11:25 PM'}, {'business_ref': 'businessref_86', 'review_id': 'reviewid_1502', 'date': '2019-04-14 23:08:41'}, {'business_ref': 'businessref_57', 'review_id': 'reviewid_919', 'date': 'October 30, 2018 at 01:06 PM'}, {'business_ref': 'businessref_13', 'review_id': 'reviewid_926', 'date': 'August 22, 2021 at 12:11 AM'}, {'business_ref': 'businessref_68', 'review_id': 'reviewid_1457', 'date': 'October 14, 2018 at 04:06 PM'}, {'business_ref': 'businessref_36', 'review_id': 'reviewid_1576', 'date': '2016-12-02 00:06:00'}, {'business_ref': 'businessref_60', 'review_id': 'reviewid_1677', 'date': '2017-03-24 23:59:00'}, {'business_ref': 'businessref_20', 'review_id': 'reviewid_160', 'date': '27 May 2017, 00:50'}, {'business_ref': 'businessref_15', 'review_id': 'reviewid_1207', 'date': 'June 20, 2018 at 02:12 PM'}, {'business_ref': 'businessref_62', 'review_id': 'reviewid_1635', 'date': '2018-04-01 10:52:37'}, {'business_ref': 'businessref_33', 'review_id': 'reviewid_1966', 'date': 'August 18, 2016 at 11:57 AM'}, {'business_ref': 'businessref_37', 'review_id': 'reviewid_1791', 'date': '2016-07-24 20:27:00'}, {'business_ref': 'businessref_92', 'review_id': 'reviewid_1986', 'date': '30 Dec 2018, 18:49'}, {'business_ref': 'businessref_66', 'review_id': 'reviewid_1137', 'date': 'June 21, 2020 at 07:59 PM'}, {'business_ref': 'businessref_33', 'review_id': 'reviewid_1555', 'date': 'August 30, 2019 at 06:15 PM'}, {'business_ref': 'businessref_6', 'review_id': 'reviewid_1408', 'date': '30 Jun 2017, 04:44'}, {'business_ref': 'businessref_12', 'review_id': 'reviewid_1388', 'date': 'October 26, 2017 at 11:10 PM'}, {'business_ref': 'businessref_79', 'review_id': 'reviewid_62', 'date': '30 Oct 2017, 01:27'}, {'business_ref': 'businessref_60', 'review_id': 'reviewid_280', 'date': '2019-05-29 19:46:00'}], 'var_function-call-3367742661720438269': ['business', 'checkin'], 'var_function-call-1993038310780031126': [{'business_id': 'businessid_41', 'attributes': 'None', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'business_id': 'businessid_74', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '4', 'BikeParking': 'False'}, 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}, {'business_id': 'businessid_92', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'True', 'NoiseLevel': "u'quiet'", 'WiFi': "u'no'"}, 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'business_id': 'businessid_10', 'attributes': {'RestaurantsGoodForGroups': 'True', 'RestaurantsDelivery': 'False', 'RestaurantsTakeOut': 'True', 'HasTV': 'True', 'BusinessAcceptsCreditCards': 'True', 'Ambience': "{'touristy': False, 'hipster': False, 'romantic': False, 'divey': False, 'intimate': False, 'trendy': False, 'upscale': False, 'classy': False, 'casual': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': False, 'brunch': False, 'breakfast': False}", 'BusinessParking': "{u'valet': False, u'garage': False, u'street': False, u'lot': True, u'validated': False}"}, 'description': "Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of 'Restaurants, Chinese'."}]}

exec(code, env_args)
