code = """import json
import pandas as pd
import re

# Load data from the provided storage file paths
with open(var_call_BUgVP0jc0oWr7HtLsDA52B48, 'r') as f:
    articles = json.load(f)
with open(var_call_5Ook0bO3DlT2PFIdda2ilavQ, 'r') as f:
    metadata = json.load(f)

# Create DataFrames
df_articles = pd.DataFrame(articles)
df_meta = pd.DataFrame(metadata)

# Ensure article_id are strings for consistent merge
df_articles['article_id'] = df_articles['article_id'].astype(str)
df_meta['article_id'] = df_meta['article_id'].astype(str)

# Merge datasets (metadata already filtered to 2015 by the previous query)
df = pd.merge(df_meta, df_articles, on='article_id', how='left')

# Fill NaNs
df['title'] = df['title'].fillna('')
df['description'] = df['description'].fillna('')

# Define a simple keyword-based classifier
sports_re = re.compile(r"\b(match|tournament|goal|scored|season|coach|league|player|olympic|world cup|fifa|nba|mlb|nhl|score|defeat|won|lost|tie|draw|penalty|cup)\b", re.I)
science_re = re.compile(r"\b(research|scientist|technology|scientists|nasa|researchers|study|vaccine|drug|computer|software|internet|robot|ai|algorithm|nuclear)\b", re.I)
business_re = re.compile(r"\b(market|stocks|shares|economy|bank|investment|investor|ipo|oil prices|opec|company|earnings|debt|merger|acquisition|profit|loss|billion|million)\b", re.I)

def classify(row):
    text = (row.get('title','') or '') + ' ' + (row.get('description','') or '')
    if sports_re.search(text):
        return 'Sports'
    if science_re.search(text):
        return 'Science/Technology'
    if business_re.search(text):
        return 'Business'
    return 'World'

# Apply classifier
df['category'] = df.apply(classify, axis=1)

# Count World articles per region
world_df = df[df['category'] == 'World']
counts = world_df['region'].value_counts().to_dict()

# Determine region with largest number
if counts:
    # Find max
    max_region = max(counts, key=lambda k: counts[k])
    max_count = counts[max_region]
    result = {"region": max_region, "count": int(max_count), "counts_by_region": counts}
else:
    result = {"region": None, "count": 0, "counts_by_region": {}}

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_BUgVP0jc0oWr7HtLsDA52B48': 'file_storage/call_BUgVP0jc0oWr7HtLsDA52B48.json', 'var_call_5Ook0bO3DlT2PFIdda2ilavQ': 'file_storage/call_5Ook0bO3DlT2PFIdda2ilavQ.json'}

exec(code, env_args)
