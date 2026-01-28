code = """import json, glob, os

# Find the correct file paths using glob
mongo_files = glob.glob('/tmp/results/*mongodb*civic_docs*.json')
funding_files = glob.glob('/tmp/results/*sqlite*funding*.json')

print('Mongo files:', mongo_files)
print('Funding files:', funding_files)

# Load the data from the correct files
if mongo_files and funding_files:
    mongo_path = mongo_files[0]  # Take the first one
    funding_path = funding_files[0]
    
    with open(mongo_path, 'r') as f:
        civic_docs = json.load(f)
    
    with open(funding_path, 'r') as f:
        funding_data = json.load(f)
    
    print(f'Loaded {len(civic_docs)} civic docs')
    print(f'Loaded {len(funding_data)} funding records')
    
    # Manually identified Spring 2022 projects
    spring_projects = [
        'Marie Canyon Green Streets',
        'PCH Median Improvements Project',
        'PCH Signal Synchronization System Improvements Project',
        'Westward Beach Road Improvements Project',
        'Civic Center Water Treatment Facility Phase 2',
        'Bluffs Park Shade Structure',
        'Permanent Skate Park',
        'PCH at Trancas Canyon Road Right Turn Lane',
        'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)',
        'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)'
    ]
    
    # Calculate funding
    total_funding = 0
    funded_projects = []
    
    for proj in spring_projects:
        for fund in funding_data:
            if fund.get('Project_Name') == proj:
                amount = int(fund.get('Amount', 0))
                total_funding += amount
                funded_projects.append((proj, amount))
                break
    
    result = {
        'project_count': len(spring_projects),
        'total_funding': total_funding,
        'projects': spring_projects,
        'funded_projects': funded_projects
    }
    
    print('__RESULT__:')
    print(json.dumps(result))
else:
    print('Files not found')"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.list_db:30': ['civic_docs'], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json', 'var_functions.execute_python:62': {'status': 'files_loaded'}, 'var_functions.query_db:68': 'file_storage/functions.query_db:68.json'}

exec(code, env_args)
