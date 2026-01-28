code = """# Check for patents that cite UC publications
# We'll search for citation patterns that include the publication numbers
result_file = locals()['var_functions.query_db:6']
with open(result_file, 'r') as f:
    sample_records = json.load(f)

# Look at a sample record to understand the citation structure better
sample_record = sample_records[0]
print("Sample record structure:")
print("Patents_info:", sample_record['Patents_info'])
print("Citation (first 200 chars):", str(sample_record['citation'])[:200])

# Check if we can extract assignee from Patents_info
import re

# Try to extract assignee from Patents_info
patents_info = sample_record['Patents_info']
assignee_match = re.match(r'^([^,]+) holds?', patents_info)
if assignee_match:
    assignee = assignee_match.group(1)
    print(f"Extracted assignee: {assignee}")"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'total_uc_patents': 8, 'sample_pub_numbers': ['US-202117472182-A', 'TW-107142982-A', 'US-11421276-B2', 'AU-2019275518-B2', 'JP-S6163700-A'], 'patents_with_citations': 5}}

exec(code, env_args)
