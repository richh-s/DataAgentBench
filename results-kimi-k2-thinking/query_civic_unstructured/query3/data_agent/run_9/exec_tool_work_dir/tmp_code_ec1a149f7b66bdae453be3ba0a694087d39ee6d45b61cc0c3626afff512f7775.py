code = """import json
import re

# Load civic documents data
civic_docs_path = var_functions.query_db_5
civic_docs_file = open(civic_docs_path)
civic_docs_data = json.load(civic_docs_file)
civic_docs_file.close()

# Load funding data
funding_path = var_functions.query_db_6
funding_file = open(funding_path)
funding_data = json.load(funding_file)
funding_file.close()

print("Civic documents loaded:", len(civic_docs_data))
print("Funding records loaded:", len(funding_data))

# Check for FEMA/emergency related funding
fema_related = []
for f in funding_data:
    name = f['Project_Name'].upper()
    if any(keyword in name for keyword in ['FEMA', 'EMERGENCY']):
        fema_related.append(f)

print("FEMA/emergency funding records:", len(fema_related))
for rec in fema_related[:10]:
    print("-", rec['Project_Name'], "($" + str(rec['Amount']) + ")")

__RESULT__:
print(json.dumps({
    "message": "Data loaded successfully",
    "civic_docs_count": len(civic_docs_data),
    "funding_count": len(funding_data),
    "fema_funding_count": len(fema_related)
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
