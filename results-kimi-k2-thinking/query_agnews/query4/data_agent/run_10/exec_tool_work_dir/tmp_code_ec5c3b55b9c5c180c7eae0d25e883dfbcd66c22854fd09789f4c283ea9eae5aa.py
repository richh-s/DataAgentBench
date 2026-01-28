code = """import json

# Read the metadata_2015 file
file_path = var_functions.query_db:5
with open(file_path, 'r') as f:
    metadata_2015 = json.load(f)

# Read the articles database file
articles_file_path = var_functions.query_db:2
with open(articles_file_path, 'r') as f:
    articles = json.load(f)

# Count 2015 articles by region
from collections import Counter
region_counts = Counter(record['region'] for record in metadata_2015)
print('Total 2015 articles:', len(metadata_2015))
print('By region:', dict(region_counts))

# Get article IDs from 2015
article_ids_2015 = set(record['article_id'] for record in metadata_2015)
print('Unique article IDs in 2015:', len(article_ids_2015))

# Check sample article titles
sample_articles = [a for a in articles if a['article_id'] in list(article_ids_2015)[:5]]
print('Sample 2015 articles:', [(a['article_id'], a['title'][:100]) for a in sample_articles])

# For now, just print a summary
result = {
    "total_2015_articles": len(metadata_2015),
    "region_distribution": dict(region_counts),
    "sample_article_count": len(sample_articles)
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
