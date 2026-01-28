code = """import json
import pandas as pd

# Load the civic documents data
civic_docs_path = '/tmp/tmp3b3v7e_m.json'

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

print(f"Number of documents: {len(civic_docs)}")
print(f"Sample document structure:")
print(f"Keys: {civic_docs[0].keys()}")
print(f"Sample text preview: {civic_docs[0]['text'][:500]}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}]}

exec(code, env_args)
