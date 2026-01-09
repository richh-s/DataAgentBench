code = """import json, pandas as pd

# Load metadata (may be a file path)
meta_src = var_call_36TKClVHghhekT0eMBHrQUhs
if isinstance(meta_src, str):
    with open(meta_src, 'r', encoding='utf-8') as f:
        meta = json.load(f)
else:
    meta = meta_src

articles = var_call_pO3brncXCq31YhqBeEVlCpnp

meta_df = pd.DataFrame(meta)
art_df = pd.DataFrame(articles)

# normalize ids
def norm_id(x):
    try:
        return int(str(x).strip())
    except Exception:
        return None
meta_df['article_id'] = meta_df['article_id'].map(norm_id)
art_df['article_id'] = art_df['article_id'].map(norm_id)

# parse year
meta_df['year'] = pd.to_datetime(meta_df['publication_date'], errors='coerce').dt.year
meta_df = meta_df[(meta_df['year']>=2010) & (meta_df['year']<=2020) & (meta_df['region']=='Europe')]

# join to get title/description
j = meta_df.merge(art_df, on='article_id', how='left')

# classify business using simple keyword heuristic
text = (j['title'].fillna('') + ' ' + j['description'].fillna('')).str.lower()
keywords = [
    'stock','stocks','wall st','wall street','dow','nasdaq','s&p','market','markets','shares','bond','bonds',
    'earnings','profit','revenue','quarter','ipo','merger','acquisition','deal','bank','banks','banking',
    'central bank','ecb','fed','interest rate','rates','inflation','gdp','economy','economic','trade','tariff',
    'oil','crude','gas','opec','company','companies','corporate','ceo','cfo','investment','investor','fund',
    'currency','euro','dollar','pound','forex','bitcoin','crypto','startup','retail','sales','manufacturing'
]
pattern = '|'.join([pd.regex.escape(k) if hasattr(pd, 'regex') else k for k in keywords])
# pandas doesn't have pd.regex.escape; use re
import re
pattern = '|'.join([re.escape(k) for k in keywords])
is_business = text.str.contains(pattern, regex=True)

biz = j[is_business].copy()
counts = biz.groupby('year').size().reindex(range(2010,2021), fill_value=0)
avg_per_year = counts.mean()

result = {
    'average_business_articles_per_year_europe_2010_2020': float(avg_per_year),
    'total_business_articles': int(counts.sum()),
    'years': 11
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_36TKClVHghhekT0eMBHrQUhs': 'file_storage/call_36TKClVHghhekT0eMBHrQUhs.json', 'var_call_pO3brncXCq31YhqBeEVlCpnp': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
