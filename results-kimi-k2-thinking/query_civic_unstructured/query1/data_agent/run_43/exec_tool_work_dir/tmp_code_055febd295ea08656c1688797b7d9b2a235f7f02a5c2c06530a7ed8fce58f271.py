code = """import json

# Load funding data (Amount > 50000)
funding_data = var_functions.query_db:90
funding_names = [item['Project_Name'] for item in funding_data]

# Load civic documents
civic_docs = var_functions.query_db:6

# Function to check if a line is likely a project name
def is_project_line(line, full_text):
    line = line.strip()
    if not line or len(line) < 5:
        return False
    
    # Skip obvious non-project lines
    skip_terms = ['page', 'schedule', 'updates', 'project description', 'staff is', 'city will', 'consultant', 'project is', 'to:', 'item', 'recommend', 'discussion:', 'public works', 'commission', 'agenda', 'civic center', 'city hall', 'subject:', 'date prepared', 'meeting date']
    if any(term in line.lower() for term in skip_terms):
        return False
    
    if line.startswith('202') or line.startswith('Item'):
        return False
    
    # Check context for design status
    pos = full_text.find(line)
    if pos >= 0:
        context = full_text[pos:pos+400]
        if 'Design' in context:
            return True
    return False

# Extract design capital projects
design_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects' in text:
        lines = text.split('\n')
        for line in lines:
            if is_project_line(line, text):
                clean_name = line.replace('•', '').replace('○', '').strip()
                if len(clean_name) > 8 and len(clean_name) < 200:
                    design_projects.add(clean_name)

# Count matches with funding > 50000
count = 0
for proj in design_projects:
    proj_lower = proj.lower()
    for funded in funding_names:
        funded_lower = funded.lower()
        # Check for name similarity (substring match)
        if proj_lower in funded_lower or funded_lower in proj_lower:
            if abs(len(proj) - len(funded)) < 40:  # Avoid false matches
                count += 1
                break

result = {'count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.list_db:82': ['civic_docs'], 'var_functions.query_db:84': 'file_storage/functions.query_db:84.json', 'var_functions.execute_python:86': [], 'var_functions.query_db:90': 'file_storage/functions.query_db:90.json', 'var_functions.execute_python:106': {'count': 7}}

exec(code, env_args)
