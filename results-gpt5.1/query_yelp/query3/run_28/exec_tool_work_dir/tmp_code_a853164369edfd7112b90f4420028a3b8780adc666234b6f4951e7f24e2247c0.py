code = """import json, pandas as pd
rl = var_call_xaVMKHVpSnmgpYlFGlJdL8Se
# map businessref_X -> businessid_X
refs = [r['business_ref'] for r in rl]
ids = set('businessid_' + r.split('_')[1] for r in refs)
# load business attributes file
path = var_call_ZZsSEQIfFqoiPyQvzNklRSqm
with open(path, 'r') as f:
    biz = json.load(f)
# filter businesses that were reviewed in 2018
biz2018 = [b for b in biz if b.get('business_id') in ids]
count = 0
for b in biz2018:
    attrs = b.get('attributes')
    if not isinstance(attrs, dict):
        continue
    bp = attrs.get('BusinessParking')
    bike = attrs.get('BikeParking')
    has_parking = False
    # consider any non-"False"/"None" as offering
    if isinstance(bp, str) and bp not in ("False", "None"):
        has_parking = True
    if isinstance(bike, str) and bike == "True":
        has_parking = True
    if has_parking:
        count += 1

import json as _j
res = _j.dumps(count)
print("__RESULT__:")
print(res)"""

env_args = {'var_call_aXelbqtsOcOWoDcPtBcDVuWH': ['checkin', 'business'], 'var_call_CwCoWE9T5aWZw7aCWlJgYmwL': [{'business_ref': 'businessref_46', 'date': '2016-08-15 21:16:00'}, {'business_ref': 'businessref_35', 'date': 'December 06, 2020 at 07:48 PM'}, {'business_ref': 'businessref_37', 'date': '24 Mar 2016, 21:40'}, {'business_ref': 'businessref_91', 'date': '2019-12-15 18:28:00'}, {'business_ref': 'businessref_47', 'date': '13 Feb 2020, 22:17'}, {'business_ref': 'businessref_54', 'date': '2021-05-26 04:57:32'}, {'business_ref': 'businessref_37', 'date': 'October 09, 2019 at 01:44 PM'}, {'business_ref': 'businessref_21', 'date': '2015-12-06 21:27:12'}, {'business_ref': 'businessref_91', 'date': '09 Jan 2021, 21:20'}, {'business_ref': 'businessref_3', 'date': 'July 21, 2020 at 06:36 PM'}, {'business_ref': 'businessref_80', 'date': '2020-10-05 20:35:07'}, {'business_ref': 'businessref_79', 'date': '03 Feb 2018, 15:15'}, {'business_ref': 'businessref_96', 'date': '2012-03-23 04:39:00'}, {'business_ref': 'businessref_33', 'date': '31 Oct 2019, 17:52'}, {'business_ref': 'businessref_48', 'date': 'August 02, 2010 at 05:18 PM'}, {'business_ref': 'businessref_74', 'date': '2021-07-16 17:24:00'}, {'business_ref': 'businessref_41', 'date': '2021-04-29 12:08:00'}, {'business_ref': 'businessref_53', 'date': '2016-10-02 12:58:00'}, {'business_ref': 'businessref_7', 'date': '2019-12-29 20:57:00'}, {'business_ref': 'businessref_36', 'date': '01 Oct 2011, 22:57'}], 'var_call_xaVMKHVpSnmgpYlFGlJdL8Se': [{'business_ref': 'businessref_79'}, {'business_ref': 'businessref_13'}, {'business_ref': 'businessref_44'}, {'business_ref': 'businessref_6'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_71'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_29'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_81'}, {'business_ref': 'businessref_33'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_52'}, {'business_ref': 'businessref_89'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_60'}, {'business_ref': 'businessref_12'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_31'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_51'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_72'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_85'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_56'}, {'business_ref': 'businessref_90'}, {'business_ref': 'businessref_97'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_34'}, {'business_ref': 'businessref_21'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_92'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_95'}, {'business_ref': 'businessref_61'}, {'business_ref': 'businessref_49'}, {'business_ref': 'businessref_10'}, {'business_ref': 'businessref_23'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_50'}, {'business_ref': 'businessref_76'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_3'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_69'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_70'}, {'business_ref': 'businessref_18'}], 'var_call_ZZsSEQIfFqoiPyQvzNklRSqm': 'file_storage/call_ZZsSEQIfFqoiPyQvzNklRSqm.json'}

exec(code, env_args)
