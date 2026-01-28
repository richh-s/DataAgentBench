code = """import json
import pandas as pd

# Load funding data
with open('data/query_result_funding.json', 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Identify disaster projects
disaster_projects = funding_df[funding_df['Project_Name'].str.contains('FEMA|CalOES|CalJPIA', case=False, na=False)]

# Find 2022 disaster projects
projects_2022 = disaster_projects[disaster_projects['Project_Name'].str.contains('2022', case=False, na=False)]

# Load civic documents
def process_documents(funding_df):
    with open('data/query_result_694eef5c4ec675b6b5f5a285.json', 'r') as f:
        civic_docs = json.load(f)
    
    additional_funding = []
    
    for doc in civic_docs:
        text = doc['text']
        if '2022' in text:
            # Check if disaster-related
            if any(term in text.lower() for term in ['fema', 'caloes', 'caljpia']):
                # Try to find matching projects
                for _, fund_proj in funding_df.iterrows():
                    proj_name = fund_proj['Project_Name']
                    # Look for key parts of project name in text
                    key_parts = proj_name.replace('(FEMA Project)', '').replace('(CalOES Project)', '').replace('(CalJPIA Project)', '').strip()
                    if len(key_parts) > 5 and key_parts.lower() in text.lower():
                        additional_funding.append(fund_proj.to_dict())
    
    return additional_funding

additional = process_documents(disaster_projects)
if additional:
    additional_df = pd.DataFrame(additional).drop_duplicates()
    all_2022 = pd.concat([projects_2022, additional_df]).drop_duplicates()
else:
    all_2022 = projects_2022

# Calculate total funding
total_funding = all_2022['Amount'].sum()
num_projects = len(all_2022)

result = {
    'total_funding': int(total_funding),
    'num_projects': int(num_projects),
    'projects': all_2022[['Project_Name', 'Amount']].to_dict('records')
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.list_db:22': ['civic_docs']}

exec(code, env_args)
