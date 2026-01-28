code = """import json, pandas as pd

# Load Europe metadata (may be file path)
meta = var_call_ZO6JGjT02rHk4OX3c7fhViLz
if isinstance(meta, str):
    with open(meta, 'r', encoding='utf-8') as f:
        meta = json.load(f)

arts = var_call_SqM7s38g5Qnzcvy0QqUpDDoS

mdf = pd.DataFrame(meta)
adf = pd.DataFrame(arts)

# Normalize ids to int
mdf['article_id'] = mdf['article_id'].astype(int)
adf['article_id'] = adf['article_id'].astype(int)

# Join
df = mdf.merge(adf, on='article_id', how='inner')

# Classify Business using a keyword heuristic
text = (df['title'].fillna('') + ' ' + df['description'].fillna('')).str.lower()

business_kw = [
    'wall st','stock','stocks','shares','share','market','markets','dow','nasdaq','s&p','sp500',
    'earnings','profit','revenue','quarter','q1','q2','q3','q4','ipo','bond','bonds','yield',
    'fed','central bank','interest rate','inflation','gdp','economy','economic','recession',
    'bank','banks','banking','loan','loans','credit','mortgage','currency','forex','dollar','euro','yen',
    'oil','crude','gas','opec','barrel','brent','wti','commodity','commodities','gold',
    'company','companies','corporate','ceo','cfo','merger','acquisition','takeover','deal',
    'investment','investor','fund','hedge','private equity','carlyle','venture',
    'airline','automaker','tech company','retail','sales','unemployment','jobs','wage'
]

pattern = r'(' + '|'.join([pd.regex.escape(k) if hasattr(pd, 'regex') else k for k in business_kw]) + r')'
# pandas doesn't have pd.regex.escape; use re
import re
pattern = r'(' + '|'.join([re.escape(k) for k in business_kw]) + r')'

is_business = text.str.contains(pattern, regex=True)

df = df[is_business].copy()

# Year
df['year'] = pd.to_datetime(df['publication_date'], errors='coerce').dt.year

yearly = df.groupby('year').size().reindex(range(2010, 2021), fill_value=0)
avg = yearly.mean()

out = json.dumps({
    'average_business_articles_per_year_europe_2010_2020': float(avg),
    'total_business_articles_europe_2010_2020': int(yearly.sum()),
    'years_counted': 11
})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_ZO6JGjT02rHk4OX3c7fhViLz': 'file_storage/call_ZO6JGjT02rHk4OX3c7fhViLz.json', 'var_call_SqM7s38g5Qnzcvy0QqUpDDoS': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
