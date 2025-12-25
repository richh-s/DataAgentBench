code = """import json, pandas as pd
from pathlib import Path

contents = json.loads(Path(var_call_06v0B3d8GHEMTTGnyrcgxsHG).read_text())
languages = json.loads(Path(var_call_pOC75Yb2eeLk4eBe0zuFIi4g).read_text())

contents_df = pd.DataFrame(contents)
languages_df = pd.DataFrame(languages)

python_repos = set(languages_df[languages_df['language_description'].str.contains('Python (', case=False, na=False)]['repo_name'])

readme_df = contents_df[contents_df['sample_path'] == 'README.md']
non_python_readme_df = readme_df[~readme_df['sample_repo_name'].isin(python_repos)]

# Use casefolded substring search instead of regex to avoid pattern issues
contents_lower = non_python_readme_df['content'].fillna('').str.casefold()

has_copyright = contents_lower.str.contains('copyright') | contents_lower.str.contains('©')

num_non_python_readmes = int(non_python_readme_df.shape[0])
num_with_copyright = int(copyright.sum()) if (copyright := has_copyright) is not None else 0

proportion = float(num_with_copyright) / num_non_python_readmes if num_non_python_readmes > 0 else None

result = {
    'num_non_python_readmes': num_non_python_readmes,
    'num_with_copyright': num_with_copyright,
    'proportion': proportion
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_06v0B3d8GHEMTTGnyrcgxsHG': 'file_storage/call_06v0B3d8GHEMTTGnyrcgxsHG.json', 'var_call_pOC75Yb2eeLk4eBe0zuFIi4g': 'file_storage/call_pOC75Yb2eeLk4eBe0zuFIi4g.json'}

exec(code, env_args)
