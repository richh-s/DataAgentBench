code = """import pandas as pd
import json
import re

# Load the funding data
with open(locals()['var_function-call-16198285528554906673'], 'r') as f:
    funding_data = json.load(f)
df_funding = pd.DataFrame(funding_data)
df_funding['Amount'] = pd.to_numeric(df_funding['Amount'])

# Load the civic documents
with open(locals()['var_function-call-10725550315301873473'], 'r') as f:
    civic_docs_data = json.load(f)

# Extract projects with 'design' status and 'capital' type
capital_design_projects = set()
exclude_keywords = ['Updates:', '(cid:', 'Project Schedule:', 'Estimated Schedule:', 'To:', 'Prepared by:', 'Approved by:', 'Date prepared:', 'Meeting date:', 'Subject:', 'RECOMMENDED ACTION:', 'DISCUSSION:', 'Page ', 'Agenda Item #']

# Define the literal parts of the regex and escape them
design_start = re.escape('Capital Improvement Projects (Design)')
construction_end = re.escape('Capital Improvement Projects (Construction)')
not_started_end = re.escape('Capital Improvement Projects (Not Started)')
disaster_end = re.escape('Disaster Recovery Projects')
flier_end = re.escape('Public Works Quarterly Update flier')

# Construct the full regex pattern using f-string
regex_pattern = f'{design_start}(.*?)(?:{construction_end}|{not_started_end}|{disaster_end}|{flier_end}|$)'

for doc in civic_docs_data:
    text = doc['text']
    match = re.search(regex_pattern, text, re.DOTALL)
    if match:
        design_section = match.group(1)
        lines = design_section.split('\n')
        for line in lines:
            line = line.strip()
            if re.match(r'^[A-Z0-9].*$', line) and len(line) > 5 and not any(line.startswith(keyword) for keyword in exclude_keywords):
                capital_design_projects.add(line)

# Filter funding data for projects that are 'capital' type and 'design' status
df_filtered_projects = df_funding[df_funding['Project_Name'].isin(capital_design_projects)]

# Count the unique projects
result_count = len(df_filtered_projects['Project_Name'].unique())

print('__RESULT__:')
print(json.dumps(result_count))"""

env_args = {'var_function-call-16198285528554906673': 'file_storage/function-call-16198285528554906673.json', 'var_function-call-10725550315301873473': 'file_storage/function-call-10725550315301873473.json'}

exec(code, env_args)
