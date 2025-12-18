code = """import json

user_reviews_data = locals()['var_function-call-14289239004150381664']
business_refs = [record['business_ref'] for record in user_reviews_data]

business_ids = []
for ref in business_refs:
    # Remove 'businessref_' prefix and add 'businessid_'
    business_id = 'businessid_' + ref.replace('businessref_', '')
    business_ids.append(business_id)

unique_business_ids = list(set(business_ids))

# Construct the MongoDB query for the business collection
mongo_query = {
    "collection": "business",
    "filter": {"business_id": {"$in": unique_business_ids}},
    "projection": {"business_id": 1, "description": 1, "_id": 0}
}

print('__RESULT__:')
print(json.dumps(mongo_query))"""

env_args = {'var_function-call-6904946465687665496': [{'user_id': 'userid_746'}, {'user_id': 'userid_1109'}, {'user_id': 'userid_1950'}, {'user_id': 'userid_1316'}, {'user_id': 'userid_1182'}, {'user_id': 'userid_151'}, {'user_id': 'userid_1158'}, {'user_id': 'userid_508'}, {'user_id': 'userid_435'}, {'user_id': 'userid_958'}, {'user_id': 'userid_1879'}, {'user_id': 'userid_308'}, {'user_id': 'userid_1179'}, {'user_id': 'userid_324'}, {'user_id': 'userid_863'}, {'user_id': 'userid_100'}, {'user_id': 'userid_1333'}, {'user_id': 'userid_1636'}, {'user_id': 'userid_1850'}, {'user_id': 'userid_711'}, {'user_id': 'userid_729'}, {'user_id': 'userid_1505'}, {'user_id': 'userid_1315'}, {'user_id': 'userid_1708'}, {'user_id': 'userid_1661'}, {'user_id': 'userid_850'}, {'user_id': 'userid_1675'}, {'user_id': 'userid_227'}, {'user_id': 'userid_577'}, {'user_id': 'userid_257'}, {'user_id': 'userid_598'}, {'user_id': 'userid_847'}, {'user_id': 'userid_673'}, {'user_id': 'userid_1856'}, {'user_id': 'userid_384'}, {'user_id': 'userid_935'}, {'user_id': 'userid_210'}, {'user_id': 'userid_1101'}, {'user_id': 'userid_945'}, {'user_id': 'userid_842'}, {'user_id': 'userid_1351'}, {'user_id': 'userid_230'}, {'user_id': 'userid_593'}, {'user_id': 'userid_1431'}, {'user_id': 'userid_686'}, {'user_id': 'userid_527'}, {'user_id': 'userid_244'}, {'user_id': 'userid_393'}, {'user_id': 'userid_1178'}, {'user_id': 'userid_526'}, {'user_id': 'userid_90'}, {'user_id': 'userid_238'}, {'user_id': 'userid_1105'}], 'var_function-call-14289239004150381664': [{'business_ref': 'businessref_74', 'date': '2021-07-16 17:24:00'}, {'business_ref': 'businessref_57', 'date': 'September 04, 2017 at 08:57 PM'}, {'business_ref': 'businessref_96', 'date': 'August 06, 2016 at 02:19 AM'}, {'business_ref': 'businessref_45', 'date': 'August 10, 2016 at 04:36 AM'}, {'business_ref': 'businessref_74', 'date': 'April 17, 2016 at 12:00 AM'}, {'business_ref': 'businessref_53', 'date': '25 Nov 2016, 20:04'}, {'business_ref': 'businessref_41', 'date': 'December 12, 2017 at 02:27 AM'}, {'business_ref': 'businessref_96', 'date': '2017-01-06 11:15:06'}, {'business_ref': 'businessref_10', 'date': '2021-11-28 23:56:00'}, {'business_ref': 'businessref_66', 'date': 'November 10, 2021 at 06:40 AM'}, {'business_ref': 'businessref_31', 'date': '24 Jan 2017, 19:28'}, {'business_ref': 'businessref_92', 'date': '2019-11-14 17:06:00'}, {'business_ref': 'businessref_26', 'date': '2018-07-23 06:45:43'}, {'business_ref': 'businessref_98', 'date': '2017-11-17 16:06:00'}, {'business_ref': 'businessref_45', 'date': 'February 06, 2018 at 07:29 PM'}, {'business_ref': 'businessref_45', 'date': 'October 28, 2016 at 03:54 PM'}, {'business_ref': 'businessref_36', 'date': '2018-05-21 17:51:00'}, {'business_ref': 'businessref_14', 'date': 'May 04, 2017 at 11:25 PM'}, {'business_ref': 'businessref_86', 'date': '2019-04-14 23:08:41'}, {'business_ref': 'businessref_57', 'date': 'October 30, 2018 at 01:06 PM'}, {'business_ref': 'businessref_13', 'date': 'August 22, 2021 at 12:11 AM'}, {'business_ref': 'businessref_68', 'date': 'October 14, 2018 at 04:06 PM'}, {'business_ref': 'businessref_36', 'date': '2016-12-02 00:06:00'}, {'business_ref': 'businessref_60', 'date': '2017-03-24 23:59:00'}, {'business_ref': 'businessref_20', 'date': '27 May 2017, 00:50'}, {'business_ref': 'businessref_15', 'date': 'June 20, 2018 at 02:12 PM'}, {'business_ref': 'businessref_62', 'date': '2018-04-01 10:52:37'}, {'business_ref': 'businessref_33', 'date': 'August 18, 2016 at 11:57 AM'}, {'business_ref': 'businessref_37', 'date': '2016-07-24 20:27:00'}, {'business_ref': 'businessref_92', 'date': '30 Dec 2018, 18:49'}, {'business_ref': 'businessref_66', 'date': 'June 21, 2020 at 07:59 PM'}, {'business_ref': 'businessref_33', 'date': 'August 30, 2019 at 06:15 PM'}, {'business_ref': 'businessref_6', 'date': '30 Jun 2017, 04:44'}, {'business_ref': 'businessref_12', 'date': 'October 26, 2017 at 11:10 PM'}, {'business_ref': 'businessref_79', 'date': '30 Oct 2017, 01:27'}, {'business_ref': 'businessref_60', 'date': '2019-05-29 19:46:00'}]}

exec(code, env_args)
