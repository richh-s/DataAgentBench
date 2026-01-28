code = """import json, pandas as pd

path = var_call_QJsMMQg6JKSHxThiAvM79wCs
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# ensure strings
for col in ['title','description']:
    df[col] = df[col].fillna('').astype(str)

df['desc_len'] = df['description'].str.len()
max_len = int(df['desc_len'].max()) if len(df) else 0
candidates = df[df['desc_len'] == max_len].copy()

# categorize as Sports by simple keyword heuristics in title/description
sports_keywords = [
    'nba','nfl','mlb','nhl','soccer','football','basketball','baseball','hockey','tennis','golf','olympic','olympics',
    'cricket','rugby','fifa','uefa','premier league','champions league','world cup','cup','league','tournament',
    'coach','quarterback','touchdown','home run','pitcher','goal','goals','match','matches','game','games','season',
    'playoff','playoffs','final','finals','win','wins','loss','losses','team','teams','player','players','championship'
]

def is_sports(row):
    text = (row.get('title','') + ' ' + row.get('description','')).lower()
    return any(k in text for k in sports_keywords)

candidates['is_sports'] = candidates.apply(is_sports, axis=1)

sports_candidates = candidates[candidates['is_sports']]
if len(sports_candidates) == 0:
    out = {"error": "No sports article found among those with max description length", "max_desc_len": max_len, "num_candidates": int(len(candidates))}
else:
    # if multiple, pick lowest article_id
    sports_candidates['article_id_int'] = pd.to_numeric(sports_candidates['article_id'], errors='coerce')
    sports_candidates = sports_candidates.sort_values(['article_id_int','title'])
    title = sports_candidates.iloc[0]['title']
    out = {"title": title, "max_desc_len": max_len, "article_id": str(sports_candidates.iloc[0]['article_id'])}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_QJsMMQg6JKSHxThiAvM79wCs': 'file_storage/call_QJsMMQg6JKSHxThiAvM79wCs.json'}

exec(code, env_args)
