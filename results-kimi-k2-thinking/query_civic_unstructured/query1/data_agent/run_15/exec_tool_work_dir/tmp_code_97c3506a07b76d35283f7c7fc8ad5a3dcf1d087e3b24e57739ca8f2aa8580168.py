code = """import json
import re

# Load the actual file paths from the storage variables
funding_result = locals()['var_functions.query_db:64']
civic_result = locals()['var_functions.query_db:40']

with open(funding_result) as f:
    funding_data = json.load(f)

with open(civic_result) as f:
    civic_docs = json.load(f)

# Create set of high-funding project names (> $50,000)
high_funding = set()
for item in funding_data:
    amt = int(item['Amount'])
    if amt > 50000:
        high_funding.add(item['Project_Name'])

# Extract capital projects in design phase
design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for design section
    design_marker = 'Capital Improvement Projects (Design)'
    construction_marker = 'Capital Improvement Projects (Construction)'
    
    if design_marker in text:
        # Get section boundaries
        start = text.find(design_marker) + len(design_marker)
        end = text.find(construction_marker, start)
        if end == -1:
            end = len(text)
        
        # Extract section
        section_text = text[start:end]
        lines = section_text.split('\n')
        
        for line in lines:
            line = line.strip()
            # Filter lines to identify project names
            if len(line) > 15:
                if not line.startswith('('):
                    if 'Updates:' not in line and 'Schedule:' not in line:
                        clean_line = re.sub(r'^(cid:\d+)\s*', '', line)
                        if len(clean_line) > 15:
                            design_projects.add(clean_line)

# Find matches using exact name matching
exact_matches = design_projects.intersection(high_funding)
result = {
    'high_funding_total': len(high_funding),
    'design_total': len(design_projects),
    'matching': len(exact_matches)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:32': [{'count': '276'}], 'var_functions.query_db:36': [], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json'}

exec(code, env_args)
