code = """import pandas as pd
import json

non_python_repos_file = open(locals()['var_function-call-897611341623711684'], 'r')
non_python_repos_data = json.load(non_python_repos_file)
non_python_repos_file.close()

non_python_repo_names = {repo['repo_name'] for repo in non_python_repos_data}

readme_contents_file = open(locals()['var_function-call-10777280853896446917'], 'r')
readme_contents_data = json.load(readme_contents_file)
readme_contents_file.close()

total_non_python_readmes = 0
readmes_with_copyright = 0

for readme in readme_contents_data:
    repo_name = readme['sample_repo_name']
    if repo_name in non_python_repo_names:
        total_non_python_readmes += 1
        content = readme['content']
        if "copyright" in content.lower():
            readmes_with_copyright += 1

proportion = readmes_with_copyright / total_non_python_readmes if total_non_python_readmes > 0 else 0

print("__RESULT__:")
print(json.dumps(proportion))"""

env_args = {'var_function-call-897611341623711684': 'file_storage/function-call-897611341623711684.json', 'var_function-call-16913143173313718971': 'file_storage/function-call-16913143173313718971.json', 'var_function-call-10777280853896446917': 'file_storage/function-call-10777280853896446917.json'}

exec(code, env_args)
