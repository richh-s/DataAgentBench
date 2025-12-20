code = """import pandas as pd
import json

# Load the full article_metadata_2015 result from the file
with open(locals()['var_function-call-4142005257738235693'], 'r') as f:
    article_metadata_2015 = json.load(f)

# Load the article_ids_2015 from the file
with open(locals()['var_function-call-10407798788679954601'], 'r') as f:
    article_ids_2015 = json.load(f)

articles_data = locals()['var_function-call-10122244090567098285']

# Create DataFrames
df_metadata_2015 = pd.DataFrame(article_metadata_2015)
df_articles = pd.DataFrame(articles_data)

# Convert 'article_id' columns to numeric, coercing errors to NaN
df_metadata_2015['article_id'] = pd.to_numeric(df_metadata_2015['article_id'], errors='coerce')
df_articles['article_id'] = pd.to_numeric(df_articles['article_id'], errors='coerce')

# Drop rows where article_id became NaN due to coercion errors
df_metadata_2015.dropna(subset=['article_id'], inplace=True)
df_articles.dropna(subset=['article_id'], inplace=True)

# Convert 'article_id' to integer type after handling NaNs
df_metadata_2015['article_id'] = df_metadata_2015['article_id'].astype(int)
df_articles['article_id'] = df_articles['article_id'].astype(int)

# Ensure article_ids_2015 are integers
article_ids_2015_int = [int(aid) for aid in article_ids_2015]

# Filter df_articles to include only articles from 2015
df_articles_2015 = df_articles[df_articles['article_id'].isin(article_ids_2015_int)]

# Merge the two DataFrames on 'article_id'
df_merged = pd.merge(df_metadata_2015, df_articles_2015, on='article_id')

# Define keywords for categories (case-insensitive)
sports_keywords = ['sport', 'team', 'game', 'match', 'league', 'cup', 'championship', 'athlete', 'coach', 'player', 'score', 'win', 'lose', 'olympic', 'football', 'basketball', 'baseball', 'soccer', 'tennis', 'golf']
business_keywords = ['business', 'market', 'economy', 'company', 'firm', 'stock', 'invest', 'finance', 'profit', 'earn', 'trade', 'deal', 'merger', 'acquisition', 'ceo', 'bank', 'industry', 'economic']
science_tech_keywords = ['science', 'technology', 'tech', 'research', 'study', 'discover', 'invent', 'develop', 'digital', 'internet', 'software', 'hardware', 'computer', 'phone', 'space', 'medical', 'health']

def categorize_article_revised(title, description):
    # Ensure title and description are strings, handle None
    title_str = str(title) if title is not None else ""
    description_str = str(description) if description is not None else ""
    text = (title_str + ' ' + description_str).lower()

    if any(keyword in text for keyword in sports_keywords):
        return 'Sports'
    if any(keyword in text for keyword in business_keywords):
        return 'Business'
    if any(keyword in text for keyword in science_tech_keywords):
        return 'Science/Technology'
    return 'World' # If it doesn't fit into other categories, it's 'World'

df_merged['category'] = df_merged.apply(lambda row: categorize_article_revised(row['title'], row['description']), axis=1)

# Filter for 'World' category articles
world_articles = df_merged[df_merged['category'] == 'World']

# Count articles per region
region_counts = world_articles['region'].value_counts().reset_index()
region_counts.columns = ['region', 'article_count']

# Find the region with the largest number of articles
if not region_counts.empty:
    largest_region = region_counts.loc[region_counts['article_count'].idxmax()]
    result = largest_region['region']
else:
    result = "No 'World' category articles found for 2015."

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-4142005257738235693': 'file_storage/function-call-4142005257738235693.json', 'var_function-call-10407798788679954601': 'file_storage/function-call-10407798788679954601.json', 'var_function-call-10122244090567098285': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-14299870682571490829': "No 'World' category articles found for 2015."}

exec(code, env_args)
