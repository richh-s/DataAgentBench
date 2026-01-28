code = """import pandas as pd
import json

# Load data from tool results
articles = var_call_pozM42g3NtdjP99YZegizHX5
meta_path = var_call_RjIC5wiX7bZCCHnzdFf5QEgJ

with open(meta_path, 'r') as f:
    metadata = json.load(f)

# Create DataFrames
df_articles = pd.DataFrame(articles)
df_meta = pd.DataFrame(metadata)

# Normalize article_id as string for joining
if 'article_id' in df_articles.columns:
    df_articles['article_id'] = df_articles['article_id'].astype(str)
if 'article_id' in df_meta.columns:
    df_meta['article_id'] = df_meta['article_id'].astype(str)

# Merge metadata (already filtered to Europe and date range) with articles
df = pd.merge(df_meta, df_articles, on='article_id', how='left')

# Prepare text for classification
df['title'] = df['title'].fillna('')
if 'description' in df.columns:
    df['description'] = df['description'].fillna('')
else:
    df['description'] = ''

df['text'] = (df['title'] + ' ' + df['description']).str.lower()

def classify_text(text):
    # Keywords for categories
    business_kw = ['wall st', 'wall street', 'stock', 'stocks', 'market', 'markets', 'economy', 'investment', 'investor', 'investment firm', 'firm', 'private investment', 'shares', 'earnings', 'bank', 'financial', 'carlyle', 'short-sellers', 'short seller', 'ipo', 'merger', 'acquisition', 'profit', 'profits', 'revenue', 'oil prices']
    sports_kw = ['football', 'soccer', 'match', 'tournament', 'goal', 'nba', 'nfl', 'olympic', 'championship', 'season']
    science_kw = ['technology', 'tech', 'science', 'research', 'space', 'nasa', 'scientists', 'study', 'computer', 'software', 'robot', 'ai', 'smartphone']
    world_kw = ['president', 'government', 'election', 'war', 'conflict', 'rebel', 'militia', 'police', 'country', 'foreign', 'minister', 'iraq', 'terror', 'attack', 'pipeline', 'exports', 'un ', 'diplomatic']

    for kw in business_kw:
        if kw in text:
            return 'Business'
    for kw in sports_kw:
        if kw in text:
            return 'Sports'
    for kw in science_kw:
        if kw in text:
            return 'Science/Technology'
    for kw in world_kw:
        if kw in text:
            return 'World'
    # default fallback
    return 'World'

# Apply classification
df['category'] = df['text'].apply(classify_text)

# Extract year and filter to 2010-2020 inclusive
df['publication_date'] = df['publication_date'].fillna('')

def extract_year(d):
    try:
        return int(d[:4])
    except:
        return None

df['year'] = df['publication_date'].apply(extract_year)

df = df[df['year'].between(2010, 2020)]

# Count business articles per year
business_counts_series = df[df['category'] == 'Business'].groupby('year').size()

counts_by_year = {str(year): int(business_counts_series.get(year, 0)) for year in range(2010, 2021)}

total_business = sum(counts_by_year.values())
average_per_year = round(total_business / 11.0, 2)

result = {
    'average_business_articles_per_year': average_per_year,
    'total_business_articles_2010_2020': int(total_business),
    'counts_by_year': counts_by_year
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_pozM42g3NtdjP99YZegizHX5': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_call_RjIC5wiX7bZCCHnzdFf5QEgJ': 'file_storage/call_RjIC5wiX7bZCCHnzdFf5QEgJ.json'}

exec(code, env_args)
