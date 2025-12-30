code = """import pandas as pd
import json
import re

# Load the funding data
with open(locals()['var_function-call-17014294750015647345'], 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = funding_df['Amount'].astype(int)

# Load the civic docs data
with open(locals()['var_function-call-7117339431964219411'], 'r') as f:
    civic_docs_data = json.load(f)

# Extract project information from civic documents
projects = []
for doc in civic_docs_data:
    text = doc['text']
    
    # Regex to find Capital Improvement Projects (Design)
    design_capital_projects_match = re.search(r'Capital Improvement Projects \(Design\)(.*?)(?:Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects|RECOMMENDED ACTION:|$)', text, re.DOTALL)
    if design_capital_projects_match:
        design_capital_section = design_capital_projects_match.group(1)
        project_names = re.findall(r'\n([A-Za-z0-9][A-Za-z0-9\s&,-]+?)(?:\n|\(cid:190))', design_capital_section)
        for name in project_names:
            name = name.strip()
            if name and "Updates:" not in name and "Project Schedule:" not in name and "Project Description:" not in name:
                projects.append({'Project_Name': name, 'type': 'capital', 'status': 'design'})

    # Regex to find Capital Improvement Projects (Construction) (if they are also mentioned as design)
    # Some projects are listed under design AND construction, so we need to be careful with the status.
    # We are specifically looking for 'design' status. The above regex should capture it correctly.
    # The prompt explicitly states to extract 'status' and says 'Projects have three statuses: "design", "completed", and "not started"'.
    # Given the structure of the civic_docs, a project can appear under a "Capital Improvement Projects (Design)" heading.
    # Let's refine the extraction to specifically target projects listed under "Capital Improvement Projects (Design)".

# Create a DataFrame for projects from civic documents
civic_projects_df = pd.DataFrame(projects)

# Merge the two dataframes
merged_df = pd.merge(funding_df, civic_projects_df, on='Project_Name', how='inner')

# Filter for capital projects with 'design' status and funding > $50,000 (already filtered in SQL)
# The SQL query already filtered for Amount > 50000.
final_projects = merged_df[(merged_df['type'] == 'capital') & (merged_df['status'] == 'design')]

# Count unique projects
count = final_projects['Project_Name'].nunique()

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_function-call-17014294750015647345': 'file_storage/function-call-17014294750015647345.json', 'var_function-call-7117339431964219411': 'file_storage/function-call-7117339431964219411.json'}

exec(code, env_args)
