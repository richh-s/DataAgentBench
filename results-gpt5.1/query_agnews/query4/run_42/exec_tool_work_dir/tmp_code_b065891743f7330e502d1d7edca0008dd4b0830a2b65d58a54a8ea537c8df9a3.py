code = """import json, pandas as pd

# Load full results if stored in files
meta_path = var_call_NuGm1IwbNhMRaiIDKyWsp9PH
arts_path = var_call_BgpuZRatc3tmEDlhgZlcwHUD

with open(meta_path, 'r') as f:
    meta = json.load(f)
with open(arts_path, 'r') as f:
    arts = json.load(f)

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# Ensure article_id types match
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# Merge on article_id
df = meta_df.merge(arts_df, on='article_id', how='inner')

# Simple keyword-based categorization for World vs others
# We'll mark as World if it seems about countries, international politics, conflicts, global orgs, etc.

world_keywords = [
    ' iraq', ' israel', ' palestin', ' sudan', 'darfur', 'afghan', ' russia', 'moscow', 'putin', 'chechnya',
    'european union', 'eu ', 'u.n.', 'un ', 'united nations', 'election', 'president', 'prime minister',
    'taliban', 'al-qaeda', 'militant', 'rebel', 'ceasefire', 'conflict', 'war ', ' troops', ' bomb', 'terror',
    'middle east', ' baghdad', ' gaza', 'west bank', 'world leaders', ' summit', ' nuclear program',
    'north korea', 'nkorea', ' kashmir', 'pakistan', 'china ', 'beijing', 'japan ', ' tokyo',
    'africa ', 'asian ', 'europe ', 'latin america', 'diplomat', ' embassy', 'border', ' refugees', 'refugee'
]

business_keywords = ['stock', 'shares', 'market', 'economy', 'investment', 'fund', 'bank', 'trade deficit', 'oil prices']
sports_keywords = [' game', ' games', ' match', 'tournament', ' cup', 'league', 'olympic', ' medal', 'score', 'coach', ' team']
scitech_keywords = [' software', 'computer', ' technology', 'scientist', ' researchers', ' study', 'research', 'nuclear plant']


def categorize(text):
    if not isinstance(text, str):
        return 'Other'
    t = ' ' + text.lower() + ' '
    # World if any world keyword present
    if any(k in t for k in world_keywords):
        return 'World'
    if any(k in t for k in sports_keywords):
        return 'Sports'
    if any(k in t for k in business_keywords):
        return 'Business'
    if any(k in t for k in scitech_keywords):
        return 'Science/Technology'
    return 'Other'

# Apply categorization using both title and description
combined = (df['title'].fillna('') + ' ' + df['description'].fillna(''))
df['category'] = combined.apply(categorize)

world_df = df[df['category'] == 'World']

# Count by region
region_counts = world_df['region'].value_counts().to_dict()

# Find max region
if region_counts:
    max_region = max(region_counts, key=region_counts.get)
else:
    max_region = None

result = {'region_with_most_world_articles_2015': max_region, 'counts_by_region': region_counts}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_NuGm1IwbNhMRaiIDKyWsp9PH': 'file_storage/call_NuGm1IwbNhMRaiIDKyWsp9PH.json', 'var_call_BgpuZRatc3tmEDlhgZlcwHUD': 'file_storage/call_BgpuZRatc3tmEDlhgZlcwHUD.json'}

exec(code, env_args)
