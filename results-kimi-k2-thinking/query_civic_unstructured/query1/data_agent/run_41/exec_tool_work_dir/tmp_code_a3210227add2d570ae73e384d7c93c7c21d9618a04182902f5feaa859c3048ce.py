code = """import json
import re

# Load data
funding_result = locals()['var_functions.query_db:24']
civic_result = locals()['var_functions.query_db:6']

# Build funding lookup dictionary
funding_lookup = {}
for item in funding_result:
    name = item['Project_Name']
    amount = int(item['Amount'])
    funding_lookup[name] = amount
    
    # Also store base name without common suffixes
    base_name = name.split(' (')[0]
    funding_lookup[base_name] = amount

# Find capital projects in design status from civic documents
design_project_names = set()

for doc in civic_result:
    text = doc.get('text', '')
    
    # Look for "Capital Improvement Projects (Design)" section
    if 'Capital Improvement Projects (Design)' in text:
        # Get the design section
        start = text.index('Capital Improvement Projects (Design)')
        section_text = text[start:]
        
        # Find end of design section
        end_markers = ['Capital Improvement Projects (Construction)', 'Disaster Recovery Projects', 'CAPITAL IMPROVEMENT PROJECTS (CONSTRUCTION)']
        end_index = len(section_text)
        for marker in end_markers:
            if marker in section_text:
                pos = section_text.index(marker)
                if pos < end_index:
                    end_index = pos
        
        design_section = section_text[:end_index]
        
        # Extract project names (look for lines that are likely project titles)
        for line in design_section.split('\n'):
            line = line.strip()
            # Skip empty or bullet points
            if not line or line.startswith('(') or line.startswith('•') or line.startswith('-'):
                continue
            # Skip metadata lines
            if 'Updates' in line or 'Schedule' in line or 'Design:' in line:
                continue
            # Check if line looks like a project name (reasonable length)
            if 10 < len(line) < 100:
                # Clean the name
                clean_name = re.sub('\s+', ' ', line).strip()
                # Remove trailing punctuation
                while clean_name and clean_name[-1] in '.:,;':
                    clean_name = clean_name[:-1]
                
                # Check if in funding lookup
                if clean_name in funding_lookup:
                    amount = funding_lookup[clean_name]
                    if amount > 50000:
                        design_project_names.add((clean_name, amount))

# Count results
count = len(design_project_names)
print('__RESULT__:')
print(str(count))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
