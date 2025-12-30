code = """import pandas as pd
import json
import re

# Load funding data
with open(locals()['var_function-call-7304760596705444282'], 'r') as f:
    funding_data = json.load(f)
df_funding = pd.DataFrame(funding_data)

# Load civic documents
with open(locals()['var_function-call-5970116011037241460'], 'r') as f:
    civic_docs = json.load(f)

# Extract project information from civic documents
design_capital_projects = []

# Pattern to find the 'Capital Improvement Projects (Design)' section
section_pattern = r"Capital Improvement Projects \(Design\)(.*?)(?:Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects|RECOMMENDED ACTION|Agenda Item # \d+\.B\.|\s*Page \d+ of \d+)"

# Pattern to extract project names within the design section
# Project names are typically followed by a bullet point (cid:190) and then 'Updates:' or 'Project Schedule:'
# Use a non-greedy match for the project name itself `+?`
project_name_pattern = re.compile(r'\n([A-Za-z0-9][A-Za-z0-9\s&,-_./()\\]+?)(?:\n\(cid:190\) Updates:|\n\(cid:190\) Project Schedule:|\n\(cid:190\) Estimated Schedule:)')

for doc in civic_docs:
    text = doc['text']
    
    section_match = re.search(section_pattern, text, re.DOTALL)
    
    if section_match:
        capital_design_section = section_match.group(1)
        
        # Find all project names in the extracted section
        found_project_names = project_name_pattern.findall(capital_design_section)
        
        for name in found_project_names:
            name = name.strip()
            if name:
                design_capital_projects.append({'Project_Name': name, 'status': 'design', 'type': 'capital'})

df_civic = pd.DataFrame(design_capital_projects)

# Ensure Amount is numeric for comparison
df_funding['Amount'] = pd.to_numeric(df_funding['Amount'])

# Merge dataframes
merged_df = pd.merge(df_funding, df_civic, on='Project_Name', how='inner')

# Count the number of projects
count = len(merged_df)

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_function-call-7304760596705444282': 'file_storage/function-call-7304760596705444282.json', 'var_function-call-5970116011037241460': 'file_storage/function-call-5970116011037241460.json'}

exec(code, env_args)
