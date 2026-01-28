code = """import json, pandas as pd
from datetime import datetime

# load sample for parsing formats
path = var_call_PYWVyhefplIODCHHDPhUaLuv
with open(path, 'r') as f:
    rows = json.load(f)

# infer date parsing in python

def parse_date(s):
    # try multiple known formats
    fmts = [
        '%Y-%m-%d %H:%M:%S',
        '%Y-%m-%d',
        '%d %b %Y, %H:%M',
        '%B %d, %Y at %I:%M %p',
        '%b %d, %Y at %I:%M %p',
    ]
    for fmt in fmts:
        try:
            return datetime.strptime(s, fmt).date()
        except Exception:
            pass
    return None

parsed = [parse_date(r['Date']) for r in rows[:50]]
res = {'parsed_ok': sum(p is not None for p in parsed), 'examples': [{'raw': rows[i]['Date'], 'parsed': (str(parsed[i]) if parsed[i] else None)} for i in range(min(10,len(rows)))]}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_1oDxJjpBDh0FKEVZMMEQl2Mo': ['index_info'], 'var_call_0TRAH6EA7OhvVx9PgRtUmyHO': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}, {'Date': '1987-01-08 00:00:00'}, {'Date': '1987-01-09 00:00:00'}, {'Date': '1987-01-12 00:00:00'}, {'Date': '1987-01-13 00:00:00'}, {'Date': '1987-01-14 00:00:00'}, {'Date': 'January 15, 1987 at 12:00 AM'}, {'Date': 'January 16, 1987 at 12:00 AM'}, {'Date': 'January 19, 1987 at 12:00 AM'}, {'Date': '20 Jan 1987, 00:00'}, {'Date': 'January 21, 1987 at 12:00 AM'}, {'Date': '22 Jan 1987, 00:00'}, {'Date': 'January 23, 1987 at 12:00 AM'}, {'Date': 'January 26, 1987 at 12:00 AM'}, {'Date': '27 Jan 1987, 00:00'}, {'Date': 'January 28, 1987 at 12:00 AM'}], 'var_call_PYWVyhefplIODCHHDPhUaLuv': 'file_storage/call_PYWVyhefplIODCHHDPhUaLuv.json'}

exec(code, env_args)
