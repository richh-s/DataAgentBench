code = """import json, pandas as pd

# Load europe metadata (may be file path)
meta_src = var_call_aPJZye1lkkpTfM93CvVBMugY
if isinstance(meta_src, str):
    with open(meta_src, 'r', encoding='utf-8') as f:
        meta = json.load(f)
else:
    meta = meta_src

articles = var_call_IVybbY9UU60nqRbKsn7EO61U

df_meta = pd.DataFrame(meta)
df_art = pd.DataFrame(articles)

# Ensure types
for c in ['article_id']:
    if c in df_meta.columns:
        df_meta[c] = df_meta[c].astype(int)
    if c in df_art.columns:
        df_art[c] = df_art[c].astype(int)

# Extract year
df_meta['year'] = df_meta['publication_date'].str.slice(0,4).astype(int)

# Join to get title/description for classification
df = df_meta.merge(df_art, on='article_id', how='left')

def is_business(row):
    text = (str(row.get('title','')) + ' ' + str(row.get('description',''))).lower()
    # simple keyword heuristic
    kws = [
        'stock','stocks','wall st','wall street','market','markets','shares','bond','bonds','treasury',
        'earnings','profit','revenue','ipo','acquisition','merger','m&a','buyout','bank','banks','fed',
        'interest rate','inflation','economy','economic','gdp','unemployment','currency','forex','dollar','euro',
        'oil','crude','opec','gas','energy','prices','price','trade','tariff','sanction','company','companies',
        'sales','investment','investor','fund','funds','hedge','private equity','carlyle','business'
    ]
    return any(k in text for k in kws)

# apply
mask_business = df.apply(is_business, axis=1)
df_biz = df[mask_business].copy()

counts = df_biz.groupby('year').size().reindex(range(2010,2021), fill_value=0)
avg = counts.mean()

result = {
    'average_business_articles_per_year_europe_2010_2020': float(avg),
    'total_business_articles_2010_2020': int(counts.sum()),
    'years': 11
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_aPJZye1lkkpTfM93CvVBMugY': 'file_storage/call_aPJZye1lkkpTfM93CvVBMugY.json', 'var_call_IVybbY9UU60nqRbKsn7EO61U': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
