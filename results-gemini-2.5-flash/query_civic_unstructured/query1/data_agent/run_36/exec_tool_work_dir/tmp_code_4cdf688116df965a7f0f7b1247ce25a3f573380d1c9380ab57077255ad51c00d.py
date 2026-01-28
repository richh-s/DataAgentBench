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

for doc in civic_docs:
    text = doc['text']
    
    # Find the section 'Capital Improvement Projects (Design)'
    capital_design_section_match = re.search(r'Capital Improvement Projects \\(Design\\)(.*?)(?:Capital Improvement Projects \\(Construction\\)|Capital Improvement Projects \\(Not Started\\)|Disaster Recovery Projects|RECOMMENDED ACTION|Agenda Item # \\d+\\.B\\.|Page \\d+ of \\d+)', text, re.DOTALL)
    
    if capital_design_section_match:
        capital_design_section = capital_design_section_match.group(1)
        # Find project names within this section.
        # Project names are typically followed by an update or schedule bullet point.
        project_names = []
        lines = capital_design_section.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            if line and not line.startswith('(cid:190)') and not line.lower().startswith('page') and not line.lower().startswith('agenda item'):
                # Check if the next line starts with a common bullet point for updates/schedule
                if i + 1 < len(lines) and (lines[i+1].strip().startswith('(cid:190) Updates:') or lines[i+1].strip().startswith('(cid:190) Project Schedule:') or lines[i+1].strip().startswith('(cid:190) Estimated Schedule:')):
                    project_names.append(line)

        for name in project_names:
            design_capital_projects.append({'Project_Name': name, 'status': 'design', 'type': 'capital'})

df_civic = pd.DataFrame(design_capital_projects)

# Ensure Amount is numeric for comparison
df_funding['Amount'] = pd.to_numeric(df_funding['Amount'])

# Merge dataframes
merged_df = pd.merge(df_funding, df_civic, on='Project_Name', how='inner')

# Filter for projects with funding greater than $50,000 (already done in SQL, but good to ensure)
# merged_df = merged_df[merged_df['Amount'] > 50000] # This filter was already applied in SQL query

# Count the number of projects
count = len(merged_df)

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_function-call-7304760596705444282': 'file_storage/function-call-7304760596705444282.json', 'var_function-call-5970116011037241460': 'file_storage/function-call-5970116011037241460.json'}

exec(code, env_args)
