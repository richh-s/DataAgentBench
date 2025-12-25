code = """import pandas as pd
import json

reviews_data = locals()['var_function-call-68412389071058765']
business_info = locals()['var_function-call-1993038310780031126']

df_reviews = pd.DataFrame(reviews_data)
df_business = pd.DataFrame(business_info)

# Clean business_id to match business_ref for merging
df_business['business_ref'] = df_business['business_id'].str.replace('businessid_', 'businessref_')

# Merge reviews with business info
df_merged = pd.DataFrame(pd.merge(df_reviews, df_business, on='business_ref', how='left'))

# Function to extract categories from description
def extract_categories(description):
    if not isinstance(description, str):
        return []

    # Keywords and phrases indicating the start of a category list
    keywords_phrases = [
        "offers a range of services in ",
        "including ",
        "seeking ",
        "in the fields of ",
        "in the category of ",
        "services and products in "
    ]

    category_str = description
    # Find the last occurrence of any of the keywords/phrases
    last_found_index = -1
    best_start_index = -1
    for kp in keywords_phrases:
        idx = description.rfind(kp)
        if idx != -1 and idx > last_found_index:
            last_found_index = idx
            best_start_index = idx + len(kp)

    if best_start_index != -1:
        category_str = description[best_start_index:]
    elif ',' in description and 'offers' in description:
        # Fallback for cases like 'this establishment offers X, Y, Z'
        # Try to find the last comma after 'offers'
        offer_index = description.rfind('offers')
        if offer_index != -1:
            # Try to find the categories after the offers phrase.
            # This is a bit heuristic, assuming categories are usually at the end.
            # For example, 'offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'
            # We want 'Candy Stores, Specialty Food, Food.'
            # Simple approach: find the last segment after the last comma if a category seems to be there.
            last_comma_index = category_str.rfind(',')
            if last_comma_index != -1 and last_comma_index > offer_index:
                 category_str = category_str[last_comma_index + 1:].strip()
            else:
                category_str = category_str[offer_index:].strip() # take from offers till end
    
    # Further cleaning and splitting
    category_str = category_str.lower().replace(' and ', ',').replace(' or ', ',')
    categories = [cat.strip() for cat in category_str.split(',') if cat.strip()]

    # Remove common non-category words or phrases that might be left over
    # For example, if 'this establishment' or location info is accidentally included
    # This is still tricky to do perfectly without more advanced NLP.
    # For now, let's keep it simple. If we see a category like 'food' at the end, that's likely intended.

    return categories


all_categories_with_reviews = []
for index, row in df_merged.iterrows():
    categories = extract_categories(row['description'])
    for cat in categories:
        all_categories_with_reviews.append({'category': cat, 'review_id': row['review_id']})

df_categories_reviews = pd.DataFrame(all_categories_with_reviews)

if not df_categories_reviews.empty:
    # Count reviews per category
    category_review_counts = df_categories_reviews.groupby('category')['review_id'].count().reset_index()
    category_review_counts.columns = ['category', 'total_reviews']

    # Get top 5 categories
    top_5_categories = category_review_counts.sort_values(by='total_reviews', ascending=False).head(5)
    result = top_5_categories.to_json(orient='records')
else:
    result = json.dumps([]) # Return empty JSON array if no categories found

print("__RESULT__:")
print(result)"""

env_args = {'var_function-call-16171340445905463813': [{'user_id': 'userid_746'}, {'user_id': 'userid_1109'}, {'user_id': 'userid_1950'}, {'user_id': 'userid_1316'}, {'user_id': 'userid_1182'}, {'user_id': 'userid_151'}, {'user_id': 'userid_1158'}, {'user_id': 'userid_508'}, {'user_id': 'userid_435'}, {'user_id': 'userid_958'}, {'user_id': 'userid_1879'}, {'user_id': 'userid_308'}, {'user_id': 'userid_1179'}, {'user_id': 'userid_324'}, {'user_id': 'userid_863'}, {'user_id': 'userid_100'}, {'user_id': 'userid_1333'}, {'user_id': 'userid_1636'}, {'user_id': 'userid_1850'}, {'user_id': 'userid_711'}, {'user_id': 'userid_729'}, {'user_id': 'userid_1505'}, {'user_id': 'userid_1315'}, {'user_id': 'userid_1708'}, {'user_id': 'userid_1661'}, {'user_id': 'userid_850'}, {'user_id': 'userid_1675'}, {'user_id': 'userid_227'}, {'user_id': 'userid_577'}, {'user_id': 'userid_257'}, {'user_id': 'userid_598'}, {'user_id': 'userid_847'}, {'user_id': 'userid_673'}, {'user_id': 'userid_1856'}, {'user_id': 'userid_384'}, {'user_id': 'userid_935'}, {'user_id': 'userid_210'}, {'user_id': 'userid_1101'}, {'user_id': 'userid_945'}, {'user_id': 'userid_842'}, {'user_id': 'userid_1351'}, {'user_id': 'userid_230'}, {'user_id': 'userid_593'}, {'user_id': 'userid_1431'}, {'user_id': 'userid_686'}, {'user_id': 'userid_527'}, {'user_id': 'userid_244'}, {'user_id': 'userid_393'}, {'user_id': 'userid_1178'}, {'user_id': 'userid_526'}, {'user_id': 'userid_90'}, {'user_id': 'userid_238'}, {'user_id': 'userid_1105'}], 'var_function-call-68412389071058765': [{'business_ref': 'businessref_74', 'review_id': 'reviewid_318', 'date': '2021-07-16 17:24:00'}, {'business_ref': 'businessref_57', 'review_id': 'reviewid_1049', 'date': 'September 04, 2017 at 08:57 PM'}, {'business_ref': 'businessref_96', 'review_id': 'reviewid_454', 'date': 'August 06, 2016 at 02:19 AM'}, {'business_ref': 'businessref_45', 'review_id': 'reviewid_1065', 'date': 'August 10, 2016 at 04:36 AM'}, {'business_ref': 'businessref_74', 'review_id': 'reviewid_704', 'date': 'April 17, 2016 at 12:00 AM'}, {'business_ref': 'businessref_53', 'review_id': 'reviewid_84', 'date': '25 Nov 2016, 20:04'}, {'business_ref': 'businessref_41', 'review_id': 'reviewid_1110', 'date': 'December 12, 2017 at 02:27 AM'}, {'business_ref': 'businessref_96', 'review_id': 'reviewid_655', 'date': '2017-01-06 11:15:06'}, {'business_ref': 'businessref_10', 'review_id': 'reviewid_1239', 'date': '2021-11-28 23:56:00'}, {'business_ref': 'businessref_66', 'review_id': 'reviewid_515', 'date': 'November 10, 2021 at 06:40 AM'}, {'business_ref': 'businessref_31', 'review_id': 'reviewid_44', 'date': '24 Jan 2017, 19:28'}, {'business_ref': 'businessref_92', 'review_id': 'reviewid_65', 'date': '2019-11-14 17:06:00'}, {'business_ref': 'businessref_26', 'review_id': 'reviewid_1216', 'date': '2018-07-23 06:45:43'}, {'business_ref': 'businessref_98', 'review_id': 'reviewid_781', 'date': '2017-11-17 16:06:00'}, {'business_ref': 'businessref_45', 'review_id': 'reviewid_334', 'date': 'February 06, 2018 at 07:29 PM'}, {'business_ref': 'businessref_45', 'review_id': 'reviewid_124', 'date': 'October 28, 2016 at 03:54 PM'}, {'business_ref': 'businessref_36', 'review_id': 'reviewid_957', 'date': '2018-05-21 17:51:00'}, {'business_ref': 'businessref_14', 'review_id': 'reviewid_1174', 'date': 'May 04, 2017 at 11:25 PM'}, {'business_ref': 'businessref_86', 'review_id': 'reviewid_1502', 'date': '2019-04-14 23:08:41'}, {'business_ref': 'businessref_57', 'review_id': 'reviewid_919', 'date': 'October 30, 2018 at 01:06 PM'}, {'business_ref': 'businessref_13', 'review_id': 'reviewid_926', 'date': 'August 22, 2021 at 12:11 AM'}, {'business_ref': 'businessref_68', 'review_id': 'reviewid_1457', 'date': 'October 14, 2018 at 04:06 PM'}, {'business_ref': 'businessref_36', 'review_id': 'reviewid_1576', 'date': '2016-12-02 00:06:00'}, {'business_ref': 'businessref_60', 'review_id': 'reviewid_1677', 'date': '2017-03-24 23:59:00'}, {'business_ref': 'businessref_20', 'review_id': 'reviewid_160', 'date': '27 May 2017, 00:50'}, {'business_ref': 'businessref_15', 'review_id': 'reviewid_1207', 'date': 'June 20, 2018 at 02:12 PM'}, {'business_ref': 'businessref_62', 'review_id': 'reviewid_1635', 'date': '2018-04-01 10:52:37'}, {'business_ref': 'businessref_33', 'review_id': 'reviewid_1966', 'date': 'August 18, 2016 at 11:57 AM'}, {'business_ref': 'businessref_37', 'review_id': 'reviewid_1791', 'date': '2016-07-24 20:27:00'}, {'business_ref': 'businessref_92', 'review_id': 'reviewid_1986', 'date': '30 Dec 2018, 18:49'}, {'business_ref': 'businessref_66', 'review_id': 'reviewid_1137', 'date': 'June 21, 2020 at 07:59 PM'}, {'business_ref': 'businessref_33', 'review_id': 'reviewid_1555', 'date': 'August 30, 2019 at 06:15 PM'}, {'business_ref': 'businessref_6', 'review_id': 'reviewid_1408', 'date': '30 Jun 2017, 04:44'}, {'business_ref': 'businessref_12', 'review_id': 'reviewid_1388', 'date': 'October 26, 2017 at 11:10 PM'}, {'business_ref': 'businessref_79', 'review_id': 'reviewid_62', 'date': '30 Oct 2017, 01:27'}, {'business_ref': 'businessref_60', 'review_id': 'reviewid_280', 'date': '2019-05-29 19:46:00'}], 'var_function-call-3367742661720438269': ['business', 'checkin'], 'var_function-call-1993038310780031126': [{'business_id': 'businessid_41', 'attributes': 'None', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'business_id': 'businessid_74', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '4', 'BikeParking': 'False'}, 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}, {'business_id': 'businessid_92', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'True', 'NoiseLevel': "u'quiet'", 'WiFi': "u'no'"}, 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'business_id': 'businessid_10', 'attributes': {'RestaurantsGoodForGroups': 'True', 'RestaurantsDelivery': 'False', 'RestaurantsTakeOut': 'True', 'HasTV': 'True', 'BusinessAcceptsCreditCards': 'True', 'Ambience': "{'touristy': False, 'hipster': False, 'romantic': False, 'divey': False, 'intimate': False, 'trendy': False, 'upscale': False, 'classy': False, 'casual': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': False, 'brunch': False, 'breakfast': False}", 'BusinessParking': "{u'valet': False, u'garage': False, u'street': False, u'lot': True, u'validated': False}"}, 'description': "Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of 'Restaurants, Chinese'."}], 'var_function-call-2943423704395968904': [{'category': 'beauty & spas', 'total_reviews': 4}, {'category': 'blow dry/out services', 'total_reviews': 2}, {'category': 'candy stores', 'total_reviews': 2}, {'category': 'cosmetic dentists', 'total_reviews': 2}, {'category': 'cosmetics & beauty supply', 'total_reviews': 2}]}

exec(code, env_args)
