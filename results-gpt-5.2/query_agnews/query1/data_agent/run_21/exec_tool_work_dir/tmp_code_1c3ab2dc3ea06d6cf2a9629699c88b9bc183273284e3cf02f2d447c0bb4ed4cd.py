code = """import json, pandas as pd

path = var_call_SG6yAd5NJc99hpAivjywQuwN
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# ensure strings
for col in ['title','description']:
    df[col] = df[col].fillna('').astype(str)

df['desc_len'] = df['description'].str.len()
max_len = int(df['desc_len'].max()) if len(df) else 0
candidates = df[df['desc_len'] == max_len]
# Determine sports articles among candidates by keyword heuristic
sports_keywords = [
    ' vs ', 'game', 'season', 'league', 'team', 'tournament', 'cup', 'championship',
    'coach', 'player', 'players', 'nba', 'nfl', 'mlb', 'nhl', 'soccer', 'football',
    'basketball', 'baseball', 'hockey', 'tennis', 'golf', 'cricket', 'olympic',
    'win', 'won', 'loss', 'match', 'race', 'grand slam', 'fifa', 'uefa'
]

def is_sports(text):
    t = text.lower()
    return any(k.strip().lower() in t for k in sports_keywords)

candidates['is_sports'] = (candidates['title'] + ' ' + candidates['description']).apply(is_sports)

sports_candidates = candidates[candidates['is_sports']]
if len(sports_candidates) == 0:
    # fallback: search entire df for max description length among sports
    df['is_sports'] = (df['title'] + ' ' + df['description']).apply(is_sports)
    sports_df = df[df['is_sports']]
    max_len = int(sports_df['desc_len'].max())
    sports_candidates = sports_df[sports_df['desc_len'] == max_len]

# If multiple, pick smallest article_id as deterministic
sports_candidates = sports_candidates.copy()
# normalize article_id numeric
sports_candidates['article_id_num'] = pd.to_numeric(sports_candidates['article_id'], errors='coerce')
sports_candidates = sports_candidates.sort_values(['article_id_num','article_id'], na_position='last')
row = sports_candidates.iloc[0]
result = {
    'title': row['title'],
    'article_id': row['article_id'],
    'description_length': int(row['desc_len'])
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_SG6yAd5NJc99hpAivjywQuwN': 'file_storage/call_SG6yAd5NJc99hpAivjywQuwN.json'}

exec(code, env_args)
