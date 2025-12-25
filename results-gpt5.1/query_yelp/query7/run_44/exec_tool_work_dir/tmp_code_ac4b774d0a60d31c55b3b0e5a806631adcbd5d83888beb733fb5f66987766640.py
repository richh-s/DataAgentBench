code = """import re, json
from datetime import datetime

samples = [row['yelping_since'] for row in var_call_ydvXpdqzyBpby2DVKqUSzh6W]

patterns = [
    '%d %b %Y, %H:%M',
    '%Y-%m-%d %H:%M:%S',
    '%B %d, %Y at %I:%M %p',
]

parsed = []
for s in samples:
    year = None
    for p in patterns:
        try:
            dt = datetime.strptime(s, p)
            year = dt.year
            break
        except Exception:
            continue
    if year is None:
        m = re.search(r'(20\\d{2})', s)
        year = int(m.group(1)) if m else None
    parsed.append({'raw': s, 'year': year})

result = json.dumps(parsed)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_pw8AmkK8tvd6lUFeRIUfemlx': [{'business_id': 'businessid_49'}, {'business_id': 'businessid_47'}, {'business_id': 'businessid_88'}, {'business_id': 'businessid_41'}, {'business_id': 'businessid_33'}, {'business_id': 'businessid_74'}, {'business_id': 'businessid_92'}, {'business_id': 'businessid_64'}, {'business_id': 'businessid_52'}, {'business_id': 'businessid_29'}, {'business_id': 'businessid_10'}, {'business_id': 'businessid_61'}, {'business_id': 'businessid_54'}, {'business_id': 'businessid_8'}, {'business_id': 'businessid_59'}, {'business_id': 'businessid_91'}, {'business_id': 'businessid_83'}, {'business_id': 'businessid_93'}, {'business_id': 'businessid_1'}, {'business_id': 'businessid_24'}, {'business_id': 'businessid_95'}, {'business_id': 'businessid_50'}, {'business_id': 'businessid_26'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_89'}, {'business_id': 'businessid_32'}, {'business_id': 'businessid_70'}, {'business_id': 'businessid_42'}, {'business_id': 'businessid_71'}, {'business_id': 'businessid_97'}, {'business_id': 'businessid_14'}, {'business_id': 'businessid_3'}, {'business_id': 'businessid_35'}, {'business_id': 'businessid_28'}, {'business_id': 'businessid_57'}, {'business_id': 'businessid_27'}, {'business_id': 'businessid_75'}, {'business_id': 'businessid_34'}, {'business_id': 'businessid_2'}, {'business_id': 'businessid_19'}, {'business_id': 'businessid_48'}, {'business_id': 'businessid_67'}, {'business_id': 'businessid_7'}, {'business_id': 'businessid_51'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_100'}, {'business_id': 'businessid_5'}, {'business_id': 'businessid_63'}, {'business_id': 'businessid_45'}, {'business_id': 'businessid_68'}, {'business_id': 'businessid_6'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_78'}, {'business_id': 'businessid_79'}, {'business_id': 'businessid_66'}, {'business_id': 'businessid_55'}, {'business_id': 'businessid_30'}, {'business_id': 'businessid_80'}, {'business_id': 'businessid_15'}, {'business_id': 'businessid_96'}, {'business_id': 'businessid_11'}, {'business_id': 'businessid_73'}, {'business_id': 'businessid_4'}, {'business_id': 'businessid_77'}, {'business_id': 'businessid_18'}, {'business_id': 'businessid_65'}, {'business_id': 'businessid_86'}, {'business_id': 'businessid_53'}, {'business_id': 'businessid_40'}, {'business_id': 'businessid_44'}, {'business_id': 'businessid_43'}, {'business_id': 'businessid_72'}, {'business_id': 'businessid_9'}, {'business_id': 'businessid_20'}, {'business_id': 'businessid_37'}, {'business_id': 'businessid_56'}, {'business_id': 'businessid_62'}, {'business_id': 'businessid_94'}, {'business_id': 'businessid_39'}, {'business_id': 'businessid_90'}, {'business_id': 'businessid_31'}, {'business_id': 'businessid_85'}, {'business_id': 'businessid_25'}, {'business_id': 'businessid_82'}, {'business_id': 'businessid_58'}, {'business_id': 'businessid_12'}, {'business_id': 'businessid_99'}, {'business_id': 'businessid_60'}, {'business_id': 'businessid_21'}, {'business_id': 'businessid_98'}, {'business_id': 'businessid_16'}, {'business_id': 'businessid_46'}, {'business_id': 'businessid_22'}, {'business_id': 'businessid_36'}, {'business_id': 'businessid_69'}, {'business_id': 'businessid_23'}, {'business_id': 'businessid_38'}, {'business_id': 'businessid_81'}, {'business_id': 'businessid_13'}, {'business_id': 'businessid_17'}], 'var_call_FwrZCyocPRJVU7w1g0CCQQ6F': ['checkin', 'business'], 'var_call_IjuIwauvMomZ37JgqLUHlkR7': [{'sample': 'ber'}, {'sample': '-08'}, {'sample': '03,'}, {'sample': '21,'}, {'sample': '-02'}, {'sample': '15,'}, {'sample': '29,'}, {'sample': '08,'}, {'sample': 'emb'}, {'sample': ' 30'}], 'var_call_ydvXpdqzyBpby2DVKqUSzh6W': [{'yelping_since': '15 Jan 2009, 16:40'}, {'yelping_since': '13 Jul 2010, 15:42'}, {'yelping_since': '2010-09-07 23:24:36'}, {'yelping_since': 'October 23, 2011 at 07:47 PM'}, {'yelping_since': '2011-08-30 13:46:26'}, {'yelping_since': '2009-12-02 18:54:31'}, {'yelping_since': '2009-04-15 12:46:06'}, {'yelping_since': 'October 04, 2009 at 05:59 PM'}, {'yelping_since': '20 Apr 2008, 16:55'}, {'yelping_since': '2007-07-28 22:22:09'}, {'yelping_since': 'January 14, 2009 at 06:31 PM'}, {'yelping_since': 'October 10, 2009 at 01:37 AM'}, {'yelping_since': '17 Nov 2008, 02:26'}, {'yelping_since': '2010-04-29 14:32:53'}, {'yelping_since': '26 Sep 2009, 02:31'}, {'yelping_since': 'May 03, 2009 at 08:19 PM'}, {'yelping_since': 'July 21, 2008 at 06:04 PM'}, {'yelping_since': 'August 13, 2009 at 01:09 PM'}, {'yelping_since': '2011-08-19 18:09:41'}, {'yelping_since': '2009-12-14 01:40:43'}]}

exec(code, env_args)
