code = """# Load the full dataset from both databases
import json
import pandas as pd
import re

# Read the funding data from the file
with open('var_functions.query_db:6', 'r') as f:
    funding_data = json.load(f)

# Convert to DataFrame for easier processing
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Read the civic documents from the file
with open('var_functions.query_db:10', 'r') as f:
    civic_docs = json.load(f)

print('__RESULT__:')
print(json.dumps({
    "funding_records": len(funding_df),
    "civic_docs_count": len(civic_docs),
    "sample_funding": funding_df.head().to_dict('records'),
    "sample_civic_doc_preview": civic_docs[0]['text'][:500] if civic_docs else "No docs"
}))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.list_db:12': ['civic_docs']}

exec(code, env_args)
