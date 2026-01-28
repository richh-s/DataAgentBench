code = """import re, json, pandas as pd

funding_records = var_call_Qvrc7xXLmlNZfOZO0Lxbndwq
funding_df = pd.DataFrame(funding_records)
funding_df['Amount'] = funding_df['Amount'].astype(int)

civic_preview = var_call_EBlsovewq6zj4dkVKJvmdwpo
texts = [doc['text'] for doc in civic_preview]
full_text = '\n'.join(texts)

projects_info = {}
lines = full_text.splitlines()
current_section = None
status_context = None

for i, line in enumerate(lines):
    stripped = line.strip()
    if not stripped:
        continue
    if stripped.startswith('Capital Improvement Projects'):
        current_section = stripped
        if 'Design' in stripped:
            status_context = 'design'
        elif 'Not Started' in stripped:
            status_context = 'not started'
        elif 'Construction' in stripped:
            status_context = 'completed'
        continue
    if any(stripped.startswith(prefix) for prefix in ['Updates', 'Project Schedule', 'Estimated Schedule', 'Project Description', 'Agenda Item', 'RECOMMENDED ACTION', 'DISCUSSION', 'Subject:', 'To:', 'Prepared by:', 'Approved by:', 'Date prepared', 'Meeting date', 'Page '] ):
        continue
    if status_context and not stripped.endswith(':') and len(stripped.split()) <= 10:
        if len(stripped.split()) >= 2 and re.search(r'[A-Z]', stripped):
            name = stripped
            if name not in projects_info:
                projects_info[name] = {'status': status_context, 'type': 'capital'}

projects_df = pd.DataFrame([
    {'Project_Name': name, 'status': info['status'], 'type': info['type']} for name, info in projects_info.items()
])

merged = pd.merge(funding_df, projects_df, on='Project_Name', how='inner')
filtered = merged[(merged['type'] == 'capital') & (merged['status'] == 'design')]
count_design_capital = int(filtered.shape[0])

result = json.dumps({'count_design_capital_over_50000': count_design_capital})

print('__RESULT__:')
print(result)"""

env_args = {'var_call_Qvrc7xXLmlNZfOZO0Lxbndwq': 'file_storage/call_Qvrc7xXLmlNZfOZO0Lxbndwq.json', 'var_call_EBlsovewq6zj4dkVKJvmdwpo': 'file_storage/call_EBlsovewq6zj4dkVKJvmdwpo.json'}

exec(code, env_args)
