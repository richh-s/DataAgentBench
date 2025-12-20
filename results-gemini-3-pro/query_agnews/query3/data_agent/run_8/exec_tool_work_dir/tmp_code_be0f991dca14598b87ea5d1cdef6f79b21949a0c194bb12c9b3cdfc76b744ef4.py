code = """import json
import pandas as pd
import os

# Load metadata
raw_meta = locals()['var_function-call-6219509864635122554']
if isinstance(raw_meta, str) and os.path.exists(raw_meta):
    with open(raw_meta, 'r') as f:
        meta_data = json.load(f)
else:
    meta_data = raw_meta

# Load articles chunk 1
raw_articles_1 = locals()['var_function-call-9198951727543333749']
if isinstance(raw_articles_1, str) and os.path.exists(raw_articles_1):
    with open(raw_articles_1, 'r') as f:
        articles_data_1 = json.load(f)
else:
    articles_data_1 = raw_articles_1

# Load articles chunk 2
raw_articles_2 = locals()['var_function-call-11629530409567554217']
if isinstance(raw_articles_2, str) and os.path.exists(raw_articles_2):
    with open(raw_articles_2, 'r') as f:
        articles_data_2 = json.load(f)
else:
    articles_data_2 = raw_articles_2

# Concatenate articles
# Use a dict to dedup by article_id in case of overlap (though query logic should prevent much overlap, IDs=100000 might be in both if strictness varied, but my split was <100000 and >=100000 effectively if I assume default sort)
# Actually, chunk 1 was "limit 100000", likely returned IDs 0 to 99999.
# Chunk 2 was ">= 100000".
# Safe to just concat.
all_articles = articles_data_1 + articles_data_2

df_meta = pd.DataFrame(meta_data)
df_articles = pd.DataFrame(all_articles)

# Convert IDs to string
df_meta['article_id'] = df_meta['article_id'].astype(str)
df_articles['article_id'] = df_articles['article_id'].astype(str)

# Dedup articles (just in case)
df_articles = df_articles.drop_duplicates(subset='article_id')

# Merge
df_merged = pd.merge(df_meta, df_articles, on='article_id', how='inner')

business_keywords = [
    'business', 'economy', 'economic', 'market', 'stock', 'shares', 'wall st', 
    'invest', 'finance', 'financial', 'trade', 'commerce', 'corporate', 'company', 
    'companies', 'profit', 'loss', 'bank', 'banking', 'dollar', 'euro', 'currency', 
    'oil', 'gold', 'price', 'rates', 'tax', 'deal', 'merger', 'acquisition', 
    'bond', 'recession', 'inflation', 'fed', 'treasury', 'carlyle', 'indus',
    'fund', 'funds', 'capital', 'sales', 'retail', 'consumer', 'spending', 'jobs', 
    'unemployment', 'growth', 'budget', 'deficit', 'debt', 'ipo', 'bid', 'sector', 
    'telecom', 'pharma', 'energy', 'export', 'import', 'tariff', 'wto', 'imf', 
    'world bank', 'central bank', 'ceo', 'cfo', 'earnings', 'quarter', 'revenue',
    'takeover', 'stake', 'shareholder', 'dividend', 'audit', 'credit', 'loan', 
    'mortgage', 'asset', 'wealth', 'rich', 'billion', 'million'
]

def is_business(row):
    text = (str(row.get('title', '')) + " " + str(row.get('description', ''))).lower()
    for kw in business_keywords:
        if kw in text:
            return True
    return False

df_merged['is_business'] = df_merged.apply(is_business, axis=1)

# Group by year
years = [str(y) for y in range(2010, 2021)]
yearly_counts = df_merged[df_merged['is_business']].groupby('year').size()
yearly_counts = yearly_counts.reindex(years, fill_value=0)

average_business = yearly_counts.mean()

print("__RESULT__:")
print(json.dumps({
    "yearly_counts": yearly_counts.to_dict(),
    "average": average_business,
    "total_merged": len(df_merged),
    "total_business": int(yearly_counts.sum())
}))"""

env_args = {'var_function-call-6219509864635122554': 'file_storage/function-call-6219509864635122554.json', 'var_function-call-11799845015617883549': 14860, 'var_function-call-4236489543979189159': [{'_id': '6944c5604aa2a519adff7871', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944c5604aa2a519adff7872', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944c5604aa2a519adff7873', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944c5604aa2a519adff7874', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944c5604aa2a519adff7875', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-13155074376232017203': [{'_id': '6944c5604aa2a519adff7871', 'article_id': '0'}], 'var_function-call-6391207851705770972': [{'_id': '6944c5604aa2a519adff7871', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944c5604aa2a519adff7872', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944c5604aa2a519adff7873', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944c5604aa2a519adff7874', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944c5604aa2a519adff7875', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-8907977861956983750': {'yearly_counts': {'2010': 0, '2011': 0, '2012': 0, '2013': 0, '2014': 0, '2015': 0, '2016': 0, '2017': 0, '2018': 0, '2019': 0, '2020': 1}, 'average': 0.09090909090909091}, 'var_function-call-15600574861589181131': {'meta_count': 14860, 'articles_count': 5, 'merged_count': 14860, 'merged_with_title_count': 1, 'sample_meta_ids': ['3', '9', '13', '14', '21'], 'sample_article_ids': ['0', '1', '2', '3', '4']}, 'var_function-call-9198951727543333749': 'file_storage/function-call-9198951727543333749.json', 'var_function-call-5505010622256258402': {'yearly_counts': {'2010': 451, '2011': 476, '2012': 476, '2013': 485, '2014': 478, '2015': 498, '2016': 485, '2017': 528, '2018': 489, '2019': 483, '2020': 494}, 'average': 485.72727272727275, 'total_merged': 11622, 'total_business': 5343}, 'var_function-call-15278340528422340182': 127583, 'var_function-call-15272939461622660653': 'file_storage/function-call-15272939461622660653.json', 'var_function-call-16916188678692330719': 'file_storage/function-call-16916188678692330719.json', 'var_function-call-13400531891492422196': [{'_id': '6944c5624aa2a519ad00ff11', 'article_id': '100000', 'title': 'Venezuelan Car-Bomb Suspect Killed, Weapons Found', 'description': " CARACAS, Venezuela (Reuters) - A Venezuelan lawyer  suspected in last week's bombing murder of a top state  prosecutor was killed in a gunfight with police on Tuesday  after he tried to ram detectives with his car and opened fire  on them, officials said."}, {'_id': '6944c5624aa2a519ad00ff12', 'article_id': '100001', 'title': 'British Muslims push to integrate', 'description': 'They are working to repair an image tattered by homegrown radicals - and to find a place in mainstream society.'}, {'_id': '6944c5624aa2a519ad00ff13', 'article_id': '100002', 'title': 'Ukraine set for talks on crisis', 'description': "Ukraine's president and opposition agree to hold talks, as huge protests over disputed elections continue."}, {'_id': '6944c5624aa2a519ad00ff14', 'article_id': '100003', 'title': 'Smoking killing millions globally', 'description': '\\Smoking killed almost 5 million people around the world in 2000, researchers have calculated.'}, {'_id': '6944c5624aa2a519ad00ff15', 'article_id': '100004', 'title': 'Outsource that reporter!', 'description': 'Reuters journalists are said to be close to striking over the outsourcing of reporting jobs to India.'}], 'var_function-call-11629530409567554217': 'file_storage/function-call-11629530409567554217.json'}

exec(code, env_args)
