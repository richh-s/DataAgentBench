code = """import json
import pandas as pd

# Load data from storage file paths provided by previous tool calls
with open(var_call_RMTMoeN7Ln8Y2W5BMRq7LCq5, 'r') as f:
    articles = json.load(f)
with open(var_call_eUXolkq4VMwGwvBXBsbjLrlC, 'r') as f:
    metadata = json.load(f)

df_articles = pd.DataFrame(articles)
df_meta = pd.DataFrame(metadata)

# Ensure article_id types are strings for safe merge
df_articles['article_id'] = df_articles['article_id'].astype(str)
df_meta['article_id'] = df_meta['article_id'].astype(str)

# Merge
df = pd.merge(df_meta, df_articles, on='article_id', how='left')

# Filter for year 2015
df['year'] = df['publication_date'].str[:4]
df_2015 = df[df['year'] == '2015'].copy()

# Category keywords
sports_kw = ['football','soccer','world cup','nba','nfl','baseball','match','tournament','goal','scored','defeat','defeated','coach','season','league','players','olympic','cricket','inning','rugby','fifa']
business_kw = ['market','stocks','shares','ipo','investment','company','firm','economy','earnings','bank','merger','acquisition','debt','commodity','oil prices','stock','investor']
sci_kw = ['scientist','scientists','research','nasa','space','technology','tech','computer','software','internet','study','researchers','drug','scientific']

def categorize_text(title, desc):
    text = ''
    if pd.notna(title):
        text += str(title).lower() + ' '
    if pd.notna(desc):
        text += str(desc).lower()
    # Sports first
    for kw in sports_kw:
        if kw in text:
            return 'Sports'
    for kw in business_kw:
        if kw in text:
            return 'Business'
    for kw in sci_kw:
        if kw in text:
            return 'Science/Technology'
    # Default to World
    return 'World'

# Apply categorization
df_2015['category'] = df_2015.apply(lambda r: categorize_text(r.get('title',''), r.get('description','')), axis=1)

# Count World category by region
world_df = df_2015[df_2015['category'] == 'World']
counts = world_df.groupby('region').size().to_dict()

if counts:
    max_count = max(counts.values())
    winning_regions = [r for r,c in counts.items() if c == max_count]
else:
    max_count = 0
    winning_regions = []

result = {
    'winning_regions': winning_regions,
    'count': max_count,
    'counts_by_region': counts
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_RMTMoeN7Ln8Y2W5BMRq7LCq5': 'file_storage/call_RMTMoeN7Ln8Y2W5BMRq7LCq5.json', 'var_call_eUXolkq4VMwGwvBXBsbjLrlC': 'file_storage/call_eUXolkq4VMwGwvBXBsbjLrlC.json'}

exec(code, env_args)
