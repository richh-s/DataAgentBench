code = """import json
import pandas as pd

# Load full records from file if needed
src = var_call_OwstK6thnVbAAKKXBkGQlJk1
if isinstance(src, str):
    with open(src, 'r', encoding='utf-8') as f:
        records = json.load(f)
else:
    records = src

df = pd.DataFrame(records)
# Ensure strings
for c in ['title','description']:
    df[c] = df[c].astype('string')

# Heuristic sports classifier based on title/description keywords
sports_kw = [
    'nba','nfl','mlb','nhl','soccer','football','baseball','basketball','hockey','golf','tennis','olympic','olympics',
    'coach','quarterback','touchdown','home run','world series','super bowl','playoffs','playoff','championship','league',
    'fifa','uefa','premier','la liga','serie a','bundesliga','mls','cricket','rugby','formula','f1','nascar','grand prix',
    'pga','atp','wta','boxing','ufc','mma','wrestling'
]

def is_sports(row):
    text = (str(row.get('title') or '') + ' ' + str(row.get('description') or '')).lower()
    return any(k in text for k in sports_kw)

sports_mask = df.apply(is_sports, axis=1)
sports_df = df.loc[sports_mask].copy()

# Character count
sports_df['desc_len'] = sports_df['description'].fillna('').map(lambda x: len(str(x)))

if len(sports_df) == 0:
    result = {'title': None}
else:
    top = sports_df.sort_values(['desc_len','article_id'], ascending=[False, True]).iloc[0]
    result = {'title': str(top['title'])}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_OwstK6thnVbAAKKXBkGQlJk1': 'file_storage/call_OwstK6thnVbAAKKXBkGQlJk1.json'}

exec(code, env_args)
