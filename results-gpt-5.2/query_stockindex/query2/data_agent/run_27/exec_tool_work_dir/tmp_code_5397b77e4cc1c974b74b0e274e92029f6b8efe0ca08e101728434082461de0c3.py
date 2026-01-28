code = """import json, pandas as pd
from datetime import datetime

def parse_date(s):
    if s is None:
        return None
    s = str(s)
    fmts = ['%Y-%m-%d','%Y-%m-%d %H:%M:%S','%d %b %Y, %H:%M','%B %d, %Y at %I:%M %p','%b %d, %Y at %I:%M %p']
    from datetime import datetime as dt
    for f in fmts:
        try:
            return dt.strptime(s, f).date()
        except Exception:
            pass
    return None

path = var_call_e9kewmQDyhnYON93UgIkkayi
with open(path,'r',encoding='utf-8') as f:
    recs = json.load(f)

df = pd.DataFrame(recs)
for c in ['Open','Close']:
    df[c] = pd.to_numeric(df[c], errors='coerce')
df['d'] = df['Date'].map(parse_date)
df = df.dropna(subset=['d','Open','Close','Index'])
df = df[(df['d']>=datetime(2018,1,1).date()) & (df['d']<datetime(2019,1,1).date())]

north_america_indices = ['IXIC','NYA','GSPTSE']

grp = df[df['Index'].isin(north_america_indices)].groupby('Index').apply(lambda g: pd.Series({
    'up_days': int((g['Close']>g['Open']).sum()),
    'down_days': int((g['Close']<g['Open']).sum()),
    'n_days': int(len(g))
}))
res = grp.reset_index()
res['more_up_than_down'] = res['up_days'] > res['down_days']

more = res[res['more_up_than_down']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps({'all': res.to_dict(orient='records'), 'more_up': more}))"""

env_args = {'var_call_P4FMzar0A6Cbv6huVOPSNK90': ['index_info'], 'var_call_6td2DKJoiBNwcRmitxuRSJTU': ['index_trade'], 'var_call_vuAY3cQFVfaKYE5fzjCpVUOZ': [], 'var_call_6vBfWq7QN5vaKYUPChxyEhbG': [{'Date': 'January 27, 2015 at 12:00 AM', 'n': '11'}, {'Date': '2017-10-12 00:00:00', 'n': '11'}, {'Date': '2015-01-16 00:00:00', 'n': '11'}, {'Date': '16 Jan 2014, 00:00', 'n': '10'}, {'Date': '07 Apr 2011, 00:00', 'n': '10'}, {'Date': '27 Sep 2013, 00:00', 'n': '10'}, {'Date': '2012-05-25 00:00:00', 'n': '10'}, {'Date': 'June 19, 2019 at 12:00 AM', 'n': '10'}, {'Date': 'July 12, 2010 at 12:00 AM', 'n': '10'}, {'Date': '2013-05-21 00:00:00', 'n': '10'}, {'Date': 'April 15, 2005 at 12:00 AM', 'n': '10'}, {'Date': '2017-06-14 00:00:00', 'n': '10'}, {'Date': '12 Nov 2010, 00:00', 'n': '10'}, {'Date': '15 May 2019, 00:00', 'n': '10'}, {'Date': '2012-06-18 00:00:00', 'n': '10'}, {'Date': '2016-12-29 00:00:00', 'n': '9'}, {'Date': 'January 15, 2021 at 12:00 AM', 'n': '9'}, {'Date': '2002-01-11 00:00:00', 'n': '9'}, {'Date': '01 Jun 2016, 00:00', 'n': '9'}, {'Date': '26 Apr 2013, 00:00', 'n': '9'}], 'var_call_jNlJkNJKjdVeMerkx8QWu7lc': {'status': 'ready'}, 'var_call_e9kewmQDyhnYON93UgIkkayi': 'file_storage/call_e9kewmQDyhnYON93UgIkkayi.json', 'var_call_GSrNj5Gy2VTnM9orz9djMXkh': [{'Index': 'GSPTSE', 'up_days': 115, 'down_days': 135, 'n_days': 251}], 'var_call_C0zV71nFiJDNcRME8fIsCcYA': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}]}

exec(code, env_args)
