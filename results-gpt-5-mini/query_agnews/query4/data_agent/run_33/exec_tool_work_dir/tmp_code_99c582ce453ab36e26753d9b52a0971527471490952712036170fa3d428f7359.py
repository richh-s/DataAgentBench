code = """import json
import pandas as pd

# Load data from storage variables (file paths)
with open(var_call_Ssg4ssIEyZZThdTKqce4zoxw, 'r', encoding='utf-8') as f:
    articles = json.load(f)
with open(var_call_Ltiy8RqXJXeFXMe93EshdKqK, 'r', encoding='utf-8') as f:
    metadata = json.load(f)

# Create DataFrames
df_articles = pd.DataFrame(articles)
df_metadata = pd.DataFrame(metadata)

# Ensure article_id types are strings
df_articles['article_id'] = df_articles['article_id'].astype(str)
df_metadata['article_id'] = df_metadata['article_id'].astype(str)

# Merge on article_id (inner join)
df = pd.merge(df_metadata, df_articles, on='article_id', how='inner')

# Lowercase text for classification
df['text'] = (df.get('title','').fillna('') + ' ' + df.get('description','').fillna('')).str.lower()

# Define keyword lists for categories
sports_kw = ['football','soccer','olympic','world cup','cup','match','goal','score','scored','nba','nfl','mlb','tennis','cricket','rugby','hockey','coach','season','player','tournament','race','fifa','goalkeeper','defeated','beat','won','loss']
business_kw = ['stock','stocks','market','markets','shares','ipo','earnings','profit','investment','bank','dollar','trade deficit','economy','oil prices','oil prices','oil','revenue','funds','mutual fund','mutual funds','bond','fed','interest rate','interest rates','acqui','merger','loan']
science_kw = ['scientist','science','research','nasa','nuclear','ph.d','phd','drug','experiment','technology','tech','computer','software','internet','e-mail','email','researchers','study','scientists','clinical','medical','disease','cure','lab']

# Classification function
def classify(text):
    if any(k in text for k in sports_kw):
        return 'Sports'
    if any(k in text for k in science_kw):
        return 'Science/Technology'
    if any(k in text for k in business_kw):
        return 'Business'
    # Default to World
    return 'World'

# Apply classification
df['category'] = df['text'].apply(classify)

# Filter to World category
world_df = df[df['category'] == 'World']

# Count by region
counts = world_df.groupby('region').size().reset_index(name='count')

# If no results, prepare empty output
if counts.empty:
    result = {'region': None, 'count': 0}
else:
    # Find region(s) with max count
    max_count = int(counts['count'].max())
    top_regions = counts[counts['count'] == max_count]['region'].tolist()
    # If multiple, return all regions as list
    if len(top_regions) == 1:
        result = {'region': top_regions[0], 'count': max_count}
    else:
        result = {'regions': top_regions, 'count': max_count}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Ssg4ssIEyZZThdTKqce4zoxw': 'file_storage/call_Ssg4ssIEyZZThdTKqce4zoxw.json', 'var_call_Ltiy8RqXJXeFXMe93EshdKqK': 'file_storage/call_Ltiy8RqXJXeFXMe93EshdKqK.json'}

exec(code, env_args)
