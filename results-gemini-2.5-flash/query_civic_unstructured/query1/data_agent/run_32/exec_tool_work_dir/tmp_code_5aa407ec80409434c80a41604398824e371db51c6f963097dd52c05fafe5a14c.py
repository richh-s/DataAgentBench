code = """import pandas as pd
import json
import re

# Load funding data
with open(locals()['var_function-call-3167471947638154986'], 'r') as f:
    funding_data = json.load(f)
df_funding = pd.DataFrame(funding_data)
df_funding['Amount'] = pd.to_numeric(df_funding['Amount'])

# Load civic documents
with open(locals()['var_function-call-17661845437254810482'], 'r') as f:
    civic_docs_data = json.load(f)

projects_info = []
for doc in civic_docs_data:
    text = doc['text']
    # Regex to find "Capital Improvement Projects (Design)" section
    capital_design_section = re.search(r"Capital Improvement Projects \(Design\)(.*?)(?:Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects|RECOMMENDED ACTION:)", text, re.DOTALL)
    if capital_design_section:
        section_text = capital_design_section.group(1)
        # Extract project names
        project_names = re.findall(r"\n\n(.*?)\n\n", section_text)
        for name in project_names:
            if name.strip() and "(cid:" not in name: # Filter out empty strings and non-project names
                projects_info.append({"Project_Name": name.strip(), "type": "capital", "status": "design"})

df_civic = pd.DataFrame(projects_info)

# Merge dataframes
merged_df = pd.merge(df_funding, df_civic, on='Project_Name', how='inner')

# Count unique projects
result_count = merged_df['Project_Name'].nunique()

print('__RESULT__:')
print(json.dumps(result_count))"""

env_args = {'var_function-call-3167471947638154986': 'file_storage/function-call-3167471947638154986.json', 'var_function-call-17661845437254810482': 'file_storage/function-call-17661845437254810482.json'}

exec(code, env_args)
