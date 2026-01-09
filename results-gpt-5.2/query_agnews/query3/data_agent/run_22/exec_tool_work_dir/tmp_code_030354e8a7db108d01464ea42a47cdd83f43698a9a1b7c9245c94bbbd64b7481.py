code = """import json, pandas as pd

# Load metadata (may be file path)
meta_src = var_call_zzv4mgSXd2NRuYCTfl1FxCQN
if isinstance(meta_src, str):
    with open(meta_src, 'r', encoding='utf-8') as f:
        meta = json.load(f)
else:
    meta = meta_src

arts = var_call_tfObuOfIIzcFgDP2inN8Tkye

dfm = pd.DataFrame(meta)
# Ensure types
if not dfm.empty:
    dfm['article_id'] = dfm['article_id'].astype(int)
    dfm['year'] = dfm['publication_date'].str.slice(0,4).astype(int)

# articles dataframe
dfa = pd.DataFrame(arts)
if not dfa.empty:
    dfa['article_id'] = dfa['article_id'].astype(int)
    dfa['text'] = (dfa['title'].fillna('') + ' ' + dfa['description'].fillna('')).str.lower()

# Join Europe 2010-2020 with article text
if dfm.empty or dfa.empty:
    avg = None
else:
    df = dfm.merge(dfa[['article_id','text']], on='article_id', how='left')

    # Simple keyword-based business classifier
    biz_kw = [
        'stock','stocks','shares','equity','equities','bond','bonds','treasury','yield','yields',
        'market','markets','wall st','dow','nasdaq','s&p','ftse','dax','cac',
        'bank','banks','banking','central bank','ecb','boe','fed',
        'inflation','gdp','economy','economic','recession','growth',
        'earnings','profit','profits','revenue','sales','quarter','guidance',
        'oil','crude','brent','wti','gas','opec',
        'deal','merger','acquisition','ipo','listing',
        'currency','currencies','forex','euro','dollar','pound',
        'interest rate','rates','loan','loans','credit','debt','default',
        'trade','tariff','exports','imports','unemployment','jobs',
        'company','companies','firm','corporate','invest','investment','investor','fund'
    ]
    pattern = '|'.join([pd.regex.escape(k) for k in biz_kw])
    df['is_business'] = df['text'].fillna('').str.contains(pattern, regex=True)

    # Count business articles per year, include all years 2010-2020
    counts = df[df['is_business']].groupby('year').size().reindex(range(2010,2021), fill_value=0)
    avg = float(counts.mean())

out = json.dumps({'average_business_articles_per_year_europe_2010_2020': avg})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_zzv4mgSXd2NRuYCTfl1FxCQN': 'file_storage/call_zzv4mgSXd2NRuYCTfl1FxCQN.json', 'var_call_tfObuOfIIzcFgDP2inN8Tkye': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
