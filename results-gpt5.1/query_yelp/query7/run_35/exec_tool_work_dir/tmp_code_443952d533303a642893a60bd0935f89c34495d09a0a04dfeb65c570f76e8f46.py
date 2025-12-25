code = """import json, re
from datetime import datetime

path = var_call_8K8dsyNZjUnyktAphsLY0673
with open(path, 'r') as f:
    users = json.load(f)

def parse_year(s):
    s = s.strip()
    fmts = ['%Y-%m-%d %H:%M:%S', '%d %b %Y, %H:%M', '%B %d, %Y at %I:%M %p', '%b %d, %Y at %I:%M %p', '%d %b %Y, %H:%M', '%d %b %Y, %H:%M', '%d %b %Y, %H:%M']
    for fmt in fmts:
        try:
            return datetime.strptime(s, fmt).year
        except Exception:
            continue
    m = re.search(r'(20\d{2}|19\d{2})', s)
    return int(m.group(1)) if m else None

user_2016 = [u['user_id'] for u in users if parse_year(u['yelping_since']) == 2016]

result = json.dumps(user_2016)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_eeAh4E1HV7QeuFXMGYlBHkyy': ['business', 'checkin'], 'var_call_PIXCJxg5ZS8nAAyfpLE4wjtB': [{'user_id': 'userid_286', 'yelping_since': '15 Jan 2009, 16:40'}, {'user_id': 'userid_1331', 'yelping_since': '13 Jul 2010, 15:42'}, {'user_id': 'userid_1880', 'yelping_since': '2010-09-07 23:24:36'}, {'user_id': 'userid_271', 'yelping_since': 'October 23, 2011 at 07:47 PM'}, {'user_id': 'userid_534', 'yelping_since': '2011-08-30 13:46:26'}, {'user_id': 'userid_1997', 'yelping_since': '2009-12-02 18:54:31'}, {'user_id': 'userid_1386', 'yelping_since': '2009-04-15 12:46:06'}, {'user_id': 'userid_237', 'yelping_since': 'October 04, 2009 at 05:59 PM'}, {'user_id': 'userid_596', 'yelping_since': '20 Apr 2008, 16:55'}, {'user_id': 'userid_948', 'yelping_since': '2007-07-28 22:22:09'}, {'user_id': 'userid_42', 'yelping_since': 'January 14, 2009 at 06:31 PM'}, {'user_id': 'userid_604', 'yelping_since': 'October 10, 2009 at 01:37 AM'}, {'user_id': 'userid_1291', 'yelping_since': '17 Nov 2008, 02:26'}, {'user_id': 'userid_995', 'yelping_since': '2010-04-29 14:32:53'}, {'user_id': 'userid_1630', 'yelping_since': '26 Sep 2009, 02:31'}, {'user_id': 'userid_1857', 'yelping_since': 'May 03, 2009 at 08:19 PM'}, {'user_id': 'userid_1936', 'yelping_since': 'July 21, 2008 at 06:04 PM'}, {'user_id': 'userid_288', 'yelping_since': 'August 13, 2009 at 01:09 PM'}, {'user_id': 'userid_1956', 'yelping_since': '2011-08-19 18:09:41'}, {'user_id': 'userid_529', 'yelping_since': '2009-12-14 01:40:43'}], 'var_call_rtuueCPczhxdrOSwY3eQoenc': [2007, 2008, 2009, 2010, 2011], 'var_call_8K8dsyNZjUnyktAphsLY0673': 'file_storage/call_8K8dsyNZjUnyktAphsLY0673.json'}

exec(code, env_args)
