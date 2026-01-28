code = """import json

# Load funding data
funding_path = '/tmp/tmpquery_db_48.json'
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Filter for disaster-related projects (containing FEMA, CalOES, CalJPIA)
disaster_projects = []
for item in funding_data:
    project_name = item.get('Project_Name', '')
    amount = int(item.get('Amount', 0))
    
    # Check if it's disaster-related
    if any(indicator in project_name for indicator in ['FEMA', 'CalOES', 'CalJPIA']):
        disaster_projects.append({
            'name': project_name,
            'amount': amount
        })

print(f"Found {len(disaster_projects)} disaster-related projects in funding data")

# Sum the funding
total_disaster_funding = sum(p['amount'] for p in disaster_projects)

print(f"Total disaster funding: ${total_disaster_funding:,}")
print("\nTop 10 disaster projects:")
for p in sorted(disaster_projects, key=lambda x: x['amount'], reverse=True)[:10]:
    print(f"- {p['name']}: ${p['amount']:,}")

result = {
    'total_disaster_funding': total_disaster_funding,
    'project_count': len(disaster_projects)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:13': 'file_storage/functions.query_db:13.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:23': 'file_storage/functions.query_db:23.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:21': 'file_storage/functions.query_db:21.json', 'var_functions.query_db:26': [{'Project_Name': '2021 Annual Street Maintenance', 'Amount': '24000'}, {'Project_Name': '2022 Annual Street Maintenance', 'Amount': '45000'}, {'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Amount': '38000'}, {'Project_Name': 'Annual Street Maintenance', 'Amount': '23000'}, {'Project_Name': 'Birdview Avenue Improvements', 'Amount': '79000'}], 'var_functions.query_db:27': 'file_storage/functions.query_db:27.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:33': 'file_storage/functions.query_db:33.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:37': 'file_storage/functions.query_db:37.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:43': 'file_storage/functions.query_db:43.json', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json'}

exec(code, env_args)
