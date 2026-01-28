code = """import json, re, os, sys

# Load data from files
civic_docs_path = locals()['var_functions.query_db:16']
funding_path = locals()['var_functions.query_db:17']

with open(civic_docs_path) as f:
    civic_docs = json.load(f)
with open(funding_path) as f:
    funding_data = json.load(f)

print("Loading data...")
completed_projects = []

# Extract project info from documents
for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line_lower = line.lower()
        
        # Look for completion in 2022
        if ('completed' in line_lower or 'completion' in line_lower) and '2022' in line:
            # Find project name
            project_name = None
            for j in range(i-1, max(0,i-5), -1):
                prev = lines[j].strip()
                if prev and not prev.startswith('(') and len(prev) > 5:
                    project_name = prev
                    break
            
            if project_name:
                # Clean up project name
                project_name = re.sub(r'^[•◦\s]+', '', project_name)
                project_name = re.sub(r'\s+', ' ', project_name).strip()
                
                if project_name and 'project' not in project_name.lower()[:50]:
                    completed_projects.append({
                        'name': project_name,
                        'year': '2022'
                    })

# Filter park-related projects
park_projects = [p for p in completed_projects if 'park' in p['name'].lower()]
print("Found", len(park_projects), "park projects completed in 2022")

# Match with funding data
funded_parks = []
total_amount = 0

for park in park_projects:
    park_name = park['name']
    
    for fund in funding_data:
        fund_name = fund['Project_Name']
        
        # Check for name match
        if (park_name.lower() in fund_name.lower() or 
            fund_name.lower() in park_name.lower() or
            re.sub(r'[^a-z]', '', park_name.lower()) in re.sub(r'[^a-z]', '', fund_name.lower())):
            
            amount = int(fund['Amount'])
            total_amount += amount
            funded_parks.append({
                'park_project': park_name,
                'funding_record': fund_name,
                'amount': amount
            })

# Output result
result = {
    "total_funding": total_amount,
    "project_count": len(funded_parks),
    "details": funded_parks
}

print("__RESULT__:")
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json'}

exec(code, env_args)
