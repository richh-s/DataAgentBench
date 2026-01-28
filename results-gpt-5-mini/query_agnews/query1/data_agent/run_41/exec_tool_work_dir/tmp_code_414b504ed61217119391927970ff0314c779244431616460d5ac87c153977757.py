code = """import json
import pandas as pd

with open(var_call_wjijicMPNedUw4ONyAHg4xMA, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
for col in ['article_id','title','description']:
    if col not in df.columns:
        df[col] = ''

df['description'] = df['description'].fillna('').astype(str)
df['title'] = df['title'].fillna('').astype(str)
df['desc_len'] = df['description'].apply(len)

keywords = ['football','soccer','basketball','baseball','tennis','golf','olympic','coach','team','league','cup','inning','bat','run','home run','tackle','manager','pitch','goalkeeper','foul','referee','boxing','wrestling','cricket','nba','mlb','nhl','mls','madden','espn','score','scored','match','season','playoff','final','goal','win','won']

sports_mask = df.apply(lambda row: any(k in (row['title'] + ' ' + row['description']).lower() for k in keywords), axis=1)

sports_df = df[sports_mask].copy()

# Show top matches
candidates = sports_df[['article_id','title','desc_len']].sort_values('desc_len', ascending=False).head(50).to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(candidates))"""

env_args = {'var_call_wjijicMPNedUw4ONyAHg4xMA': 'file_storage/call_wjijicMPNedUw4ONyAHg4xMA.json', 'var_call_cx5PEPS95YUVsIvlHoiREaKF': None, 'var_call_Ats8FczWZ8SwMGxhTTwZuUnX': {'count': 0, 'top_title': None, 'top_desc_len': None, 'candidates': []}, 'var_call_aJqG3rrWo7CQ8FQ1AtonOPh1': 'file_storage/call_aJqG3rrWo7CQ8FQ1AtonOPh1.json', 'var_call_nruyzJAR6yKoMAqgfjuLfSis': 'AMD starts shipping 90-nanometer chips to customers'}

exec(code, env_args)
