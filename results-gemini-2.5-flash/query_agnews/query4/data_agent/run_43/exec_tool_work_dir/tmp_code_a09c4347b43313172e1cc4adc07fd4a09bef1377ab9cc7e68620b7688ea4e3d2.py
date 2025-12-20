code = """import json

world_articles_raw = json.loads(locals()['var_function-call-5168486326354216759']['results'][0])
world_article_ids = [article['article_id'] for article in world_articles_raw]

# Construct the SQL query for article_metadata
# Filter by article_id and publication_date in 2015
placeholders = ', '.join([str(id) for id in world_article_ids])

sql_query = f'''
SELECT
  region,
  publication_date
FROM
  article_metadata
WHERE
  article_id IN ({placeholders}) AND strftime('%Y', publication_date) = '2015';
'''

print("__RESULT__:")
print(json.dumps(sql_query))"""

env_args = {'var_function-call-5168486326354216759': [{'_id': '6943fdba5da807438c1b5fc9', 'article_id': '4'}, {'_id': '6943fdba5da807438c1b5ff8', 'article_id': '51'}, {'_id': '6943fdba5da807438c1b5fff', 'article_id': '58'}, {'_id': '6943fdba5da807438c1b601c', 'article_id': '87'}, {'_id': '6943fdba5da807438c1b6029', 'article_id': '100'}]}

exec(code, env_args)
