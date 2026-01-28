code = """import json

# Load funding data (projects > $50k)
with open(locals()['var_functions.query_db:44']) as f:
    funding_data = json.load(f)

# Load civic documents
with open(locals()['var_functions.query_db:2']) as f:
    civic_docs = json.load(f)

# Create lookup for funding projects
funding_names = set([rec['Project_Name'] for rec in funding_data])
print('Funding projects count:', len(funding_names))

# Extract design status capital projects from documents
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start >= 0:
        construction_start = text.find('Capital Improvement Projects (Construction)', design_start)
        if construction_start < 0:
            construction_start = len(text)
        
        section = text[design_start:construction_start]
        
        # Split by blocks
        blocks = section.split('\n\n')
        for block in blocks:
            block = block.strip()
            if block and 'Design)' not in block and len(block) > 15:
                # Get first line
                lines = [line.strip() for line in block.split('\n') if line.strip()]
                if lines:
                    first_line = lines[0]
                    # Validate it's a project name
                    if (first_line and 'Updates' not in first_line and 
                        'Schedule' not in first_line and not first_line.isupper() and
                        len(first_line) > 5):
                        design_projects.append(first_line)

print('Design projects found:', len(design_projects))

# Match projects by comparing names (normalized)
def normalize_name(n):
    n2 = n.split('(')[0].strip().lower()
    n2 = n2.replace('project', '').replace('improvements', '')
    return n2.strip()

matched_count = 0
for dname in design_projects:
    d_clean = normalize_name(dname)
    
    for fund_name in list(funding_names):
        f_clean = normalize_name(fund_name)
        
        if d_clean in f_clean or f_clean in d_clean:
            matched_count += 1
            funding_names.discard(fund_name)
            break

result = {'count': matched_count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)
