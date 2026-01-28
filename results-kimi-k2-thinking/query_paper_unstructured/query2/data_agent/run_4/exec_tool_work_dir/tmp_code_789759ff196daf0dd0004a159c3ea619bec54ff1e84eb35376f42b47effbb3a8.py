code = """import json

# Previous result is stored, access it
prev_result_key = 'var_functions.execute_python:12'
prev_result = locals().get(prev_result_key)

# If it's a file path, read it
if isinstance(prev_result, str):
    with open(prev_result) as f:
        result_data = json.load(f)
else:
    result_data = prev_result

avg = result_data.get('average_citation_count')
count = result_data.get('acm_papers_count')

if avg is not None:
    final = "The average citation count for ACM papers cited in 2018 is %.1f citations per paper (based on %d ACM papers)." % (avg, count)
else:
    final = "No ACM papers were found in the 2018 citations data."

print('__RESULT__:')
print(json.dumps(final))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': {'average_citation_count': 68.5, 'acm_papers_count': 2}}

exec(code, env_args)
