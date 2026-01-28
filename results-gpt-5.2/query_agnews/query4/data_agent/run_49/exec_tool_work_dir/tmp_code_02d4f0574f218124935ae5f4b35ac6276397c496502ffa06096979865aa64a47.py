code = """import json, pandas as pd

meta = var_call_UZ3HKRWywFBYVd9Shp5L7Y3x
if isinstance(meta, str):
    with open(meta, 'r', encoding='utf-8') as f:
        meta = json.load(f)
meta_df = pd.DataFrame(meta)
meta_df['article_id'] = meta_df['article_id'].astype(int)

article_ids = meta_df['article_id'].unique().tolist()
chunk_size = 500
articles = []
for i in range(0, len(article_ids), chunk_size):
    chunk = article_ids[i:i+chunk_size]
    q = {
        "collection": "articles",
        "filter": {"article_id": {"$in": chunk}},
        "projection": {"_id": 0, "article_id": 1, "title": 1, "description": 1},
        "limit": len(chunk)
    }
    res = query_db(db_name="articles_database", query=json.dumps(q))
    articles.extend(res)

art_df = pd.DataFrame(articles)
art_df['article_id'] = art_df['article_id'].astype(int)
art_df['title'] = art_df.get('title', '').fillna('')
art_df['description'] = art_df.get('description', '').fillna('')

sports_kw = ['match','tournament','league','cup','goal','coach','player','season','nba','nfl','mlb','nhl','fifa','uefa','olympic','grand slam','cricket','tennis','soccer','football','basketball','baseball','hockey','golf','formula 1','f1']
business_kw = ['stock','stocks','market','markets','shares','earnings','revenue','profit','merger','acquisition','ipo','fed','inflation','gdp','economy','economic','bank','banks','oil','brent','wti','dollar','euro','currency','trade','tariff','company','companies','ceo','startup','unemployment']
sci_kw = ['software','app','apps','smartphone','iphone','android','google','microsoft','apple','amazon','facebook','twitter','ai','artificial intelligence','robot','robots','space','nasa','rocket','satellite','gene','genetic','dna','climate','temperature','research','study','scientists','quantum','cyber','hack','hacker','internet','chip','semiconductor']

def classify(text):
    t = str(text).lower()
    if any(k in t for k in sports_kw):
        return 'Sports'
    if any(k in t for k in business_kw):
        return 'Business'
    if any(k in t for k in sci_kw):
        return 'Science/Technology'
    return 'World'

art_df['full_text'] = (art_df['title'].astype(str) + ' ' + art_df['description'].astype(str)).str.strip()
art_df['category'] = art_df['full_text'].apply(classify)

world_ids = set(art_df.loc[art_df['category']=='World','article_id'].tolist())
world_meta = meta_df[meta_df['article_id'].isin(world_ids)]
counts = world_meta.groupby('region').size().sort_values(ascending=False)

max_count = int(counts.iloc[0]) if len(counts)>0 else 0
top_regions = counts[counts==max_count].index.tolist()

out = {"top_regions": top_regions, "world_article_count": max_count}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_UZ3HKRWywFBYVd9Shp5L7Y3x': 'file_storage/call_UZ3HKRWywFBYVd9Shp5L7Y3x.json'}

exec(code, env_args)
