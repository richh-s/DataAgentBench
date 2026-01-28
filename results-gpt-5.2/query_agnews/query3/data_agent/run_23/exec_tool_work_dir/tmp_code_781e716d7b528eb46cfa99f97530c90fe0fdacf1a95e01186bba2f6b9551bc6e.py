code = """import json, pandas as pd

# Load metadata (Europe, 2010-2020) from file
meta_path = var_call_a1gmGS1B5SFqqF6V5yANVSOB
with open(meta_path, 'r', encoding='utf-8') as f:
    meta = json.load(f)

arts = var_call_NpIlVVLUrcfI0AIo9ZPwM5Le

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# Normalize ids to int where possible
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# Join
df = meta_df.merge(arts_df, on='article_id', how='inner')

# Basic Business classifier via keywords
business_kw = [
    'stock','stocks','market','markets','wall st','wall street','dow','nasdaq','s&p',
    'earnings','profit','revenue','sales','ipo','shares','share','bond','bonds','yield',
    'inflation','gdp','economy','economic','central bank','ecb','interest rate','rates',
    'bank','banks','banking','loan','loans','credit','debt','currency','euro','dollar',
    'oil','crude','gas','energy','opec','gold','commodity','commodities',
    'trade','tariff','exports','imports','business','company','companies','corporate',
    'merger','acquisition','buyout','invest','investment','investor','hedge fund',
    'unemployment','jobs','employment','retail','consumer','housing','real estate',
    'inflation','deficit','budget','tax'
]

def is_business(title, desc):
    t = ((title or '') + ' ' + (desc or '')).lower()
    return any(k in t for k in business_kw)

df['is_business'] = [is_business(t,d) for t,d in zip(df.get('title',''), df.get('description',''))]

biz = df[df['is_business']].copy()
biz['year'] = pd.to_datetime(biz['publication_date'], errors='coerce').dt.year
biz = biz[(biz['year']>=2010) & (biz['year']<=2020)]

counts = biz.groupby('year')['article_id'].nunique().reindex(range(2010,2021), fill_value=0)
avg_per_year = counts.mean()

out = {
    'average_business_articles_per_year_europe_2010_2020': float(avg_per_year),
    'total_business_articles': int(counts.sum()),
    'years': 11
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_a1gmGS1B5SFqqF6V5yANVSOB': 'file_storage/call_a1gmGS1B5SFqqF6V5yANVSOB.json', 'var_call_NpIlVVLUrcfI0AIo9ZPwM5Le': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
