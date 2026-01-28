code = """import json, pandas as pd

# Load 2015 metadata (may be file path)
meta = var_call_f2tEtHfoqCOPhkrHxfxU7wnn
if isinstance(meta, str):
    with open(meta, 'r') as f:
        meta = json.load(f)

arts = var_call_88nzaqU1Y98RnA6iQapXevLE

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# Ensure numeric ids for join
meta_df['article_id'] = pd.to_numeric(meta_df['article_id'], errors='coerce')
arts_df['article_id'] = pd.to_numeric(arts_df['article_id'], errors='coerce')

# Simple keyword-based classifier for 4 categories
world_kw = [
    'iraq','iran','israel','palestin','gaza','afghan','pakistan','india','china','japan','korea','russia','ukraine',
    'syria','lebanon','yemen','saudi','turkey','europe','eu ','e.u','nato','un ','u.n','united nations',
    'britain','england','france','germany','spain','italy','greek','australia','canada','mexico','brazil',
    'africa','nigeria','kenya','sudan','congo','somalia','egypt','libya','election','parliament','president',
    'minister','militant','rebel','terror','bomb','hostage','war','ceasefire','sanction','diplomat','embassy'
]
sports_kw = ['nba','nfl','mlb','nhl','soccer','football','basketball','baseball','hockey','tennis','golf','olympic','fifa','uefa','cricket','rugby','coach','tournament','match','league','cup','grand slam']
biz_kw = ['stock','wall st','dow','nasdaq','earnings','profit','revenue','shares','bond','oil','crude','inflation','gdp','economy','bank','fed','interest rate','currency','dollar','euro','merger','acquisition','ipo','market','company','corporate']
sci_kw = ['software','internet','technology','tech','computer','chip','semiconductor','microsoft','google','apple','facebook','ai','robot','space','nasa','mars','satellite','science','scientist','research','study','gene','genome','medical','drug','disease','climate','energy','battery']

def classify(text):
    t = (text or '').lower()
    # score by keyword hits
    def score(kws):
        s = 0
        for kw in kws:
            if kw in t:
                s += 1
        return s
    scores = {
        'World': score(world_kw),
        'Sports': score(sports_kw),
        'Business': score(biz_kw),
        'Science/Technology': score(sci_kw)
    }
    # choose max; tie-breaker preference World->Business->Sports->Sci/Tech
    order = ['World','Business','Sports','Science/Technology']
    maxv = max(scores.values())
    tops = [k for k,v in scores.items() if v==maxv]
    for k in order:
        if k in tops:
            return k

# Merge and classify
joined = meta_df.merge(arts_df, on='article_id', how='inner')
joined['text'] = joined['title'].fillna('') + ' ' + joined['description'].fillna('')
joined['category'] = joined['text'].map(classify)

world_2015 = joined[joined['category']=='World']
counts = world_2015.groupby('region')['article_id'].count().sort_values(ascending=False)

result = {
    'top_region': None if counts.empty else counts.index[0],
    'top_count': None if counts.empty else int(counts.iloc[0]),
    'counts_by_region': {k:int(v) for k,v in counts.to_dict().items()}
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_f2tEtHfoqCOPhkrHxfxU7wnn': 'file_storage/call_f2tEtHfoqCOPhkrHxfxU7wnn.json', 'var_call_88nzaqU1Y98RnA6iQapXevLE': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
