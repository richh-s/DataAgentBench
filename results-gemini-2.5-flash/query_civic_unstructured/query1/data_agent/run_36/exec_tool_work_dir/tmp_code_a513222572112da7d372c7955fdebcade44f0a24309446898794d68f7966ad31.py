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
    # Regex to find Capital Improvement Projects (Design)
    # This pattern specifically looks for the section "Capital Improvement Projects (Design)"
    # and then lists the projects under it until another "Capital Improvement Projects" section or similar
    # or "Disaster Recovery Projects"
    
    capital_design_section_match = re.search(r'Capital Improvement Projects \(Design\)(.*?)(?:Capital Improvement Projects \(|Disaster Recovery Projects|RECOMMENDED ACTION|Page \d+ of \d+)', text, re.DOTALL)
    if capital_design_section_match:
        capital_design_section = capital_design_section_match.group(1)
        # Find project names within this section, assuming they are on new lines
        project_names = re.findall(r'\n([A-Za-z0-9][A-Za-z0-9\s&,-_./()\\]+?)(?:\n|\(cid:190))', capital_design_section)
        for name in project_names:
            name = name.strip()
            if name and "Updates" not in name and "Project Schedule" not in name and "Discussion" not in name and "RECOMMENDED ACTION" not in name:
                design_capital_projects.append({'Project_Name': name, 'status': 'design', 'type': 'capital'})

df_civic = pd.DataFrame(design_capital_projects)

# Merge dataframes
merged_df = pd.merge(df_funding, df_civic, on='Project_Name', how='inner')

# Count the number of projects
count = len(merged_df)

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_function-call-7304760596705444282': 'file_storage/function-call-7304760596705444282.json', 'var_function-call-5970116011037241460': 'file_storage/function-call-5970116011037241460.json'}

exec(code, env_args)
