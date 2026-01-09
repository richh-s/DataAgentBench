code = """import json, pandas as pd
path = var_call_3p9kEtPNPVtJ6GZ5dSiHI9jr
with open(path,'r',encoding='utf-8') as f:
    records = json.load(f)

df = pd.DataFrame(records)
# ensure strings
for c in ['title','description']:
    df[c] = df[c].fillna('').astype(str)

def is_sports(text):
    t = text.lower()
    sports_terms = [
        'nba','nfl','mlb','nhl','soccer','football','basketball','baseball','hockey','tennis','golf','cricket',
        'olympic','olympics','championship','tournament','match','season','coach','player','players','team','teams',
        'league','cup','open','grand slam','world series','super bowl','touchdown','goal','goals','fielder','pitcher',
        'rookie','playoff','playoffs','final','finals','boxing','ufc','mma','f1','formula','nascar','racing'
    ]
    return any(term in t for term in sports_terms)

sports_mask = df.apply(lambda r: is_sports(r['title'] + ' ' + r['description']), axis=1)
sports_df = df[sports_mask].copy()
sports_df['desc_len'] = sports_df['description'].str.len()
# pick max length
row = sports_df.loc[sports_df['desc_len'].idxmax()] if len(sports_df)>0 else None
answer = row['title'] if row is not None else None
print('__RESULT__:')
print(json.dumps({'title': answer, 'max_description_length': int(row['desc_len']) if row is not None else None, 'sports_count': int(len(sports_df))}))"""

env_args = {'var_call_3p9kEtPNPVtJ6GZ5dSiHI9jr': 'file_storage/call_3p9kEtPNPVtJ6GZ5dSiHI9jr.json'}

exec(code, env_args)
