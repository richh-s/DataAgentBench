code = """import json
import re

# Read the data files
with open('/tmp/tmp9q1f0j8y.json', 'r') as f:
    civic_docs = json.load(f)

with open('/tmp/tmphg9s8x_1.json', 'r') as f:
    funding_data = json.load(f)

# Create funding lookup
funding_lookup = {}
for f in funding_data:
    try:
        funding_lookup[f['Project_Name'].lower()] = int(f['Amount'])
    except:
        pass

# Extract projects
def extract_disaster_projects_2022_from_text(text):
    projects = []
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip if empty or common headers
        if not line or any(line.startswith(p) for p in ['Public Works', 'Commission', 'Agenda', 'To:', 'Prepared', 'Approved', 'Date', 'Meeting', 'Subject:', 'RECOMMENDED', 'DISCUSSION:', 'Capital Improvement', 'Page', '•', '(cid:']):
            continue
        
        # Check if next lines contain project info
        has_updates = any('Updates:' in lines[j] for j in range(i+1, min(i+5, len(lines))))
        has_schedule = any('Schedule:' in lines[j] for j in range(i+1, min(i+5, len(lines))))
        
        if has_updates or has_schedule:
            project_name = line
            
            # Check if disaster-related
            is_disaster = any(indicator.lower() in project_name.lower() for indicator in ['FEMA', 'CalJPIA', 'CalOES', 'fire', 'disaster', 'emergency'])
            
            if is_disaster:
                # Find start date
                start_date = None
                for j in range(i+1, min(i+15, len(lines))):
                    schedule_line = lines[j].strip()
                    if 'Begin Construction:' in schedule_line or 'Advertise:' in schedule_line:
                        date_match = re.search(r'(\d{4}|Spring \d{4}|Summer \d{4}|Fall \d{4}|Winter \d{4}|\d{4}-[A-Za-z]+)', schedule_line)
                        if date_match:
                            start_date = date_match.group(1)
                            break
                
                if start_date and '2022' in start_date:
                    projects.append({
                        'Project_Name': project_name,
                        'start_date': start_date
                    })
    
    return projects

# Process all documents
all_disaster_projects_2022 = []
for doc in civic_docs:
    projects = extract_disaster_projects_2022_from_text(doc['text'])
    all_disaster_projects_2022.extend(projects)

# Match with funding
total_funding = 0
matched_projects = []

for proj in all_disaster_projects_2022:
    proj_name = proj['Project_Name'].lower()
    
    # Exact match
    if proj_name in funding_lookup:
        amount = funding_lookup[proj_name]
        total_funding += amount
        matched_projects.append({
            'project': proj['Project_Name'],
            'amount': amount,
            'start_date': proj['start_date']
        })
    else:
        # Fuzzy match
        for funding_name, amount in funding_lookup.items():
            if (proj_name in funding_name or funding_name in proj_name) and ('fema' in funding_name or 'caljpia' in funding_name or 'caloes' in funding_name):
                total_funding += amount
                matched_projects.append({
                    'project': proj['Project_Name'],
                    'funding_name': funding_name,
                    'amount': amount,
                    'start_date': proj['start_date']
                })
                break

print('__RESULT__:')
print(json.dumps({
    'total_funding': total_funding,
    'matched_projects': matched_projects,
    'disaster_projects_2022_found': len(all_disaster_projects_2022)
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
