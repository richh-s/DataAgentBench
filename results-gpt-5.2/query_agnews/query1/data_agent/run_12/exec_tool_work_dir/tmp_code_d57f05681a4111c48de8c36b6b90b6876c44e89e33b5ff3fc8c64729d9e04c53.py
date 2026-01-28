code = """import json, pandas as pd

path = var_call_hgWlxVr97vYyOQe145GrVZ9J
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# ensure strings
for c in ['title','description']:
    df[c] = df[c].fillna('').astype(str)

df['desc_len'] = df['description'].str.len()
max_len = int(df['desc_len'].max()) if len(df) else 0
candidates = df[df['desc_len'] == max_len].copy()
# Identify sports articles among candidates
sports_mask = candidates['title'].str.contains(r"\b(football|soccer|nba|nfl|mlb|nhl|golf|tennis|olympic|cricket|rugby|baseball|basketball|hockey|coach|tournament|match|cup|league|playoff|goal|run|inning|touchdown|quarterback|seed|grand slam|f1|formula|nascar|box|boxing|wrestling)\b", case=False, regex=True) | \
              candidates['description'].str.contains(r"\b(football|soccer|nba|nfl|mlb|nhl|golf|tennis|olympic|cricket|rugby|baseball|basketball|hockey|coach|tournament|match|cup|league|playoff|goal|run|inning|touchdown|quarterback|seed|grand slam|f1|formula|nascar|box|boxing|wrestling)\b", case=False, regex=True)

sports_candidates = candidates[sports_mask]
# If none, scan all articles for max desc length within sports category
if sports_candidates.empty:
    sports_mask_all = df['title'].str.contains(r"\b(football|soccer|nba|nfl|mlb|nhl|golf|tennis|olympic|cricket|rugby|baseball|basketball|hockey|coach|tournament|match|cup|league|playoff|goal|run|inning|touchdown|quarterback|seed|grand slam|f1|formula|nascar|box|boxing|wrestling)\b", case=False, regex=True) | \
                     df['description'].str.contains(r"\b(football|soccer|nba|nfl|mlb|nhl|golf|tennis|olympic|cricket|rugby|baseball|basketball|hockey|coach|tournament|match|cup|league|playoff|goal|run|inning|touchdown|quarterback|seed|grand slam|f1|formula|nascar|box|boxing|wrestling)\b", case=False, regex=True)
    sports_df = df[sports_mask_all].copy()
    sports_df['desc_len'] = sports_df['description'].str.len()
    max_len = int(sports_df['desc_len'].max()) if len(sports_df) else 0
    sports_candidates = sports_df[sports_df['desc_len'] == max_len]

# pick first deterministically by title then article_id
if sports_candidates.empty:
    title = None
else:
    sports_candidates['article_id_num'] = pd.to_numeric(sports_candidates.get('article_id'), errors='coerce')
    sports_candidates = sports_candidates.sort_values(['title','article_id_num'], na_position='last')
    title = sports_candidates.iloc[0]['title']

print('__RESULT__:')
print(json.dumps({'title': title, 'max_description_length': max_len}))"""

env_args = {'var_call_hgWlxVr97vYyOQe145GrVZ9J': 'file_storage/call_hgWlxVr97vYyOQe145GrVZ9J.json'}

exec(code, env_args)
