code = """import json

# Read the sample data from the query result
with open('var_functions.query_db:2.json', 'r') as f:
    sample_data = json.load(f)

print("Sample data structure:")
for i, record in enumerate(sample_data[:3]):
    print("\n--- Record " + str(i+1) + " ---")
    print("Patents_info: " + str(record['Patents_info']))
    print("citation sample (first 200 chars): " + str(record['citation'])[:200] + "...")
    print("cpc sample (first 200 chars): " + str(record['cpc'])[:200] + "...")

# Count total records and find UNIV CALIFORNIA records
with open('var_functions.query_db:2.json', 'r') as f:
    data = json.load(f)
    
total_records = len(data)
uc_records = []

for record in data:
    if 'UNIV CALIFORNIA' in record['Patents_info']:
        uc_records.append(record)

print("\n\nTotal records: " + str(total_records))
print("Records with UNIV CALIFORNIA: " + str(len(uc_records)))

if uc_records:
    print("\nExample UNIV CALIFORNIA record (first 1000 chars):")
    print(json.dumps(uc_records[0], indent=2)[:1000])
else:
    print("\nNo UNIV CALIFORNIA records found in the sample. Let's query the full database.")"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition']}

exec(code, env_args)
