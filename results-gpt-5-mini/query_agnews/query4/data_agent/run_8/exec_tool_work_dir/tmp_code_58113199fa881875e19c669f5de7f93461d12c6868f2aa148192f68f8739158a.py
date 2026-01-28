code = """import json
import pandas as pd
import re

# load metadata results
records_meta = None
if isinstance(var_call_TvXXrwZrGiS2PKVwWHLNM5Lg, str):
    # it's a file path
    with open(var_call_TvXXrwZrGiS2PKVwWHLNM5Lg, 'r', encoding='utf-8') as f:
        records_meta = json.load(f)
else:
    records_meta = var_call_TvXXrwZrGiS2PKVwWHLNM5Lg

records_articles = var_call_CKJwRySOyxA01fNkpk5cQKdR

# DataFrames
df_meta = pd.DataFrame(records_meta)
df_articles = pd.DataFrame(records_articles)

# Ensure article_id as string for merge
df_meta['article_id'] = df_meta['article_id'].astype(str)
df_articles['article_id'] = df_articles['article_id'].astype(str)

# Merge
df = pd.merge(df_meta, df_articles, on='article_id', how='left')

# Fillna for title/description
df['title'] = df['title'].fillna('').astype(str)
with pd.option_context('mode.chained_assignment', None):
    df['description'] = df['description'].fillna('').astype(str)

# Classification keywords
world_k = ['president','election','rebel','rebels','military','soldier','attack','attacks','crisis','government','minister','diplomat','diplomats','war','peace','border','sanction','refugee','court','terror','terrorist','siege','Iraq','Syria','Russia','China','United States','U.S.','UK','Afghanistan','Libya','international','foreign']
political_indicators = ['president','election','government','minister','diplomat','sanction','international','foreign']
sports_k = ['match','season','goal','score','football','soccer','tennis','basketball','baseball','olympic','coach','tournament','win','won','defeat','league','cup','player','players','fifa','nba','mlb','nfl']
business_k = ['stock','stocks','market','markets','economy','earnings','investment','firm','company','companies','commercial','Wall St','wall st','shares','billion','merger','acquisition','bank','dollar','business','crude','oil','prices']
tech_k = ['technology','tech','scientist','scientists','research','nasa','space','computer','software','internet','digital','study','laboratory','innovation']

# compile lowercased matching
def count_matches(text, keywords):
    text = text.lower()
    total = 0
    for k in keywords:
        k_l = k.lower()
        # use word boundary for alpha keywords, else just substring
        if re.search(r"\w", k_l):
            total += len(re.findall(r"\\b" + re.escape(k_l) + r"\\b", text))
        else:
            total += text.count(k_l)
    return total

def classify_row(row):
    text = (row.get('title','') + ' ' + row.get('description','')).lower()
    counts = {
        'World': count_matches(text, world_k + political_indicators),
        'Sports': count_matches(text, sports_k),
        'Business': count_matches(text, business_k),
        'Science/Technology': count_matches(text, tech_k)
    }
    # If all zero, attempt to use source tag like (Reuters) or presence of country names as World
    if sum(counts.values()) == 0:
        # if contains country names -> World
        country_words = ['china','russia','iraq','syria','afghanistan','libya','united states','u.s.','uk','europe','africa','asia','north america','south america']
        if any(re.search(r"\\b"+re.escape(c)+r"\\b", text) for c in country_words):
            return 'World'
        # if contains market/economy terms
        if count_matches(text, business_k) > 0:
            return 'Business'
        # default fallback World
        return 'World'
    # choose max
    category = max(counts.items(), key=lambda x: x[1])[0]
    return category

# Apply classification
df['category'] = df.apply(classify_row, axis=1)

# Filter for World category and count by region
world_counts = df[df['category']=='World'].groupby('region').size().to_dict()

# Determine region with max
if world_counts:
    max_region = max(world_counts.items(), key=lambda x: x[1])[0]
    max_count = int(world_counts[max_region])
    result = {"region": max_region, "count": max_count}
else:
    result = {"region": None, "count": 0}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_TvXXrwZrGiS2PKVwWHLNM5Lg': 'file_storage/call_TvXXrwZrGiS2PKVwWHLNM5Lg.json', 'var_call_CKJwRySOyxA01fNkpk5cQKdR': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
