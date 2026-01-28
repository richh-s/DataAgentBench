code = """import json
import pandas as pd
import re
from collections import Counter

# Load merged 2015 data from previous step
merged_data = locals()['var_functions.execute_python:30']

# Actually I need to reload from the files to get the full data
articles_path = locals()['var_functions.query_db:4']
metadata_2015_path = locals()['var_functions.query_db:22']

with open(articles_path, 'r') as f:
    articles_data = json.load(f)

with open(metadata_2015_path, 'r') as f:
    metadata_2015 = json.load(f)

articles_df = pd.DataFrame(articles_data)
metadata_2015_df = pd.DataFrame(metadata_2015)

# Merge the data
merged_df = articles_df.merge(metadata_2015_df, on='article_id', how='inner')

# Define World category keywords
world_keywords = [
    'iraq', 'iraqi', 'opec', 'oil', 'eurozone', 'euro', 'trade', 'deficit', 'global', 'international',
    'china', 'chinese', 'japan', 'japanese', 'asia', 'asian', 'europe', 'european', 'africa', 'african',
    'dollar', 'currency', 'economy', 'economic', 'military', 'war', 'peace', 'united nations', 'un',
    'world bank', 'imf', 'world trade', 'foreign', 'embassy', 'diplomatic', 'summit', 'diplomacy',
    'embargoes', 'sanctions', 'border', 'mexico', 'canada', 'australia', 'india', 'korea', 'nuclear'
]

# Function to classify if article is World category
def is_world_category(title, description):
    text = f"{title} {description}".lower()
    
    # Specific patterns for World news
    if re.search(r'\b(iraq|iraqi|optec|eurozone|euro|trade deficit|dollar|united nations|foreign policy|diplomatic|embassy|summit|imf|world bank)\b', text):
        return True
    
    references_multiple_regions = sum([
        'asia' in text or 'asian' in text,
        'europe' in text or 'european' in text, 
        'africa' in text or 'african' in text,
        'south america' in text,
        'north america' in text,
        'mexico' in text,
        'canada' in text,
        'japan' in text or 'japanese' in text,
        'china' in text or 'chinese' in text,
        'india' in text or 'indian' in text
    ])
    
    if references_multiple_regions >= 2:
        return True
    
    if any(keyword in text for keyword in world_keywords):
        # Exclude sports-specific terms
        sports_keywords = ['nba', 'nfl', 'football', 'soccer', 'basketball', 'baseball', 'hockey', 'tennis', 'golf']
        if any(sport in text for sport in sports_keywords):
            return False
        return True
    
    return False

# Classify articles
merged_df['is_world'] = merged_df.apply(lambda row: is_world_category(row['title'], row['description']), axis=1)

# Filter World articles
world_articles = merged_df[merged_df['is_world'] == True]

# Count by region
region_counts = world_articles['region'].value_counts()

result = {
    "total_2015_articles": len(merged_df),
    "world_articles": len(world_articles),
    "region_counts": region_counts.to_dict(),
    "top_region": region_counts.index[0] if not region_counts.empty else None,
    "top_region_count": region_counts.iloc[0] if not region_counts.empty else 0
}

print('__RESULT__:')
print(json.dumps(result, default=str))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:20': {'articles_count': 10000, 'metadata_count': 127600, 'articles_columns': ['article_id', 'title', 'description'], 'metadata_columns': ['article_id', 'author_id', 'region', 'publication_date']}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:26': {'total_articles': 10000, 'articles_2015': 6696, 'sample_articles': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}], 'sample_metadata': [{'article_id': '13', 'region': 'Europe', 'publication_date': '2015-10-17'}, {'article_id': '18', 'region': 'South America', 'publication_date': '2015-08-15'}]}, 'var_functions.execute_python:30': {'merged_count': 494, 'regions_available': {'Europe': 105, 'Africa': 101, 'North America': 98, 'South America': 97, 'Asia': 93}}}

exec(code, env_args)
