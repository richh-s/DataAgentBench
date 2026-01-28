code = """import json, re

# Load data
funding_file = globals()['var_functions.query_db:4']
civic_file = globals()['var_functions.query_db:5']

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Create funding dictionary
funding_dict = {}
for record in funding_data:
    try:
        amount = int(record['Amount'])
        funding_dict[record['Project_Name']] = amount
    except:
        continue

# Count projects with design status, capital type, and funding > 50000
count = 0
matching_projects = []

for doc in civic_docs:
    text = doc.get('text', '').lower()
    
    # Check if this document contains design status and capital projects
    has_design = 'design' in text
    has_capital = 'capital improvement' in text
    
    if has_design and has_capital:
        # Extract project names and check funding
        lines = text.split('
')
        for line in lines:
            line_clean = line.strip()
            # Look for potential project names (start with capital letter, not boilerplate)
            if line_clean and line_clean[0].isupper():
                # Check if this is a project name by looking at context
                if (
                    line_clean not in ['Public', 'Agenda', 'Subject', 'To:', 'Prepared by:', 'RECOMMENDED ACTION'] and
                    not line_clean.startswith('(') and
                    not line_clean.startswith('Page')
                ):
                    # Check funding for this project
                    amount = funding_dict.get(line_clean, 0)
                    if amount > 50000:
                        # Check if design-related text appears near this project
                        project_start = text.find(line_clean.lower())
                        if project_start > 0:
                            snippet = text[project_start:project_start+500]
                            if 'design' in snippet:
                                count += 1
                                matching_projects.append(line_clean)

print("__RESULT__:")
print(json.dumps({
    "count": count,
    "sample_projects": matching_projects[:10]
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:14': ['var_functions.list_db:0', 'var_functions.list_db:1', 'var_functions.query_db:4', 'var_functions.query_db:5'], 'var_functions.execute_python:20': {'funding_count': 276, 'civic_docs_count': 5, 'sample_funding_name': 'Birdview Avenue Improvements'}, 'var_functions.execute_python:22': {'projects_with_funding': 276, 'sample_projects': ['Birdview Avenue Improvements', 'Birdview Avenue Improvements (CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Broad Beach Road Water Quality Repair', 'City Hall Roof Replacement', 'City Traffic Signals Backup Power', 'Civic Center Stormwater Diversion Structure', 'Clover Heights Storm Drain', 'Corral Canyon Culvert Repairs']}, 'var_functions.execute_python:24': {'funding_projects': 276, 'message': 'Loaded funding data'}, 'var_functions.execute_python:26': {'total_funding_projects': 276, 'funding_dict_size': 276}}

exec(code, env_args)
