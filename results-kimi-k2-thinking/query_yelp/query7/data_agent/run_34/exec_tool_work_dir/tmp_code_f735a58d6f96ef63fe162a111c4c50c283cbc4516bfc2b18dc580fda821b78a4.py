code = """import json
import pandas as pd
import re
from collections import defaultdict

# Load all data
users_file = locals()['var_functions.query_db:24']
reviews_file = locals()['var_functions.query_db:30']
businesses = locals()['var_functions.query_db:32']

with open(users_file, 'r') as f:
    users_2016 = json.load(f)

with open(reviews_file, 'r') as f:
    reviews_2016 = json.load(f)

# Map business ID to categories
business_categories = {}
category_review_counts = defaultdict(int)

for business in businesses:
    business_id = business['business_id']
    description = business.get('description', '')
    
    # Extract categories from description
    # Look for pattern: "...services in X, Y, Z." or "...services including X, Y, and Z."
    categories = []
    
    # Pattern 1: "services in <categories>" or "service in <categories>"
    match1 = re.search(r'\bservice[s]? (?:offers|in|including) ([^.]+)', description, re.IGNORECASE)
    if match1:
        text = match1.group(1)
        # Extract comma-separated categories
        cats = re.findall(r'[A-Z][a-zA-Z &\-]+(?=,|\band\b|\.)', text)
        categories = [cat.strip() for cat in cats if cat.strip()]
        
        # If no pattern found, try to extract from end of description
        if not categories:
            # Pattern 2: Look for list at end of description after "in" or "including"
            parts = description.split('providing a range of services in ')
            if len(parts) > 1:
                cat_text = parts[1]
                # Split by comma and "and"
                raw_cats = re.split(r', | and ', cat_text.rstrip('.'))
                categories = [cat.strip() for cat in raw_cats if cat.strip()]
    
    # Pattern 3: Alternative patterns
    if not categories:
        # Look for "services including X, Y, and Z"
        match3 = re.search(r'including ([^.]+)\.?', description, re.IGNORECASE)
        if match3:
            text = match3.group(1)
            raw_cats = re.split(r', | and ', text)
            categories = [cat.strip() for cat in raw_cats if cat.strip()]
    
    # Pattern 4: For businesses that don't match above, try generic listing
    if not categories and 'services' in description.lower():
        # Find capitalized words that might be categories
        words = re.findall(r'[A-Z][a-z]+(?: [A-Z][a-z]+)*(?:\s*&\s*[A-Z][a-z]+)*', description)
        # Filter out location words and common noise
        exclude_words = {'Located', 'At', 'This', 'Facility', 'Offers', 'Range', 'Of', 'Services', 'In'}
        categories = [w.strip() for w in words if w.strip() not in exclude_words and len(w.strip()) > 3]
    
    business_categories[business_id] = categories

# Count reviews by users who registered in 2016
user_ids_2016 = {user['user_id'] for user in users_2016}
business_review_counts = defaultdict(int)

for review in reviews_2016:
    if review['user_id'] in user_ids_2016:
        business_ref = review['business_ref']
        business_id = business_ref.replace('businessref_', 'businessid_')
        business_review_counts[business_id] += 1

# Sum reviews by category
for business_id, review_count in business_review_counts.items():
    categories = business_categories.get(business_id, [])
    for category in categories:
        category_review_counts[category] += review_count

# Sort categories by total reviews
top_categories = sorted(category_review_counts.items(), key=lambda x: x[1], reverse=True)[:5]

print("__RESULT__:")
print(json.dumps({
    "top_5_categories": top_categories,
    "total_categories": len(category_review_counts),
    "total_businesses_with_categories": len([b for b, cats in business_categories.items() if cats])
}))"""

env_args = {'var_functions.list_db:0': ['business', 'checkin'], 'var_functions.query_db:2': [{'user_id': 'userid_286', 'name': 'Todd', 'review_count': '376', 'yelping_since': '15 Jan 2009, 16:40', 'useful': '1373', 'funny': '723', 'cool': '639', 'elite': '2010,2011,2012,2013,2014'}, {'user_id': 'userid_1331', 'name': 'Patt', 'review_count': '1028', 'yelping_since': '13 Jul 2010, 15:42', 'useful': '9050', 'funny': '3249', 'cool': '5929', 'elite': '2011,2012,2013,2014,2015,2016,2017,2018,2019,20,20,2021'}, {'user_id': 'userid_1880', 'name': 'Norma', 'review_count': '57', 'yelping_since': '2010-09-07 23:24:36', 'useful': '217', 'funny': '57', 'cool': '115', 'elite': '2012,2013'}, {'user_id': 'userid_271', 'name': 'Antony', 'review_count': '49', 'yelping_since': 'October 23, 2011 at 07:47 PM', 'useful': '116', 'funny': '159', 'cool': '34', 'elite': ''}, {'user_id': 'userid_534', 'name': 'Mandy', 'review_count': '754', 'yelping_since': '2011-08-30 13:46:26', 'useful': '2925', 'funny': '775', 'cool': '988', 'elite': '2011,2012,2013,2014,2015,2016,2017,2018,2019,20,20,2021'}], 'var_functions.query_db:4': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.query_db:6': [{'user_id': 'userid_1231', 'name': 'Ashley', 'review_count': '1110', 'yelping_since': '14 Sep 2016, 00:32', 'useful': '2871', 'funny': '672', 'cool': '2410', 'elite': '2017,2018,2019,20,20,2021'}, {'user_id': 'userid_343', 'name': 'Chaz', 'review_count': '8', 'yelping_since': '02 Feb 2016, 04:30', 'useful': '1', 'funny': '0', 'cool': '0', 'elite': ''}, {'user_id': 'userid_746', 'name': 'Rita', 'review_count': '179', 'yelping_since': '2016-06-23 01:59:28', 'useful': '205', 'funny': '27', 'cool': '55', 'elite': '2017,2018,2019,20,20,2021'}, {'user_id': 'userid_505', 'name': 'Jameela', 'review_count': '4', 'yelping_since': 'September 10, 2016 at 08:02 PM', 'useful': '1', 'funny': '0', 'cool': '0', 'elite': ''}, {'user_id': 'userid_898', 'name': 'Tuyen', 'review_count': '92', 'yelping_since': 'January 15, 2016 at 06:33 PM', 'useful': '190', 'funny': '30', 'cool': '52', 'elite': '2017,2018,2019,20,20,2021'}, {'user_id': 'userid_144', 'name': 'Michael', 'review_count': '4', 'yelping_since': '25 Feb 2016, 04:52', 'useful': '4', 'funny': '4', 'cool': '4', 'elite': ''}, {'user_id': 'userid_1927', 'name': 'Ken', 'review_count': '147', 'yelping_since': 'October 13, 2016 at 04:29 AM', 'useful': '235', 'funny': '12', 'cool': '99', 'elite': '2018,2019,20,20,2021'}, {'user_id': 'userid_1109', 'name': 'Bruce', 'review_count': '23', 'yelping_since': '2016-10-16 18:32:25', 'useful': '14', 'funny': '11', 'cool': '1', 'elite': ''}, {'user_id': 'userid_1950', 'name': 'Samantha', 'review_count': '120', 'yelping_since': '2016-04-16 03:42:28', 'useful': '90', 'funny': '25', 'cool': '40', 'elite': '2018,2019,20,20,2021'}, {'user_id': 'userid_1316', 'name': 'Kathleen', 'review_count': '289', 'yelping_since': '2016-12-29 21:32:44', 'useful': '379', 'funny': '82', 'cool': '232', 'elite': '2018,2019,20,20,2021'}], 'var_functions.execute_python:8': {'users_sample': 10, 'business_sample': 2, 'date_formats_observed': True}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.list_db:12': ['review', 'tip', 'user'], 'var_functions.execute_python:22': {'available_vars': ['var_functions.query_db:2', 'var_functions.query_db:4', 'var_functions.query_db:6', 'var_functions.query_db:10'], 'vars_count': 9}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:28': {'total_users_2016': 168, 'sample_users': ['userid_100', 'userid_1013', 'userid_1030', 'userid_1068', 'userid_1070']}, 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.execute_python:34': {'total_users_2016': 168, 'total_reviews': 150, 'reviews_by_users_2016': 150, 'businesses_reviewed': 62, 'sample_business_counts': {'businessid_36': 3, 'businessid_79': 8, 'businessid_23': 1, 'businessid_67': 5, 'businessid_37': 6}}}

exec(code, env_args)
