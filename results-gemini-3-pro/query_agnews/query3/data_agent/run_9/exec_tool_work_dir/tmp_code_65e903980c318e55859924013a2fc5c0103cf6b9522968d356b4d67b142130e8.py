code = """import json

# Load metadata IDs
with open(locals()['var_function-call-9790443739614513755'], 'r') as f:
    metadata_list = json.load(f)

article_year_map = {}
for item in metadata_list:
    aid = int(item['article_id'])
    year = int(item['publication_date'].split('-')[0])
    article_year_map[aid] = year

# Load articles
with open(locals()['var_function-call-13176827165821674892'], 'r') as f:
    articles_list = json.load(f)

sample_titles = []
count = 0
for article in articles_list:
    try:
        aid = int(article.get('article_id'))
    except:
        continue
        
    if aid in article_year_map:
        sample_titles.append(article.get('title', '') + " - " + article.get('description', ''))
        count += 1
        if count >= 20:
            break

print("__RESULT__:")
print(json.dumps(sample_titles))"""

env_args = {'var_function-call-9790443739614513755': 'file_storage/function-call-9790443739614513755.json', 'var_function-call-3385916558167782532': 'file_storage/function-call-3385916558167782532.json', 'var_function-call-16581665091431742479': 14860, 'var_function-call-13176827165821674892': 'file_storage/function-call-13176827165821674892.json', 'var_function-call-8099412520408383884': {'business_counts_per_year': {'2010': 0, '2011': 0, '2012': 0, '2013': 0, '2014': 0, '2015': 0, '2016': 0, '2017': 0, '2018': 0, '2019': 0, '2020': 0}, 'total_business': 0, 'average': 0.0, 'filtered_articles': 5762}}

exec(code, env_args)
