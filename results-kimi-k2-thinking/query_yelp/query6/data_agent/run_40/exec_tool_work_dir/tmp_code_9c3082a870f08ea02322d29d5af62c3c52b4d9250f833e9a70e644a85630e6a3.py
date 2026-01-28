code = """import json
import re

# Load data from files since they might be large
reviews_file = var_functions.query_db:6
business_file = var_functions.query_db:8

# If these are strings (file paths), load them
if isinstance(reviews_file, str):
    with open(reviews_file, 'r') as f:
        reviews_data = json.load(f)
else:
    reviews_data = reviews_file

if isinstance(business_file, str):
    with open(business_file, 'r') as f:
        business_data = json.load(f)
else:
    business_data = business_file

# Process reviews
business_ratings = {}
for review in reviews_data:
    business_ref = review['business_ref']
    rating = int(review['rating'])
    
    if business_ref not in business_ratings:
        business_ratings[business_ref] = []
    business_ratings[business_ref].append(rating)

# Calculate stats for businesses with >= 5 reviews
business_stats = []
for business_ref, ratings in business_ratings.items():
    review_count = len(ratings)
    if review_count >= 5:
        avg_rating = sum(ratings) / review_count
        business_stats.append({
            'business_ref': business_ref,
            'review_count': review_count,
            'avg_rating': avg_rating
        })

# Find best business
if business_stats:
    best = max(business_stats, key=lambda x: x['avg_rating'])
    ref_id = best['business_ref'].replace('businessref_', '')
    business_id = 'businessid_' + ref_id
    
    business_info = None
    for biz in business_data:
        if biz['business_id'] == business_id:
            business_info = biz
            break
    
    if business_info:
        desc = business_info.get('description', '')
        category = 'Unknown'
        
        patterns = [
            r'services (?:in|including) ([^\.]+)',
            r'offers ([^\.]+)',
            r'range of services including ([^\.]+)'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, desc)
            if match:
                categories = match.group(1).strip()
                category = categories.split(',')[0].strip()
                break
        
        result = {
            'business_name': business_info['name'],
            'average_rating': round(best['avg_rating'], 2),
            'review_count': best['review_count'],
            'category': category
        }
    else:
        result = {'error': 'Business not found'}
else:
    result = {'error': 'No qualifying businesses'}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['business', 'checkin'], 'var_functions.query_db:2': [{'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8'}, {'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81'}, {'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39'}, {'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5'}, {'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28'}], 'var_functions.list_db:4': ['review', 'tip', 'user'], 'var_functions.query_db:6': [{'review_id': 'reviewid_76', 'business_ref': 'businessref_16', 'rating': '1', 'date': '2016-01-01 02:46:00'}, {'review_id': 'reviewid_459', 'business_ref': 'businessref_23', 'rating': '5', 'date': '2016-06-28 02:18:33'}, {'review_id': 'reviewid_78', 'business_ref': 'businessref_8', 'rating': '5', 'date': '2016-03-12 14:19:00'}, {'review_id': 'reviewid_1383', 'business_ref': 'businessref_9', 'rating': '5', 'date': '2016-05-24 23:15:00'}, {'review_id': 'reviewid_190', 'business_ref': 'businessref_96', 'rating': '5', 'date': '2016-02-25 04:58:04'}, {'review_id': 'reviewid_31', 'business_ref': 'businessref_8', 'rating': '5', 'date': '2016-05-15 04:34:00'}, {'review_id': 'reviewid_1588', 'business_ref': 'businessref_47', 'rating': '5', 'date': '2016-06-24 19:38:03'}, {'review_id': 'reviewid_1447', 'business_ref': 'businessref_37', 'rating': '5', 'date': '2016-06-02 18:48:00'}, {'review_id': 'reviewid_1715', 'business_ref': 'businessref_8', 'rating': '4', 'date': '2016-02-24 18:52:00'}, {'review_id': 'reviewid_1075', 'business_ref': 'businessref_43', 'rating': '4', 'date': '2016-05-16 22:46:00'}, {'review_id': 'reviewid_842', 'business_ref': 'businessref_14', 'rating': '3', 'date': '2016-05-06 16:02:13'}, {'review_id': 'reviewid_1510', 'business_ref': 'businessref_21', 'rating': '1', 'date': '2016-06-01 12:40:27'}, {'review_id': 'reviewid_1594', 'business_ref': 'businessref_16', 'rating': '3', 'date': '2016-05-17 07:05:00'}, {'review_id': 'reviewid_1149', 'business_ref': 'businessref_31', 'rating': '1', 'date': '2016-04-19 23:46:00'}, {'review_id': 'reviewid_742', 'business_ref': 'businessref_30', 'rating': '2', 'date': '2016-03-08 05:52:00'}, {'review_id': 'reviewid_677', 'business_ref': 'businessref_81', 'rating': '1', 'date': '2016-03-25 21:45:04'}, {'review_id': 'reviewid_1947', 'business_ref': 'businessref_71', 'rating': '5', 'date': '2016-01-04 02:38:00'}, {'review_id': 'reviewid_1664', 'business_ref': 'businessref_31', 'rating': '1', 'date': '2016-06-20 23:50:23'}, {'review_id': 'reviewid_1330', 'business_ref': 'businessref_46', 'rating': '5', 'date': '2016-03-28 01:57:00'}, {'review_id': 'reviewid_1438', 'business_ref': 'businessref_99', 'rating': '5', 'date': '2016-05-23 05:02:00'}, {'review_id': 'reviewid_1421', 'business_ref': 'businessref_40', 'rating': '5', 'date': '2016-06-20 15:01:00'}, {'review_id': 'reviewid_1325', 'business_ref': 'businessref_9', 'rating': '5', 'date': '2016-04-02 23:09:00'}, {'review_id': 'reviewid_1340', 'business_ref': 'businessref_68', 'rating': '1', 'date': '2016-03-10 23:52:49'}, {'review_id': 'reviewid_1335', 'business_ref': 'businessref_11', 'rating': '5', 'date': '2016-06-03 20:33:00'}, {'review_id': 'reviewid_629', 'business_ref': 'businessref_21', 'rating': '1', 'date': '2016-05-10 20:15:12'}, {'review_id': 'reviewid_1718', 'business_ref': 'businessref_9', 'rating': '5', 'date': '2016-05-08 03:51:05'}, {'review_id': 'reviewid_1769', 'business_ref': 'businessref_8', 'rating': '3', 'date': '2016-06-27 11:15:38'}, {'review_id': 'reviewid_1323', 'business_ref': 'businessref_46', 'rating': '5', 'date': '2016-03-13 00:55:00'}, {'review_id': 'reviewid_903', 'business_ref': 'businessref_68', 'rating': '1', 'date': '2016-03-29 10:58:00'}, {'review_id': 'reviewid_122', 'business_ref': 'businessref_88', 'rating': '5', 'date': '2016-06-26 17:45:00'}, {'review_id': 'reviewid_1324', 'business_ref': 'businessref_9', 'rating': '2', 'date': '2016-01-01 19:40:00'}, {'review_id': 'reviewid_1902', 'business_ref': 'businessref_71', 'rating': '1', 'date': '2016-05-12 21:06:18'}, {'review_id': 'reviewid_647', 'business_ref': 'businessref_28', 'rating': '5', 'date': '2016-03-02 22:59:37'}, {'review_id': 'reviewid_95', 'business_ref': 'businessref_71', 'rating': '5', 'date': '2016-02-17 00:37:00'}, {'review_id': 'reviewid_1592', 'business_ref': 'businessref_37', 'rating': '5', 'date': '2016-05-25 15:30:00'}, {'review_id': 'reviewid_1088', 'business_ref': 'businessref_9', 'rating': '3', 'date': '2016-04-29 21:21:00'}, {'review_id': 'reviewid_950', 'business_ref': 'businessref_17', 'rating': '5', 'date': '2016-03-12 15:27:00'}, {'review_id': 'reviewid_1937', 'business_ref': 'businessref_82', 'rating': '4', 'date': '2016-01-11 20:06:01'}], 'var_functions.query_db:8': [{'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'attributes': 'None', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}]}

exec(code, env_args)
