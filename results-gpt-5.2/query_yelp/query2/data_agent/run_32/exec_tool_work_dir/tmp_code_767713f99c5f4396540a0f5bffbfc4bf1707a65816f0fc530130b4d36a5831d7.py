code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

biz = load_records(var_call_oKBjiky7ugl5mkFZxoSM4UOy)

biz_df = pd.DataFrame(biz)

pat = re.compile(r'\b([A-Z]{2})\b')

# More robust: grab last 2-letter token after comma patterns
pat2 = re.compile(r',\s*([A-Z]{2})\b')

def get_state(desc):
    if not isinstance(desc, str):
        return None
    ms = pat2.findall(desc)
    if not ms:
        return None
    # pick last 2-letter after comma; filter to US states + DC
    states = set(['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY','DC'])
    for s in reversed(ms):
        if s in states:
            return s
    return None

biz_df['state']=biz_df['description'].map(get_state)
state_counts = biz_df['state'].value_counts(dropna=False).head(20).to_dict()

print('__RESULT__:')
print(json.dumps(state_counts))"""

env_args = {'var_call_oKBjiky7ugl5mkFZxoSM4UOy': 'file_storage/call_oKBjiky7ugl5mkFZxoSM4UOy.json', 'var_call_1owFHRVlFVEdG6D1fY6LjENE': 'file_storage/call_1owFHRVlFVEdG6D1fY6LjENE.json', 'var_call_hHZLfBDcqG1GOuqkmlZAbZME': {'state': None, 'total_reviews': 0, 'average_business_rating': None}}

exec(code, env_args)
