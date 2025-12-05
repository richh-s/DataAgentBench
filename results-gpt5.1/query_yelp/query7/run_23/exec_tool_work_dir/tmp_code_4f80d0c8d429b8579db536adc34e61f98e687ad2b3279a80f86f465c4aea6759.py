code = """import json, re, pandas as pd
path = var_call_JhoKQEPhwDEV7KP4HbaJR8sn
with open(path, 'r') as f:
    data = json.load(f)
rows = []
for r in data:
    s = r['yelping_since']
    m = re.search(r'(19|20)\d{2}', s)
    year = int(m.group(0)) if m else None
    rows.append({'user_id': r['user_id'], 'year': year})
df = pd.DataFrame(rows)
users_2016 = df[df['year'] == 2016]['user_id'].tolist()
result = json.dumps(users_2016)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_lN9wcU5juyhkqWJovDWX97SV': ['business', 'checkin'], 'var_call_QJvAp5hu6ywOJ0Sf2QD2QZ8f': [{'yelping_since': 'October 10, 2009 at 01:37 AM'}, {'yelping_since': 'May 21, 2011 at 03:22 PM'}, {'yelping_since': '2005-07-18 06:22:37'}, {'yelping_since': '2009-04-30 03:16:12'}, {'yelping_since': 'August 18, 2008 at 08:13 AM'}, {'yelping_since': 'May 23, 2009 at 05:44 PM'}, {'yelping_since': '22 Jul 2007, 21:50'}, {'yelping_since': '2011-01-22 16:07:48'}, {'yelping_since': '2010-12-15 02:17:17'}, {'yelping_since': 'April 23, 2010 at 07:48 PM'}, {'yelping_since': '09 Dec 2007, 01:03'}, {'yelping_since': '12 Feb 2011, 01:00'}, {'yelping_since': '2009-04-17 13:38:22'}, {'yelping_since': 'January 17, 2011 at 10:14 PM'}, {'yelping_since': '07 Sep 2009, 22:20'}, {'yelping_since': '2011-04-17 16:27:25'}, {'yelping_since': '2010-06-26 21:11:26'}, {'yelping_since': '29 Feb 2012, 02:51'}, {'yelping_since': '2010-04-19 19:23:27'}, {'yelping_since': '2010-07-12 16:29:17'}], 'var_call_JhoKQEPhwDEV7KP4HbaJR8sn': 'file_storage/call_JhoKQEPhwDEV7KP4HbaJR8sn.json'}

exec(code, env_args)
