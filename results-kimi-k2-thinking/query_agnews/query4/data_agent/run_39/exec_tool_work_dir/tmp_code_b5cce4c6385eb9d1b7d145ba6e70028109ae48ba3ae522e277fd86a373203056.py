code = """import json
import pandas as pd

# Access the file paths from storage
metadata_file_path = locals()['var_functions.query_db:2']
articles_file_path = locals()['var_functions.query_db:20']

# Read the files
with open(metadata_file_path, 'r') as f:
    metadata_list = json.load(f)

with open(articles_file_path, 'r') as f:
    articles_list = json.load(f)

# Convert to DataFrames
metadata_df = pd.DataFrame(metadata_list)
articles_df = pd.DataFrame(articles_list)

# Convert article_id to integer
metadata_df['article_id'] = pd.to_numeric(metadata_df['article_id'], errors='coerce')
articles_df['article_id'] = pd.to_numeric(articles_df['article_id'], errors='coerce')

# Merge the dataframes
merged_df = pd.merge(metadata_df, articles_df, on='article_id', how='inner')

# Add category based on title and description keywords
def categorize_article(title, description):
    if pd.isna(title):
        title = ''
    if pd.isna(description):
        description = ''
    
    combined = (title + ' ' + description).lower()
    
    # Tech keywords
    tech_keywords = ['google', 'hp', 'hewlett', 'technology', 'tech', 'internet', 'web', 'software', 'hardware', 'computer', 'digital', 'data', 'online', 'cyber']
    
    # Sports keywords
    sports_keywords = ['sport', 'game', 'match', 'player', 'team', 'score', 'goal', 'olympic', 'championship', 'season', 'coach', 'basketball', 'football', 'soccer', 'baseball', 'tennis', 'golf']
    
    # Business keywords
    business_keywords = ['stock', 'market', 'economy', 'business', 'company', 'firm', 'share', 'profit', 'loss', 'revenue', 'investment', 'trade', 'deficit', 'bank', 'rate', 'interest', 'oil', 'price', 'energy']
    
    # Count keyword matches
    tech_matches = sum(1 for word in tech_keywords if word in combined)
    sports_matches = sum(1 for word in sports_keywords if word in word in combined)
    business_matches = sum(1 for word in business_keywords if word in combined)
    
    # Determine category based on highest keyword matches
    scores = {'science/technology': tech_matches, 'sports': sports_matches, 'business': business_matches}
    max_score = max(scores.values())
    
    if max_score > 0:
        # Return category with highest score
        max_category = [cat for cat, score in scores.items() if score == max_score][0]
        return max_category
    else:
        # Default to World if no specific category found
        return 'world'

# Apply categorization
merged_df['category'] = merged_df.apply(lambda row: categorize_article(row['title'], row['description']), axis=1)

# Filter for World category and count by region
world_articles = merged_df[merged_df['category'] == 'world']
region_counts = world_articles['region'].value_counts()

result = {
    'world_articles_count': len(world_articles),
    'top_regions': region_counts.head().to_dict(),
    'region_with_most_world_articles': region_counts.idxmax() if not region_counts.empty else 'None',
    'total_articles_2015': len(merged_df)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['authors', 'article_metadata'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:18': {'available_files': []}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:24': {'metadata_count': 6696, 'articles_count': 2000, 'sample_metadata': {'article_id': '13', 'region': 'Europe', 'publication_date': '2015-10-17'}, 'sample_articles': {'_id': '6969efa516ce055fb771239d', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}}}

exec(code, env_args)
