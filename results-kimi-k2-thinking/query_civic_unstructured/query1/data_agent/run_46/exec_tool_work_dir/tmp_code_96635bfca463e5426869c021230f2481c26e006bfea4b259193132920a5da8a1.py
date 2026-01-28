code = """import json, re, os

# Load file paths from variables
funding_file = str(locals()['var_functions.query_db:6'])
civic_file = str(locals()['var_functions.query_db:8'])

# Load JSON data
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

with open(civic_file, 'r') as f:
    civic_documents = json.load(f)

# Process funding data - create map of projects with amount > 50000
def normalize_project_name(name):
    name = re.sub(r'\s*\(FEMA[^\)]*\)', '', name, flags=re.I)
    name = re.sub(r'\s*\(CalOES[^\)]*\)', '', name, flags=re.I)
    name = re.sub(r'\s*\(CalJPIA[^\)]*\)', '', name, flags=re.I)
    name = re.sub(r'\s+Project\s*$', '', name, flags=re.I)
    return name.strip().lower()

funding_map = {}
for record in funding_records:
    amount = int(record['Amount'])
    if amount > 50000:
        normalized = normalize_project_name(record['Project_Name'])
        if normalized:
            funding_map[normalized] = record['Project_Name']

# Extract capital projects with design status from civic documents
capital_design_projects = set()

for doc in civic_documents:
    text_content = doc.get('text', '')
    
    # Locate the Capital Improvement Projects (Design) section
    design_section_start = text_content.find('Capital Improvement Projects (Design)')
    if design_section_start == -1:
        continue
    
    # Find end of design section
    construction_section_start = text_content.find('Capital Improvement Projects (Construction)', design_section_start)
    if construction_section_start == -1:
        construction_section_start = len(text_content)
    
    design_section_text = text_content[design_section_start:construction_section_start]
    section_lines = design_section_text.split('\n')
    
    # Identify project names in the design section
    for i, current_line in enumerate(section_lines):
        current_line = current_line.strip()
        
        # Filter out non-project lines
        if len(current_line) < 10:
            continue
        if current_line.startswith('(') or 'Capital Improvement' in current_line:
            continue
        
        # Check if next lines contain project metadata
        if i + 1 < len(section_lines):
            upcoming_text = ' '.join(section_lines[i+1:min(i+5, len(section_lines))])
            if 'Updates:' in upcoming_text or 'Schedule:' in upcoming_text:
                # Verify this is not a disaster project
                if 'FEMA' not in current_line and 'CalOES' not in current_line and 'CalJPIA' not in current_line:
                    # Verify this is a capital project
                    infrastructure_keywords = ['road','park','drain','bridge','facility','system','plan','structure','study','improvements','repairs','street','water','traffic','building']
                    if any(kw in current_line.lower() for kw in infrastructure_keywords):
                        capital_design_projects.add(current_line)

# Match projects with funding records
funded_project_count = 0

for project in capital_design_projects:
    normalized_project = normalize_project_name(project)
    if not normalized_project:
        continue
    
    # Check for direct or partial match in funding map
    for funded_key in funding_map:
        if normalized_project in funded_key or funded_key in normalized_project:
            funded_project_count += 1
            break

print('__RESULT__:')
print(json.dumps({'count': funded_project_count}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
