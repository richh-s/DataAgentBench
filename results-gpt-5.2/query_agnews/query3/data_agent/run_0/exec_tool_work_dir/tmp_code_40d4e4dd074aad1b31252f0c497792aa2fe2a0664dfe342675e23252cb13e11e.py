code = """import json, pandas as pd

# Load metadata (Europe, 2010-2020)
meta_src = var_call_zMDXe4JUCMSOUDseUmt7SUVz
if isinstance(meta_src, str):
    with open(meta_src, 'r', encoding='utf-8') as f:
        meta = json.load(f)
else:
    meta = meta_src

articles = var_call_Tx60og7AUEob2srbPCrhMwJs

meta_df = pd.DataFrame(meta)
art_df = pd.DataFrame(articles)

# Normalize ids to int
meta_df['article_id'] = pd.to_numeric(meta_df['article_id'], errors='coerce')
art_df['article_id'] = pd.to_numeric(art_df['article_id'], errors='coerce')
meta_df = meta_df.dropna(subset=['article_id'])
art_df = art_df.dropna(subset=['article_id'])
meta_df['article_id'] = meta_df['article_id'].astype(int)
art_df['article_id'] = art_df['article_id'].astype(int)

# Join to get title/description for Europe articles
df = meta_df.merge(art_df, on='article_id', how='left')

def is_business_row(row):
    txt = f"{row.get('title','')} {row.get('description','')}".lower()
    # simple keyword-based classification for Business
    keywords = [
        'stock','stocks','wall st','wall street','market','markets','shares','bond','bonds','yield','yields',
        'earnings','profit','revenue','sales','ipo','merger','acquisition','buyout','deal',
        'bank','banks','banking','fed','central bank','interest rate','rates','inflation','gdp','economy','economic',
        'oil','crude','gas','energy','prices','price','commodity','commodities','trade','tariff',
        'company','companies','corporate','ceo','investor','investment','fund','hedge','private equity',
        'currency','dollar','euro','forex','exchange rate'
    ]
    return any(k in txt for k in keywords)

# Determine business articles
biz_mask = df.apply(is_business_row, axis=1)
biz_df = df[biz_mask].copy()

# Year and counts
biz_df['year'] = pd.to_datetime(biz_df['publication_date'], errors='coerce').dt.year
biz_df = biz_df[(biz_df['year']>=2010) & (biz_df['year']<=2020)]
counts = biz_df.groupby('year').size().reindex(range(2010,2021), fill_value=0)
avg_per_year = counts.mean()

out = {
    "average_business_articles_per_year_europe_2010_2020": float(avg_per_year),
    "total_business_articles": int(counts.sum()),
    "years": 11
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_zMDXe4JUCMSOUDseUmt7SUVz': 'file_storage/call_zMDXe4JUCMSOUDseUmt7SUVz.json', 'var_call_Tx60og7AUEob2srbPCrhMwJs': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
