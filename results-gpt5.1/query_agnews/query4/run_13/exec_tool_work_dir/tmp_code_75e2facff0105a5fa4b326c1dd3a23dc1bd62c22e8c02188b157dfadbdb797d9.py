code = """import json, pandas as pd

data_path = var_call_6oGomQDIjNQn7Row7g8BPqi9
with open(data_path, 'r') as f:
    metadata = json.load(f)

articles = var_call_vjzI9nr6XHcNa9d6w6ypCr7U

md_df = pd.DataFrame(metadata)
art_df = pd.DataFrame(articles)

md_df['article_id'] = pd.to_numeric(md_df['article_id'], errors='coerce')
art_df['article_id'] = pd.to_numeric(art_df['article_id'], errors='coerce')

world_keywords = ['iraq', 'u.n.', 'united nations', 'palestinian', 'israel', 'afghanistan', 'bomb', 'rebel', 'election', 'president', 'terror', 'war', 'military', 'government', 'prime minister']

def is_world(row):
    text = (str(row.get('title', '')) + ' ' + str(row.get('description', ''))).lower()
    return any(kw in text for kw in world_keywords)

art_df['is_world'] = art_df.apply(is_world, axis=1)

merged = md_df.merge(art_df[['article_id', 'is_world']], on='article_id', how='left')

merged['is_world'] = merged['is_world'].fillna(False)

world_2015 = merged[merged['is_world'] == True]

counts = world_2015.groupby('region').size().sort_values(ascending=False)

if len(counts) == 0:
    result = None
else:
    top_region = counts.index[0]
    result = top_region

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_6oGomQDIjNQn7Row7g8BPqi9': 'file_storage/call_6oGomQDIjNQn7Row7g8BPqi9.json', 'var_call_vjzI9nr6XHcNa9d6w6ypCr7U': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
