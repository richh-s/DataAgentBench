code = """import json

# Load civic documents from the file
civic_docs_path = "/tmp/tmp7q6r1zwh.json"
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Load funding data from the file
funding_data_path = "/tmp/tmptf8vwxq6.json"
with open(funding_data_path, 'r') as f:
    funding_data = json.load(f)

print("Data loaded successfully")
print(f"Civic documents: {len(civic_docs)}")
print(f"Funding records: {len(funding_data)}")

# Look for projects that mention "2022" in the civic docs text
projects_2022 = []
for doc in civic_docs:
    text = doc.get('text', '')
    if '2022' in text and ('Morning View' in text or 'morning view' in text):
        # Find the specific project line
        lines = text.split('\n')
        for line in lines:
            if '2022' in line and 'Morning View' in line:
                projects_2022.append(line.strip())
                print(f"Found project line: {line.strip()}")

# Check for this project in funding data
target_project = "2022 Morning View Resurfacing & Storm Drain Improvements"
matching_funding = [f for f in funding_data if f['Project_Name'] == target_project]

print(f"\nFound {len(matching_funding)} matching funding records")
if matching_funding:
    print(f"Funding amount: ${matching_funding[0]['Amount']}")

print(f"\nProjects starting in 2022: {len(projects_2022)}")
print(f"Total funding for these projects: ${sum(int(f['Amount']) for f in matching_funding)}")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:4': [], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.list_db:8': ['Funding'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)
