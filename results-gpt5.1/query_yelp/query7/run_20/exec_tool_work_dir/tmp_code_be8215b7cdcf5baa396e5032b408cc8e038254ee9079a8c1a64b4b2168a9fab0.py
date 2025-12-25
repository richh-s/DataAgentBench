code = """import json, pandas as pd, re
from datetime import datetime

path = var_call_Vi2ZH6uo4eHXSgls0ThS6bif
with open(path, 'r') as f:
    data = json.load(f)

rows = []
for r in data:
    s = r['yelping_since']
    year = None
    for fmt in ['%Y-%m-%d %H:%M:%S', '%B %d, %Y at %I:%M %p', '%d %b %Y, %H:%M', '%Y-%m-%d', '%m/%d/%Y']:
        try:
            dt = datetime.strptime(s, fmt)
            year = dt.year
            break
        except Exception:
            continue
    if year is None:
        m = re.search(r'(\d{4})', s)
        if m:
            year = int(m.group(1))
    if year is not None:
        rows.append({'user_id': r['user_id'], 'year': year})

users_2016 = [r['user_id'] for r in rows if r['year'] == 2016]

result = json.dumps(users_2016)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_tjE5OgXJFWj31A232x2T7DNn': ['checkin', 'business'], 'var_call_WpEBb9KhWT8ibglddOM4dy6O': [{'yelping_since': '2007-07-28 22:22:09'}, {'yelping_since': 'January 14, 2009 at 06:31 PM'}, {'yelping_since': '31 Oct 2006, 20:51'}, {'yelping_since': '2009-04-23 16:18:47'}, {'yelping_since': '2009-04-15 16:56:42'}, {'yelping_since': 'January 14, 2010 at 06:08 PM'}, {'yelping_since': 'July 10, 2006 at 05:45 PM'}, {'yelping_since': 'January 12, 2011 at 07:35 PM'}, {'yelping_since': '2010-09-08 13:59:31'}, {'yelping_since': 'July 20, 2010 at 09:05 PM'}, {'yelping_since': '21 Jun 2012, 22:45'}, {'yelping_since': '17 Jul 2009, 23:51'}, {'yelping_since': '05 Jul 2012, 15:33'}, {'yelping_since': '07 Mar 2012, 16:33'}, {'yelping_since': '2010-03-24 16:46:09'}, {'yelping_since': 'October 26, 2011 at 12:55 PM'}, {'yelping_since': '21 Jan 2011, 21:09'}, {'yelping_since': '09 Apr 2012, 21:28'}, {'yelping_since': '03 Jun 2009, 16:15'}, {'yelping_since': 'April 15, 2011 at 08:46 PM'}], 'var_call_Vi2ZH6uo4eHXSgls0ThS6bif': 'file_storage/call_Vi2ZH6uo4eHXSgls0ThS6bif.json'}

exec(code, env_args)
