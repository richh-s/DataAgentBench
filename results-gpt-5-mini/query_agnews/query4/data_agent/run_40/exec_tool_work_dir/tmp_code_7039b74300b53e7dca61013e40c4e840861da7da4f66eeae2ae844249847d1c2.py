code = """import json
import pandas as pd
# Load the articles list from storage variable
articles = var_call_KK5FQOSDyK7EFOpmFauBsuUq
# Load the large metadata JSON file from path stored in var_call_f6xMIgBNp7TNMUzUcWJpT54r
with open(var_call_f6xMIgBNp7TNMUzUcWJpT54r, 'r') as f:
    metadata = json.load(f)
# Create DataFrames
df_articles = pd.DataFrame(articles)
df_metadata = pd.DataFrame(metadata)
# Ensure article_id types are strings for join
df_articles['article_id'] = df_articles['article_id'].astype(str)
df_metadata['article_id'] = df_metadata['article_id'].astype(str)
# Merge metadata for 2015 with articles
df = pd.merge(df_metadata, df_articles, on='article_id', how='left')
# Define keyword-based classifier
world_kw = ['president','minister','government','election','dead','killed','attack','war','border','refugee','country','countries','united nations','un','diplomat','diplomatic','ceasefire','treaty','parliament','protest','police','court','terror','terrorist','bomb','minister','coup','regime','sanction']
business_kw = ['stock','stocks','market','economy','financial','bank','banks','company','companies','shares','billion','million','revenue','profit','loss','invest','investment','ipo','firm','sales']
sports_kw = ['match','game','season','goal','score','scores','win','won','defeat','team','player','players','coach','tournament','league','cup','football','soccer','basketball','baseball','rugby','olympic','fifa','mlb','nba']
tech_kw = ['technology','tech','scientist','scientists','research','study','nasa','space','internet','software','google','apple','facebook','device','robot','ai','artificial intelligence','gadget']

from collections import Counter

def classify_text(text):
    if not isinstance(text, str):
        text = ''
    s = text.lower()
    scores = {'World':0, 'Business':0, 'Sports':0, 'Science/Technology':0}
    for kw in world_kw:
        if kw in s:
            scores['World'] += 1
    for kw in business_kw:
        if kw in s:
            scores['Business'] += 1
    for kw in sports_kw:
        if kw in s:
            scores['Sports'] += 1
    for kw in tech_kw:
        if kw in s:
            scores['Science/Technology'] += 1
    # If no keywords matched, fallback: classify as World if contains common news indicators about countries
    if sum(scores.values()) == 0:
        # simple heuristics: if contains Reuters/AFP and mentions country names? default to World
        if any(x in s for x in ['reuters','afp','associated press','ap']):
            return 'World'
        return 'World'
    # choose max, with tiebreaker priority
    order = ['World','Business','Sports','Science/Technology']
    max_score = max(scores.values())
    candidates = [k for k,v in scores.items() if v==max_score]
    for cat in order:
        if cat in candidates:
            return cat
    return 'World'

# Apply classifier on title+description
texts = (df['title'].fillna('') + ' ' + df['description'].fillna('')).astype(str)
df['category'] = texts.apply(classify_text)

# Filter 2015 rows already ensured from metadata query; count World category by region
world_df = df[df['category']=='World']
counts = Counter(world_df['region'].fillna('Unknown'))
# Convert to regular dict
counts_dict = dict(counts)
# Determine top region (if tie, pick one with max count sorted alphabetically for determinism)
if counts_dict:
    max_count = max(counts_dict.values())
    top_regions = sorted([r for r,c in counts_dict.items() if c==max_count])
    top_region = top_regions[0]
else:
    top_region = None

result = {'top_region': top_region, 'counts': counts_dict}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_f6xMIgBNp7TNMUzUcWJpT54r': 'file_storage/call_f6xMIgBNp7TNMUzUcWJpT54r.json', 'var_call_KK5FQOSDyK7EFOpmFauBsuUq': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
