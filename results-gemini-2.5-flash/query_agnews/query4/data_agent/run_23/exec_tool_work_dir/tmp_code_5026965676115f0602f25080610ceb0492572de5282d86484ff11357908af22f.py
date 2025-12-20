code = """import json
article_ids_string = locals()['var_function-call-1470303306693408111']['query_db_response']['results'][0]
article_ids_list = json.loads(article_ids_string)
article_ids = [item['article_id'] for item in article_ids_list]
print("__RESULT__:")
print(json.dumps(article_ids))"""

env_args = {'var_function-call-1470303306693408111': [{'_id': '6943f7eeb0926f2de7ced5b9', 'article_id': '4'}, {'_id': '6943f7eeb0926f2de7ced5e8', 'article_id': '51'}, {'_id': '6943f7eeb0926f2de7ced5ef', 'article_id': '58'}, {'_id': '6943f7eeb0926f2de7ced60c', 'article_id': '87'}, {'_id': '6943f7eeb0926f2de7ced619', 'article_id': '100'}]}

exec(code, env_args)
