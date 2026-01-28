code = """import json
import re
from collections import defaultdict

# Load business data
business_file = locals()['var_functions.query_db:8']
with open(business_file) as f:
    businesses = json.load(f)

# Create mapping from business_id to categories
business_id_to_categories = {}
for business in businesses:
    business_id = business['business_id']
    description = business.get('description', '')
    
    # Extract categories from description
    # Look for patterns like "services in X, Y, and Z" or "category of 'X, Y'"
    categories = []
    
    # Pattern 1: "services in A, B, C, and D"
    match1 = re.search(r'services in (.+?)(?:\.|$)', description, re.IGNORECASE)
    if match1:
        cat_text = match1.group(1)
        # Remove "and" before splitting
        cat_text = re.sub(r'\sand\s', ', ', cat_text)
        cats = [c.strip() for c in cat_text.split(',') if c.strip()]
        categories.extend(cats)
    
    # Pattern 2: "category of 'X, Y'"
    match2 = re.search(r"category of '(.+?)'", description)
    if match2:
        cat_text = match2.group(1)
        cats = [c.strip() for c in cat_text.split(',') if c.strip()]
        categories.extend(cats)
    
    # Pattern 3: "fields of A, B, C"
    match3 = re.search(r'fields of (.+?)(?:\.|$)', description, re.IGNORECASE)
    if match3:
        cat_text = match3.group(1)
        cat_text = re.sub(r'\sand\s', ', ', cat_text)
        cats = [c.strip() for c in cat_text.split(',') if c.strip()]
        categories.extend(cats)
    
    business_id_to_categories[business_id] = categories

# Count how many businesses have categories
businesses_with_cats = sum(1 for cats in business_id_to_categories.values() if cats)

print('__RESULT__:')
print(json.dumps({
    'total_businesses': len(businesses),
    'businesses_with_categories': businesses_with_cats,
    'sample_categories': {k: business_id_to_categories[k] for k in list(business_id_to_categories.keys())[:5]}
}))"""

env_args = {'var_functions.list_db:0': ['review', 'tip', 'user'], 'var_functions.query_db:2': [{'user_id': 'userid_286', 'name': 'Todd', 'review_count': '376', 'yelping_since': '15 Jan 2009, 16:40', 'useful': '1373', 'funny': '723', 'cool': '639', 'elite': '2010,2011,2012,2013,2014'}, {'user_id': 'userid_1331', 'name': 'Patt', 'review_count': '1028', 'yelping_since': '13 Jul 2010, 15:42', 'useful': '9050', 'funny': '3249', 'cool': '5929', 'elite': '2011,2012,2013,2014,2015,2016,2017,2018,2019,20,20,2021'}, {'user_id': 'userid_1880', 'name': 'Norma', 'review_count': '57', 'yelping_since': '2010-09-07 23:24:36', 'useful': '217', 'funny': '57', 'cool': '115', 'elite': '2012,2013'}, {'user_id': 'userid_271', 'name': 'Antony', 'review_count': '49', 'yelping_since': 'October 23, 2011 at 07:47 PM', 'useful': '116', 'funny': '159', 'cool': '34', 'elite': ''}, {'user_id': 'userid_534', 'name': 'Mandy', 'review_count': '754', 'yelping_since': '2011-08-30 13:46:26', 'useful': '2925', 'funny': '775', 'cool': '988', 'elite': '2011,2012,2013,2014,2015,2016,2017,2018,2019,20,20,2021'}], 'var_functions.query_db:5': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.query_db:6': [{'user_id': 'userid_1231', 'yelping_since': '14 Sep 2016, 00:32'}, {'user_id': 'userid_343', 'yelping_since': '02 Feb 2016, 04:30'}, {'user_id': 'userid_746', 'yelping_since': '2016-06-23 01:59:28'}, {'user_id': 'userid_505', 'yelping_since': 'September 10, 2016 at 08:02 PM'}, {'user_id': 'userid_898', 'yelping_since': 'January 15, 2016 at 06:33 PM'}, {'user_id': 'userid_144', 'yelping_since': '25 Feb 2016, 04:52'}, {'user_id': 'userid_1927', 'yelping_since': 'October 13, 2016 at 04:29 AM'}, {'user_id': 'userid_1109', 'yelping_since': '2016-10-16 18:32:25'}, {'user_id': 'userid_1950', 'yelping_since': '2016-04-16 03:42:28'}, {'user_id': 'userid_1316', 'yelping_since': '2016-12-29 21:32:44'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:14': {'total_users_2016': 168, 'sample_users': ['userid_1231', 'userid_343', 'userid_746', 'userid_505', 'userid_898']}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'total_users_2016': 168, 'total_reviews_by_2016_users': 126, 'sample_reviews': [{'user_id': 'userid_655', 'business_ref': 'businessref_36', 'date': '22 Oct 2021, 21:44'}, {'user_id': 'userid_1397', 'business_ref': 'businessref_23', 'date': '2016-06-28 02:18:33'}, {'user_id': 'userid_1274', 'business_ref': 'businessref_67', 'date': '2018-01-02 21:35:31'}]}}

exec(code, env_args)
