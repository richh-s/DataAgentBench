code = """import json, pandas as pd, re

def load_result(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

meta = load_result(var_call_VWftFPlgtATavFXmeYorhkqz)
arts = load_result(var_call_TfxaCKk9PtyCrDtdMe7D6BnC)

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)
arts_df['text'] = (arts_df['title'].fillna('') + ' ' + arts_df['description'].fillna('')).str.lower()

world_kw = [
    'iraq','iran','israel','gaza','palestin','syria','lebanon','jordan','yemen','afghanistan','pakistan','india','china','japan','korea','russia','ukraine','crimea','nato','united nations',
    'diplomat','embassy','prime minister','parliament','rebels','militant','terror','bomb','attack','killed','war','ceasefire','refugee','immigrant','border','sanction','summit','treaty','coup'
]
pattern = re.compile(r'(' + '|'.join(re.escape(k) for k in world_kw) + r')')
arts_df['is_world'] = arts_df['text'].str.contains(pattern)

joined = meta_df.merge(arts_df[['article_id','is_world']], on='article_id', how='inner')
counts = joined[joined['is_world']].groupby('region', as_index=False).size().sort_values('size', ascending=False)

out = {'region': None, 'world_articles_2015': 0}
if not counts.empty:
    top = counts.iloc[0]
    out = {'region': str(top['region']), 'world_articles_2015': int(top['size'])}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_VWftFPlgtATavFXmeYorhkqz': 'file_storage/call_VWftFPlgtATavFXmeYorhkqz.json', 'var_call_TfxaCKk9PtyCrDtdMe7D6BnC': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
