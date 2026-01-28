code = """import json

# Access the file path from the previous query result
file_path = locals()['var_functions.query_db:5']

# Read the European articles data from the file
with open(file_path, 'r') as f:
    europe_articles = json.load(f)

# Extract article IDs and publication years
europe_article_data = []
for article in europe_articles:
    article_id = int(article['article_id'])
    pub_date = article['publication_date']
    year = int(pub_date.split('-')[0])
    europe_article_data.append({
        'article_id': article_id,
        'year': year,
        'publication_date': pub_date
    })

# Count articles per year
from collections import Counter
year_counts = Counter([item['year'] for item in europe_article_data])

print('__RESULT__:')
print(json.dumps({
    'total_europe_articles': len(europe_article_data),
    'articles_per_year': dict(year_counts),
    'sample_data': europe_article_data[:5]
}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.list_db:2': ['authors', 'article_metadata'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
