code = """import pandas as pd
import json

users_2016 = locals()['var_function-call-11278366116780345626']
reviews_data = pd.read_json(locals()['var_function-call-15994286323775235926'])

def parse_review_date(date_str):
    if isinstance(date_str, list):
        date_str = date_str[0] # Assuming only one date per review
    if 'at' in date_str:
        return pd.to_datetime(date_str, format='%B %d, %Y at %I:%M %p', errors='coerce')
    elif ',' in date_str:
        return pd.to_datetime(date_str, format='%d %b %Y, %H:%M', errors='coerce')
    else:
        return pd.to_datetime(date_str, errors='coerce')

reviews_data['date_parsed'] = reviews_data['date'].apply(parse_review_date)

# Filter reviews by users registered in 2016 and review date in or after 2016
filtered_reviews = reviews_data[
    (reviews_data['user_id'].isin(users_2016)) & 
    (reviews_data['date_parsed'].dt.year >= 2016)
]

# Extract unique business_ref IDs from filtered reviews
business_refs = filtered_reviews['business_ref'].str.replace('businessref_', 'businessid_').unique().tolist()

print('__RESULT__:')
print(json.dumps(business_refs))"""

env_args = {'var_function-call-13108768714940623492': [{'_id': '6859a000fe8b31cd7362e2ab', 'name': 'Steps to Learning Montessori Preschool', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-8905274414612016032': [{'yelping_since': '15 Jan 2009, 16:40'}], 'var_function-call-16896666519348856818': 'file_storage/function-call-16896666519348856818.json', 'var_function-call-11278366116780345626': ['userid_1231', 'userid_343', 'userid_746', 'userid_505', 'userid_898', 'userid_144', 'userid_1927', 'userid_1109', 'userid_1950', 'userid_1316', 'userid_805', 'userid_1182', 'userid_431', 'userid_1287', 'userid_151', 'userid_1274', 'userid_1158', 'userid_643', 'userid_1558', 'userid_1542', 'userid_508', 'userid_435', 'userid_1398', 'userid_958', 'userid_68', 'userid_145', 'userid_518', 'userid_1879', 'userid_1981', 'userid_64', 'userid_211', 'userid_308', 'userid_1444', 'userid_1179', 'userid_677', 'userid_537', 'userid_208', 'userid_1397', 'userid_324', 'userid_795', 'userid_863', 'userid_100', 'userid_1333', 'userid_1636', 'userid_38', 'userid_1850', 'userid_401', 'userid_711', 'userid_729', 'userid_1505', 'userid_374', 'userid_1315', 'userid_597', 'userid_386', 'userid_1978', 'userid_862', 'userid_1068', 'userid_1708', 'userid_522', 'userid_1246', 'userid_339', 'userid_1786', 'userid_1661', 'userid_152', 'userid_1376', 'userid_851', 'userid_1940', 'userid_216', 'userid_39', 'userid_850', 'userid_1419', 'userid_425', 'userid_582', 'userid_333', 'userid_1288', 'userid_252', 'userid_676', 'userid_361', 'userid_1675', 'userid_1490', 'userid_123', 'userid_227', 'userid_510', 'userid_577', 'userid_242', 'userid_771', 'userid_1350', 'userid_1077', 'userid_1013', 'userid_1030', 'userid_1902', 'userid_367', 'userid_257', 'userid_598', 'userid_847', 'userid_1343', 'userid_792', 'userid_673', 'userid_243', 'userid_1072', 'userid_369', 'userid_622', 'userid_1758', 'userid_1856', 'userid_384', 'userid_1533', 'userid_1736', 'userid_1161', 'userid_359', 'userid_318', 'userid_1871', 'userid_655', 'userid_108', 'userid_131', 'userid_1760', 'userid_935', 'userid_1139', 'userid_210', 'userid_70', 'userid_25', 'userid_1101', 'userid_97', 'userid_1624', 'userid_1739', 'userid_942', 'userid_945', 'userid_842', 'userid_986', 'userid_1717', 'userid_1351', 'userid_406', 'userid_230', 'userid_914', 'userid_593', 'userid_1083', 'userid_742', 'userid_1938', 'userid_356', 'userid_876', 'userid_1431', 'userid_424', 'userid_686', 'userid_527', 'userid_641', 'userid_1346', 'userid_1766', 'userid_207', 'userid_1070', 'userid_989', 'userid_927', 'userid_244', 'userid_1816', 'userid_1756', 'userid_393', 'userid_1409', 'userid_197', 'userid_1178', 'userid_526', 'userid_90', 'userid_661', 'userid_238', 'userid_1897', 'userid_241', 'userid_1262', 'userid_1727', 'userid_1105', 'userid_744', 'userid_1263'], 'var_function-call-15994286323775235926': 'file_storage/function-call-15994286323775235926.json'}

exec(code, env_args)
