code = """import json, pandas as pd

reviews = pd.DataFrame(var_call_YZU6UuP2rhi0g9itAKUQBxmy)

import pathlib, json as jsonlib
path = pathlib.Path(var_call_ZwXCsg6Y1aTgncyAMM2Y1R4H)
with path.open() as f:
    business_data = jsonlib.load(f)

biz = pd.DataFrame(business_data)

reviews['business_id'] = reviews['business_ref'].str.replace('businessref_', 'businessid_', regex=False)

import re

def extract_categories(desc):
    if not isinstance(desc, str):
        return []
    m = re.search(r"offers(?:[^.]*?) (.+)", desc)
    if not m:
        return []
    cats_part = m.group(1)
    cats_part = cats_part.split('.')[0]
    parts = [c.strip(" '|") for c in cats_part.split(',')]
    return [p for p in parts if p]

biz['categories'] = biz['description'].apply(extract_categories)

biz_exploded = biz.explode('categories')

merged = reviews.merge(biz_exploded[['business_id','categories']], on='business_id', how='left')

merged['review_count'] = merged['review_count'].astype(int)

cat_counts = merged.groupby('categories', dropna=True)['review_count'].sum().reset_index()

cat_counts = cat_counts[cat_counts['categories'].notna()]

top5 = cat_counts.sort_values('review_count', ascending=False).head(5)

result = top5.to_dict(orient='records')

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_OaUvmllcUAVdb8Ajjw1rkNqy': ['checkin', 'business'], 'var_call_WYNMYWUsrZRFmyV5clsVv8zM': [{'user_id': 'userid_237', 'yelping_since': 'October 04, 2009 at 05:59 PM'}, {'user_id': 'userid_995', 'yelping_since': '2010-04-29 14:32:53'}, {'user_id': 'userid_1465', 'yelping_since': 'June 13, 2008 at 08:02 PM'}, {'user_id': 'userid_12', 'yelping_since': '2011-02-16 02:36:34'}, {'user_id': 'userid_1576', 'yelping_since': '13 May 2011, 01:49'}, {'user_id': 'userid_163', 'yelping_since': 'April 23, 2010 at 07:48 PM'}, {'user_id': 'userid_1271', 'yelping_since': 'November 01, 2010 at 02:19 PM'}, {'user_id': 'userid_754', 'yelping_since': '2010-12-14 20:24:07'}, {'user_id': 'userid_1400', 'yelping_since': '2011-05-30 01:29:42'}, {'user_id': 'userid_346', 'yelping_since': '2009-04-23 15:50:07'}, {'user_id': 'userid_33', 'yelping_since': 'August 10, 2010 at 03:55 PM'}, {'user_id': 'userid_1921', 'yelping_since': '08 Oct 2011, 00:36'}, {'user_id': 'userid_1193', 'yelping_since': 'September 16, 2010 at 02:28 AM'}, {'user_id': 'userid_442', 'yelping_since': '2011-04-17 16:27:25'}, {'user_id': 'userid_558', 'yelping_since': '2010-10-25 17:25:22'}, {'user_id': 'userid_1835', 'yelping_since': '2007-06-06 18:24:15'}, {'user_id': 'userid_115', 'yelping_since': '28 Mar 2010, 23:26'}, {'user_id': 'userid_486', 'yelping_since': 'February 04, 2012 at 03:41 AM'}, {'user_id': 'userid_1979', 'yelping_since': '13 Dec 2011, 21:29'}, {'user_id': 'userid_720', 'yelping_since': '2010-11-25 19:00:56'}], 'var_call_mKpIdwAMO8sYNTO7vMcK3Ioa': [{'user_id': 'userid_746'}, {'user_id': 'userid_505'}, {'user_id': 'userid_898'}, {'user_id': 'userid_1927'}, {'user_id': 'userid_1109'}, {'user_id': 'userid_1950'}, {'user_id': 'userid_1316'}, {'user_id': 'userid_1182'}, {'user_id': 'userid_431'}, {'user_id': 'userid_1287'}, {'user_id': 'userid_151'}, {'user_id': 'userid_1158'}, {'user_id': 'userid_508'}, {'user_id': 'userid_435'}, {'user_id': 'userid_958'}, {'user_id': 'userid_145'}, {'user_id': 'userid_1879'}, {'user_id': 'userid_308'}, {'user_id': 'userid_1179'}, {'user_id': 'userid_677'}, {'user_id': 'userid_1397'}, {'user_id': 'userid_324'}, {'user_id': 'userid_795'}, {'user_id': 'userid_863'}, {'user_id': 'userid_100'}, {'user_id': 'userid_1333'}, {'user_id': 'userid_1636'}, {'user_id': 'userid_1850'}, {'user_id': 'userid_711'}, {'user_id': 'userid_729'}, {'user_id': 'userid_1505'}, {'user_id': 'userid_1315'}, {'user_id': 'userid_597'}, {'user_id': 'userid_386'}, {'user_id': 'userid_1978'}, {'user_id': 'userid_1068'}, {'user_id': 'userid_1708'}, {'user_id': 'userid_1246'}, {'user_id': 'userid_339'}, {'user_id': 'userid_1661'}, {'user_id': 'userid_152'}, {'user_id': 'userid_216'}, {'user_id': 'userid_850'}, {'user_id': 'userid_333'}, {'user_id': 'userid_252'}, {'user_id': 'userid_1675'}, {'user_id': 'userid_1490'}, {'user_id': 'userid_123'}, {'user_id': 'userid_227'}, {'user_id': 'userid_577'}, {'user_id': 'userid_242'}, {'user_id': 'userid_771'}, {'user_id': 'userid_1350'}, {'user_id': 'userid_1013'}, {'user_id': 'userid_1902'}, {'user_id': 'userid_257'}, {'user_id': 'userid_598'}, {'user_id': 'userid_847'}, {'user_id': 'userid_1343'}, {'user_id': 'userid_673'}, {'user_id': 'userid_243'}, {'user_id': 'userid_622'}, {'user_id': 'userid_1856'}, {'user_id': 'userid_384'}, {'user_id': 'userid_1871'}, {'user_id': 'userid_655'}, {'user_id': 'userid_108'}, {'user_id': 'userid_131'}, {'user_id': 'userid_1760'}, {'user_id': 'userid_935'}, {'user_id': 'userid_210'}, {'user_id': 'userid_1101'}, {'user_id': 'userid_1739'}, {'user_id': 'userid_945'}, {'user_id': 'userid_842'}, {'user_id': 'userid_1717'}, {'user_id': 'userid_1351'}, {'user_id': 'userid_406'}, {'user_id': 'userid_230'}, {'user_id': 'userid_914'}, {'user_id': 'userid_593'}, {'user_id': 'userid_1083'}, {'user_id': 'userid_356'}, {'user_id': 'userid_876'}, {'user_id': 'userid_1431'}, {'user_id': 'userid_424'}, {'user_id': 'userid_686'}, {'user_id': 'userid_527'}, {'user_id': 'userid_1766'}, {'user_id': 'userid_244'}, {'user_id': 'userid_393'}, {'user_id': 'userid_1409'}, {'user_id': 'userid_1178'}, {'user_id': 'userid_526'}, {'user_id': 'userid_90'}, {'user_id': 'userid_238'}, {'user_id': 'userid_1897'}, {'user_id': 'userid_241'}, {'user_id': 'userid_1262'}, {'user_id': 'userid_1105'}, {'user_id': 'userid_744'}, {'user_id': 'userid_1263'}], 'var_call_YZU6UuP2rhi0g9itAKUQBxmy': [{'business_ref': 'businessref_44', 'review_count': '1'}, {'business_ref': 'businessref_13', 'review_count': '1'}, {'business_ref': 'businessref_79', 'review_count': '4'}, {'business_ref': 'businessref_74', 'review_count': '2'}, {'business_ref': 'businessref_66', 'review_count': '2'}, {'business_ref': 'businessref_67', 'review_count': '2'}, {'business_ref': 'businessref_33', 'review_count': '3'}, {'business_ref': 'businessref_81', 'review_count': '1'}, {'business_ref': 'businessref_15', 'review_count': '1'}, {'business_ref': 'businessref_36', 'review_count': '3'}, {'business_ref': 'businessref_89', 'review_count': '3'}, {'business_ref': 'businessref_60', 'review_count': '2'}, {'business_ref': 'businessref_12', 'review_count': '2'}, {'business_ref': 'businessref_17', 'review_count': '1'}, {'business_ref': 'businessref_43', 'review_count': '3'}, {'business_ref': 'businessref_53', 'review_count': '1'}, {'business_ref': 'businessref_57', 'review_count': '4'}, {'business_ref': 'businessref_37', 'review_count': '4'}, {'business_ref': 'businessref_8', 'review_count': '2'}, {'business_ref': 'businessref_86', 'review_count': '2'}, {'business_ref': 'businessref_62', 'review_count': '1'}, {'business_ref': 'businessref_31', 'review_count': '1'}, {'business_ref': 'businessref_99', 'review_count': '1'}, {'business_ref': 'businessref_88', 'review_count': '2'}, {'business_ref': 'businessref_26', 'review_count': '3'}, {'business_ref': 'businessref_68', 'review_count': '1'}, {'business_ref': 'businessref_23', 'review_count': '1'}, {'business_ref': 'businessref_41', 'review_count': '1'}, {'business_ref': 'businessref_10', 'review_count': '1'}, {'business_ref': 'businessref_45', 'review_count': '4'}, {'business_ref': 'businessref_96', 'review_count': '2'}, {'business_ref': 'businessref_98', 'review_count': '3'}, {'business_ref': 'businessref_22', 'review_count': '1'}, {'business_ref': 'businessref_14', 'review_count': '1'}, {'business_ref': 'businessref_20', 'review_count': '1'}, {'business_ref': 'businessref_46', 'review_count': '1'}, {'business_ref': 'businessref_1', 'review_count': '1'}, {'business_ref': 'businessref_6', 'review_count': '1'}, {'business_ref': 'businessref_91', 'review_count': '1'}, {'business_ref': 'businessref_7', 'review_count': '1'}, {'business_ref': 'businessref_92', 'review_count': '2'}], 'var_call_ZwXCsg6Y1aTgncyAMM2Y1R4H': 'file_storage/call_ZwXCsg6Y1aTgncyAMM2Y1R4H.json'}

exec(code, env_args)
