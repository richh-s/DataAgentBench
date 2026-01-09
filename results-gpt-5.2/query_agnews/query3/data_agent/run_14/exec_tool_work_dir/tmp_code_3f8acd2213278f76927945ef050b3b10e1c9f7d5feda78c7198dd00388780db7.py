code = """import json, pandas as pd

# load europe metadata
path = var_call_wg8Qp8qMEGpdziDbTlR3lNOw
with open(path, 'r', encoding='utf-8') as f:
    europe = json.load(f)

df_meta = pd.DataFrame(europe)
df_meta['article_id'] = df_meta['article_id'].astype(int)

df_art = pd.DataFrame(var_call_sLtsc8mKE3JWrlS4cUrd0b7i)
df_art['article_id'] = df_art['article_id'].astype(int)

df = df_meta.merge(df_art, on='article_id', how='inner')

# classify business via simple keyword rules on title+description
text = (df['title'].fillna('') + ' ' + df['description'].fillna('')).str.lower()

business_kw = [
    'stocks','stock','wall st','wall street','market','markets','shares','equity','equities',
    'earnings','profit','profits','revenue','sales','ipo','nasdaq','dow','s&p',
    'bank','banks','banking','finance','financial','fed','central bank','interest rate','rates',
    'economy','economic','inflation','gdp','recession','growth','unemployment',
    'oil','crude','gas','opec','pipeline','export','imports','trade','tariff',
    'company','companies','firm','merger','acquisition','takeover','ceo','cfo',
    'investment','investor','fund','hedge','private equity','carlyle'
]
pattern = '|'.join([pd.regex.escape(k) if hasattr(pd, 'regex') else k for k in business_kw])
# pandas doesn't have regex.escape; use re
import re
pattern = '|'.join([re.escape(k) for k in business_kw])

is_business = text.str.contains(pattern, regex=True)

df_bus = df[is_business].copy()

counts = df_bus.groupby('year').size().reindex([str(y) for y in range(2010,2021)], fill_value=0)
avg = counts.mean()

out = {
    'average_business_articles_per_year_europe_2010_2020': float(avg),
    'total_business_articles_2010_2020': int(counts.sum()),
    'years_counted': 11
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_wg8Qp8qMEGpdziDbTlR3lNOw': 'file_storage/call_wg8Qp8qMEGpdziDbTlR3lNOw.json', 'var_call_sLtsc8mKE3JWrlS4cUrd0b7i': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
