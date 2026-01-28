code = """import json
import re

# Read the civic documents data
civic_docs_path = var_functions.query_db_5
civic_docs_file = open(civic_docs_path)
civic_docs_data = json.load(civic_docs_file)
civic_docs_file.close()

# Read the funding data
funding_path = var_functions.query_db_6
funding_file = open(funding_path)
funding_data = json.load(funding_file)
funding_file.close()

print("Number of civic documents:", len(civic_docs_data))
print("Number of funding records:", len(funding_data))

print("\nSample civic document keys:", list(civic_docs_data[0].keys()))
print("Sample civic document text preview:")
text_preview = civic_docs_data[0]['text'][:500]
print(text_preview)

print("\nSample funding records:")
for i, rec in enumerate(funding_data[:3]):
    print(rec)

print("\nFirst few funding records with FEMA in name:")
fema_funding = [f for f in funding_data if 'FEMA' in f['Project_Name'].upper()]
print("Found", len(fema_funding), "records with FEMA in project name")
for rec in fema_funding[:5]:
    print(rec)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
