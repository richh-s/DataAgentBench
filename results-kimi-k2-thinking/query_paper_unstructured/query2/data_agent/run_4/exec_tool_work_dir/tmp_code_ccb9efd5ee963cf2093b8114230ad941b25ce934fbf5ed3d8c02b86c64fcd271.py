code = """import json

# Get the result from previous execution
result = var_functions.execute_python:12

# Handle if it's a file path
if isinstance(result, str) and '.json' in result:
    with open(result) as f:
        result = json.load(f)

average = result.get('average_citation_count')
count = result.get('acm_papers_count')

if average is not None:
    answer = f"The average citation count for ACM papers cited in 2018 is {average:.1f} citations per paper (based on {count} ACM papers)."
else:
    answer = "No ACM papers were found in the 2018 citations data."

print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': {'average_citation_count': 68.5, 'acm_papers_count': 2}}

exec(code, env_args)
