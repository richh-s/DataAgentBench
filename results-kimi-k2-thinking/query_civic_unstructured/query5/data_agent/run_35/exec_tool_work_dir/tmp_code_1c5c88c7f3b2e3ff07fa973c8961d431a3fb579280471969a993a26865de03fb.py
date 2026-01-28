code = """import json
import re

# First, load all funding data
funding_file = '/tmp/tmpj4_6s1y9.json'
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

print(f"Total funding records: {len(funding_data)}")

# Identify disaster-related projects from funding data
disaster_projects_funding = [
    item for item in funding_data 
    if any(keyword in item['Project_Name'].upper() for keyword in ['FEMA', 'CALOES', 'CALJPIA'])
]

print(f"Disaster-related projects in funding database: {len(disaster_projects_funding)}")

# Create a dictionary for easy lookup: project_name -> amount
disaster_funding_lookup = {}
for item in disaster_projects_funding:
    name = item['Project_Name']
    amount = int(item['Amount'])
    if name in disaster_funding_lookup:
        disaster_funding_lookup[name] += amount
    else:
        disaster_funding_lookup[name] = amount

print(f"\nDisaster projects with funding:")
for name, amount in disaster_funding_lookup.items():
    print(f"- {name}: ${amount:,}")

# Now load civic documents
docs_file = '/tmp/tmpy4j0_8x6.json'
with open(docs_file, 'r') as f:
    civic_docs = json.load(f)

print(f"\n\nLoaded {len(civic_docs)} civic documents")

# Function to extract disaster projects that started in 2022
def extract_disaster_projects_starting_2022(docs):
    projects_2022 = []
    
    for doc in docs:
        text = doc.get('text', '')
        lines = text.split('\n')
        
        for i, line in enumerate(lines):
            line = line.strip()
            
            # Look for lines that might be project names
            # Skip headers, markers, and metadata
            skip_patterns = [
                'Page', 'Agenda', 'Prepared by', 'Approved by', 'Subject:',
                'RECOMMENDED ACTION', 'DISCUSSION', 'To:', 'Chair', 'Date prepared',
                'Public Works', 'Commission', 'Item', '===', '---', '•', '■', '(cid:'
            ]
            
            should_skip = any(pattern in line for pattern in skip_patterns)
            should_skip = should_skip or line.startswith('(')
            should_skip = should_skip or len(line) < 5 or len(line) > 200
            
            if should_skip:
                continue
            
            # Check if this is a disaster project
            is_disaster = any(keyword in line.upper() for keyword in ['FEMA', 'CALOES', 'CALJPIA'])
            
            # Look for start date 2022 in nearby lines
            started_in_2022 = False
            status = 'unknown'
            
            # Look ahead and behind for schedule/status info
            window_start = max(0, i-3)
            window_end = min(len(lines), i+8)
            
            for j in range(window_start, window_end):
                context_line = lines[j].strip()
                
                # Check for 2022 start dates
                if '2022' in context_line:
                    # Look for keywords indicating start/begin
                    start_keywords = ['begin', 'start', 'advertise', 'design', 'construction'] 
                    if any(kw in context_line.lower() for kw in start_keywords):
                        started_in_2022 = True
                
                # Check for status
                if 'Updates:' in context_line or j == i+1:
                    # Look for status in the next few lines
                    for k in range(j+1, min(len(lines), j+5)):
                        status_line = lines[k].lower()
                        if 'design' in status_line:
                            status = 'design'
                            break
                        elif 'construction' in status_line:
                            status = 'construction'
                            break
                        elif 'completed' in status_line:
                            status = 'completed'
                            break
                        elif 'not started' in status_line:
                            status = 'not started'
                            break
            
            # If not explicitly disaster, check context for disaster indicators
            if not is_disaster and not started_in_2022:
                for j in range(window_start, window_end):
                    context_line = lines[j].upper()
                    if any(keyword in context_line for keyword in ['FEMA', 'CALOES', 'CALJPIA']):
                        is_disaster = True
                        break
            
            # Check if it's a 2022 project (starts with 2022)
            if line.startswith('2022') and not is_disaster:
                # Check if disaster-related in context
                for j in range(window_start, window_end):
                    context_line = lines[j].upper()
                    if any(keyword in context_line for keyword in ['FEMA', 'CALOES', 'CALJPIA', 'DISASTER', 'RECOVERY']):
                        is_disaster = True
                        started_in_2022 = True
                        break
            
            # Add if both conditions met
            if is_disaster and started_in_2022:
                projects_2022.append({
                    'Project_Name': line,
                    'status': status,
                    'start_year': '2022'
                })
    
    return projects_2022

# Extract projects
projects_2022 = extract_disaster_projects_starting_2022(civic_docs)

print(f"\nDisaster projects starting in 2022 found in documents: {len(projects_2022)}")

for proj in projects_2022:
    print(f"- {proj['Project_Name']} (Status: {proj['status']})")

# Match with funding and calculate total
matched_projects = []
total_funding = 0

for proj in projects_2022:
    proj_name = proj['Project_Name']
    
    # Direct match
    if proj_name in disaster_funding_lookup:
        amount = disaster_funding_lookup[proj_name]
        matched_projects.append({
            'project_name': proj_name,
            'amount': amount,
            'status': proj['status']
        })
        total_funding += amount
    else:
        # Try to find similar matches - look for projects with same base name
        # This handles cases like "Project Name" vs "Project Name (FEMA Project)"
        for fund_proj, amount in disaster_funding_lookup.items():
            # Check if one is contained in the other
            if proj_name in fund_proj or fund_proj in proj_name:
                matched_projects.append({
                    'project_name': fund_proj,
                    'amount': amount,
                    'status': proj['status']
                })
                total_funding += amount
                break

print(f"\n\nMatched {len(matched_projects)} projects with funding")
print(f"Total funding for disaster projects starting in 2022: ${total_funding:,}")

# Detailed breakdown
print(f"\nDetailed breakdown:")
for proj in matched_projects:
    print(f"- {proj['project_name']}: ${proj['amount']:,} (Status: {proj['status']})")

result = {
    'total_funding': total_funding,
    'project_count': len(matched_projects),
    'projects': matched_projects
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
