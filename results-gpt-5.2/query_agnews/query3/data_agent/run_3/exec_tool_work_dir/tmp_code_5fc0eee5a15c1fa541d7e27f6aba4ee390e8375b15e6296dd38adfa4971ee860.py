code = """import json, pandas as pd, re

# Load Europe 2010-2020 metadata
meta_src = var_call_PsQbQMsVbFG64tOwubqOqDxm
if isinstance(meta_src, str):
    with open(meta_src, 'r', encoding='utf-8') as f:
        meta = json.load(f)
else:
    meta = meta_src

df_meta = pd.DataFrame(meta)
# Ensure types
if df_meta.empty:
    out = {"average_business_articles_per_year": 0, "years": list(range(2010, 2021)), "business_article_counts_by_year": {str(y): 0 for y in range(2010, 2021)}}
    print('__RESULT__:')
    print(json.dumps(out))
    raise SystemExit

df_meta['article_id'] = df_meta['article_id'].astype(str)
df_meta['year'] = df_meta['publication_date'].str.slice(0,4).astype(int)

# Articles content
arts = pd.DataFrame(var_call_BNKgjGrLL8jrKnwan8a1HMlU)
arts['article_id'] = arts['article_id'].astype(str)
arts['text'] = (arts['title'].fillna('') + ' ' + arts['description'].fillna('')).str.lower()

# Business keyword heuristic
kw = [
    'stock','stocks','wall st','wall street','shares','share','bond','bonds','treasury','nasdaq','dow','s&p',
    'earnings','profit','revenue','ipo','merger','acquisition','buyout','takeover','bank','banks','banking',
    'fed','federal reserve','ecb','central bank','interest rate','rates','inflation','gdp','economy','economic',
    'market','markets','oil','crude','opec','currency','dollar','euro','yen','forex','trade','exports','imports',
    'company','companies','corporate','ceo','cfo','investment','investors','fund','hedge','private equity'
]
pattern = re.compile(r'(' + '|'.join(re.escape(k) for k in kw) + r')')
arts['is_business'] = arts['text'].apply(lambda s: bool(pattern.search(s)))

# Join Europe subset with business flag
joined = df_meta.merge(arts[['article_id','is_business']], on='article_id', how='left')
joined['is_business'] = joined['is_business'].fillna(False)

biz = joined[joined['is_business']].copy()
counts = biz.groupby('year').size().reindex(range(2010,2021), fill_value=0)
avg = counts.mean()

out = {
    "average_business_articles_per_year": float(avg),
    "years": list(range(2010, 2021)),
    "business_article_counts_by_year": {str(int(k)): int(v) for k,v in counts.items()},
    "total_business_articles_2010_2020": int(counts.sum())
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_PsQbQMsVbFG64tOwubqOqDxm': 'file_storage/call_PsQbQMsVbFG64tOwubqOqDxm.json', 'var_call_BNKgjGrLL8jrKnwan8a1HMlU': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
