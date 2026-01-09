code = """import json, pandas as pd

# Load Europe metadata (possibly from file)
meta = var_call_WZfFscRjC9nxjG8JWFDNZXSK
if isinstance(meta, str):
    with open(meta, 'r') as f:
        meta = json.load(f)

a = var_call_lPDskkqUxb7iBk87TZmtgXUU
# articles query returned directly list
articles = a

df_meta = pd.DataFrame(meta)
df_articles = pd.DataFrame(articles)

# Normalize types
for col in ['article_id']:
    df_meta[col] = pd.to_numeric(df_meta[col], errors='coerce')
    df_articles[col] = pd.to_numeric(df_articles[col], errors='coerce')

df_meta = df_meta.dropna(subset=['article_id','publication_date'])
df_articles = df_articles.dropna(subset=['article_id'])

# Merge
df = df_meta.merge(df_articles, on='article_id', how='inner')

# Simple keyword-based business classifier
text = (df['title'].fillna('') + ' ' + df['description'].fillna('')).str.lower()

business_kw = [
    'stock','stocks','wall st','wall street','nasdaq','dow','s&p','share','shares','equity','equities','bond','bonds','yield','yields',
    'market','markets','earnings','profit','revenue','quarter','ipo','merger','acquisition','acquire','takeover',
    'bank','banks','banking','fed','ecb','central bank','interest rate','rates','inflation',
    'oil','crude','brent','wti','gas','energy','opec',
    'currency','currencies','forex','dollar','euro','yen','pound',
    'economy','economic','gdp','recession','trade','tariff','exports','import',
    'company','companies','corporate','ceo','startup','invest','investment','fund','hedge',
    'unemployment','jobs report','consumer','retail','sales'
]
pattern = r'(' + '|'.join([pd.re.escape(k) for k in business_kw]) + r')'

is_business = text.str.contains(pattern, regex=True, na=False)

df_biz = df[is_business].copy()
df_biz['year'] = pd.to_datetime(df_biz['publication_date'], errors='coerce').dt.year

df_biz = df_biz[(df_biz['year']>=2010) & (df_biz['year']<=2020)]

counts = df_biz.groupby('year').size().reindex(range(2010,2021), fill_value=0)
avg_per_year = counts.mean()

result = {
    'average_business_articles_per_year_europe_2010_2020': float(avg_per_year),
    'total_business_articles': int(counts.sum()),
    'years': 11
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_WZfFscRjC9nxjG8JWFDNZXSK': 'file_storage/call_WZfFscRjC9nxjG8JWFDNZXSK.json', 'var_call_lPDskkqUxb7iBk87TZmtgXUU': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
