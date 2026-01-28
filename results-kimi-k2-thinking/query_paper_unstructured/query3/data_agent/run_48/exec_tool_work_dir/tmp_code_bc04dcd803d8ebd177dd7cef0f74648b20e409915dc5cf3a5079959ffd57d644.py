code = """import json, os, re

# Debug: Check what variables are available
print("Available variables:")
for name in sorted(dir()):
    if name.startswith('var_'):
        value = locals()[name]
        print(f"  {name}: {type(value)}")
        if isinstance(value, str) and os.path.exists(value):
            print(f"    -> File exists: {value}")

# Try to find and load the files
paper_docs_path = None
citations_path = None

for name in dir():
    if name.startswith('var_'):
        value = locals()[name]
        if isinstance(value, str) and value.endswith('.json'):
            if 'query_db:24' in name:
                paper_docs_path = value
            elif 'query_db:28' in name:
                citations_path = value

print(f"\nPaper docs path: {paper_docs_path}")
print(f"Citations path: {citations_path}")

# Check if files exist
if paper_docs_path and os.path.exists(paper_docs_path):
    print(f"Paper docs file size: {os.path.getsize(paper_docs_path)} bytes")
if citations_path and os.path.exists(citations_path):
    print(f"Citations file size: {os.path.getsize(citations_path)} bytes")"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:7': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
