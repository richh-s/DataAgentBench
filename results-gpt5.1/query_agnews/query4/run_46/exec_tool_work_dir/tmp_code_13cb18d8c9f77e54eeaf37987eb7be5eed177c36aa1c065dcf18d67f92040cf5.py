code = """import json, pandas as pd

articles = pd.DataFrame(var_call_zHN1DCMb1RUeVvy7Ol1CfTeC)

with open(var_call_xsQiJeAHUNxwh4Zy19oIkUgz, 'r') as f:
    meta = pd.DataFrame(json.load(f))

world_keywords = ['world', 'global', 'international', 'abroad', 'foreign', 'iraq', 'afghanistan', 'europe', 'asia', 'africa', 'latin america', 'middle east']

def is_world(row):
    text = f"{row['title']} {row['description']}".lower()
    return any(k in text for k in world_keywords)

articles['article_id'] = articles['article_id'].astype(int)
articles['is_world'] = articles.apply(is_world, axis=1)

world_articles = articles[articles['is_world']]

merged = pd.merge(meta, world_articles[['article_id']], on='article_id', how='inner')

counts = merged.groupby('region').size().sort_values(ascending=False)

result = {
    'region_with_most_world_articles_2015': counts.idxmax() if not counts.empty else None,
    'counts_by_region': counts.to_dict()
}

result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_zHN1DCMb1RUeVvy7Ol1CfTeC': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_call_xsQiJeAHUNxwh4Zy19oIkUgz': 'file_storage/call_xsQiJeAHUNxwh4Zy19oIkUgz.json'}

exec(code, env_args)
