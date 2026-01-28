code = """import json
import re
from collections import Counter

# Get reviews from 2016-registered users (44 reviews)
reviews_data = locals().get('var_functions.query_db:10', [])

# Read the complete business data from file
business_file_path = locals().get('var_functions.query_db:26')
with open(business_file_path, 'r') as f:
    all_business_data = json.load(f)

# Build complete business category mapping
business_categories = {}
business_names = {}

for biz in all_business_data:
    biz_id = biz['business_id']
    biz_num = biz_id.split('_')[1]
    business_ref_id = f'businessref_{biz_num}'
    
    desc = biz['description']
    
    # Extract categories systematically
    categories = []
    
    # Primary pattern: look for category lists in the description
    # Pattern 1: "services in A, B, C, and D."
    match1 = re.search(r'services? in (.*?)(?:\.|Located at|$)', desc, re.IGNORECASE | re.DOTALL)
    if match1:
        text = match1.group(1)
        potential_cats = re.split(r',\s*|\s+and\s+|\.|\n', text)
        for cat in potential_cats:
            cat = cat.strip()
            if cat and len(cat) > 2:
                cat = cat.rstrip('.').strip()
                if cat not in categories:
                    categories.append(cat)
    
    # Pattern 2: "including A, B, C, and D."
    if not categories or len(categories) < 2:
        match2 = re.search(r'including (.*?)(?:\.|Located at|$)', desc, re.IGNORECASE | re.DOTALL)
        if match2:
            text = match2.group(1)
            potential_cats = re.split(r',\s*|\s+and\s+|\.|\n', text)
            for cat in potential_cats:
                cat = cat.strip()
                if cat and len(cat) > 2:
                    cat = cat.rstrip('.').strip()
                    if cat not in categories:
                        categories.append(cat)
    
    # Pattern 3: End of description usually has categories comma-separated
    if not categories or len(categories) < 2:
        # Get the last substantial part of the description
        parts = desc.split('.')
        for part in reversed(parts):
            part = part.strip()
            if len(part) > 20:  # Must be substantial
                # Look for comma-separated capitalized words
                if ',' in part and any(c.isupper() for c in part):
                    potential_cats = re.split(r',\s*', part)
                    for cat in potential_cats:
                        cat = cat.strip()
                        if cat and len(cat) > 2 and any(c.isalpha() for c in cat):
                            # Clean up
                            cat = cat.rstrip('.').strip()
                            if cat not in categories:
                                categories.append(cat)
                break
    
    # Pattern 4: Special handling for descriptions that end with category list
    if not categories or len(categories) < 2:
        # Look for patterns like "...making it perfect for X, Y, Z."
        ending_match = re.search(r'\b(for|in|including)\s+([A-Z][a-zA-Z\s&/-]+(?:,\s+[A-Z][a-zA-Z\s&/-]+)+)', desc)
        if ending_match:
            cat_list = ending_match.group(2)
            potential_cats = re.split(r',\s*', cat_list)
            for cat in potential_cats:
                cat = cat.strip()
                if cat and len(cat) > 2:
                    cat = cat.rstrip('.').strip()
                    if cat not in categories:
                        categories.append(cat)
    
    business_categories[business_ref_id] = categories
    business_names[business_ref_id] = desc[:100]  # Store snippet for debugging

# Now process reviews
reviews_by_year = {}
category_review_counts = Counter()
processed_businesses = set()
unmatched_businesses = set()

for review in reviews_data:
    date_str = review['date']
    business_ref = review['business_ref']
    
    # Extract year
    year_match = re.search(r'(20\d{2})', date_str)
    if year_match and int(year_match.group(1)) >= 2016:
        year = year_match.group(1)
        reviews_by_year[year] = reviews_by_year.get(year, 0) + 1
        
        processed_businesses.add(business_ref)
        
        # Get categories for this business
        if business_ref in business_categories and business_categories[business_ref]:
            cats = business_categories[business_ref]
            for cat in cats:
                category_review_counts[cat] += 1
        else:
            unmatched_businesses.add(business_ref)

# Get top 5 categories
top_5_categories = category_review_counts.most_common(5)

# Prepare results
result = {
    'total_reviews_from_2016_users': len(reviews_data),
    'reviews_since_2016': sum(reviews_by_year.values()),
    'reviews_by_year': reviews_by_year,
    'unique_businesses_reviewed': len(processed_businesses),
    'businesses_with_category_data': len(processed_businesses) - len(unmatched_businesses),
    'businesses_missing_category_data': len(unmatched_businesses),
    'total_categories_found': len(category_review_counts),
    'top_5_categories': []
}

for category, count in top_5_categories:
    result['top_5_categories'].append({
        'category': category,
        'review_count': count
    })

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['review', 'tip', 'user'], 'var_functions.list_db:2': ['checkin', 'business'], 'var_functions.query_db:4': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.query_db:6': [{'user_id': 'userid_746', 'name': 'Rita', 'review_count': '179', 'yelping_since': '2016-06-23 01:59:28', 'useful': '205', 'funny': '27', 'cool': '55', 'elite': '2017,2018,2019,20,20,2021'}, {'user_id': 'userid_1109', 'name': 'Bruce', 'review_count': '23', 'yelping_since': '2016-10-16 18:32:25', 'useful': '14', 'funny': '11', 'cool': '1', 'elite': ''}, {'user_id': 'userid_1950', 'name': 'Samantha', 'review_count': '120', 'yelping_since': '2016-04-16 03:42:28', 'useful': '90', 'funny': '25', 'cool': '40', 'elite': '2018,2019,20,20,2021'}, {'user_id': 'userid_1316', 'name': 'Kathleen', 'review_count': '289', 'yelping_since': '2016-12-29 21:32:44', 'useful': '379', 'funny': '82', 'cool': '232', 'elite': '2018,2019,20,20,2021'}, {'user_id': 'userid_1182', 'name': 'Caroline', 'review_count': '33', 'yelping_since': '2016-03-20 18:41:14', 'useful': '59', 'funny': '7', 'cool': '29', 'elite': ''}, {'user_id': 'userid_151', 'name': 'Dawn', 'review_count': '3', 'yelping_since': '2016-11-07 18:40:10', 'useful': '3', 'funny': '1', 'cool': '1', 'elite': ''}, {'user_id': 'userid_1158', 'name': 'Wendel', 'review_count': '90', 'yelping_since': '2016-01-31 16:25:04', 'useful': '83', 'funny': '12', 'cool': '11', 'elite': ''}, {'user_id': 'userid_508', 'name': 'Jim', 'review_count': '41', 'yelping_since': '2016-07-08 22:37:42', 'useful': '35', 'funny': '6', 'cool': '9', 'elite': ''}, {'user_id': 'userid_435', 'name': 'Danielle', 'review_count': '13', 'yelping_since': '2016-10-31 09:46:54', 'useful': '7', 'funny': '1', 'cool': '3', 'elite': ''}, {'user_id': 'userid_958', 'name': 'Deanna', 'review_count': '47', 'yelping_since': '2016-03-23 20:55:45', 'useful': '42', 'funny': '11', 'cool': '25', 'elite': '2017,2018'}], 'var_functions.query_db:8': [{'user_id': 'userid_746'}, {'user_id': 'userid_1109'}, {'user_id': 'userid_1950'}, {'user_id': 'userid_1316'}, {'user_id': 'userid_1182'}, {'user_id': 'userid_151'}, {'user_id': 'userid_1158'}, {'user_id': 'userid_508'}, {'user_id': 'userid_435'}, {'user_id': 'userid_958'}, {'user_id': 'userid_1879'}, {'user_id': 'userid_308'}, {'user_id': 'userid_1179'}, {'user_id': 'userid_324'}, {'user_id': 'userid_863'}, {'user_id': 'userid_100'}, {'user_id': 'userid_1333'}, {'user_id': 'userid_1636'}, {'user_id': 'userid_1850'}, {'user_id': 'userid_711'}, {'user_id': 'userid_729'}, {'user_id': 'userid_1505'}, {'user_id': 'userid_1315'}, {'user_id': 'userid_1708'}, {'user_id': 'userid_1661'}, {'user_id': 'userid_850'}, {'user_id': 'userid_1675'}, {'user_id': 'userid_227'}, {'user_id': 'userid_577'}, {'user_id': 'userid_257'}, {'user_id': 'userid_598'}, {'user_id': 'userid_847'}, {'user_id': 'userid_673'}, {'user_id': 'userid_1856'}, {'user_id': 'userid_384'}, {'user_id': 'userid_935'}, {'user_id': 'userid_210'}, {'user_id': 'userid_1101'}, {'user_id': 'userid_945'}, {'user_id': 'userid_842'}, {'user_id': 'userid_1351'}, {'user_id': 'userid_230'}, {'user_id': 'userid_593'}, {'user_id': 'userid_1431'}, {'user_id': 'userid_686'}, {'user_id': 'userid_527'}, {'user_id': 'userid_244'}, {'user_id': 'userid_393'}, {'user_id': 'userid_1178'}, {'user_id': 'userid_526'}, {'user_id': 'userid_90'}, {'user_id': 'userid_238'}, {'user_id': 'userid_1105'}], 'var_functions.query_db:10': [{'user_id': 'userid_1158', 'business_ref': 'businessref_8', 'date': '18 Oct 2016, 17:57'}, {'user_id': 'userid_1101', 'business_ref': 'businessref_74', 'date': '2021-07-16 17:24:00'}, {'user_id': 'userid_1105', 'business_ref': 'businessref_57', 'date': 'September 04, 2017 at 08:57 PM'}, {'user_id': 'userid_863', 'business_ref': 'businessref_96', 'date': 'August 06, 2016 at 02:19 AM'}, {'user_id': 'userid_308', 'business_ref': 'businessref_45', 'date': 'August 10, 2016 at 04:36 AM'}, {'user_id': 'userid_729', 'business_ref': 'businessref_74', 'date': 'April 17, 2016 at 12:00 AM'}, {'user_id': 'userid_1431', 'business_ref': 'businessref_6', 'date': '08 Aug 2016, 22:11'}, {'user_id': 'userid_935', 'business_ref': 'businessref_53', 'date': '25 Nov 2016, 20:04'}, {'user_id': 'userid_1856', 'business_ref': 'businessref_41', 'date': 'December 12, 2017 at 02:27 AM'}, {'user_id': 'userid_435', 'business_ref': 'businessref_96', 'date': '2017-01-06 11:15:06'}, {'user_id': 'userid_1178', 'business_ref': 'businessref_10', 'date': '2021-11-28 23:56:00'}, {'user_id': 'userid_1109', 'business_ref': 'businessref_66', 'date': 'November 10, 2021 at 06:40 AM'}, {'user_id': 'userid_593', 'business_ref': 'businessref_31', 'date': '24 Jan 2017, 19:28'}, {'user_id': 'userid_1182', 'business_ref': 'businessref_92', 'date': '2019-11-14 17:06:00'}, {'user_id': 'userid_230', 'business_ref': 'businessref_26', 'date': '2018-07-23 06:45:43'}, {'user_id': 'userid_244', 'business_ref': 'businessref_98', 'date': '2017-11-17 16:06:00'}, {'user_id': 'userid_1316', 'business_ref': 'businessref_45', 'date': 'February 06, 2018 at 07:29 PM'}, {'user_id': 'userid_324', 'business_ref': 'businessref_45', 'date': 'October 28, 2016 at 03:54 PM'}, {'user_id': 'userid_1850', 'business_ref': 'businessref_36', 'date': '2018-05-21 17:51:00'}, {'user_id': 'userid_686', 'business_ref': 'businessref_14', 'date': 'May 04, 2017 at 11:25 PM'}, {'user_id': 'userid_1950', 'business_ref': 'businessref_86', 'date': '2019-04-14 23:08:41'}, {'user_id': 'userid_945', 'business_ref': 'businessref_57', 'date': 'October 30, 2018 at 01:06 PM'}, {'user_id': 'userid_1179', 'business_ref': 'businessref_13', 'date': 'August 22, 2021 at 12:11 AM'}, {'user_id': 'userid_1879', 'business_ref': 'businessref_68', 'date': 'October 14, 2018 at 04:06 PM'}, {'user_id': 'userid_526', 'business_ref': 'businessref_51', 'date': '01 Nov 2018, 00:25'}, {'user_id': 'userid_577', 'business_ref': 'businessref_33', 'date': '18 Apr 2019, 22:26'}, {'user_id': 'userid_850', 'business_ref': 'businessref_36', 'date': '2016-12-02 00:06:00'}, {'user_id': 'userid_958', 'business_ref': 'businessref_60', 'date': '2017-03-24 23:59:00'}, {'user_id': 'userid_1661', 'business_ref': 'businessref_20', 'date': '27 May 2017, 00:50'}, {'user_id': 'userid_210', 'business_ref': 'businessref_15', 'date': 'June 20, 2018 at 02:12 PM'}, {'user_id': 'userid_90', 'business_ref': 'businessref_97', 'date': '20 Jun 2020, 00:03'}, {'user_id': 'userid_151', 'business_ref': 'businessref_62', 'date': '2018-04-01 10:52:37'}, {'user_id': 'userid_1708', 'business_ref': 'businessref_72', 'date': '06 Mar 2016, 21:20'}, {'user_id': 'userid_100', 'business_ref': 'businessref_33', 'date': 'August 18, 2016 at 11:57 AM'}, {'user_id': 'userid_598', 'business_ref': 'businessref_37', 'date': '2016-07-24 20:27:00'}, {'user_id': 'userid_746', 'business_ref': 'businessref_92', 'date': '30 Dec 2018, 18:49'}, {'user_id': 'userid_1675', 'business_ref': 'businessref_66', 'date': 'June 21, 2020 at 07:59 PM'}, {'user_id': 'userid_393', 'business_ref': 'businessref_51', 'date': '07 Mar 2020, 05:21'}, {'user_id': 'userid_1505', 'business_ref': 'businessref_33', 'date': 'August 30, 2019 at 06:15 PM'}, {'user_id': 'userid_842', 'business_ref': 'businessref_6', 'date': '30 Jun 2017, 04:44'}, {'user_id': 'userid_257', 'business_ref': 'businessref_12', 'date': 'October 26, 2017 at 11:10 PM'}, {'user_id': 'userid_1333', 'business_ref': 'businessref_79', 'date': '30 Oct 2017, 01:27'}, {'user_id': 'userid_1636', 'business_ref': 'businessref_9', 'date': '20 Feb 2017, 18:06'}, {'user_id': 'userid_711', 'business_ref': 'businessref_60', 'date': '2019-05-29 19:46:00'}], 'var_functions.query_db:12': [{'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.execute_python:14': {'total_reviews_processed': 44, 'top_5_categories': [{'category': 'Nail Salons', 'review_count': 3}, {'category': 'Hair Removal', 'review_count': 3}, {'category': 'Beauty & Spas', 'review_count': 3}, {'category': 'and Waxing', 'review_count': 3}, {'category': 'Internal Medicine', 'review_count': 1}]}, 'var_functions.query_db:16': [{'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.query_db:18': [{'user_id': 'userid_746'}, {'user_id': 'userid_1109'}, {'user_id': 'userid_1950'}, {'user_id': 'userid_1316'}, {'user_id': 'userid_1182'}, {'user_id': 'userid_151'}, {'user_id': 'userid_1158'}, {'user_id': 'userid_508'}, {'user_id': 'userid_435'}, {'user_id': 'userid_958'}, {'user_id': 'userid_1879'}, {'user_id': 'userid_308'}, {'user_id': 'userid_1179'}, {'user_id': 'userid_324'}, {'user_id': 'userid_863'}, {'user_id': 'userid_100'}, {'user_id': 'userid_1333'}, {'user_id': 'userid_1636'}, {'user_id': 'userid_1850'}, {'user_id': 'userid_711'}, {'user_id': 'userid_729'}, {'user_id': 'userid_1505'}, {'user_id': 'userid_1315'}, {'user_id': 'userid_1708'}, {'user_id': 'userid_1661'}, {'user_id': 'userid_850'}, {'user_id': 'userid_1675'}, {'user_id': 'userid_227'}, {'user_id': 'userid_577'}, {'user_id': 'userid_257'}, {'user_id': 'userid_598'}, {'user_id': 'userid_847'}, {'user_id': 'userid_673'}, {'user_id': 'userid_1856'}, {'user_id': 'userid_384'}, {'user_id': 'userid_935'}, {'user_id': 'userid_210'}, {'user_id': 'userid_1101'}, {'user_id': 'userid_945'}, {'user_id': 'userid_842'}, {'user_id': 'userid_1351'}, {'user_id': 'userid_230'}, {'user_id': 'userid_593'}, {'user_id': 'userid_1431'}, {'user_id': 'userid_686'}, {'user_id': 'userid_527'}, {'user_id': 'userid_244'}, {'user_id': 'userid_393'}, {'user_id': 'userid_1178'}, {'user_id': 'userid_526'}, {'user_id': 'userid_90'}, {'user_id': 'userid_238'}, {'user_id': 'userid_1105'}], 'var_functions.execute_python:20': {'total_reviews_processed': 44, 'unique_businesses_reviewed': 31, 'total_unique_categories': 7, 'top_5_categories': [{'category': 'Nail Salons', 'review_count': 3}, {'category': 'Hair Removal', 'review_count': 3}, {'category': 'Beauty & Spas', 'review_count': 3}, {'category': 'and Waxing', 'review_count': 3}, {'category': 'Internal Medicine', 'review_count': 1}]}, 'var_functions.execute_python:24': {'num_reviews': 44, 'num_businesses': 5, 'sample_reviews': [{'user_id': 'userid_1158', 'business_ref': 'businessref_8', 'date': '18 Oct 2016, 17:57'}, {'user_id': 'userid_1101', 'business_ref': 'businessref_74', 'date': '2021-07-16 17:24:00'}, {'user_id': 'userid_1105', 'business_ref': 'businessref_57', 'date': 'September 04, 2017 at 08:57 PM'}, {'user_id': 'userid_863', 'business_ref': 'businessref_96', 'date': 'August 06, 2016 at 02:19 AM'}, {'user_id': 'userid_308', 'business_ref': 'businessref_45', 'date': 'August 10, 2016 at 04:36 AM'}], 'sample_businesses': [{'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}]}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:28': {'total_reviews_processed': 44, 'reviews_by_year': {'2016': 11, '2021': 4, '2017': 12, '2019': 5, '2018': 9, '2020': 3}, 'unique_businesses_reviewed': 31, 'businesses_with_categories': 16, 'businesses_missing_categories': 15, 'total_unique_categories': 70, 'top_5_categories': [{'category': 'Shopping', 'review_count': 7}, {'category': 'Restaurants', 'review_count': 6}, {'category': 'Grocery', 'review_count': 6}, {'category': 'American (New)', 'review_count': 5}, {'category': 'Food', 'review_count': 5}]}, 'var_functions.query_db:30': [{'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'business_id': 'businessid_74', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}, {'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'business_id': 'businessid_10', 'description': "Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of 'Restaurants, Chinese'."}], 'var_functions.execute_python:32': {'unique_business_refs_count': 31, 'sample_business_refs': ['businessref_15', 'businessref_74', 'businessref_8', 'businessref_10', 'businessref_33', 'businessref_20', 'businessref_97', 'businessref_86', 'businessref_36', 'businessref_62']}}

exec(code, env_args)
