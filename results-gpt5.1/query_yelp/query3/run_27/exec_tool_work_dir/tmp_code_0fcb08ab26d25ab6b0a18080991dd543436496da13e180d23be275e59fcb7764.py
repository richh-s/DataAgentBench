code = """import json, pandas as pd, os

reviews_2018 = var_call_QxYHwn6rJIujBObPIOjcHYcB

# convert business_ref (businessref_X) to business_id (businessid_X)
ids_2018 = set()
for r in reviews_2018:
    br = r['business_ref']
    if br.startswith('businessref_'):
        ids_2018.add('businessid_' + br.split('_',1)[1])

# load full business attributes file
path = var_call_fhyewmYrqMR4Z0tMsNq5c930
with open(path, 'r') as f:
    business_data = json.load(f)

count = 0
for b in business_data:
    bid = b.get('business_id')
    if bid not in ids_2018:
        continue
    attrs = b.get('attributes')
    if not attrs or attrs == 'None':
        continue
    has_bike = attrs.get('BikeParking') == 'True'
    has_parking = False
    bp = attrs.get('BusinessParking')
    if isinstance(bp, str) and bp not in ('None', 'False'):
        # string like "{'garage': False, 'street': False, ...}"
        s = bp.replace('u"', '"').replace("u'", "'")
        try:
            d = eval(s)
            if isinstance(d, dict) and any(d.values()):
                has_parking = True
        except Exception:
            pass
    if has_bike or has_parking:
        count += 1

result = json.dumps(count)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_2XAwbLitukzmPOyOJgOwKxpy': ['checkin', 'business'], 'var_call_e2nnF3JsjnGbRL8dHh7BoSie': [{'business_ref': 'businessref_46', 'date': '2016-08-15 21:16:00'}, {'business_ref': 'businessref_35', 'date': 'December 06, 2020 at 07:48 PM'}, {'business_ref': 'businessref_37', 'date': '24 Mar 2016, 21:40'}, {'business_ref': 'businessref_91', 'date': '2019-12-15 18:28:00'}, {'business_ref': 'businessref_47', 'date': '13 Feb 2020, 22:17'}, {'business_ref': 'businessref_54', 'date': '2021-05-26 04:57:32'}, {'business_ref': 'businessref_37', 'date': 'October 09, 2019 at 01:44 PM'}, {'business_ref': 'businessref_21', 'date': '2015-12-06 21:27:12'}, {'business_ref': 'businessref_91', 'date': '09 Jan 2021, 21:20'}, {'business_ref': 'businessref_3', 'date': 'July 21, 2020 at 06:36 PM'}, {'business_ref': 'businessref_80', 'date': '2020-10-05 20:35:07'}, {'business_ref': 'businessref_79', 'date': '03 Feb 2018, 15:15'}, {'business_ref': 'businessref_96', 'date': '2012-03-23 04:39:00'}, {'business_ref': 'businessref_33', 'date': '31 Oct 2019, 17:52'}, {'business_ref': 'businessref_48', 'date': 'August 02, 2010 at 05:18 PM'}, {'business_ref': 'businessref_74', 'date': '2021-07-16 17:24:00'}, {'business_ref': 'businessref_41', 'date': '2021-04-29 12:08:00'}, {'business_ref': 'businessref_53', 'date': '2016-10-02 12:58:00'}, {'business_ref': 'businessref_7', 'date': '2019-12-29 20:57:00'}, {'business_ref': 'businessref_36', 'date': '01 Oct 2011, 22:57'}, {'business_ref': 'businessref_59', 'date': 'March 16, 2020 at 11:04 PM'}, {'business_ref': 'businessref_9', 'date': '13 Nov 2016, 14:16'}, {'business_ref': 'businessref_26', 'date': '2020-01-24 11:02:00'}, {'business_ref': 'businessref_6', 'date': '08 Aug 2016, 22:11'}, {'business_ref': 'businessref_36', 'date': '2015-11-12 01:04:50'}, {'business_ref': 'businessref_14', 'date': '2020-09-20 06:10:00'}, {'business_ref': 'businessref_46', 'date': 'June 05, 2018 at 11:54 PM'}, {'business_ref': 'businessref_10', 'date': '2017-01-07 21:21:00'}, {'business_ref': 'businessref_66', 'date': 'December 19, 2017 at 12:41 AM'}, {'business_ref': 'businessref_48', 'date': 'February 03, 2011 at 05:45 PM'}, {'business_ref': 'businessref_85', 'date': 'July 31, 2012 at 12:57 AM'}, {'business_ref': 'businessref_66', 'date': '2020-08-23 18:14:21'}, {'business_ref': 'businessref_66', 'date': '10 Jan 2020, 18:47'}, {'business_ref': 'businessref_86', 'date': '2017-10-23 18:42:00'}, {'business_ref': 'businessref_71', 'date': 'April 02, 2015 at 02:01 AM'}, {'business_ref': 'businessref_57', 'date': '26 Dec 2015, 21:34'}, {'business_ref': 'businessref_6', 'date': '18 Feb 2010, 15:57'}, {'business_ref': 'businessref_92', 'date': '28 Sep 2013, 17:37'}, {'business_ref': 'businessref_9', 'date': '2016-10-23 22:05:00'}, {'business_ref': 'businessref_66', 'date': '2016-07-20 21:17:03'}, {'business_ref': 'businessref_41', 'date': '17 Jan 2019, 20:22'}, {'business_ref': 'businessref_72', 'date': '2016-12-26 22:44:42'}, {'business_ref': 'businessref_74', 'date': '2020-07-06 14:42:00'}, {'business_ref': 'businessref_89', 'date': '27 Mar 2016, 00:58'}, {'business_ref': 'businessref_16', 'date': '15 Dec 2008, 23:36'}, {'business_ref': 'businessref_21', 'date': 'February 05, 2020 at 05:57 PM'}, {'business_ref': 'businessref_88', 'date': '14 Jun 2020, 02:18'}, {'business_ref': 'businessref_14', 'date': '2016-05-06 16:02:13'}, {'business_ref': 'businessref_60', 'date': 'June 28, 2020 at 10:12 PM'}, {'business_ref': 'businessref_79', 'date': '20 Sep 2017, 20:55'}], 'var_call_QxYHwn6rJIujBObPIOjcHYcB': [{'business_ref': 'businessref_79'}, {'business_ref': 'businessref_13'}, {'business_ref': 'businessref_44'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_29'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_81'}, {'business_ref': 'businessref_33'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_52'}, {'business_ref': 'businessref_89'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_60'}, {'business_ref': 'businessref_12'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_31'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_51'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_72'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_85'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_56'}, {'business_ref': 'businessref_90'}, {'business_ref': 'businessref_97'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_92'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_95'}, {'business_ref': 'businessref_61'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_34'}, {'business_ref': 'businessref_21'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_49'}, {'business_ref': 'businessref_10'}, {'business_ref': 'businessref_23'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_50'}, {'business_ref': 'businessref_76'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_3'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_69'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_70'}, {'business_ref': 'businessref_18'}, {'business_ref': 'businessref_6'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_71'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_73'}], 'var_call_fhyewmYrqMR4Z0tMsNq5c930': 'file_storage/call_fhyewmYrqMR4Z0tMsNq5c930.json'}

exec(code, env_args)
