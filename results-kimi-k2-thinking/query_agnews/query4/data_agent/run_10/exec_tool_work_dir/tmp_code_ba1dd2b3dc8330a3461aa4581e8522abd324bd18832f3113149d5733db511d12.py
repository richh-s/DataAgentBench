code = """import json

# Load the saved variables correctly
articles_file = locals()['var_functions.query_db:2']
metadata_file = locals()['var_functions.query_db:5']

# Read the files
with open(articles_file, 'r') as f:
    articles = json.load(f)

with open(metadata_file, 'r') as f:
    metadata_2015 = json.load(f)

print('Load successful')
print('Total articles in database:', len(articles))
print('Total articles in 2015 metadata:', len(metadata_2015))

# Extract 2015 article IDs
article_ids_2015 = set(record['article_id'] for record in metadata_2015)

# Filter articles published in 2015
articles_2015 = [a for a in articles if a['article_id'] in article_ids_2015]

print('Articles found for 2015:', len(articles_2015))
print('Article IDs from metadata:', len(article_ids_2015))
print('Intersection count:', len(articles_2015))

# Show sample articles
print('Sample 2015 articles:')
for i, article in enumerate(articles_2015[:5]):
    print(f"{i+1}. ID: {article['article_id']}, Title: {article['title'][:80]}")

result = {
    'articles_in_database': len(articles),
    'metadata_entries_2015': len(metadata_2015),
    'matching_articles_2015': len(articles_2015)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
