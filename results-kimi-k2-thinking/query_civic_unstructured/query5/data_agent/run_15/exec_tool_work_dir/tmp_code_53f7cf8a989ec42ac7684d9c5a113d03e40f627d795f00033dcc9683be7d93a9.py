code = """import json
import re

# Load funding data
funding_file = var_functions.query_db:18
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
docs_file = var_functions.query_db:19
with open(docs_file, 'r') as f:
    civic_docs = json.load(f)

# Extract funding information into a dict for easy lookup
funding_dict = {}
for fund in funding_data:
    proj_name = fund.get('Project_Name', '').strip()
    amount = int(fund.get('Amount', 0))
    funding_dict[proj_name] = amount

# Parse civic documents to find disaster projects that started in 2022
disaster_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    # Look for disaster-related sections
    in_disaster_section = False
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Check if we're entering a disaster recovery section
        if re.search(r'Disaster Recovery|Disaster.*Projects|FEMA Projects', line, re.IGNORECASE):
            in_disaster_section = True
            continue
            
        # Look for project names (typically all caps or with specific patterns)
        if in_disaster_section and len(line) > 10:
            # Check if this looks like a project name
            has_project_indicators = re.search(r'Project|Repair|Improvement|Construction|Replacement|Culvert|Bridge|Drain|Wall', line, re.IGNORECASE)
            not_metadata = not re.search(r'Agenda|Public Works|Commission|Fiscal Year|Capital Improvement', line, re.IGNORECASE)
            
            if has_project_indicators and not_metadata:
                current_project = line
                
                # Look ahead for 2022 dates
                for j in range(i, min(i+10, len(lines))):
                    next_line = lines[j].strip()
                    if re.search(r'2022', next_line) and not re.search(r'2022-2023|FY|Fiscal', next_line):
                        disaster_projects_2022.append(current_project)
                        break

# Also check for projects with explicit (FEMA Project) or similar suffixes
for doc in civic_docs:
    text = doc.get('text', '')
    # Find all project names with disaster suffixes
    matches = re.findall(r'[^\n]*\(FEMA[^\)]*\)[^\n]*', text, re.IGNORECASE)
    matches += re.findall(r'[^\n]*\(CalOES[^\)]*\)[^\n]*', text, re.IGNORECASE)
    matches += re.findall(r'[^\n]*\(CalJPIA[^\)]*\)[^\n]*', text, re.IGNORECASE)
    
    for match in matches:
        # Check if this project started in 2022
        if re.search(r'2022', text):
            # Extract project name (without the suffix if possible)
            proj_name = match.strip()
            disaster_projects_2022.append(proj_name)

# Get unique projects
unique_projects = list(set(disaster_projects_2022))

# Match with funding data and calculate total
total_funding = 0
matched_projects = []

for proj in unique_projects:
    # Clean up project name for matching
    proj_clean = proj.split('(cid:')[0].strip()
    
    # Direct match
    if proj_clean in funding_dict:
        amount = funding_dict[proj_clean]
        total_funding += amount
        matched_projects.append((proj_clean, amount))
    else:
        # Try fuzzy matching - remove suffixes and match base name
        base_name = re.sub(r'\s*\([^)]*\)\s*$', '', proj_clean)
        if base_name in funding_dict:
            amount = funding_dict[base_name]
            total_funding += amount
            matched_projects.append((proj_clean, amount))

# Generate result
result = f"Total funding for disaster-related projects that started in 2022: ${total_funding:,}\n\n"
result += "Matched Projects:\n"
for proj, amount in matched_projects:
    result += f"- {proj}: ${amount:,}\n"

result += f"\nNumber of projects: {len(matched_projects)}"

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.list_db:16': ['Funding'], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:19': 'file_storage/functions.query_db:19.json'}

exec(code, env_args)
