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
for doc in civic_docs_data:
    text = doc['text']
    # Find the section for 'Capital Improvement Projects (Design)'
    match = re.search(r'Capital Improvement Projects \(Design\)(.*?)(?:Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects|Public Works Quarterly Update flier|$)', text, re.DOTALL)
    if match:
        design_section = match.group(1)
        # Extract project names from this section
        # Project names are usually at the beginning of a line, followed by some details
        projects_in_design = re.findall(r'\n([A-Za-z0-9][A-Za-z0-9\s\-&,/\\()_\.]+?)\n', design_section)
        for project in projects_in_design:
            # Clean up the project name (remove leading/trailing spaces, newlines, etc.)
            clean_project = project.strip()
            if clean_project and not clean_project.startswith('(cid:'): # Filter out non-project lines
                capital_design_projects.add(clean_project)

# Filter funding data for projects that are 'capital' type and 'design' status
df_filtered_projects = df_funding[df_funding['Project_Name'].isin(capital_design_projects)]

# Count the unique projects
result_count = len(df_filtered_projects['Project_Name'].unique())

print('__RESULT__:')
print(json.dumps(result_count))"""

env_args = {'var_function-call-16198285528554906673': 'file_storage/function-call-16198285528554906673.json', 'var_function-call-10725550315301873473': 'file_storage/function-call-10725550315301873473.json'}

exec(code, env_args)
