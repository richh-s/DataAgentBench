code = """import json
import re

# Get business data
business_result = locals()['var_functions.query_db:8']

# Check if it's a file path or array
business_data = []
if isinstance(business_result, str) and business_result.endswith('.json'):
    with open(business_result, 'r') as f:
        business_data = json.load(f)
else:
    business_data = business_result

# Extract categories from description
business_categories = []
for biz in business_data:
    desc = biz.get('description', '')
    # Find text after "services in" or similar patterns and before period
    services_text = desc
    if 'services in' in desc:
        services_text = desc.split('services in')[1]
    elif 'services including' in desc:
        services_text = desc.split('services including')[1]
    elif 'offers' in desc and 'a range of' in desc:
        services_text = desc.split('a range of')[1]
    
    # Extract categories (comma-separated or 'and' separated)
    categories = []
    # Look for categories pattern: words separated by commas or 'and'
    # Try to find the part that's likely a list of categories
    match = re.search(r'(Education|Elementary Schools|Hair Salons|Beauty & Spas|Active Life|Health & Medical|Nail Salons|Doctors|Restaurants|Food|Shopping|Local Services|Nightlife|Bars)', services_text)
    if match:
        # For now, let's just extract the first category found
        # We'll improve this logic
        pass

print('__RESULT__:')
print(json.dumps({
    'business_records': len(business_data),
    'sample_business': business_data[0] if business_data else None
}))"""

env_args = {'var_functions.list_db:0': ['business', 'checkin'], 'var_functions.query_db:2': [{'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.query_db:4': [{'user_id': 'userid_746', 'yelping_since': '2016-06-23 01:59:28'}, {'user_id': 'userid_1109', 'yelping_since': '2016-10-16 18:32:25'}, {'user_id': 'userid_1950', 'yelping_since': '2016-04-16 03:42:28'}, {'user_id': 'userid_1316', 'yelping_since': '2016-12-29 21:32:44'}, {'user_id': 'userid_1182', 'yelping_since': '2016-03-20 18:41:14'}, {'user_id': 'userid_151', 'yelping_since': '2016-11-07 18:40:10'}, {'user_id': 'userid_1158', 'yelping_since': '2016-01-31 16:25:04'}, {'user_id': 'userid_508', 'yelping_since': '2016-07-08 22:37:42'}, {'user_id': 'userid_435', 'yelping_since': '2016-10-31 09:46:54'}, {'user_id': 'userid_958', 'yelping_since': '2016-03-23 20:55:45'}, {'user_id': 'userid_1879', 'yelping_since': '2016-07-08 17:56:11'}, {'user_id': 'userid_308', 'yelping_since': '2016-07-02 23:48:36'}, {'user_id': 'userid_1179', 'yelping_since': '2016-12-18 17:31:52'}, {'user_id': 'userid_324', 'yelping_since': '2016-10-10 22:09:08'}, {'user_id': 'userid_863', 'yelping_since': '2016-01-16 00:45:41'}, {'user_id': 'userid_100', 'yelping_since': '2016-08-18 11:39:42'}, {'user_id': 'userid_1333', 'yelping_since': '2016-12-07 14:57:41'}, {'user_id': 'userid_1636', 'yelping_since': '2016-02-14 23:51:28'}, {'user_id': 'userid_1850', 'yelping_since': '2016-07-22 19:26:01'}, {'user_id': 'userid_711', 'yelping_since': '2016-07-07 22:59:48'}, {'user_id': 'userid_729', 'yelping_since': '2016-02-06 00:41:18'}, {'user_id': 'userid_1505', 'yelping_since': '2016-07-14 00:26:46'}, {'user_id': 'userid_1315', 'yelping_since': '2016-03-07 02:47:32'}, {'user_id': 'userid_1708', 'yelping_since': '2016-03-06 20:06:53'}, {'user_id': 'userid_1661', 'yelping_since': '2016-06-13 00:48:17'}, {'user_id': 'userid_850', 'yelping_since': '2016-04-05 22:20:15'}, {'user_id': 'userid_1675', 'yelping_since': '2016-02-13 20:18:19'}, {'user_id': 'userid_227', 'yelping_since': '2016-01-16 01:12:00'}, {'user_id': 'userid_577', 'yelping_since': '2016-08-05 21:32:23'}, {'user_id': 'userid_257', 'yelping_since': '2016-10-19 21:58:32'}, {'user_id': 'userid_598', 'yelping_since': '2016-07-24 20:27:40'}, {'user_id': 'userid_847', 'yelping_since': '2016-08-04 20:28:55'}, {'user_id': 'userid_673', 'yelping_since': '2016-09-29 14:11:39'}, {'user_id': 'userid_1856', 'yelping_since': '2016-11-19 23:19:11'}, {'user_id': 'userid_384', 'yelping_since': '2016-04-21 20:00:19'}, {'user_id': 'userid_935', 'yelping_since': '2016-03-04 03:53:07'}, {'user_id': 'userid_210', 'yelping_since': '2016-06-24 03:16:47'}, {'user_id': 'userid_1101', 'yelping_since': '2016-06-13 19:58:37'}, {'user_id': 'userid_945', 'yelping_since': '2016-05-08 04:31:48'}, {'user_id': 'userid_842', 'yelping_since': '2016-02-21 19:02:44'}, {'user_id': 'userid_1351', 'yelping_since': '2016-03-30 02:56:55'}, {'user_id': 'userid_230', 'yelping_since': '2016-09-28 21:47:27'}, {'user_id': 'userid_593', 'yelping_since': '2016-11-18 05:33:16'}, {'user_id': 'userid_1431', 'yelping_since': '2016-01-06 23:48:07'}, {'user_id': 'userid_686', 'yelping_since': '2016-02-20 02:24:38'}, {'user_id': 'userid_527', 'yelping_since': '2016-06-26 04:19:08'}, {'user_id': 'userid_244', 'yelping_since': '2016-02-06 05:06:29'}, {'user_id': 'userid_393', 'yelping_since': '2016-08-16 18:42:51'}, {'user_id': 'userid_1178', 'yelping_since': '2016-05-05 18:04:24'}, {'user_id': 'userid_526', 'yelping_since': '2016-12-16 00:17:31'}, {'user_id': 'userid_90', 'yelping_since': '2016-07-14 00:52:49'}, {'user_id': 'userid_238', 'yelping_since': '2016-12-29 01:41:33'}, {'user_id': 'userid_1105', 'yelping_since': '2016-03-15 21:53:34'}], 'var_functions.query_db:6': [{'review_id': 'reviewid_318', 'user_id': 'userid_1101', 'business_ref': 'businessref_74', 'date': '2021-07-16 17:24:00'}, {'review_id': 'reviewid_1049', 'user_id': 'userid_1105', 'business_ref': 'businessref_57', 'date': 'September 04, 2017 at 08:57 PM'}, {'review_id': 'reviewid_454', 'user_id': 'userid_863', 'business_ref': 'businessref_96', 'date': 'August 06, 2016 at 02:19 AM'}, {'review_id': 'reviewid_1065', 'user_id': 'userid_308', 'business_ref': 'businessref_45', 'date': 'August 10, 2016 at 04:36 AM'}, {'review_id': 'reviewid_704', 'user_id': 'userid_729', 'business_ref': 'businessref_74', 'date': 'April 17, 2016 at 12:00 AM'}], 'var_functions.query_db:8': [{'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.execute_python:14': {'total_users_2016': 53, 'sample_users': ['userid_746', 'userid_1109', 'userid_1950', 'userid_1316', 'userid_1182']}}

exec(code, env_args)
