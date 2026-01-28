code = """import json, pandas as pd
path = var_call_uqdlqnHwoyhnos3S9z0Br2aQ
with open(path,'r',encoding='utf-8') as f:
    cand = json.load(f)
df = pd.DataFrame(cand)
# sports keywords heuristic
kw = r"\b(nfl|nba|mlb|nhl|ncaa|soccer|football|baseball|basketball|hockey|tennis|golf|olymp|world cup|championship|playoff|quarterback|touchdown|home run|coach|team|vs\.?|at\s+no\.?|stadium|tickets|season)\b"
mask = df['title'].str.lower().str.contains(kw, regex=True, na=False)
df_s = df[mask].copy()
# pick longest desc among these candidates by reloading full descriptions from main dataset file
main_path = var_call_0HNmqm4wqN6v5lk90DqStdOT
with open(main_path,'r',encoding='utf-8') as f:
    recs = json.load(f)
main = pd.DataFrame(recs)[['article_id','title','description']]
main['desc_len']=main['description'].fillna('').map(len)
merged = main.merge(df_s[['article_id']], on='article_id', how='inner')
row = merged.sort_values(['desc_len','article_id'], ascending=[False, True]).head(1)
ans = row[['title']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(ans))"""

env_args = {'var_call_0HNmqm4wqN6v5lk90DqStdOT': 'file_storage/call_0HNmqm4wqN6v5lk90DqStdOT.json', 'var_call_pexuNncc1BpI9RkDyr1D0D7T': [], 'var_call_8xPFkBCfbaNPlaKXgrOVDk7r': [], 'var_call_03p80bmyGOoafnQu34eShb2x': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'author_id': '992', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'author_id': '820', 'region': 'South America', 'publication_date': '2021-02-04'}, {'article_id': '3', 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '4', 'author_id': '39', 'region': 'Africa', 'publication_date': '2012-02-01'}], 'var_call_uqdlqnHwoyhnos3S9z0Br2aQ': 'file_storage/call_uqdlqnHwoyhnos3S9z0Br2aQ.json', 'var_call_kXiJntOM5xbwsrm33vrJxqqS': [], 'var_call_RBmwIIMx5uQjKOK43ojFWGSO': [{'article_id': '31510', 'title': 'Cavaliers, Hokies Play Host', 'description': "Akron at No. 12 Virginia &lt;br&gt;   Where:  Scott Stadium, Charlottesville&lt;br&gt;   When:  3 p.m.    Radio:  WTNT-570    Tickets:  Sold out &lt;br&gt;   Another Top QB:  Like North Carolina's Darian Durant last week, Akron quarterback Charlie Frye is the key to his team's slim chances of upsetting the Cavaliers. The 6-foot-4 senior, likened by Virginia Coach Al Groh to recent ACC stars Matt Schaub and Philip Rivers, ranks fourth among active NCAA quarterbacks with 9,048 career passing yards. In losses the past two weeks to Penn State and Middle Tennessee, Frye completed 60 of 80 passes for 622 yards. Weather permitting, he will present a challenge for an inexperienced Virginia secondary that made a few too many errors in deep coverage in its first two games."}]}

exec(code, env_args)
