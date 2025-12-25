code = """import json
import pandas as pd
import re

meta_path = locals()['var_function-call-1304167582762502927']
articles_path = locals()['var_function-call-4198962169091228890']

with open(meta_path, 'r') as f:
    meta_data = json.load(f)
with open(articles_path, 'r') as f:
    articles_data = json.load(f)

df_meta = pd.DataFrame(meta_data)
df_articles = pd.DataFrame(articles_data)

df_meta['article_id'] = df_meta['article_id'].astype(int)
df_articles['article_id'] = df_articles['article_id'].astype(int)

df = pd.merge(df_meta, df_articles, on='article_id', how='inner')

sample_titles = df['title'].head(5).tolist()

keywords = ["economy", "market"] 
def check(text):
    text = text.lower()
    found = []
    for kw in keywords:
        if re.search(r'\b' + re.escape(kw) + r'\b', text):
            found.append(kw)
    return found

df['matches'] = df.apply(lambda row: check(str(row['title']) + " " + str(row['description'])), axis=1)
match_count = df['matches'].apply(lambda x: len(x) > 0).sum()

debug_info = {
    "sample_titles": sample_titles,
    "match_count_simple": int(match_count)
}

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-1304167582762502927': 'file_storage/function-call-1304167582762502927.json', 'var_function-call-641571560304296616': 'file_storage/function-call-641571560304296616.json', 'var_function-call-5674583780523164016': [{'_id': '6944d845bdad7807dc849895', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944d845bdad7807dc849896', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944d845bdad7807dc849897', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944d845bdad7807dc849898', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944d845bdad7807dc849899', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-4198962169091228890': 'file_storage/function-call-4198962169091228890.json', 'var_function-call-16544878985627064892': 84.0, 'var_function-call-13466724560110333408': 0.0, 'var_function-call-16025191490921363899': 'debug'}

exec(code, env_args)
