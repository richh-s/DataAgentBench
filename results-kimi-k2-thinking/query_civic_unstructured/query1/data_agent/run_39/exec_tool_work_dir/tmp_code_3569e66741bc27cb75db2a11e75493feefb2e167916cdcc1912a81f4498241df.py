code = """import json

# Load data
funding_file = var_functions.query_db:0
civic_file = var_functions.query_db:2

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Get the text from first document
doc_text = str(civic_docs[0]['text'])

# Find projects in design status - look for the design section
design_keyword = 'Capital Improvement Projects (Design)'
construction_keyword = 'Capital Improvement Projects (Construction)'

design_start = doc_text.find(design_keyword)
construction_start = doc_text.find(construction_keyword)

project_list = []

if design_start >= 0 and construction_start > design_start:
    design_section = doc_text[design_start:construction_start]
    # Split into lines
    section_lines = design_section.split('\n')
    for line_idx in range(len(section_lines)):
        current_line = section_lines[line_idx].strip()
        # Skip empty or marker lines
        if not current_line or current_line.startswith('(cid:') or current_line.startswith('Page'):
            continue
        # Check if next line has project update markers
        if line_idx + 1 < len(section_lines):
            next_line = section_lines[line_idx + 1]
            if 'Updates:' in next_line and '(cid:' in next_line:
                project_list.append(current_line)

# Remove duplicates
unique_projects = list(set(project_list))

# Match with funding data > $50,000
matched_funding = []
for project_name in unique_projects:
    for funding_record in funding_data:
        if funding_record['Project_Name'] == project_name and int(funding_record['Amount']) > 50000:
            matched_funding.append(funding_record['Project_Name'])

result = {
    'design_projects': sorted(unique_projects),
    'total_design_count': len(unique_projects),
    'matching_funding': sorted(matched_funding),
    'matching_count': len(matched_funding)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['civic_docs']}

exec(code, env_args)
