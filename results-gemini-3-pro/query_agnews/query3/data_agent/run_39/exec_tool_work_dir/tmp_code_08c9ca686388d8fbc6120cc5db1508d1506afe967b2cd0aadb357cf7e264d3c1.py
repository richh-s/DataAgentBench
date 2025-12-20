code = """import json
import pandas as pd
import re

# Load metadata
metadata_file = locals()['var_function-call-1557171304419617632']
with open(metadata_file, 'r') as f:
    metadata_data = json.load(f)
df_meta = pd.DataFrame(metadata_data)

# Load articles
articles_data = locals()['var_function-call-4617174131752082327']
# If articles_data is a string (file path), load it. If it's a list, use it directly.
if isinstance(articles_data, str) and (articles_data.endswith('.json') or '/' in articles_data or '\\' in articles_data):
    with open(articles_data, 'r') as f:
        articles_data = json.load(f)
df_articles = pd.DataFrame(articles_data)

# Ensure ID types match
df_meta['article_id'] = df_meta['article_id'].astype(int)
df_articles['article_id'] = df_articles['article_id'].astype(int)

# Merge
df = pd.merge(df_meta, df_articles, on='article_id', how='inner')

# Define categorization logic
def get_category(text):
    text = text.lower()
    # Simple keyword lists based on AG News categories
    business_keywords = ['stocks', 'stock', 'market', 'economy', 'oil', 'price', 'prices', 'business', 'profit', 'sales', 'trade', 'dollar', 'euro', 'bank', 'invest', 'rate', 'quarter', 'revenue', 'share', 'shares', 'company', 'corp', 'inc', 'wall st', 'financial', 'growth', 'earnings', 'deal', 'merger', 'acquisition', 'bond', 'yield', 'futures', 'nasdaq', 'dow', 'index', 'fed', 'federal reserve', 'inflation', 'ceo', 'cfo', 'bankrupt']
    
    sports_keywords = ['sport', 'game', 'cup', 'match', 'score', 'win', 'loss', 'team', 'season', 'league', 'player', 'coach', 'olympic', 'champion', 'football', 'soccer', 'baseball', 'basketball', 'hockey', 'tennis', 'golf', 'medal', 'athlete', 'race', 'racing', 'tournament', 'stadium']
    
    scitech_keywords = ['computer', 'software', 'technology', 'science', 'space', 'nasa', 'web', 'internet', 'google', 'microsoft', 'apple', 'linux', 'virus', 'security', 'chip', 'mobile', 'phone', 'network', 'online', 'server', 'data', 'satellite', 'orbit', 'moon', 'mars', 'research', 'study', 'scientist']
    
    world_keywords = ['president', 'minister', 'iraq', 'war', 'military', 'bomb', 'killed', 'police', 'government', 'election', 'official', 'country', 'state', 'un', 'united nations', 'eu', 'europe', 'china', 'russia', 'iran', 'israel', 'palestine', 'nuclear', 'blast', 'attack', 'peace', 'treaty', 'talks']
    
    counts = {'Business': 0, 'Sports': 0, 'Sci/Tech': 0, 'World': 0}
    
    for word in business_keywords:
        if word in text:
            counts['Business'] += 1
    for word in sports_keywords:
        if word in text:
            counts['Sports'] += 1
    for word in scitech_keywords:
        if word in text:
            counts['Sci/Tech'] += 1
    for word in world_keywords:
        if word in text:
            counts['World'] += 1
            
    # Return category with max count
    # Handle ties: Default to World if ambiguous? Or prioritize Business?
    # AG News is balanced.
    
    if max(counts.values()) == 0:
        return 'Unknown'
    
    return max(counts, key=counts.get)

# Apply classification
df['full_text'] = df['title'] + " " + df['description']
df['category'] = df['full_text'].apply(get_category)

# Filter for Business
business_articles = df[df['category'] == 'Business']

# Extract year
df['year'] = pd.to_datetime(df['publication_date']).dt.year
business_articles['year'] = pd.to_datetime(business_articles['publication_date']).dt.year

# Count per year
yearly_counts = business_articles.groupby('year').size()

# Fill missing years with 0
all_years = range(2010, 2021)
yearly_counts = yearly_counts.reindex(all_years, fill_value=0)

# Calculate average
average_per_year = yearly_counts.mean()

print("__RESULT__:")
print(json.dumps({"average": average_per_year, "yearly_counts": yearly_counts.to_dict()}))"""

env_args = {'var_function-call-1557171304419617632': 'file_storage/function-call-1557171304419617632.json', 'var_function-call-4617174131752082327': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
