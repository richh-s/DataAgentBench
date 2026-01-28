code = """import json, pandas as pd
path = var_call_lLaAwLLr8HyeR7T2RkRPpBsE
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# ensure strings
for c in ['title','description']:
    df[c] = df[c].fillna('').astype(str)

df['desc_len'] = df['description'].str.len()
# sports heuristic: title/description contains sports keywords or leagues/teams
sports_terms = [
    'nba','nfl','mlb','nhl','ncaa','soccer','football','basketball','baseball','hockey','tennis','golf','olympic','olympics',
    'formula','f1','nascar','cricket','rugby','boxing','mma','ufc','wimbledon','super bowl','world cup','grand slam',
    'coach','quarterback','touchdown','home run','pitcher','goal','match','tournament','championship','playoffs','season',
    'yankees','red sox','lakers','celtics','patriots','cowboys','manchester','barcelona','real madrid','arsenal','chelsea'
]
pat = r'(?i)(' + '|'.join([pd.regex.escape(t) if hasattr(pd, 'regex') else t for t in sports_terms]) + r')'
# pandas doesn't have regex.escape; use re
import re
pat = r'(?i)(' + '|'.join([re.escape(t) for t in sports_terms]) + r')'
mask = df['title'].str.contains(pat, regex=True, na=False) | df['description'].str.contains(pat, regex=True, na=False)
# take the max desc_len among likely sports
sports_df = df[mask].copy()
# if none matched, fallback to overall max
if len(sports_df)==0:
    best = df.sort_values(['desc_len','article_id'], ascending=[False, True]).iloc[0]
else:
    best = sports_df.sort_values(['desc_len','article_id'], ascending=[False, True]).iloc[0]

result = {'article_id': int(best['article_id']) if str(best['article_id']).isdigit() else best['article_id'], 'title': best['title'], 'description_length': int(best['desc_len'])}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_lLaAwLLr8HyeR7T2RkRPpBsE': 'file_storage/call_lLaAwLLr8HyeR7T2RkRPpBsE.json'}

exec(code, env_args)
