code = """import json
import os

# Load the MongoDB results (physical activity and 2016)
result_key = 'var_functions.query_db:6'
mongo_results = locals().get(result_key, [])

# If it's a file path (string), read the file
if isinstance(mongo_results, str) and os.path.exists(mongo_results):
    with open(mongo_results, 'r') as f:
        mongo_results = json.load(f)

print(f"Number of documents: {len(mongo_results)}")
print("First document keys:", list(mongo_results[0].keys()) if mongo_results else "No results")
print("Sample filename:", mongo_results[0]['filename'] if mongo_results else "No results")

__RESULT__:
print(json.dumps({"count": len(mongo_results), "sample": mongo_results[0]['filename'] if mongo_results else None}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
