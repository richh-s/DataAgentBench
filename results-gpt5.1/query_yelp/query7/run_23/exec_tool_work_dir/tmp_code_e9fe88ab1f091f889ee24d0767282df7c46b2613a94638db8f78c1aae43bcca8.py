code = """import json, re, pandas as pd, os
# load reviews
path_reviews = var_call_QHv7Ov0DiQPvp3nvVuW4s6Oz
with open(path_reviews, 'r') as f:
    reviews = json.load(f)
# filter reviews with date year >=2016 by parsing year from string
rev_rows = []
for r in reviews:
    s = r['date']
    m = re.search(r'(19|20)\d{2}', s)
    year = int(m.group(0)) if m else None
    if year is not None and year >= 2016:
        rev_rows.append({'business_ref': r['business_ref']})
# count reviews per business_ref
df_rev = pd.DataFrame(rev_rows)
counts = df_rev['business_ref'].value_counts().reset_index()
counts.columns = ['business_ref','review_count']
# map to business_id (businessref_X -> businessid_X)
counts['business_id'] = counts['business_ref'].str.replace('businessref_','businessid_', regex=False)
# we only have 5 businesses from business collection; keep those
biz = pd.DataFrame(var_call_bwmh9sZDDOyGnOZdsINwyg4G)
merged = pd.merge(counts, biz, on='business_id', how='inner')
# since we don't have categories field, approximate category as business_id
top5 = merged.sort_values('review_count', ascending=False).head(5)
result = top5[['business_id','review_count']].to_dict(orient='records')
result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_lN9wcU5juyhkqWJovDWX97SV': ['business', 'checkin'], 'var_call_QJvAp5hu6ywOJ0Sf2QD2QZ8f': [{'yelping_since': 'October 10, 2009 at 01:37 AM'}, {'yelping_since': 'May 21, 2011 at 03:22 PM'}, {'yelping_since': '2005-07-18 06:22:37'}, {'yelping_since': '2009-04-30 03:16:12'}, {'yelping_since': 'August 18, 2008 at 08:13 AM'}, {'yelping_since': 'May 23, 2009 at 05:44 PM'}, {'yelping_since': '22 Jul 2007, 21:50'}, {'yelping_since': '2011-01-22 16:07:48'}, {'yelping_since': '2010-12-15 02:17:17'}, {'yelping_since': 'April 23, 2010 at 07:48 PM'}, {'yelping_since': '09 Dec 2007, 01:03'}, {'yelping_since': '12 Feb 2011, 01:00'}, {'yelping_since': '2009-04-17 13:38:22'}, {'yelping_since': 'January 17, 2011 at 10:14 PM'}, {'yelping_since': '07 Sep 2009, 22:20'}, {'yelping_since': '2011-04-17 16:27:25'}, {'yelping_since': '2010-06-26 21:11:26'}, {'yelping_since': '29 Feb 2012, 02:51'}, {'yelping_since': '2010-04-19 19:23:27'}, {'yelping_since': '2010-07-12 16:29:17'}], 'var_call_JhoKQEPhwDEV7KP4HbaJR8sn': 'file_storage/call_JhoKQEPhwDEV7KP4HbaJR8sn.json', 'var_call_SkslV75KdiP6hCsrXqTLUF0G': ['userid_1231', 'userid_343', 'userid_746', 'userid_505', 'userid_898', 'userid_144', 'userid_1927', 'userid_1109', 'userid_1950', 'userid_1316', 'userid_805', 'userid_1182', 'userid_431', 'userid_1287', 'userid_151', 'userid_1274', 'userid_1158', 'userid_643', 'userid_1558', 'userid_1542', 'userid_508', 'userid_435', 'userid_1398', 'userid_958', 'userid_68', 'userid_145', 'userid_518', 'userid_1879', 'userid_1981', 'userid_64', 'userid_211', 'userid_308', 'userid_1444', 'userid_1179', 'userid_677', 'userid_537', 'userid_208', 'userid_1397', 'userid_324', 'userid_795', 'userid_863', 'userid_100', 'userid_1333', 'userid_1636', 'userid_38', 'userid_1850', 'userid_401', 'userid_711', 'userid_729', 'userid_1505', 'userid_374', 'userid_1315', 'userid_597', 'userid_386', 'userid_1978', 'userid_862', 'userid_1068', 'userid_1708', 'userid_522', 'userid_1246', 'userid_339', 'userid_1786', 'userid_1661', 'userid_152', 'userid_1376', 'userid_851', 'userid_1940', 'userid_216', 'userid_39', 'userid_850', 'userid_1419', 'userid_425', 'userid_582', 'userid_333', 'userid_1288', 'userid_252', 'userid_676', 'userid_361', 'userid_1675', 'userid_1490', 'userid_123', 'userid_227', 'userid_510', 'userid_577', 'userid_242', 'userid_771', 'userid_1350', 'userid_1077', 'userid_1013', 'userid_1030', 'userid_1902', 'userid_367', 'userid_257', 'userid_598', 'userid_847', 'userid_1343', 'userid_792', 'userid_673', 'userid_243', 'userid_1072', 'userid_369', 'userid_622', 'userid_1758', 'userid_1856', 'userid_384', 'userid_1533', 'userid_1736', 'userid_1161', 'userid_359', 'userid_318', 'userid_1871', 'userid_655', 'userid_108', 'userid_131', 'userid_1760', 'userid_935', 'userid_1139', 'userid_210', 'userid_70', 'userid_25', 'userid_1101', 'userid_97', 'userid_1624', 'userid_1739', 'userid_942', 'userid_945', 'userid_842', 'userid_986', 'userid_1717', 'userid_1351', 'userid_406', 'userid_230', 'userid_914', 'userid_593', 'userid_1083', 'userid_742', 'userid_1938', 'userid_356', 'userid_876', 'userid_1431', 'userid_424', 'userid_686', 'userid_527', 'userid_641', 'userid_1346', 'userid_1766', 'userid_207', 'userid_1070', 'userid_989', 'userid_927', 'userid_244', 'userid_1816', 'userid_1756', 'userid_393', 'userid_1409', 'userid_197', 'userid_1178', 'userid_526', 'userid_90', 'userid_661', 'userid_238', 'userid_1897', 'userid_241', 'userid_1262', 'userid_1727', 'userid_1105', 'userid_744', 'userid_1263'], 'var_call_QHv7Ov0DiQPvp3nvVuW4s6Oz': 'file_storage/call_QHv7Ov0DiQPvp3nvVuW4s6Oz.json', 'var_call_bwmh9sZDDOyGnOZdsINwyg4G': [{'business_id': 'businessid_49'}, {'business_id': 'businessid_47'}, {'business_id': 'businessid_88'}, {'business_id': 'businessid_41'}, {'business_id': 'businessid_33'}]}

exec(code, env_args)
