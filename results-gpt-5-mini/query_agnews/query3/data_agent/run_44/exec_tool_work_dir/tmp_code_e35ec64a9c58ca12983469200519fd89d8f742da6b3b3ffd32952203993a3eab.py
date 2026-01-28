code = """import json
import pandas as pd

# Load previous tool results from storage files
with open(var_call_ADooTJsoYTQedMHxPY31nFQW, 'r') as f:
    meta = json.load(f)
with open(var_call_DTmKHxnsHgilUD1O0ooSK0Is, 'r') as f:
    arts = json.load(f)

df_meta = pd.DataFrame(meta)
df_art = pd.DataFrame(arts)

# Ensure article_id are strings for a proper merge
df_meta['article_id'] = df_meta['article_id'].astype(str)
df_art['article_id'] = df_art['article_id'].astype(str)

# Merge metadata (filtered to Europe 2010-2020 by previous query) with articles
df = pd.merge(df_meta, df_art, on='article_id', how='left')

# Extract year
df['year'] = df['publication_date'].str.slice(0,4).astype(int)

# Classification keyword lists
business_kw = ['econom', 'economy', 'market', 'markets', 'stock', 'stocks', 'ipo', 'share', 'shares', 'bank', 'banks', 'investment', 'investor', 'trade', 'trades', 'commercial', 'finance', 'financial', 'money', 'funds', 'currency', 'dollar', 'euro', 'gdp', 'inflation', 'unemployment', 'profit', 'loss', 'revenue', 'earnings']
sports_kw = ['football', 'soccer', 'match', 'goal', 'season', 'tournament', 'nba', 'nfl', 'mlb', 'coach', 'player', 'score', 'cup', 'championship', 'olympic', 'olympics']
science_kw = ['technology', 'tech', 'scientist', 'scientists', 'research', 'nuclear', 'drug', 'drugs', 'science', 'computer', 'software', 'hardware', 'internet', 'ai', 'artificial intelligence', 'climate', 'study', 'researchers', 'medical', 'disease', 'health', 'biotech']
world_kw = ['war', 'election', 'president', 'prime minister', 'conflict', 'country', 'countries', 'military', 'refugee', 'attack', 'minister', 'united nations', 'diplomat', 'diplomacy', 'government', 'politic', 'political', 'terror', 'terrorist']

def classify_row(title, desc):
    text = ''
    if isinstance(title, str):
        text += title + ' '
    if isinstance(desc, str):
        text += desc
    text = text.lower()
    # Sports priority
    for kw in sports_kw:
        if kw in text:
            return 'Sports'
    # Business
    for kw in business_kw:
        if kw in text:
            return 'Business'
    # Science/Technology
    for kw in science_kw:
        if kw in text:
            return 'Science/Technology'
    # World
    for kw in world_kw:
        if kw in text:
            return 'World'
    # Default
    return 'World'

# Apply classification
df['category'] = df.apply(lambda r: classify_row(r.get('title',''), r.get('description','')), axis=1)

# Consider years 2010 through 2020 inclusive
years = list(range(2010, 2021))
counts = {str(y): 0 for y in years}

business_df = df[df['category'] == 'Business']
by_year = business_df.groupby('year').size().to_dict()
for y,v in by_year.items():
    if 2010 <= int(y) <= 2020:
        counts[str(int(y))] = int(v)

average = sum(counts.values()) / len(years)

result = {
    'yearly_business_counts': counts,
    'average_business_articles_per_year': average
}

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_ADooTJsoYTQedMHxPY31nFQW': 'file_storage/call_ADooTJsoYTQedMHxPY31nFQW.json', 'var_call_DTmKHxnsHgilUD1O0ooSK0Is': 'file_storage/call_DTmKHxnsHgilUD1O0ooSK0Is.json'}

exec(code, env_args)
