code = """# Let's see what's in the variable
import json

# Try to access the variable directly if it's small, or read from file if it's a path
result = locals().get('var_functions.query_db:2', None)
if isinstance(result, str) and result.endswith('.json'):
    # It's a file path
    with open(result, 'r') as f:
        metadata_result = json.load(f)
else:
    # It's a list
    metadata_result = result if result else []

# Extract article IDs for Amy Jones
if metadata_result:
    article_ids = [item['article_id'] for item in metadata_result]
    print('__RESULT__:')
    print(json.dumps({'article_ids': article_ids[:10], 'total_count': len(article_ids), 'message': 'Successfully extracted'}))
else:
    print('__RESULT__:')
    print(json.dumps({'error': 'No data found'}))"""

env_args = {'var_functions.query_db:0': [{'author_id': '218', 'name': 'Amy Jones'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
