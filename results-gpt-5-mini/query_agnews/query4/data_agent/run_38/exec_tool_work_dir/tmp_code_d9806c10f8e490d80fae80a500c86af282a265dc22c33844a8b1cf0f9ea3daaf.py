code = """import json
import pandas as pd

# Load the large JSON results from storage file paths provided by previous tool calls
with open(var_call_tm3Bd6RxkaarWI4Dt3IQoV6H, 'r') as f:
    articles = json.load(f)
with open(var_call_vcG4YDYzbue5hL1NKiEe3Btk, 'r') as f:
    metadata = json.load(f)

# Create DataFrames
df_articles = pd.DataFrame(articles)
df_metadata = pd.DataFrame(metadata)

# Ensure article_id types are consistent (strings)
df_articles['article_id'] = df_articles['article_id'].astype(str)
df_metadata['article_id'] = df_metadata['article_id'].astype(str)

# Merge on article_id for articles published in 2015 (metadata already filtered by query)
df = pd.merge(df_metadata, df_articles[['article_id', 'title', 'description']], on='article_id', how='left')

# Simple rule-based classifier for categories
sports_kw = ['football','soccer','nba','nfl','mlb','cricket','olympic','olympics','goal','score','match','tournament','season','coach','team','league','won','loss','defeat','beat','championship','pitcher','home run','touchdown']
business_kw = ['market','markets','stocks','stock','shares','bank','finance','financial','economy','economic','ipo','merger','acquisition','investment','company','firm','profit','loss','debt','dow','nasdaq','ftse','profit','revenue']
tech_kw = ['technology','tech','science','scientists','research','software','internet','google','apple','microsoft','ai','robot','robotics','nasa','space','cyber','gadget','device','computer']

def classify(row):
    text = ' '.join([str(row.get('title','') or ''), str(row.get('description','') or '')]).lower()
    # check sports
    for kw in sports_kw:
        if kw in text:
            return 'Sports'
    for kw in business_kw:
        if kw in text:
            return 'Business'
    for kw in tech_kw:
        if kw in text:
            return 'Science/Technology'
    return 'World'

# Apply classification
df['category'] = df.apply(classify, axis=1)

# Count World category per region
world_df = df[df['category']=='World']
counts = world_df['region'].value_counts().to_dict()

# Determine max
if counts:
    max_count = max(counts.values())
    top_regions = [r for r,c in counts.items() if c==max_count]
    if len(top_regions)==1:
        result = {'region': top_regions[0], 'count': max_count}
    else:
        result = {'regions': top_regions, 'count': max_count}
else:
    result = {'region': None, 'count': 0}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_tm3Bd6RxkaarWI4Dt3IQoV6H': 'file_storage/call_tm3Bd6RxkaarWI4Dt3IQoV6H.json', 'var_call_vcG4YDYzbue5hL1NKiEe3Btk': 'file_storage/call_vcG4YDYzbue5hL1NKiEe3Btk.json'}

exec(code, env_args)
