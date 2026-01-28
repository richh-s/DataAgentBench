code = """import json, pandas as pd

# Load metadata 2015 from file
path = var_call_57O2V5x46WiWYpvfPUbDEPpq
with open(path, 'r', encoding='utf-8') as f:
    meta = json.load(f)

arts = var_call_2Z6OEGbZMWdlnHasLCys2vRG

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# Normalize ids to int
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# Join
df = meta_df.merge(arts_df, on='article_id', how='inner')

# Simple keyword-based classifier for World
text = (df['title'].fillna('') + ' ' + df['description'].fillna('')).str.lower()
world_kw = [
    'iraq','iran','israel','palestin','gaza','hamas','hezbollah','syria','assad','russia','ukraine','crimea',
    'china','beijing','hong kong','taiwan','japan','tokyo','korea','seoul','north korea','kim jong',
    'india','pakistan','afghanistan','taliban','yemen','saudi','turkey','ankara','erdogan',
    'europe','eu ','e.u','brussels','nato','un ','u.n','united nations','geneva','paris','london','berlin',
    'mexico','brazil','argentina','venezuela','colombia','cuba','haiti','bolivia',
    'africa','nigeria','kenya','somalia','sudan','egypt','libya','algeria','tunisia','congo',
    'terror','militant','rebels','bomb','blast','attack','hostage','war','ceasefire','election','coup','prime minister','president',
    'refugee','migrant','immigration','border','diplomat','embassy','sanction'
]
world_pat = '|'.join([pd.regex.escape(k) for k in world_kw])

# Heuristics to avoid business/sports/tech false positives
sports_pat = r"\b(nba|nfl|mlb|nhl|soccer|football|tennis|golf|olympic|world cup|championship|tournament|coach|match|league)\b"
biz_pat = r"\b(stocks?|shares?|wall st|dow|nasdaq|s\&p|earnings?|profit|revenue|ipo|acquisition|merger|bank|fed|interest rates?|oil prices?|crude|economy|inflation)\b"
tech_pat = r"\b(software|internet|smartphone|android|iphone|microsoft|google|apple|chip|semiconductor|ai |artificial intelligence|nasa|space|satellite|physics|biotech|genome)\b"

is_world = text.str.contains(world_pat, regex=True)
# If it's strongly sports/business/tech and not world-geo, drop
is_sports = text.str.contains(sports_pat, regex=True)
is_biz = text.str.contains(biz_pat, regex=True)
is_tech = text.str.contains(tech_pat, regex=True)

world_df = df[is_world & ~(is_sports & ~is_world) & ~(is_biz & ~is_world) & ~(is_tech & ~is_world)]

counts = world_df.groupby('region')['article_id'].nunique().sort_values(ascending=False)
if len(counts)==0:
    result = {"region": None, "count": 0}
else:
    top_region = counts.index[0]
    top_count = int(counts.iloc[0])
    # handle ties
    tied = counts[counts==counts.iloc[0]].index.tolist()
    result = {"region": top_region, "count": top_count, "tied_regions": tied}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_57O2V5x46WiWYpvfPUbDEPpq': 'file_storage/call_57O2V5x46WiWYpvfPUbDEPpq.json', 'var_call_2Z6OEGbZMWdlnHasLCys2vRG': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
