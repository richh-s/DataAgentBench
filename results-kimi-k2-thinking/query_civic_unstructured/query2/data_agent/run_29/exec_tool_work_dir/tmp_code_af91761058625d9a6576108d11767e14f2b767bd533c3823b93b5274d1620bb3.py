code = """import json

# Load the data from files
civic_docs_file = '/tmp/tmpz5hptp8z.json'
funding_file = '/tmp/tmphs_qx5r1.json'

with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)
    
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Function to check if a project name is park-related
def is_park_related(project_name):
    if not project_name:
        return False
    name_lower = project_name.lower()
    return 'park' in name_lower or 'playground' in name_lower

# Dictionary to store project info: project_name -> {status, et, topic}
project_info = {}

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Split into lines for parsing
    lines = text.split('\n')
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Detect project name based on context
        # Project names are typically followed by (cid: markers or Update/Schedule info
        if len(line) > 5 and not line.startswith('(') and not line.startswith('---'):
            # Check if next few lines contain project-related markers
            is_project = False
            for j in range(i+1, min(i+6, len(lines))):
                next_line = lines[j].lower()
                if any(marker in next_line for marker in ['updates:', 'project schedule:', 'complete construction:', '(cid:']):
                    is_project = True
                    break
            
            if is_project:
                current_project = line
                if line not in project_info:
                    project_info[line] = {'status': '', 'et': '', 'topic': ''}
                
                # Determine topic from project name
                if is_park_related(line):
                    project_info[line]['topic'] = 'park'
        
        # Extract status and completion date if we have a current project
        if current_project and current_project in project_info:
            line_lower = line.lower()
            
            # Check for completion status
            if any(phrase in line_lower for phrase in ['completed', 'construction was completed', 'notice of completion', 'complete construction']):
                project_info[current_project]['status'] = 'completed'
                if 'construction:' in line_lower:
                    # Extract date from "Complete Construction: November 2022" format
                    parts = line.split(':')
                    if len(parts) > 1:
                        date_str = parts[1].strip()
                        project_info[current_project]['et'] = date_str
                elif '2022' in line:
                    project_info[current_project]['et'] = '2022'
            elif 'complete construction:' in line_lower:
                project_info[current_project]['status'] = 'completed'
                # Extract the date part
                match = line.split(':')
                if len(match) > 1:
                    date_str = match[1].strip()
                    if '2022' in date_str:
                        project_info[current_project]['et'] = date_str

# Filter for park-related projects completed in 2022
park_projects_2022 = []
for proj_name, info in project_info.items():
    if (info.get('status') == 'completed' and 
        '2022' in str(info.get('et', '')) and 
        is_park_related(proj_name)):
        park_projects_2022.append({
            'Project_Name': proj_name,
            'status': info['status'],
            'et': info['et'],
            'topic': 'park'
        })

# Match with funding data using flexible matching
def normalize_name(name):
    return name.lower().strip().replace('  ', ' ')

funding_matches = []
matched_funding_projects = set()

for park_proj in park_projects_2022:
    park_name = park_proj['Project_Name']
    park_name_norm = normalize_name(park_name)
    
    for fund in funding_data:
        fund_name = fund['Project_Name']
        fund_name_norm = normalize_name(fund_name)
        
        # Check for various matching scenarios
        is_match = False
        
        # 1. Exact match
        if park_name_norm == fund_name_norm:
            is_match = True
        # 2. One is substring of the other
        elif park_name_norm in fund_name_norm or fund_name_norm in park_name_norm:
            is_match = True
        # 3. Key components match (for cases like "Bluffs Park Shade Structure" vs "Bluffs Park Shade")
        else:
            park_words = set(park_name_norm.split())
            fund_words = set(fund_name_norm.split())
            # If they share at least 3 key words and mention the same location
            if len(park_words.intersection(fund_words)) >= 3:
                is_match = True
        
        if is_match and fund_name not in matched_funding_projects:
            funding_matches.append({
                'project_name': park_name,
                'funding_name': fund_name,
                'amount': int(fund['Amount']),
                'funding_source': fund['Funding_Source']
            })
            matched_funding_projects.add(fund_name)
            break  # Match each park project to at most one funding record

# Calculate total funding
total_funding = sum(m['amount'] for m in funding_matches)

result = {
    'park_projects_2022': park_projects_2022,
    'funding_matches': funding_matches,
    'total_funding': total_funding
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
