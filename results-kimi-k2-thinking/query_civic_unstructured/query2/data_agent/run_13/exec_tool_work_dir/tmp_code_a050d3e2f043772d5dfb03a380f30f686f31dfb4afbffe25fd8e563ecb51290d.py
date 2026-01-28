code = """import json
import os

# Access the stored results - they are file paths, not direct variables
try:
    # Try to read the civic documents file
    with open('var_functions.query_db:2', 'r') as f:
        civic_docs = json.load(f)
except:
    # If direct file doesn't work, check what files exist in current directory
    files = os.listdir('.')
    civic_docs = []
    for file in files:
        if 'civic' in file.lower() or 'query_db' in file:
            try:
                with open(file, 'r') as f:
                    content = f.read()
                    if '[' in content and ']' in content:
                        civic_docs = json.loads(content)
                        break
            except:
                continue

# Try to read funding data
try:
    with open('var_functions.query_db:24', 'r') as f:
        funding_data = json.load(f)
except:
    # Try alternative approach
    funding_data = []
    for file in files:
        if 'funding' in file.lower() or 'query_db' in file:
            try:
                with open(file, 'r') as f:
                    content = f.read()
                    if '[' in content and ']' in content:
                        funding_data = json.loads(content)
                        break
            except:
                continue

# If we still don't have data, use preview info
if not civic_docs or not funding_data:
    print('__RESULT__:')
    print(json.dumps({
        'error': 'Could not load data files',
        'civic_docs_loaded': len(civic_docs) > 0,
        'funding_data_loaded': len(funding_data) > 0
    }))
else:
    # Successfully loaded data
    
    # From the preview, we know these park projects were completed in 2022:
    # 1. Bluffs Park Shade Structure - completed November 2022
    
    park_projects_2022 = []
    
    # Look for park projects completed in 2022 in the documents
    for doc in civic_docs:
        text = doc.get('text', '')
        if not text:
            continue
            
        # Check if this document mentions park projects completed in 2022
        lines = text.split('\n')
        
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            # Look for park project names
            if 'park' in line.lower() and len(line) < 100 and not line.startswith('('):
                # Look ahead for completion information
                context = '\n'.join(lines[i:i+5])
                if 'completed' in context.lower() and '2022' in context:
                    project_name = line.split('Updates:')[0].strip()
                    if project_name and not any(x in project_name.lower() for x in ['page', 'item', 'public works', 'capital improvement']):
                        park_projects_2022.append(project_name)
            
            i += 1
    
    # Add known project from preview
    if not park_projects_2022:
        # From the preview we saw this explicitly
        if any('Bluffs Park Shade Structure' in json.dumps(docs) for docs in civic_docs):
            park_projects_2022.append('Bluffs Park Shade Structure')
    
    # Remove duplicates
    park_projects_2022 = list(set(park_projects_2022))
    
    # Now find funding for these projects
    total_funding = 0
    funding_matches = []
    
    for fund in funding_data:
        fund_name = fund.get('Project_Name', '')
        amount = int(fund.get('Amount', 0))
        
        for park_proj in park_projects_2022:
            if park_proj and fund_name and park_proj.lower() in fund_name.lower():
                total_funding += amount
                funding_matches.append({
                    'project': park_proj,
                    'funding_record': fund_name,
                    'amount': amount
                })
                break  # Each project counted once
    
    # Also check for any park project with amount
    if total_funding == 0:
        # Try direct search in funding data for park projects
        for fund in funding_data:
            fund_name = fund.get('Project_Name', '')
            amount = int(fund.get('Amount', 0))
            
            if 'park' in fund_name.lower() and 'shade' in fund_name.lower() and 'bluff' in fund_name.lower():
                total_funding = amount
                funding_matches.append({
                    'project': 'Bluffs Park Shade Structure',
                    'funding_record': fund_name,
                    'amount': amount
                })
                break
    
    print('__RESULT__:')
    print(json.dumps({
        'park_projects_2022': park_projects_2022,
        'total_funding': total_funding,
        'funding_matches': funding_matches
    }))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
