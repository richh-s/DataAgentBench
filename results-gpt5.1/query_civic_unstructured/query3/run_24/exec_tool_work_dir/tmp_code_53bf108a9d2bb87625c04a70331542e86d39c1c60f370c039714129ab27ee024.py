code = """import json, re
from pathlib import Path

# Load full funding data
path_funding = Path(var_call_MleU84a3eahj0xfTVXHFERNK)
funding = json.loads(path_funding.read_text())

# Build set of project names that look emergency/FEMA related based on name keywords
kw_pattern = re.compile(r"emergency|fema", re.I)

emerg_projects = []
for row in funding:
    name = row.get('Project_Name','')
    if kw_pattern.search(name):
        emerg_projects.append(row)

result = emerg_projects

result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_MleU84a3eahj0xfTVXHFERNK': 'file_storage/call_MleU84a3eahj0xfTVXHFERNK.json', 'var_call_ngLfcK8tXbZ2lXJcp7voIyiX': 'file_storage/call_ngLfcK8tXbZ2lXJcp7voIyiX.json'}

exec(code, env_args)
