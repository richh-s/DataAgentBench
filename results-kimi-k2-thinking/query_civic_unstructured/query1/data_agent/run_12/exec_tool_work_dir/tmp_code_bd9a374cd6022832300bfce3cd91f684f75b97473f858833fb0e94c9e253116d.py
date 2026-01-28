code = """import json

# Get the file paths from the storage
funding_file_path = 'var_functions.query_db:0'
civic_file_path = 'var_functions.query_db:1'

# Read funding data
with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

# Read civic documents data
with open(civic_file_path, 'r') as f:
    civic_docs_data = json.load(f)

# Create funding lookup
funding_lookup = {}
for item in funding_data:
    funding_lookup[item['Project_Name']] = int(item['Amount'])

# Find capital projects in design status
capital_design_projects = []

for doc in civic_docs_data:
    if 'text' not in doc:
        continue
    
    text = doc['text']
    
    # Look for the specific section header
    if 'Capital Improvement Projects (Design)' in text:
        # Get the section content
        start = text.find('Capital Improvement Projects (Design)')
        section = text[start:]
        
        # Find end of section
        end_pos = float('inf')
        for marker in ['Capital Improvement Projects (Construction)', 
                       'Capital Improvement Projects (Not Started)',
                       'Disaster Recovery Projects']:
            pos = section.find(marker)
            if pos > 0 and pos < end_pos:
                end_pos = pos
        
        if end_pos != float('inf'):
            design_section = section[:end_pos]
        else:
            design_section = section
        
        # Extract potential project names
        lines = design_section.split('\n')
        for line in lines:
            line = line.strip()
            if not line or len(line) < 5:
                continue
            
            # Skip headers and markers
            skip_terms = ['Capital Improvement', 'Projects (Design)', 'Updates:', 'Schedule:']
            if any(term in line for term in skip_terms):
                continue
            
            # Skip bullet points
            if line.startswith('(') or line.startswith('-') or line.startswith('•'):
                continue
            
            # Check if this is a funded project with amount > 50000
            if line in funding_lookup and funding_lookup[line] > 50000:
                capital_design_projects.append(line)

# Remove duplicates
capital_design_projects = list(set(capital_design_projects))

# Prepare result
result = json.dumps({
    'count': len(capital_design_projects),
    'projects': capital_design_projects
})

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json'}

exec(code, env_args)
