code = """import json, pandas as pd, re

meta = var_call_yhOSfDBju4k2FnHSANHMChkU
if isinstance(meta, str):
    with open(meta, 'r', encoding='utf-8') as f:
        meta = json.load(f)
meta_df = pd.DataFrame(meta)
meta_df['article_id'] = meta_df['article_id'].astype(int)
meta_df['year'] = pd.to_datetime(meta_df['publication_date'], errors='coerce').dt.year
meta_df = meta_df[(meta_df['year']>=2010) & (meta_df['year']<=2020)]

arts = var_call_36rHCvIwGJpjlHMhMka0HFC8
arts_df = pd.DataFrame(arts)
arts_df['article_id'] = arts_df['article_id'].astype(int)

join_df = meta_df[['article_id','year']].merge(arts_df, on='article_id', how='left')
join_df['text'] = (join_df['title'].fillna('') + ' ' + join_df['description'].fillna('')).str.lower()

biz_kw = [
    'stocks','stock','shares','share','wall st','wall street','dow','nasdaq','s&p',
    'earnings','profit','revenue','sales','forecast','outlook','quarter','q1','q2','q3','q4',
    'bank','banks','banking','central bank','ecb','fed','interest rate','rates','inflation','gdp',
    'economy','economic','recession','growth','market','markets','trading','investor','investment','fund',
    'oil','crude','gas','energy','opec','pipeline',
    'company','companies','corporate','ceo','merger','acquisition','ipo','debt','bond','bonds',
    'currency','euro','dollar','forex','exchange rate'
]
pattern = r'(' + '|'.join([re.escape(k) for k in biz_kw]) + r')'
join_df['is_business'] = join_df['text'].str.contains(pattern, regex=True, na=False)

per_year = join_df.loc[join_df['is_business']].groupby('year').size().reindex(range(2010,2021), fill_value=0)
avg_per_year = per_year.mean()

result = {
    'average_business_articles_per_year_europe_2010_2020': float(avg_per_year),
    'total_business_articles': int(per_year.sum()),
    'years_counted': 11,
    'per_year': {int(k): int(v) for k,v in per_year.items()}
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_yhOSfDBju4k2FnHSANHMChkU': 'file_storage/call_yhOSfDBju4k2FnHSANHMChkU.json', 'var_call_36rHCvIwGJpjlHMhMka0HFC8': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
