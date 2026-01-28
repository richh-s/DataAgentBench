code = """import json
from pathlib import Path
# read metadata repo list from file path variable
p = Path(var_call_Ar4UdGo0OWCFZGX2WDFXrvLF)
metadata_repos = set(json.loads(p.read_text()))
commits = var_call_yI1o65A51V1KSXrKAavnC585
# commits is a list of dicts with 'repo_name' and 'cnt'
total = 0
for r in commits:
    if r.get('repo_name') in metadata_repos:
        try:
            total += int(r.get('cnt', 0))
        except:
            try:
                total += int(float(r.get('cnt', 0)))
            except:
                pass

import json
print("__RESULT__:")
print(json.dumps(total))"""

env_args = {'var_call_1sX8tQU6i238bWeSZ48JyTi2': 'file_storage/call_1sX8tQU6i238bWeSZ48JyTi2.json', 'var_call_Ar4UdGo0OWCFZGX2WDFXrvLF': 'file_storage/call_Ar4UdGo0OWCFZGX2WDFXrvLF.json', 'var_call_yI1o65A51V1KSXrKAavnC585': [{'repo_name': 'facebook/react', 'cnt': '104'}, {'repo_name': 'tensorflow/tensorflow', 'cnt': '114'}, {'repo_name': 'Microsoft/vscode', 'cnt': '171'}, {'repo_name': 'apple/swift', 'cnt': '963'}, {'repo_name': 'twbs/bootstrap', 'cnt': '251'}, {'repo_name': 'torvalds/linux', 'cnt': '13413'}]}

exec(code, env_args)
