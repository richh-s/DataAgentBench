code = """import json, pandas as pd

with open(var_call_0BzdDYLpl9Zeobve7HyBANz7, 'r') as f:
    metadata = json.load(f)

articles = var_call_dYwNCDf02raheYLZp19Gh8z4

md_df = pd.DataFrame(metadata)
art_df = pd.DataFrame(articles)

md_df['year'] = md_df['publication_date'].str.slice(0,4).astype(int)
md_2015 = md_df[md_df['year'] == 2015].copy()

md_2015['article_id'] = md_2015['article_id'].astype(str)
art_df['article_id'] = art_df['article_id'].astype(str)

merged = md_2015.merge(art_df, on='article_id', how='inner')

world_keywords = ['war','election','president','government','iraq','united nations','u.n.','terror','conflict','minister','parliament','troops','bomb','attack','peace','diplomat','allies','alliance','foreign','embassy','summit','nato','palestinian','israel','afghanistan','pakistan','nuclear','missile','sanction','refugee','border','crisis']

def is_world(title, desc):
    text = (str(title) + ' ' + str(desc)).lower()
    return any(k in text for k in world_keywords)

if not merged.empty:
    merged['is_world'] = merged.apply(lambda r: is_world(r['title'], r['description']), axis=1)
    world_df = merged[merged['is_world']]
    counts = world_df.groupby('region').size().sort_values(ascending=False)
    answer = counts.index[0] if not counts.empty else None
else:
    answer = None

print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_0BzdDYLpl9Zeobve7HyBANz7': 'file_storage/call_0BzdDYLpl9Zeobve7HyBANz7.json', 'var_call_dYwNCDf02raheYLZp19Gh8z4': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_call_lJQfa5RsNVFZppTooEH8vBbE': {'md_cols': ['article_id', 'region', 'publication_date'], 'art_cols': ['article_id', 'title', 'description']}}

exec(code, env_args)
