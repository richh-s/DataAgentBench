code = """import json
import re

file_path = locals()['var_function-call-4838891230296315133']
with open(file_path, 'r') as f:
    papers = json.load(f)

print("__RESULT__:")
info = {
    "count": len(papers),
    "first_paper_preview": papers[0]['text'][:500] if papers else "No papers",
    "first_filename": papers[0]['filename'] if papers else "No papers"
}
print(json.dumps(info))"""

env_args = {'var_function-call-12813325699209905495': 'file_storage/function-call-12813325699209905495.json', 'var_function-call-4838891230296315133': 'file_storage/function-call-4838891230296315133.json', 'var_function-call-7940884221126680243': []}

exec(code, env_args)
