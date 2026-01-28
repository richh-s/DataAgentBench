code = """import json, pandas as pd

# Load 2015 metadata (possibly from file)
md = var_call_VMKTHBMSn0dBauaA9x4oCqMT
if isinstance(md, str):
    with open(md, 'r', encoding='utf-8') as f:
        md = json.load(f)

arts = var_call_F7u5fQ2PlSxkoBTC5eIFlwrt
if isinstance(arts, str):
    with open(arts, 'r', encoding='utf-8') as f:
        arts = json.load(f)

md_df = pd.DataFrame(md)
arts_df = pd.DataFrame(arts)

# normalize types
md_df['article_id'] = md_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)
arts_df['title'] = arts_df['title'].fillna('')
arts_df['description'] = arts_df['description'].fillna('')

df = md_df.merge(arts_df, on='article_id', how='inner')
text = (df['title'].astype(str) + ' ' + df['description'].astype(str)).str.lower()

# simple keyword-based categorization
world_kw = [
    'iraq','iran','israel','palestin','gaza','hamas','hezbollah','syria','syrian','afghanistan','taliban',
    'pakistan','india','china','japan','north korea','south korea','kim','putin','russia','ukraine','crimea',
    'european union','eu ','nato','united nations','u.n.','un ','refugee','migrant','immigration',
    'terror','bomb','attack','militant','insurgent','ceasefire','peace talks','election','president','prime minister',
    'parliament','government','protest','coup','diplomat','embassy','sanction','war','conflict','rebel',
    'border','hostage','pope','vatican','britain','uk ','london','france','germany','spain','italy','greece',
    'turkey','egypt','libya','nigeria','sudan','kenya','somalia','congo','south africa','zimbabwe',
    'mexico','brazil','argentina','venezuela','colombia','chile','peru','saudi','yemen','jordan','lebanon',
    'kurd','baghdad','moscow','kiev','kyiv','beijing','tokyo','seoul','tehran','jerusalem'
]

sports_kw = ['game','games','match','tournament','league','nba','nfl','mlb','nhl','soccer','football','baseball','basketball','hockey','tennis','golf','olympic','championship','coach','season','player','team','world cup']
biz_kw = ['stock','stocks','wall street','shares','earnings','profit','revenue','market','economy','economic','oil','crude','inflation','interest rate','bank','fed','ipo','merger','acquisition','company','corporate','dollar','euro','yen','trade','tariff']
tech_kw = ['software','hardware','internet','online','app','smartphone','android','iphone','microsoft','google','apple','facebook','twitter','amazon','ai','artificial intelligence','robot','space','nasa','satellite','chip','semiconductor','biotech','genome','science','scientist','research','study','clinical','technology','tech']

# score by keyword counts
import numpy as np

def score(keywords):
    s = np.zeros(len(text), dtype=int)
    for kw in keywords:
        s += text.str.contains(kw, regex=False).astype(int).to_numpy()
    return s

scores = pd.DataFrame({
    'World': score(world_kw),
    'Sports': score(sports_kw),
    'Business': score(biz_kw),
    'Science/Technology': score(tech_kw)
})

# choose category: highest score; if all zero, fall back to Business if finance terms exist else World? We'll use tie-break order World, Business, Sports, Science/Technology.
order = ['World','Business','Sports','Science/Technology']
maxv = scores.max(axis=1)
cat = []
for i in range(len(scores)):
    if maxv.iat[i] == 0:
        # heuristic fallback
        if scores.at[i,'Business']>0:
            cat.append('Business')
        elif scores.at[i,'Sports']>0:
            cat.append('Sports')
        elif scores.at[i,'Science/Technology']>0:
            cat.append('Science/Technology')
        else:
            cat.append('World')
    else:
        # handle ties
        tied = [c for c in scores.columns if scores.at[i,c]==maxv.iat[i]]
        for c in order:
            if c in tied:
                cat.append(c)
                break

df['category'] = cat
world_df = df[df['category']=='World']

counts = world_df.groupby('region', dropna=False).size().sort_values(ascending=False)

if len(counts)==0:
    result = {'region': None, 'world_article_count_2015': 0}
else:
    top_region = counts.index[0]
    result = {'region': str(top_region), 'world_article_count_2015': int(counts.iloc[0])}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_VMKTHBMSn0dBauaA9x4oCqMT': 'file_storage/call_VMKTHBMSn0dBauaA9x4oCqMT.json', 'var_call_F7u5fQ2PlSxkoBTC5eIFlwrt': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
