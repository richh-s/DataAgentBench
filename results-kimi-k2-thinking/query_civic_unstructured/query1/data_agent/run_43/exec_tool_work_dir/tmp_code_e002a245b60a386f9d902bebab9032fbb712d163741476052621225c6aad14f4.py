code = """import json

# Load funding data (projects with Amount > 50000)
funding_file = var_functions.query_db:60
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Load civic documents
civic_file = var_functions.query_db:6
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Build funding map: project name -> amount
funding_map = {}
for item in funding_records:
    project_name = item['Project_Name']
    amount = int(item['Amount'])
    funding_map[project_name] = amount

# Extract capital projects with design status from civic documents
design_capital_projects = []

def is_likely_design_project(line, full_text):
    ""Check if a line is a design project name""
    line = line.strip()
    if not line or len(line) < 5:
        return False
    
    # Skip non-project lines
    skip_patterns = ['page', 'schedule', 'updates', 'project description', 'staff is', 'city will', 'consultant', 'project is', 'to:', 'item', 'recommend', 'discussion:', 'public works', 'commission', 'agenda', 'civic center', 'city hall']
    if any(pattern in line.lower() for pattern in skip_patterns):
        return False
    
    if line.startswith('202') or line.startswith('Item'):
        return False
    
    # Check if design status is mentioned in context
    pos = full_text.find(line)
    if pos >= 0:
        context_window = full_text[pos:pos+500]
        if 'Design' in context_window or 'design' in context_window.lower():
            # Check if it's in a capital projects section
            section_start = max(0, pos-1000)
            section_text = full_text[section_start:pos+500]
            if 'Capital Improvement Projects' in section_text:
                return True
    
    return False

# Process each document
for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Find capital improvement projects in design phase
    lines = text.split('\n')
    in_capital_section = False
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Detect capital improvement projects sections
        if 'Capital Improvement Projects' in line:
            in_capital_section = True
            continue
        
        # Check if we're in a relevant section
        if in_capital_section:
            # Check if this line is a project name and in design status
            if is_likely_design_project(line, text):
                # Clean and add the project name
                clean_name = line.replace('•', '').replace('○', '').strip()
                if 8 < len(clean_name) < 200:
                    # Avoid duplicates
                    if clean_name not in [p['name'] for p in design_capital_projects]:
                        design_capital_projects.append({
                            'name': clean_name,
                            'status': 'design',
                            'type': 'capital'
                        })

# Match design projects with funding data
count = 0
matched_projects = []

# Build a list of all funded project names for matching
funded_project_names = list(funding_map.keys())

def get_matching_funding_project(design_name, funded_names):
    ""Find the best matching funded project name""
    d_lower = design_name.lower()
    
    # Direct match
    if design_name in funded_names:
        return design_name
    
    # Substring matching
    for funded in funded_names:
        f_lower = funded.lower()
        # Check if one contains the other
        if d_lower in f_lower or f_lower in d_lower:
            # Check length similarity (avoid matching "Park" to "Park Improvements Project")
            if abs(len(design_name) - len(funded)) < 40:
                return funded
    
    return None

for design_proj in design_capital_projects:
    matched_funding = get_matching_funding_project(design_proj['name'], funded_project_names)
    if matched_funding:
        amount = funding_map[matched_funding]
        count += 1
        matched_projects.append({
            'project': design_proj['name'],
            'funded_as': matched_funding,
            'amount': amount
        })

# Return the count
result = {'count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json'}

exec(code, env_args)
