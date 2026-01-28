code = """import json
import pandas as pd

# Load data from previous tool results (file paths are stored in these variables)
metadata_path = var_call_ShhESQk3hfs88JLAUy0SSB82
articles_path = var_call_fdsvo3z9haQ9Zi9YepmTfslw

with open(metadata_path, 'r', encoding='utf-8') as f:
    metadata = json.load(f)
with open(articles_path, 'r', encoding='utf-8') as f:
    articles = json.load(f)

md = pd.DataFrame(metadata)
arts = pd.DataFrame(articles)

# Ensure article_id is string for merging
md['article_id'] = md['article_id'].astype(str)
arts['article_id'] = arts['article_id'].astype(str)

# Merge
df = pd.merge(md, arts, on='article_id', how='left')

# Combine title and description
df['text'] = (df['title'].fillna('') + ' ' + df['description'].fillna('')).str.lower()

# Define keyword sets for classification
sports_kw = ['football', 'soccer', 'match', 'goal', 'league', 'tournament', 'olympic', 'olympics', 'nba', 'nfl', 'mlb', 'nhl', 'cricket', 'coach', 'season', 'victory', 'defeat', 'score', 'world cup', 'cup final']
business_kw = ['stock', 'market', 'shares', 'ipo', 'investment', 'company', 'companies', 'economy', 'profit', 'loss', 'bank', 'revenue', 'merger', 'acquisition', 'business', 'financial', 'oil prices', 'oil', 'trade deficit']
science_kw = ['scientist', 'research', 'study', 'nasa', 'space', 'technology', 'tech', 'computer', 'software', 'internet', 'scientific', 'dna', 'researchers', 'lab', 'chemical', 'physics']

def classify(text):
    s = text
    sports_count = sum(s.count(k) for k in sports_kw)
    business_count = sum(s.count(k) for k in business_kw)
    science_count = sum(s.count(k) for k in science_kw)
    counts = {'Sports': sports_count, 'Business': business_count, 'Science/Technology': science_count}
    max_cat = max(counts, key=lambda k: counts[k])
    if counts[max_cat] == 0:
        return 'World'
    # If tie or other, pick the category with highest count; if tie prefer Sports>Business>Science
    max_val = counts[max_cat]
    tied = [k for k,v in counts.items() if v==max_val and v>0]
    if len(tied) == 1:
        return max_cat
    priority = ['Sports','Business','Science/Technology']
    for p in priority:
        if p in tied:
            return p
    return 'World'

# Apply classification
df['category'] = df['text'].apply(classify)

# Filter to World category
world_df = df[df['category']=='World']

# Count by region
region_counts = world_df.groupby('region').size().to_dict()

if len(region_counts)==0:
    result = {'region': None, 'count': 0}
else:
    # find max
    max_count = max(region_counts.values())
    top_regions = [r for r,c in region_counts.items() if c==max_count]
    # If multiple top regions, include all
    result = {'top_regions': top_regions, 'count': int(max_count)}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_5bqAvpJmFvknUszExQqMcoeN': ['articles'], 'var_call_ZPHBruObinwzi3wISqk4ubg7': ['authors', 'article_metadata'], 'var_call_ShhESQk3hfs88JLAUy0SSB82': 'file_storage/call_ShhESQk3hfs88JLAUy0SSB82.json', 'var_call_fdsvo3z9haQ9Zi9YepmTfslw': 'file_storage/call_fdsvo3z9haQ9Zi9YepmTfslw.json'}

exec(code, env_args)
