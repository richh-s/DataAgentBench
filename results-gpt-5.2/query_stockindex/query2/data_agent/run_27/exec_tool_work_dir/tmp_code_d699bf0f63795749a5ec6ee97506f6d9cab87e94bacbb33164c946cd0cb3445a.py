code = """import json, pandas as pd
from datetime import datetime

def parse_date(s):
    if s is None:
        return None
    s = str(s)
    fmts = ['%Y-%m-%d','%Y-%m-%d %H:%M:%S','%d %b %Y, %H:%M','%B %d, %Y at %I:%M %p','%b %d, %Y at %I:%M %p']
    for f in fmts:
        try:
            return datetime.strptime(s, f).date()
        except Exception:
            pass
    return None

path = var_call_e9kewmQDyhnYON93UgIkkayi
with open(path,'r',encoding='utf-8') as f:
    recs = json.load(f)

df = pd.DataFrame(recs)
# numeric
for c in ['Open','Close']:
    df[c] = pd.to_numeric(df[c], errors='coerce')

df['parsed_date'] = df['Date'].map(parse_date)
df = df.dropna(subset=['parsed_date','Open','Close','Index'])
df2018 = df[(df['parsed_date']>=datetime(2018,1,1).date()) & (df['parsed_date']<datetime(2019,1,1).date())]

# define North American indices present in dataset (common symbols)
na_candidates = {'^GSPC','^DJI','^IXIC','^RUT','^GSPTSE','GSPTSE','^MXX','MXX','^BVSP','BVSP'}
# also include known Canada TSX symbol often '^GSPTSE'

df2018_na = df2018[df2018['Index'].isin(na_candidates)]

grp = df2018_na.groupby('Index').apply(lambda g: pd.Series({
    'up_days': int((g['Close']>g['Open']).sum()),
    'down_days': int((g['Close']<g['Open']).sum()),
    'n_days': int(len(g))
}))

res = grp.reset_index().to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_P4FMzar0A6Cbv6huVOPSNK90': ['index_info'], 'var_call_6td2DKJoiBNwcRmitxuRSJTU': ['index_trade'], 'var_call_vuAY3cQFVfaKYE5fzjCpVUOZ': [], 'var_call_6vBfWq7QN5vaKYUPChxyEhbG': [{'Date': 'January 27, 2015 at 12:00 AM', 'n': '11'}, {'Date': '2017-10-12 00:00:00', 'n': '11'}, {'Date': '2015-01-16 00:00:00', 'n': '11'}, {'Date': '16 Jan 2014, 00:00', 'n': '10'}, {'Date': '07 Apr 2011, 00:00', 'n': '10'}, {'Date': '27 Sep 2013, 00:00', 'n': '10'}, {'Date': '2012-05-25 00:00:00', 'n': '10'}, {'Date': 'June 19, 2019 at 12:00 AM', 'n': '10'}, {'Date': 'July 12, 2010 at 12:00 AM', 'n': '10'}, {'Date': '2013-05-21 00:00:00', 'n': '10'}, {'Date': 'April 15, 2005 at 12:00 AM', 'n': '10'}, {'Date': '2017-06-14 00:00:00', 'n': '10'}, {'Date': '12 Nov 2010, 00:00', 'n': '10'}, {'Date': '15 May 2019, 00:00', 'n': '10'}, {'Date': '2012-06-18 00:00:00', 'n': '10'}, {'Date': '2016-12-29 00:00:00', 'n': '9'}, {'Date': 'January 15, 2021 at 12:00 AM', 'n': '9'}, {'Date': '2002-01-11 00:00:00', 'n': '9'}, {'Date': '01 Jun 2016, 00:00', 'n': '9'}, {'Date': '26 Apr 2013, 00:00', 'n': '9'}], 'var_call_jNlJkNJKjdVeMerkx8QWu7lc': {'status': 'ready'}, 'var_call_e9kewmQDyhnYON93UgIkkayi': 'file_storage/call_e9kewmQDyhnYON93UgIkkayi.json'}

exec(code, env_args)
