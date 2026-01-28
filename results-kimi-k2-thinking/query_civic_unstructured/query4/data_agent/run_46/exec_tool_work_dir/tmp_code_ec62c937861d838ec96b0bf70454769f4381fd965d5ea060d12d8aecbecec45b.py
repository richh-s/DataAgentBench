code = """import json

# Load civic documents data
civic_docs_path = var_functions.query_db:2
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Load funding data  
funding_path = var_functions.query_db:5
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

print(f"Civic documents: {len(civic_docs)}")
print(f"Funding records: {len(funding_data)}")

# Look at first civic doc structure
first_doc = civic_docs[0]
print(f"First doc keys: {list(first_doc.keys())}")
print(f"First doc filename: {first_doc.get('filename')}")
print(f"First doc text preview: {first_doc.get('text', '')[:500]}")

__RESULT__:
json.dumps({"status": "data_loaded", "doc_count": len(civic_docs), "funding_count": len(funding_data)})"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}]}

exec(code, env_args)
