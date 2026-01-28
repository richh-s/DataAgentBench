code = """import json
import re

# Load civic documents from file
var_civic_docs = locals()['var_functions.query_db:2']  # Mongo query result stored under this key
if isinstance(var_civic_docs, str):
    with open(var_civic_docs, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = var_civic_docs

# Load funding data from file
var_funding = locals()['var_functions.query_db:6']  # SQL query result stored under this key
if isinstance(var_funding, str):
    with open(var_funding, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = var_funding

# Parse civic documents to extract project information
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for project name patterns
    # Pattern 1: Projects listed under "Capital Improvement Projects (Design)"
    if 'Capital Improvement Projects (Design)' in text:
        design_section = text.split('Capital Improvement Projects (Design)')[1]
        # Split into individual projects
        proj_blocks = re.split(r'\n\s*\n', design_section)
        
        for block in proj_blocks:
            # Extract project name (first line that doesn't start with special chars)
            lines = [line.strip() for line in block.split('\n') if line.strip()]
            for line in lines:
                if line and not line.startswith('(') and not line.startswith('•') and not line.startswith('▪') and not line.startswith('▪') and 'Updates:' not in line and 'Schedule:' not in line:
                    # This is likely a project name
                    project_name = line
                    
                    # Determine type (disaster projects have FEMA/CalOES in name)
                    proj_type = "disaster" if any(x in project_name for x in ["(FEMA", "(CalOES", "(CalJPIA"]) else "capital"
                    
                    # Check funding for this project
                    for fund in funding_data:
                        if fund.get('Project_Name') == project_name:
                            amount = int(fund.get('Amount', 0))
                            if amount > 50000:
                                projects.append({
                                    'Project_Name': project_name,
                                    'Type': proj_type,
                                    'Status': 'design',
                                    'Amount': amount
                                })
                            break
                    break  # Only first non-empty line is project name

# Count capital projects with design status and funding > $50,000
capital_design_count = len([p for p in projects if p['Type'] == 'capital' and p['Status'] == 'design'])

print('__RESULT__:')
print(json.dumps(capital_design_count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
