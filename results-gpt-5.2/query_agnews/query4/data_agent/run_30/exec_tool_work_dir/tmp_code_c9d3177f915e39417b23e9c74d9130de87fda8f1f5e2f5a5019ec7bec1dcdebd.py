code = """import json, pandas as pd, re

# load 2015 metadata (article_id, region)
meta_src = var_call_YWTZPuGTlGrLy5kbZi3T3ZW7
if isinstance(meta_src, str):
    with open(meta_src, 'r') as f:
        meta = json.load(f)
else:
    meta = meta_src
meta_df = pd.DataFrame(meta)
meta_df['article_id'] = meta_df['article_id'].astype(int)

# load articles
arts = var_call_cYCGfW9qC83sQSmXtKbLBpBo
arts_df = pd.DataFrame(arts)
arts_df['article_id'] = arts_df['article_id'].astype(int)
arts_df['text'] = (arts_df['title'].fillna('') + ' ' + arts_df['description'].fillna('')).str.lower()

# heuristic categorization
world_kw = [
    r'\biraq\b', r'\biran\b', r'\bsyria\b', r'\bafghanistan\b', r'\byemen\b', r'\bisrael\b', r'\bpalestin', r'\bgaza\b', r'\bhamas\b', r'\bhezbollah\b',
    r'\brussia\b', r'\bukrain', r'\bputin\b', r'\bmoscow\b', r'\bkremlin\b',
    r'\bchina\b', r'\bbeijing\b', r'\bjapan\b', r'\bkorea\b', r'\bnorth korea\b', r'\bsouth korea\b',
    r'\bindia\b', r'\bpaki', r'\bbangladesh\b',
    r'\bfrance\b', r'\bgermany\b', r'\bitaly\b', r'\bspain\b', r'\buk\b', r'\bbritain\b', r'\blondon\b', r'\beu\b', r'\beuropean union\b',
    r'\bafrica\b', r'\bnigeria\b', r'\bkenya\b', r'\bsudan\b', r'\bsomalia\b', r'\begypt\b', r'\blibya\b',
    r'\bpakistan\b', r'\bsaudi\b', r'\bturkey\b', r'\bqatar\b', r'\bkuwait\b', r'\blebanon\b', r'\bjordan\b',
    r'\bunited nations\b', r'\bun\b', r'\bnato\b', r'\brefugee\b', r'\bmigrant\b', r'\bearthquake\b', r'\btsunami\b', r'\bterror\b', r'\bmilitant\b', r'\bwar\b', r'\bceasefire\b', r'\bsanction\b', r'\bcoup\b', r'\belection\b'
]

sports_kw = [r'\bnhl\b', r'\bnba\b', r'\bnfl\b', r'\bmlb\b', r'\bsoccer\b', r'\bfootball\b', r'\bcricket\b', r'\btennis\b', r'\bgolf\b', r'\bolympic', r'\bmatch\b', r'\bcoach\b', r'\bchampionship\b', r'\bplayoff', r'\bgoal\b', r'\binnings\b']

biz_kw = [r'\bstocks\b', r'\bwall st\b', r'\bmarket\b', r'\bearnings\b', r'\bprofit\b', r'\brevenue\b', r'\bshares\b', r'\bbank\b', r'\bipo\b', r'\bmerger\b', r'\bacquisition\b', r'\boil\b', r'\bcrude\b', r'\bgold\b', r'\binflation\b', r'\bgdp\b', r'\beconom', r'\bdebt\b', r'\bcurrency\b', r'\bdollar\b']

sci_kw = [r'\bscience\b', r'\bresearch\b', r'\bstudy\b', r'\bscientist\b', r'\bspace\b', r'\bnasa\b', r'\bplanet\b', r'\basteroid\b', r'\bgalaxy\b', r'\btechnology\b', r'\btech\b', r'\bsoftware\b', r'\bcomputer\b', r'\binternet\b', r'\biphone\b', r'\bandroid\b', r'\bgoogle\b', r'\bfacebook\b', r'\bmicrosoft\b', r'\bai\b', r'\brobot\b', r'\bcyber\b', r'\bhacker\b', r'\bvirus\b', r'\bvaccine\b', r'\bgenome\b', r'\bclimate\b']

compiled = {
    'World': [re.compile(p) for p in world_kw],
    'Sports': [re.compile(p) for p in sports_kw],
    'Business': [re.compile(p) for p in biz_kw],
    'Science/Technology': [re.compile(p) for p in sci_kw],
}

priority = ['Sports','Business','Science/Technology','World']

def classify(text):
    scores = {k:0 for k in compiled}
    for cat, pats in compiled.items():
        for pat in pats:
            if pat.search(text):
                scores[cat] += 1
    # choose best by score; tie-breaker by priority list with World last
    best_cat = max(scores, key=lambda k: scores[k])
    if scores[best_cat] == 0:
        return 'World'
    top = [k for k,v in scores.items() if v==scores[best_cat]]
    if len(top)==1:
        return best_cat
    for p in priority:
        if p in top:
            return p
    return best_cat

arts_df['category'] = arts_df['text'].map(classify)

# join with 2015 meta and filter world
joined = meta_df.merge(arts_df[['article_id','category']], on='article_id', how='left')
world_2015 = joined[joined['category']=='World']
counts = world_2015.groupby('region').size().sort_values(ascending=False)
if len(counts)==0:
    result = {'region': None, 'world_article_count': 0}
else:
    result = {'region': counts.index[0], 'world_article_count': int(counts.iloc[0])}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_B5L53djnSMZhgT1q13FuaQjD': [{'region': 'Asia'}, {'region': 'North America'}, {'region': 'South America'}, {'region': 'Europe'}, {'region': 'Africa'}], 'var_call_I53b7vt2GkkcWBNQs9cZFTaJ': [{'n': '6696'}], 'var_call_YWTZPuGTlGrLy5kbZi3T3ZW7': 'file_storage/call_YWTZPuGTlGrLy5kbZi3T3ZW7.json', 'var_call_cYCGfW9qC83sQSmXtKbLBpBo': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
