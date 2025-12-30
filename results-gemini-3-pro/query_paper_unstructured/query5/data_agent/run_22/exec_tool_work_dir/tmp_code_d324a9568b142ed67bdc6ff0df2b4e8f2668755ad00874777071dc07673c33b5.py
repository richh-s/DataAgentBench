code = """import json
import re

papers_path = locals()['var_function-call-3655541512535358306']
with open(papers_path, 'r') as f:
    papers_data = json.load(f)

matches = []
for p in papers_data:
    text = p.get('text', '')
    # Check if CHI is present anywhere in first 500 chars
    if "CHI" in text[:500]:
        matches.append(text[:200].replace('\n', ' '))
    if len(matches) >= 10:
        break

print("__RESULT__:")
print(json.dumps(matches))"""

env_args = {'var_function-call-10316639782376097408': ['Citations', 'sqlite_sequence'], 'var_function-call-10316639782376098289': ['paper_docs'], 'var_function-call-10316639782376099170': 'file_storage/function-call-10316639782376099170.json', 'var_function-call-10316639782376095955': 'file_storage/function-call-10316639782376095955.json', 'var_function-call-3655541512535358306': 'file_storage/function-call-3655541512535358306.json', 'var_function-call-17554690775413640325': {'total_citations': 0, 'chi_paper_count': 0, 'papers_with_citations': 0, 'sample_titles': []}}

exec(code, env_args)
