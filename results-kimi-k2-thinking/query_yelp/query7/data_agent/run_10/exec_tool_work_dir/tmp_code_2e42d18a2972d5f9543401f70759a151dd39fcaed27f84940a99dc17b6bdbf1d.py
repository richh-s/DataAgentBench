code = """import json
import re

# Load data from storage
reviews_file = locals()['var_functions.query_db:14']
business_file = locals()['var_functions.query_db:20']

with open(reviews_file, 'r') as f:
    reviews_data = json.load(f)

with open(business_file, 'r') as f:
    business_data = json.load(f)

print('Original data loaded:')
print(f'Reviews: {len(reviews_data)}')
print(f'Businesses: {len(business_data)}')

# Extract business_id from business_ref (remove 'businessref_' prefix and convert to int)
for review in reviews_data:
    if 'business_ref' in review and review['business_ref']:
        ref_id = review['business_ref'].replace('businessref_', '')
        try:
            review['business_num_id'] = int(ref_id)
        except ValueError:
            review['business_num_id'] = None
    else:
        review['business_num_id'] = None

# Extract business_id from business_id (remove 'businessid_' prefix and convert to int)
for business in business_data:
    if 'business_id' in business and business['business_id']:
        bus_id = business['business_id'].replace('businessid_', '')
        try:
            business['business_num_id'] = int(bus_id)
        except ValueError:
            business['business_num_id'] = None
    else:
        business['business_num_id'] = None

# Create mapping from business_num_id to description
business_map = {}
for business in business_data:
    if business.get('business_num_id') is not None:
        business_map[business['business_num_id']] = business.get('description', '')

# Function to extract categories from description
def extract_categories(description):
    if not description:
        return []
    
    # Look for patterns like "in the categories of X, Y, and Z"
    # or "providing services in X, Y, Z"
    # or ending with "... X, Y, and Z."
    
    categories = []
    
    # Pattern 1: ending with "X, Y, and Z." or similar
    desc_end = description.split('.')[-2] if len(description.split('.')) > 1 else description
    
    # Pattern 2: "services in [categories]"
    services_match = re.search(r'services in ([^.]+)', description, re.IGNORECASE)
    if services_match:
        cat_text = services_match.group(1)
        # Split by comma and 'and'
        parts = re.split(r',|\sand\s', cat_text)
        for part in parts:
            part = part.strip()
            if part and len(part) < 50:  # Avoid long fragments
                categories.append(part)
    
    # Pattern 3: "categories of [categories]"
    categories_match = re.search(r'categories of ([^.]+)', description, re.IGNORECASE)
    if categories_match:
        cat_text = categories_match.group(1)
        parts = re.split(r',|\sand\s', cat_text)
        for part in parts:
            part = part.strip()
            if part and len(part) < 50:
                categories.append(part)
    
    # Pattern 4: ending enumeration
    # Find patterns like "X, Y, and Z" at the end
    end_match = re.search(r'([A-Z][a-z\s\&\-]+),\s([A-Z][a-z\s\&\-]+)(?:,\s)?(?:and\s)?([A-Z][a-z\s\&\-]+)?\.?$', desc_end)
    if end_match and not categories:  # Only if we didn't find categories yet
        for group in end_match.groups():
            if group and len(group.strip()) < 50:
                categories.append(group.strip())
    
    # Clean up categories
    cleaned = []
    for cat in categories:
        # Remove "making it a go-to destination for" etc.
        cat = re.sub(r'^.*?(?:for|in|including)\s+', '', cat, flags=re.IGNORECASE)
        # Remove trailing "enthusiasts" etc.
        cat = re.sub(r'\s+(?:enthusiasts|perfect for|making it a|to meet all your|for all your).*$', '', cat, flags=re.IGNORECASE)
        cat = cat.strip()
        if cat and cat not in ['Food', 'Restaurants']:  # Too generic
            cleaned.append(cat)
    
    return cleaned if cleaned else []

# Process each review and extract categories
category_review_counts = {}

for review in reviews_data:
    business_num_id = review.get('business_num_id')
    if not business_num_id:
        continue
    
    description = business_map.get(business_num_id, '')
    categories = extract_categories(description)
    
    if not categories:
        # Fallback: try to extract single main category from start of description
        if description:
            # Look for first comma-separated item or category
            first_cat = description.split(',')[0].strip()
            if len(first_cat) < 50:
                categories = [first_cat]
    
    for category in categories:
        category_review_counts[category] = category_review_counts.get(category, 0) + 1

# Sort by review count
sorted_categories = sorted(category_review_counts.items(), key=lambda x: x[1], reverse=True)

top_5 = sorted_categories[:5]

result = {
    'total_reviews_processed': len(reviews_data),
    'unique_businesses_reviewed': len(set(r.get('business_ref') for r in reviews_data if r.get('business_ref'))),
    'top_5_categories': top_5
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['business', 'checkin'], 'var_functions.query_db:2': [{'user_id': 'userid_286', 'name': 'Todd', 'review_count': '376', 'yelping_since': '15 Jan 2009, 16:40', 'useful': '1373', 'funny': '723', 'cool': '639', 'elite': '2010,2011,2012,2013,2014'}], 'var_functions.query_db:5': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}], 'var_functions.query_db:8': [{'user_id': 'userid_286', 'yelping_since': '15 Jan 2009, 16:40'}, {'user_id': 'userid_1331', 'yelping_since': '13 Jul 2010, 15:42'}, {'user_id': 'userid_1880', 'yelping_since': '2010-09-07 23:24:36'}, {'user_id': 'userid_271', 'yelping_since': 'October 23, 2011 at 07:47 PM'}, {'user_id': 'userid_534', 'yelping_since': '2011-08-30 13:46:26'}, {'user_id': 'userid_1997', 'yelping_since': '2009-12-02 18:54:31'}, {'user_id': 'userid_1386', 'yelping_since': '2009-04-15 12:46:06'}, {'user_id': 'userid_237', 'yelping_since': 'October 04, 2009 at 05:59 PM'}, {'user_id': 'userid_596', 'yelping_since': '20 Apr 2008, 16:55'}, {'user_id': 'userid_948', 'yelping_since': '2007-07-28 22:22:09'}], 'var_functions.query_db:10': [{'user_id': 'userid_1231', 'yelping_since': '14 Sep 2016, 00:32'}, {'user_id': 'userid_343', 'yelping_since': '02 Feb 2016, 04:30'}, {'user_id': 'userid_746', 'yelping_since': '2016-06-23 01:59:28'}, {'user_id': 'userid_505', 'yelping_since': 'September 10, 2016 at 08:02 PM'}, {'user_id': 'userid_898', 'yelping_since': 'January 15, 2016 at 06:33 PM'}, {'user_id': 'userid_144', 'yelping_since': '25 Feb 2016, 04:52'}, {'user_id': 'userid_1927', 'yelping_since': 'October 13, 2016 at 04:29 AM'}, {'user_id': 'userid_1109', 'yelping_since': '2016-10-16 18:32:25'}, {'user_id': 'userid_1950', 'yelping_since': '2016-04-16 03:42:28'}, {'user_id': 'userid_1316', 'yelping_since': '2016-12-29 21:32:44'}], 'var_functions.query_db:12': [{'user_id': 'userid_1231'}, {'user_id': 'userid_343'}, {'user_id': 'userid_746'}, {'user_id': 'userid_505'}, {'user_id': 'userid_898'}, {'user_id': 'userid_144'}, {'user_id': 'userid_1927'}, {'user_id': 'userid_1109'}, {'user_id': 'userid_1950'}, {'user_id': 'userid_1316'}, {'user_id': 'userid_805'}, {'user_id': 'userid_1182'}, {'user_id': 'userid_431'}, {'user_id': 'userid_1287'}, {'user_id': 'userid_151'}, {'user_id': 'userid_1274'}, {'user_id': 'userid_1158'}, {'user_id': 'userid_643'}, {'user_id': 'userid_1558'}, {'user_id': 'userid_1542'}, {'user_id': 'userid_508'}, {'user_id': 'userid_435'}, {'user_id': 'userid_1398'}, {'user_id': 'userid_958'}, {'user_id': 'userid_68'}, {'user_id': 'userid_145'}, {'user_id': 'userid_518'}, {'user_id': 'userid_1879'}, {'user_id': 'userid_1981'}, {'user_id': 'userid_64'}, {'user_id': 'userid_211'}, {'user_id': 'userid_308'}, {'user_id': 'userid_1444'}, {'user_id': 'userid_1179'}, {'user_id': 'userid_677'}, {'user_id': 'userid_537'}, {'user_id': 'userid_208'}, {'user_id': 'userid_1397'}, {'user_id': 'userid_324'}, {'user_id': 'userid_795'}, {'user_id': 'userid_863'}, {'user_id': 'userid_100'}, {'user_id': 'userid_1333'}, {'user_id': 'userid_1636'}, {'user_id': 'userid_38'}, {'user_id': 'userid_1850'}, {'user_id': 'userid_401'}, {'user_id': 'userid_711'}, {'user_id': 'userid_729'}, {'user_id': 'userid_1505'}, {'user_id': 'userid_374'}, {'user_id': 'userid_1315'}, {'user_id': 'userid_597'}, {'user_id': 'userid_386'}, {'user_id': 'userid_1978'}, {'user_id': 'userid_862'}, {'user_id': 'userid_1068'}, {'user_id': 'userid_1708'}, {'user_id': 'userid_522'}, {'user_id': 'userid_1246'}, {'user_id': 'userid_339'}, {'user_id': 'userid_1786'}, {'user_id': 'userid_1661'}, {'user_id': 'userid_152'}, {'user_id': 'userid_1376'}, {'user_id': 'userid_851'}, {'user_id': 'userid_1940'}, {'user_id': 'userid_216'}, {'user_id': 'userid_39'}, {'user_id': 'userid_850'}, {'user_id': 'userid_1419'}, {'user_id': 'userid_425'}, {'user_id': 'userid_582'}, {'user_id': 'userid_333'}, {'user_id': 'userid_1288'}, {'user_id': 'userid_252'}, {'user_id': 'userid_676'}, {'user_id': 'userid_361'}, {'user_id': 'userid_1675'}, {'user_id': 'userid_1490'}, {'user_id': 'userid_123'}, {'user_id': 'userid_227'}, {'user_id': 'userid_510'}, {'user_id': 'userid_577'}, {'user_id': 'userid_242'}, {'user_id': 'userid_771'}, {'user_id': 'userid_1350'}, {'user_id': 'userid_1077'}, {'user_id': 'userid_1013'}, {'user_id': 'userid_1030'}, {'user_id': 'userid_1902'}, {'user_id': 'userid_367'}, {'user_id': 'userid_257'}, {'user_id': 'userid_598'}, {'user_id': 'userid_847'}, {'user_id': 'userid_1343'}, {'user_id': 'userid_792'}, {'user_id': 'userid_673'}, {'user_id': 'userid_243'}, {'user_id': 'userid_1072'}, {'user_id': 'userid_369'}, {'user_id': 'userid_622'}, {'user_id': 'userid_1758'}, {'user_id': 'userid_1856'}, {'user_id': 'userid_384'}, {'user_id': 'userid_1533'}, {'user_id': 'userid_1736'}, {'user_id': 'userid_1161'}, {'user_id': 'userid_359'}, {'user_id': 'userid_318'}, {'user_id': 'userid_1871'}, {'user_id': 'userid_655'}, {'user_id': 'userid_108'}, {'user_id': 'userid_131'}, {'user_id': 'userid_1760'}, {'user_id': 'userid_935'}, {'user_id': 'userid_1139'}, {'user_id': 'userid_210'}, {'user_id': 'userid_70'}, {'user_id': 'userid_25'}, {'user_id': 'userid_1101'}, {'user_id': 'userid_97'}, {'user_id': 'userid_1624'}, {'user_id': 'userid_1739'}, {'user_id': 'userid_942'}, {'user_id': 'userid_945'}, {'user_id': 'userid_842'}, {'user_id': 'userid_986'}, {'user_id': 'userid_1717'}, {'user_id': 'userid_1351'}, {'user_id': 'userid_406'}, {'user_id': 'userid_230'}, {'user_id': 'userid_914'}, {'user_id': 'userid_593'}, {'user_id': 'userid_1083'}, {'user_id': 'userid_742'}, {'user_id': 'userid_1938'}, {'user_id': 'userid_356'}, {'user_id': 'userid_876'}, {'user_id': 'userid_1431'}, {'user_id': 'userid_424'}, {'user_id': 'userid_686'}, {'user_id': 'userid_527'}, {'user_id': 'userid_641'}, {'user_id': 'userid_1346'}, {'user_id': 'userid_1766'}, {'user_id': 'userid_207'}, {'user_id': 'userid_1070'}, {'user_id': 'userid_989'}, {'user_id': 'userid_927'}, {'user_id': 'userid_244'}, {'user_id': 'userid_1816'}, {'user_id': 'userid_1756'}, {'user_id': 'userid_393'}, {'user_id': 'userid_1409'}, {'user_id': 'userid_197'}, {'user_id': 'userid_1178'}, {'user_id': 'userid_526'}, {'user_id': 'userid_90'}, {'user_id': 'userid_661'}, {'user_id': 'userid_238'}, {'user_id': 'userid_1897'}, {'user_id': 'userid_241'}, {'user_id': 'userid_1262'}, {'user_id': 'userid_1727'}, {'user_id': 'userid_1105'}, {'user_id': 'userid_744'}, {'user_id': 'userid_1263'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:18': {'total_reviews': 150, 'sample_reviews': [{'review_id': 'reviewid_1264', 'user_id': 'userid_655', 'business_ref': 'businessref_36', 'date': '22 Oct 2021, 21:44'}, {'review_id': 'reviewid_814', 'user_id': 'userid_582', 'business_ref': 'businessref_79', 'date': '17 Jul 2020, 20:30'}, {'review_id': 'reviewid_459', 'user_id': 'userid_1397', 'business_ref': 'businessref_23', 'date': '2016-06-28 02:18:33'}, {'review_id': 'reviewid_756', 'user_id': 'userid_1274', 'business_ref': 'businessref_67', 'date': '2018-01-02 21:35:31'}, {'review_id': 'reviewid_1500', 'user_id': 'userid_1030', 'business_ref': 'businessref_37', 'date': '28 Sep 2016, 17:19'}], 'unique_business_refs': 62}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
