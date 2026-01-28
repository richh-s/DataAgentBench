code = """import json
import re

# Get the data from storage
reviews = locals()['var_functions.query_db:7']
businesses = locals()['var_functions.query_db:12']

# Create mapping from business numeric ID to business info
business_map = {}
for business in businesses:
    # Extract numeric ID from business_id (format: businessid_X)
    business_id_full = business['business_id']
    business_num_id = business_id_full.replace('businessid_', '')
    
    # Parse categories from description
    description = business['description']
    categories = []
    
    # The description format seems to have categories after "including" or "services in"
    if 'including' in description:
        # Extract text after "including"
        parts = description.split('including')
        if len(parts) > 1:
            categories_part = parts[1].split('.')[0].split('Located at')[0]
            # Split by commas and clean up
            categories = [cat.strip() for cat in categories_part.split(',') if cat.strip()]
    elif 'services in' in description:
        # Extract text after "services in"
        parts = description.split('services in')
        if len(parts) > 1:
            categories_part = parts[1].split('.')[0].split('Located at')[0]
            # Split by commas and clean up
            categories = [cat.strip() for cat in categories_part.split(',') if cat.strip()]
    
    business_map[business_num_id] = {
        'name': business['name'],
        'business_id_full': business_id_full,
        'review_count': int(business['review_count']),
        'categories': categories,
        'description': description
    }

# Group reviews by business numeric ID
business_reviews = {}
for review in reviews:
    business_ref = review['business_ref']
    # Extract numeric ID from business_ref (format: businessref_X)
    business_num_id = business_ref.replace('businessref_', '')
    
    rating = int(review['rating'])
    
    if business_num_id not in business_reviews:
        business_reviews[business_num_id] = []
    
    business_reviews[business_num_id].append(rating)

# Calculate average ratings for businesses that have at least 5 total reviews
valid_businesses = []
for business_num_id, ratings in business_reviews.items():
    # Check if this business exists in our business_map and has >=5 reviews
    if business_num_id in business_map:
        business_info = business_map[business_num_id]
        if business_info['review_count'] >= 5:
            avg_rating = sum(ratings) / len(ratings)
            valid_businesses.append({
                'name': business_info['name'],
                'business_id': business_info['business_id_full'],
                'review_count': business_info['review_count'],
                'avg_rating': avg_rating,
                'num_reviews_in_period': len(ratings),
                'categories': business_info['categories'],
                'description': business_info['description']
            })

# Sort by average rating descending to find the highest
valid_businesses.sort(key=lambda x: x['avg_rating'], reverse=True)

# Get the top business
top_business = valid_businesses[0] if valid_businesses else None

print('__RESULT__:')
print(json.dumps(top_business, indent=2))"""

env_args = {'var_functions.list_db:0': ['business', 'checkin'], 'var_functions.list_db:2': ['review', 'tip', 'user'], 'var_functions.query_db:4': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_functions.query_db:7': [{'review_id': 'reviewid_76', 'business_ref': 'businessref_16', 'rating': '1', 'date': '2016-01-01 02:46:00'}, {'review_id': 'reviewid_459', 'business_ref': 'businessref_23', 'rating': '5', 'date': '2016-06-28 02:18:33'}, {'review_id': 'reviewid_78', 'business_ref': 'businessref_8', 'rating': '5', 'date': '2016-03-12 14:19:00'}, {'review_id': 'reviewid_1383', 'business_ref': 'businessref_9', 'rating': '5', 'date': '2016-05-24 23:15:00'}, {'review_id': 'reviewid_190', 'business_ref': 'businessref_96', 'rating': '5', 'date': '2016-02-25 04:58:04'}, {'review_id': 'reviewid_31', 'business_ref': 'businessref_8', 'rating': '5', 'date': '2016-05-15 04:34:00'}, {'review_id': 'reviewid_1588', 'business_ref': 'businessref_47', 'rating': '5', 'date': '2016-06-24 19:38:03'}, {'review_id': 'reviewid_1447', 'business_ref': 'businessref_37', 'rating': '5', 'date': '2016-06-02 18:48:00'}, {'review_id': 'reviewid_1715', 'business_ref': 'businessref_8', 'rating': '4', 'date': '2016-02-24 18:52:00'}, {'review_id': 'reviewid_1075', 'business_ref': 'businessref_43', 'rating': '4', 'date': '2016-05-16 22:46:00'}, {'review_id': 'reviewid_842', 'business_ref': 'businessref_14', 'rating': '3', 'date': '2016-05-06 16:02:13'}, {'review_id': 'reviewid_1510', 'business_ref': 'businessref_21', 'rating': '1', 'date': '2016-06-01 12:40:27'}, {'review_id': 'reviewid_1594', 'business_ref': 'businessref_16', 'rating': '3', 'date': '2016-05-17 07:05:00'}, {'review_id': 'reviewid_1149', 'business_ref': 'businessref_31', 'rating': '1', 'date': '2016-04-19 23:46:00'}, {'review_id': 'reviewid_742', 'business_ref': 'businessref_30', 'rating': '2', 'date': '2016-03-08 05:52:00'}, {'review_id': 'reviewid_677', 'business_ref': 'businessref_81', 'rating': '1', 'date': '2016-03-25 21:45:04'}, {'review_id': 'reviewid_1947', 'business_ref': 'businessref_71', 'rating': '5', 'date': '2016-01-04 02:38:00'}, {'review_id': 'reviewid_1664', 'business_ref': 'businessref_31', 'rating': '1', 'date': '2016-06-20 23:50:23'}, {'review_id': 'reviewid_1330', 'business_ref': 'businessref_46', 'rating': '5', 'date': '2016-03-28 01:57:00'}, {'review_id': 'reviewid_1438', 'business_ref': 'businessref_99', 'rating': '5', 'date': '2016-05-23 05:02:00'}, {'review_id': 'reviewid_1421', 'business_ref': 'businessref_40', 'rating': '5', 'date': '2016-06-20 15:01:00'}, {'review_id': 'reviewid_1325', 'business_ref': 'businessref_9', 'rating': '5', 'date': '2016-04-02 23:09:00'}, {'review_id': 'reviewid_1340', 'business_ref': 'businessref_68', 'rating': '1', 'date': '2016-03-10 23:52:49'}, {'review_id': 'reviewid_1335', 'business_ref': 'businessref_11', 'rating': '5', 'date': '2016-06-03 20:33:00'}, {'review_id': 'reviewid_629', 'business_ref': 'businessref_21', 'rating': '1', 'date': '2016-05-10 20:15:12'}, {'review_id': 'reviewid_1718', 'business_ref': 'businessref_9', 'rating': '5', 'date': '2016-05-08 03:51:05'}, {'review_id': 'reviewid_1769', 'business_ref': 'businessref_8', 'rating': '3', 'date': '2016-06-27 11:15:38'}, {'review_id': 'reviewid_1323', 'business_ref': 'businessref_46', 'rating': '5', 'date': '2016-03-13 00:55:00'}, {'review_id': 'reviewid_903', 'business_ref': 'businessref_68', 'rating': '1', 'date': '2016-03-29 10:58:00'}, {'review_id': 'reviewid_122', 'business_ref': 'businessref_88', 'rating': '5', 'date': '2016-06-26 17:45:00'}, {'review_id': 'reviewid_1324', 'business_ref': 'businessref_9', 'rating': '2', 'date': '2016-01-01 19:40:00'}, {'review_id': 'reviewid_1902', 'business_ref': 'businessref_71', 'rating': '1', 'date': '2016-05-12 21:06:18'}, {'review_id': 'reviewid_647', 'business_ref': 'businessref_28', 'rating': '5', 'date': '2016-03-02 22:59:37'}, {'review_id': 'reviewid_95', 'business_ref': 'businessref_71', 'rating': '5', 'date': '2016-02-17 00:37:00'}, {'review_id': 'reviewid_1592', 'business_ref': 'businessref_37', 'rating': '5', 'date': '2016-05-25 15:30:00'}, {'review_id': 'reviewid_1088', 'business_ref': 'businessref_9', 'rating': '3', 'date': '2016-04-29 21:21:00'}, {'review_id': 'reviewid_950', 'business_ref': 'businessref_17', 'rating': '5', 'date': '2016-03-12 15:27:00'}, {'review_id': 'reviewid_1937', 'business_ref': 'businessref_82', 'rating': '4', 'date': '2016-01-11 20:06:01'}], 'var_functions.query_db:8': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.execute_python:10': {'top_business': {'name': 'Breeze Blow Dry Bar', 'business_id': 'businessid_47', 'review_count': 81, 'avg_rating': 5.0, 'num_reviews_in_period': 1, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, 'valid_businesses_count': 2, 'all_valid': [{'name': 'Breeze Blow Dry Bar', 'business_id': 'businessid_47', 'review_count': 81, 'avg_rating': 5.0, 'num_reviews_in_period': 1, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'name': 'Impact Guns', 'business_id': 'businessid_88', 'review_count': 39, 'avg_rating': 5.0, 'num_reviews_in_period': 1, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}]}, 'var_functions.query_db:12': [{'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.execute_python:14': {'name': 'Breeze Blow Dry Bar', 'business_id': 'businessid_47', 'review_count': 81, 'avg_rating': 5.0, 'num_reviews_in_period': 1, 'categories': ['Hair Salons', 'Beauty & Spas', 'Hair Stylists', 'Skin Care', 'Blow Dry/Out Services', 'and Makeup Artists']}}

exec(code, env_args)
