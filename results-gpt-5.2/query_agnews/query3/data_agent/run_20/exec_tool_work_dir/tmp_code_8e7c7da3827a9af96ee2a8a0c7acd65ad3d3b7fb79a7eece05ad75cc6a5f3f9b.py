code = """import json, pandas as pd

# Load Europe metadata rows (possibly file path)
meta_src = var_call_4tk1Qyuk8zuCB8iZticbrmVt
if isinstance(meta_src, str):
    with open(meta_src, 'r') as f:
        meta = json.load(f)
else:
    meta = meta_src

arts = var_call_nETuVEREXJvl4INmD7RZGqnf

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# Normalize types
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# Join to get title/description for Europe 2010-2020
df = meta_df.merge(arts_df, on='article_id', how='inner')

# Simple keyword-based business classifier
text = (df['title'].fillna('') + ' ' + df['description'].fillna('')).str.lower()

def is_business(s):
    kws = [
        'stock','stocks','shares','share','market','markets','wall st','wall street','dow','nasdaq','s&p',
        'earnings','profit','revenue','sales','quarter','q1','q2','q3','q4','forecast','outlook',
        'economy','economic','inflation','gdp','jobs','unemployment','interest rate','fed','ecb','central bank',
        'bank','banks','banking','loan','loans','mortgage','credit','debt','bond','bonds','treasury','yield',
        'oil','crude','gas','energy','opec','pipeline',
        'company','companies','firm','corp','corporation','inc','ltd','plc','ceo','cfo','ipo','merger','acquisition',
        'antitrust','regulator','regulation','trade','tariff','export','imports','currency','euro','dollar','forex',
        'business','finance','financial','investment','investor','fund','hedge','private equity','venture',
        'prices','costs'
    ]
    return any(k in s for k in kws)

biz_mask = text.apply(is_business)
biz_df = df[biz_mask].copy()

biz_df['year'] = biz_df['publication_date'].str.slice(0,4).astype(int)
counts = biz_df.groupby('year').size().reindex(range(2010,2021), fill_value=0)
avg = counts.mean()

out = {
    'average_business_articles_per_year_europe_2010_2020': float(avg),
    'total_business_articles': int(counts.sum()),
    'years': 11
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_4tk1Qyuk8zuCB8iZticbrmVt': 'file_storage/call_4tk1Qyuk8zuCB8iZticbrmVt.json', 'var_call_nETuVEREXJvl4INmD7RZGqnf': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
