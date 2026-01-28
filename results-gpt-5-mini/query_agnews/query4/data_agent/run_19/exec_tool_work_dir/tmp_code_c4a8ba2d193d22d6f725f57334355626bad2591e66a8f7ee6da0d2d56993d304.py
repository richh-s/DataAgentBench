code = """import json
import pandas as pd

# Load data from storage-provided file paths
with open(var_call_kr1EH5P8btqWR4Jkmh7C6HfN, 'r') as f:
    metadata = json.load(f)
with open(var_call_ILpW9hRLGpgq8H6exVaedmKh, 'r') as f:
    articles = json.load(f)

md_df = pd.DataFrame(metadata)
art_df = pd.DataFrame(articles)

# Ensure article_id types are string for join
md_df['article_id'] = md_df['article_id'].astype(str)
art_df['article_id'] = art_df['article_id'].astype(str)

# Merge
merged = pd.merge(md_df, art_df, on='article_id', how='left')

# Simple keyword-based classifier
sports_kw = ['match','goal','season','coach','player','team','wins','win','lost','league','game','score','tournament','olympic','olympics','cup','football','soccer','nba','nfl','mlb','cricket','tennis','fifa','f1','golf','goalkeeper','striker','win:','defeat','draw']
business_kw = ['stock','stocks','market','markets','economy','trade deficit','trade','invest','investment','shares','profit','profits','bank','opec','oil prices','oil','company','firm','business','merger','acquisition','ipo','interest rates','rates','price','prices','dollar']
sci_kw = ['scientist','research','nuclear','drug','experiment','technology','tech','computer','scientists','nasa','space','chemical','study','cure','ph.d','researchers','laboratory','scientific']

def classify(row):
    text = ''
    if pd.notnull(row.get('title')):
        text += str(row.get('title')) + ' '
    if pd.notnull(row.get('description')):
        text += str(row.get('description'))
    t = text.lower()
    # sports
    for kw in sports_kw:
        if kw in t:
            return 'Sports'
    for kw in business_kw:
        if kw in t:
            return 'Business'
    for kw in sci_kw:
        if kw in t:
            return 'Science/Technology'
    return 'World'

merged['category'] = merged.apply(classify, axis=1)

# Filter 2015 (already), keep World
world = merged[merged['category']=='World']

# Count by region
counts = world['region'].value_counts().to_dict()
if counts:
    top_region = max(counts, key=lambda k: counts[k])
    top_count = counts[top_region]
else:
    top_region = None
    top_count = 0

result = {
    'top_region': top_region,
    'top_count': int(top_count),
    'counts': {k:int(v) for k,v in counts.items()}
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_kr1EH5P8btqWR4Jkmh7C6HfN': 'file_storage/call_kr1EH5P8btqWR4Jkmh7C6HfN.json', 'var_call_ILpW9hRLGpgq8H6exVaedmKh': 'file_storage/call_ILpW9hRLGpgq8H6exVaedmKh.json'}

exec(code, env_args)
