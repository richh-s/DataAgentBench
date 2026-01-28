code = """import json
import re

# Load data
# Access variables from previous steps
civic_docs_path = locals()['var_function-call-7157939871696024413']
funding_data_path = locals()['var_function-call-17433077485285005998']

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_data_path, 'r') as f:
    funding_data = json.load(f)

# Combine text from all docs
full_text = '\n'.join([doc['text'] for doc in civic_docs])

# Split into lines
lines = full_text.split('\n')

projects = []
current_project = None
current_block = []

# Regex for bullet points
bullet_pattern = re.compile(r'^\(cid:\d+\)')

# Iterate lines
for i, line in enumerate(lines):
    line = line.strip()
    if not line:
        continue
    
    # Check if this line is likely a project name
    is_header = False
    if not bullet_pattern.match(line) and 'Page' not in line and 'Agenda Item' not in line:
        # Check next line
        if i + 1 < len(lines):
            next_line = lines[i+1].strip()
            # Check for markers
            if '(cid:190)' in next_line or 'Updates:' in next_line or 'Project Description:' in next_line:
                is_header = True
            elif next_line == '':
                 # Check line after empty line
                 if i + 2 < len(lines):
                     next_next_line = lines[i+2].strip()
                     if '(cid:190)' in next_next_line or 'Updates:' in next_next_line or 'Project Description:' in next_next_line:
                         is_header = True

    if is_header:
        if current_project:
            projects.append({'name': current_project, 'text': '\n'.join(current_block)})
        current_project = line
        current_block = []
    else:
        if current_project:
            current_block.append(line)

if current_project:
    projects.append({'name': current_project, 'text': '\n'.join(current_block)})

# Analyze projects
completed_park_projects_2022 = []

for p in projects:
    name = p['name']
    text = p['text'].lower()
    
    # Check if park related
    if 'park' in name.lower() or 'park' in text:
        # Check for completed in 2022
        # Regex to capture year after 'completed'
        # Matches: "completed ... 2022" or "complete construction ... 2022"
        # We need to be careful not to match "completed in 2021" if 2022 is mentioned elsewhere.
        # But generally these updates are short.
        
        # Look for "completed" followed by "2022" within reasonable distance (e.g. same sentence or line)
        # But here 'text' is a block.
        
        # Specific patterns seen in preview:
        # "Construction was completed November 2022"
        # "Construction was completed, November 2022"
        
        match = re.search(r'completed.*?([a-zA-Z]+)[\s,]+(202\d)', text)
        found_year = None
        if match:
            if match.group(2) == '2022':
                found_year = '2022'
        
        if not found_year:
            match2 = re.search(r'complete construction:.*?([a-zA-Z]+)[\s,]+(202\d)', text)
            if match2:
                if match2.group(2) == '2022':
                    found_year = '2022'
        
        if found_year == '2022':
            completed_park_projects_2022.append(name)

# Sum funding
total_funding = 0
matched_projects = []

for cp in completed_park_projects_2022:
    # Try exact match first
    matched = False
    for fund in funding_data:
        # Normalize: strip and lower
        f_name = fund['Project_Name'].strip().lower()
        c_name = cp.strip().lower()
        
        if f_name == c_name:
            total_funding += int(fund['Amount'])
            matched_projects.append(fund['Project_Name'])
            matched = True
            # Don't break immediately, in case multiple funding sources?
            # "Funding table contains funding records... Fields: Funding_ID, Project_Name, Amount"
            # If a project has multiple funding records, they will have different Funding_IDs.
            # I should sum ALL records for that project name.
            # So I should filter funding_data for this project name.
            
    # If not matched by exact string, try substring?
    if not matched:
        # Retry with sum if substring matches?
        # Be careful of partial matches like "Park" matching "Legacy Park".
        # But "Bluffs Park Shade Structure" should match exactly.
        pass

# Refined matching logic:
# Iterate over UNIQUE extracted project names
unique_extracted = list(set(completed_park_projects_2022))
final_total = 0
final_matched = []

for cp in unique_extracted:
    c_name = cp.strip().lower()
    project_fund = 0
    match_found = False
    for fund in funding_data:
        f_name = fund['Project_Name'].strip().lower()
        if f_name == c_name:
            project_fund += int(fund['Amount'])
            match_found = True
    
    if match_found:
        final_total += project_fund
        final_matched.append(cp)

print('__RESULT__:')
print(json.dumps({'total_funding': final_total, 'projects': final_matched, 'extracted': unique_extracted}))"""

env_args = {'var_function-call-7157939871696024413': 'file_storage/function-call-7157939871696024413.json', 'var_function-call-17433077485285005998': 'file_storage/function-call-17433077485285005998.json'}

exec(code, env_args)
