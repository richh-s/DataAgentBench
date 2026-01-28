code = """import json
import pandas as pd
import re

# Load metadata results from 2015 (stored in a file path)
with open(var_call_jm85jivNDbNdTdQEuK7jnaut, 'r') as f:
    meta_list = json.load(f)

articles_list = var_call_R2jNBknJi6SeeBgyEJpgv69C

# Create DataFrames
df_meta = pd.DataFrame(meta_list)
df_articles = pd.DataFrame(articles_list)

# Ensure article_id are strings
df_meta['article_id'] = df_meta['article_id'].astype(str)
df_articles['article_id'] = df_articles['article_id'].astype(str)

# Merge
df = pd.merge(df_meta, df_articles, on='article_id', how='left')

# Prepare classification keywords
sports_kw = [r'\bmatch\b', r'\bleague\b', r'\bgoal\b', r'\bscore\b', r'\bplayer\b', r'\bcoach\b', r'\btournament\b', r'\bseason\b', r'\bwin\b', r'\bfootball\b', r'\bsoccer\b', r'\bboxing\b', r'\bbasketball\b', r'\bcricket\b', r'\bolympic\b', r'\bchampionship\b']
business_kw = [r'\bstock\b', r'\bmarket\b', r'\beconomy\b', r'\binvest\b', r'\bfirm\b', r'\bshares\b', r'\bipo\b', r'\bmerger\b', r'\bacquisition\b', r'\bbusiness\b', r'\bprofit\b', r'\bearnings\b', r'\bcompany\b', r'\bbillion\b', r'\bmillion\b', r'\boil prices\b', r'\bWall St\b', r'\bWall Street\b']
science_kw = [r'\bscience\b', r'\bscientist\b', r'\bresearch\b', r'\btechnology\b', r'\btech\b', r'\bNASA\b', r'\bspace\b', r'\brobot\b', r'\bAI\b', r'\bsmartphone\b', r'\bcomputer\b']
# world will be default if none of the above

# Combine title and description
df['text'] = ((df['title'].fillna('') + ' ') + df['description'].fillna('')).str.lower()

# Classification function

def contains_any(text, patterns):
    for p in patterns:
        if re.search(p, text):
            return True
    return False

cats = []
for t in df['text']:
    if contains_any(t, sports_kw):
        cats.append('Sports')
    elif contains_any(t, business_kw):
        cats.append('Business')
    elif contains_any(t, science_kw):
        cats.append('Science/Technology')
    else:
        cats.append('World')

df['category'] = cats

# Filter for 2015 (should already be)
df2015 = df[df['publication_date'].str.startswith('2015-')]

# Count World by region
world_df = df2015[df2015['category']=='World']
counts = world_df.groupby('region').size().to_dict()

if counts:
    max_count = max(counts.values())
    top_regions = sorted([r for r,c in counts.items() if c==max_count])
else:
    max_count = 0
    top_regions = []

result = {
    'top_regions': top_regions,
    'max_count': int(max_count),
    'counts': counts
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_OoKHmo9bJ5zwkJnDvuV58Gni': ['articles'], 'var_call_HdTXyE0OafYrI9bshoo0iSiC': ['authors', 'article_metadata'], 'var_call_jm85jivNDbNdTdQEuK7jnaut': 'file_storage/call_jm85jivNDbNdTdQEuK7jnaut.json', 'var_call_R2jNBknJi6SeeBgyEJpgv69C': [{'_id': '6959a5342d95f78d21b9f583', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6959a5342d95f78d21b9f584', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6959a5342d95f78d21b9f585', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6959a5342d95f78d21b9f586', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6959a5342d95f78d21b9f587', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
