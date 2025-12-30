code = """import re, json, pandas as pd

funding_records = var_call_TrTbkuE4mQWE5DgrbFTkIZUF
civic_docs = var_call_LxmJvzaILhIL32F5HGpYfuiz

funding_df = pd.DataFrame(funding_records)
funding_df['Amount'] = funding_df['Amount'].astype(int)

text = ' '.join(doc['text'] for doc in civic_docs)

sections = re.split(r'Capital Improvement Projects \((Design|Construction|Not Started)\)', text)

projects = []
for i in range(1, len(sections), 2):
    status = sections[i].lower()
    body = sections[i+1]
    proj_names = re.findall(r'\n\n([A-Z][A-Za-z0-9&.,’'"()\- ]+?)\n\n', body)
    for name in proj_names:
        name_clean = ' '.join(name.split())
        projects.append({'Project_Name': name_clean, 'status': status})

projects_df = pd.DataFrame(projects).drop_duplicates()
projects_df['type'] = 'capital'

merged = pd.merge(funding_df, projects_df, on='Project_Name', how='inner')

result_count = int(((merged['status'] == 'design') & (merged['type'] == 'capital') & (merged['Amount'] > 50000)).sum())

out = json.dumps({'count': result_count})
print("__RESULT__:")
print(out)"""

env_args = {'var_call_TrTbkuE4mQWE5DgrbFTkIZUF': 'file_storage/call_TrTbkuE4mQWE5DgrbFTkIZUF.json', 'var_call_LxmJvzaILhIL32F5HGpYfuiz': 'file_storage/call_LxmJvzaILhIL32F5HGpYfuiz.json'}

exec(code, env_args)
