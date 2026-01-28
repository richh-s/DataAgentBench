code = """import json
import os
import re

try:
    # Load data from files
    with open('file_storage/functions.query_db:38.json', 'r') as f:
        civic_docs = json.load(f)
    
    with open('file_storage/functions.query_db:28.json', 'r') as f:
        funding_data = json.load(f)
    
    # Create funding map
    funding_map = {}
    for rec in funding_data:
        name = rec['Project_Name']
        amt = int(str(rec['Amount']))
        funding_map[name] = amt
    
    # Parse civic documents
    spring_2022_projects = []
    for doc in civic_docs:
        text = doc.get('text', '')
        lines = text.split('\n')
        
        for i, line in enumerate(lines):
            
            # Look for Spring 2022 dates
            if line and '2022' in line and 'spring' in line.lower():
                # Look for project name above this line
                for j in range(i-1, max(-1, i-5), -1):
                    prev = lines[j].strip()
                    if prev.isupper() and len(prev) > 8:
                        proj = prev
                        if proj in funding_map:
                            funding = funding_map[proj]
                            spring_2022_projects.append({
                                'name': proj,
                                'funding': funding
                            })
                        break
    
    total = sum(p['funding'] for p in spring_2022_projects)
    
    result = {
        'count': len(spring_2022_projects),
        'total_funding': total,
        'projects': spring_2022_projects
    }
    
    print('__RESULT__:')
    print(json.dumps(result))
    
except Exception as e:
    print('__RESULT__:')
    print(json.dumps({'error': str(e)}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': 'Loaded 5 civic docs and 500 funding records', 'var_functions.list_db:24': ['civic_docs'], 'var_functions.execute_python:26': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:28': [{'Project_Name': '2021 Annual Street Maintenance', 'Amount': '24000'}, {'Project_Name': '2022 Annual Street Maintenance', 'Amount': '45000'}, {'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Amount': '38000'}, {'Project_Name': 'Annual Street Maintenance', 'Amount': '23000'}, {'Project_Name': 'Birdview Avenue Improvements', 'Amount': '79000'}, {'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': '85000'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Amount': '14000'}, {'Project_Name': 'Bluffs Park Shade Structure', 'Amount': '21000'}, {'Project_Name': 'Bluffs Park Workout Station', 'Amount': '39000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Amount': '87000'}], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json'}

exec(code, env_args)
