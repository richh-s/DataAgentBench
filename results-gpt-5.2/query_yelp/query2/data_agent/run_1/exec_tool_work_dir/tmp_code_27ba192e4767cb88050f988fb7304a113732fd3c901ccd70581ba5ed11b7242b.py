code = """import json, re, pandas as pd
path = var_call_sEv23LjnqO49MSBvPhfKlGY3
with open(path,'r',encoding='utf-8') as f:
    biz = json.load(f)

def parse_state(desc):
    states = {
        'AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY','DC'
    }
    if not desc:
        return None
    for mm in re.finditer(r"\b([A-Z]{2})\b", desc):
        st=mm.group(1)
        if st in states:
            return st
    return None

rows=[]
for r in biz:
    st=parse_state(r.get('description'))
    try:
        rc=int(r.get('review_count'))
    except:
        rc=None
    rows.append({'state':st,'review_count':rc})

df=pd.DataFrame(rows)
print('__RESULT__:')
print(json.dumps({'rows':len(df),'non_null_state':int(df.state.notna().sum()),'states':sorted(df.state.dropna().unique().tolist())[:20]}))"""

env_args = {'var_call_Pr7tc0HKLfl3LZJKrJI2qkwZ': 'file_storage/call_Pr7tc0HKLfl3LZJKrJI2qkwZ.json', 'var_call_2KcQNtpgWpdSy1Ok7ZD7VufB': [{'ok': '1'}], 'var_call_iDLnvQzRnnHRmtOtfJh3kfSb': {'error': 'no data'}, 'var_call_sEv23LjnqO49MSBvPhfKlGY3': 'file_storage/call_sEv23LjnqO49MSBvPhfKlGY3.json'}

exec(code, env_args)
