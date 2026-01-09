code = """import json, pandas as pd

# load metadata 2015
path_meta = var_call_7wQlNKxSgi2WCehLh2BOx9pn
with open(path_meta, 'r') as f:
    meta = json.load(f)
meta_df = pd.DataFrame(meta)
meta_df['article_id'] = meta_df['article_id'].astype(str)

# load articles
path_art = var_call_FH1eyV1XWkMZ4b7OYV8PRjtY
with open(path_art, 'r') as f:
    arts = json.load(f)
arts_df = pd.DataFrame(arts)
arts_df['article_id'] = arts_df['article_id'].astype(str)

# join only 2015 articles
df = meta_df.merge(arts_df, on='article_id', how='left')

def categorize(title, desc):
    text = ((title or '') + ' ' + (desc or '')).lower()
    sports = ['sport', 'sports', 'game', 'match', 'tournament', 'league', 'nba', 'nfl', 'mlb', 'nhl', 'soccer', 'football', 'cricket', 'tennis', 'golf', 'olympic', 'olympics', 'fifa', 'coach', 'player', 'team']
    business = ['stock', 'market', 'shares', 'ipo', 'earnings', 'profit', 'revenue', 'economy', 'economic', 'trade', 'inflation', 'bank', 'banks', 'opec', 'oil', 'crude', 'currency', 'dollar', 'euro', 'imf', 'central bank', 'interest rate', 'merger', 'acquisition', 'aerospace', 'fund', 'invest', 'investment', 'prices']
    sci = ['science', 'scientist', 'research', 'technology', 'tech', 'internet', 'software', 'hardware', 'ai', 'artificial intelligence', 'computer', 'google', 'nasa', 'space', 'physics', 'biology', 'medical', 'medicine', 'health', 'genome', 'climate', 'robot', 'cyber', 'quantum']
    # score by keyword hits
    def score(keys):
        return sum(1 for k in keys if k in text)
    s_sports = score(sports)
    s_business = score(business)
    s_sci = score(sci)
    # world as default; but if explicit geo/politics/conflict terms push world
    world_terms = ['president', 'government', 'election', 'war', 'conflict', 'iraq', 'iran', 'china', 'russia', 'israel', 'palestinian', 'un', 'united nations', 'nato', 'refugee', 'terror', 'attack', 'military', 'pipeline', 'export', 'sanctions', 'diplomat']
    s_world = score(world_terms)

    # choose max among sports/business/sci; if none significant or world higher, World
    max_other = max(s_sports, s_business, s_sci)
    if max_other == 0:
        return 'World'
    # if world dominates others by >=1 and reasonably present
    if s_world >= max_other and s_world > 0:
        return 'World'
    if s_sports == max_other and s_sports >= s_business and s_sports >= s_sci:
        return 'Sports'
    if s_business == max_other and s_business >= s_sci:
        return 'Business'
    return 'Science/Technology'


df['category'] = [categorize(t, d) for t, d in zip(df['title'], df['description'])]
world_df = df[df['category'] == 'World']
counts = world_df.groupby('region').size().sort_values(ascending=False)
if counts.empty:
    result = {'region': None, 'world_articles_2015': 0}
else:
    top_region = counts.index[0]
    result = {'region': str(top_region), 'world_articles_2015': int(counts.iloc[0])}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_7wQlNKxSgi2WCehLh2BOx9pn': 'file_storage/call_7wQlNKxSgi2WCehLh2BOx9pn.json', 'var_call_FH1eyV1XWkMZ4b7OYV8PRjtY': 'file_storage/call_FH1eyV1XWkMZ4b7OYV8PRjtY.json'}

exec(code, env_args)
