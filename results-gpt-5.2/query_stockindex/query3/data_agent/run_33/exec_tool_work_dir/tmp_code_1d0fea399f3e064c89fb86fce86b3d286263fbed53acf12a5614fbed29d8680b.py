code = """import json, pandas as pd
from datetime import datetime

def parse_date(s):
    if s is None:
        return None
    s = str(s).strip()
    fmts = [
        "%Y-%m-%d",
        "%Y-%m-%d %H:%M:%S",
        "%d %b %Y, %H:%M",
        "%b %d, %Y at %I:%M %p",
        "%B %d, %Y at %I:%M %p",
        "%b %d, %Y",
        "%B %d, %Y",
    ]
    for f in fmts:
        try:
            return datetime.strptime(s, f).date().isoformat()
        except Exception:
            pass
    # try pandas
    try:
        return pd.to_datetime(s, errors='coerce').date().isoformat()
    except Exception:
        return None

samples = [r['Date'] for r in var_call_zAQmgj6aeYMp2ef4zfMBIwF8]
parsed = [parse_date(x) for x in samples]
print('__RESULT__:')
print(json.dumps({'samples': samples, 'parsed': parsed}))"""

env_args = {'var_call_UQNKGW67dSqn2nd1Mho4VPxt': ['index_info'], 'var_call_PVuChzZX3CspOa7HKxa95Eeg': ['index_trade'], 'var_call_zAQmgj6aeYMp2ef4zfMBIwF8': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}]}

exec(code, env_args)
