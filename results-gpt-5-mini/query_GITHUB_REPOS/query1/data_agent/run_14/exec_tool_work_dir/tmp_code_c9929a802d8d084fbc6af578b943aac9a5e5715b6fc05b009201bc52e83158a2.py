code = """import json
# Read previous result
res = var_call_ppAFr5iaZIF0zcgk2bMRqpSa

# Prepare final answer string
if res['proportion'] is None:
    answer = 'No README.md files found for non-Python repositories.'
else:
    pct = res['proportion'] * 100
    answer = f"Among repositories that do not use Python, {res['numerator']}/{res['denominator']} ({pct:.2f}%) of their README.md files include copyright information."

print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_zyMq5UoU7qXiQM6xakep8ECH': 'file_storage/call_zyMq5UoU7qXiQM6xakep8ECH.json', 'var_call_26h4cDEbWcoiCRhpmNWOpHl4': 'file_storage/call_26h4cDEbWcoiCRhpmNWOpHl4.json', 'var_call_ppAFr5iaZIF0zcgk2bMRqpSa': {'numerator': 21, 'denominator': 138, 'proportion': 0.15217391304347827, 'examples_of_matches': [{'sample_repo_name': 'selenith/plasmide', 'sample_path': 'tools/ckeditor/README.md'}, {'sample_repo_name': 'durka/named-block', 'sample_path': 'README.md'}, {'sample_repo_name': 'blond/hash-set', 'sample_path': 'README.md'}, {'sample_repo_name': 'mluisbrown/Memories', 'sample_path': 'README.md'}, {'sample_repo_name': 'marcelklehr/gulf-contenteditable', 'sample_path': 'README.md'}]}}

exec(code, env_args)
