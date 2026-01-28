code = """import json, pandas as pd

# Load metadata (may be file path)
meta_src = var_call_F3TIUIFzl6Mov089DjzzkF9C
if isinstance(meta_src, str):
    with open(meta_src, 'r', encoding='utf-8') as f:
        meta = json.load(f)
else:
    meta = meta_src

arts = var_call_suIJzYH6ElBumIH46bDbDeCH

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# Normalize types
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# Join Europe 2010-2020 with article text
df = meta_df.merge(arts_df, on='article_id', how='inner')

text = (df['title'].fillna('') + ' ' + df['description'].fillna('')).str.lower()

# Simple keyword-based business classifier
biz_kw = [
    'business','market','markets','stock','stocks','shares','wall st','wall street','dow','nasdaq','s&p',
    'bank','banks','banking','loan','loans','credit','mortgage','bond','bonds','yield','treasury',
    'economy','economic','gdp','inflation','deflation','recession','growth','jobs','unemployment',
    'oil','crude','gas','energy','opec','price','prices','commodity','commodities',
    'company','companies','corporate','earnings','profit','profits','revenue','sales','merger','acquisition','ipo',
    'investment','investor','investors','fund','hedge','private equity','carlyle',
    'trade','tariff','exports','imports','currency','dollar','euro','yen','forex','exchange rate',
    'central bank','ecb','fed','interest rate','rates'
]
pattern = '|'.join([pd.regex.escape(k) for k in biz_kw])
# pandas doesn't have regex.escape; use re
import re
pattern = '|'.join([re.escape(k) for k in biz_kw])

is_business = text.str.contains(pattern, regex=True)

df['year'] = pd.to_datetime(df['publication_date'], errors='coerce').dt.year
biz_counts = df[is_business].groupby('year')['article_id'].count().reindex(range(2010, 2021), fill_value=0)

avg_per_year = biz_counts.mean()

out = {
    'average_business_articles_per_year_europe_2010_2020': float(avg_per_year),
    'total_business_articles_2010_2020': int(biz_counts.sum()),
    'years_counted': 11
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_F3TIUIFzl6Mov089DjzzkF9C': 'file_storage/call_F3TIUIFzl6Mov089DjzzkF9C.json', 'var_call_suIJzYH6ElBumIH46bDbDeCH': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
