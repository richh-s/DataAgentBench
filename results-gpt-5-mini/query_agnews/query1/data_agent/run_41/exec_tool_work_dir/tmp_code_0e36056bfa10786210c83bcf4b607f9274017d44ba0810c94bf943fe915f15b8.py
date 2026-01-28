code = """import json
import pandas as pd
import re

with open(var_call_wjijicMPNedUw4ONyAHg4xMA, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
for col in ['article_id','title','description']:
    if col not in df.columns:
        df[col] = ''

df['description'] = df['description'].fillna('').astype(str)
df['desc_len'] = df['description'].apply(len)

# Broader sports keywords
keywords = ['game','match','season','goal','score','scored','defeat','defeats','beat','beats','won','win','loss','lose',
            'quarterback','basketball','football','soccer','tennis','baseball','golf','olympic','olympics','coach','team',
            'league','cup','inning','innings','bat','run','home run','tackle','tries','manager','pitch','goalkeeper',
            'foul','referee','boxing','mma','wrestling','cricket','nba','mlb','nhl','mls','playoff','final','semifinal','rookie',
            'cycling','race','racing','driver','drivers','motorsport','f1','nhra','nascar','formula','federation','athlete','athletes']
pattern = re.compile(r"\b(" + "|".join([re.escape(k) for k in keywords]) + r")\b", re.IGNORECASE)

# scoring

def score_text(text):
    return len(pattern.findall(text))

df['score'] = (df['title'].fillna('') + ' ' + df['description'].fillna('')).apply(score_text)

sports_df = df[df['score']>0].copy()

if sports_df.empty:
    out = {'count': 0, 'top_title': None, 'top_desc_len': None, 'candidates': []}
else:
    max_len = sports_df['desc_len'].max()
    top = sports_df[sports_df['desc_len']==max_len].iloc[0]
    candidates = sports_df.sort_values('desc_len', ascending=False)[['article_id','title','desc_len','score']].head(50).to_dict(orient='records')
    out = {'count': int(sports_df.shape[0]), 'top_title': top['title'], 'top_desc_len': int(top['desc_len']), 'candidates': candidates}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_wjijicMPNedUw4ONyAHg4xMA': 'file_storage/call_wjijicMPNedUw4ONyAHg4xMA.json', 'var_call_cx5PEPS95YUVsIvlHoiREaKF': None}

exec(code, env_args)
