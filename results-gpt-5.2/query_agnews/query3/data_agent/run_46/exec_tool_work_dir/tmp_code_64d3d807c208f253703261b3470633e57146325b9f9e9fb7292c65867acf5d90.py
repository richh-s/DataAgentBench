code = """import json, pandas as pd

def load_records(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

meta = load_records(var_call_WYEwp4oVXrumBGA8BBUIUcro)
arts = load_records(var_call_tjiZ4kxdtDtgGb52s4YgQ0io)

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# normalize ids
meta_df['article_id'] = meta_df['article_id'].astype(str)
arts_df['article_id'] = arts_df['article_id'].astype(str)

# join europe 2010-2020 with content
df = meta_df.merge(arts_df, on='article_id', how='inner')

# simple rule-based business classifier using title+description keywords
text = (df['title'].fillna('') + ' ' + df['description'].fillna('')).str.lower()

business_terms = [
    'stock','stocks','wall st','wall street','dow','nasdaq','s&p','earnings','profit','revenue',
    'market','markets','shares','ipo','bond','bonds','yield','yields','inflation','gdp','economy',
    'economic','central bank','ecb','fed','interest rate','rates','currency','euro','pound','dollar',
    'oil','crude','gas','opec','gold','commodit','bank','banks','banking','loan','loans','credit',
    'mortgage','housing','real estate','deal','merger','acquisition','m&a','company','companies',
    'corporate','ceo','cfo','invest','investment','investor','fund','hedge','private equity',
    'trade','tariff','import','export','unemployment'
]

def is_business(s):
    for term in business_terms:
        if term in s:
            return True
    return False

biz_mask = text.apply(is_business)
biz_df = df[biz_mask].copy()

biz_df['year'] = biz_df['publication_date'].str.slice(0,4).astype(int)
counts = biz_df.groupby('year')['article_id'].nunique().reindex(range(2010,2021), fill_value=0)
avg_per_year = counts.mean()

out = {
    'average_business_articles_per_year_europe_2010_2020': float(avg_per_year),
    'total_business_articles_europe_2010_2020': int(counts.sum()),
    'years': list(range(2010,2021))
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_WYEwp4oVXrumBGA8BBUIUcro': 'file_storage/call_WYEwp4oVXrumBGA8BBUIUcro.json', 'var_call_tjiZ4kxdtDtgGb52s4YgQ0io': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
