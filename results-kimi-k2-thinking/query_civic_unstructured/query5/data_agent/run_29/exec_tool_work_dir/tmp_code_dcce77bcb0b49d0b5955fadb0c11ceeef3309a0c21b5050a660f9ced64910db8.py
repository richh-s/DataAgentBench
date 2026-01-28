code = """import json
import re

# Read civic documents
civic_file = open('/tmp/tmp9q1f0j8y.json', 'r')
civic_docs = json.load(civic_file)
civic_file.close()

# Read funding data
funding_file = open('/tmp/tmphg9s8x_1.json', 'r')
funding_records = json.load(funding_file)
funding_file.close()

# Build funding lookup
funding_lookup = {}
for record in funding_records:
    project_name = record.get('Project_Name', '').lower()
    amount = int(record.get('Amount', 0))
    if project_name and amount > 0:
        funding_lookup[project_name] = amount

# Extract disaster projects starting in 2022
disaster_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    current_project = None
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        if not line or len(line) < 5:
            continue
            
        line_lower = line.lower()
        
        # Check if this line is a project name (based on context)
        # Skip headers and bullet points
        if any(line.startswith(x) for x in ['Public Works', 'Commission', 'Agenda', 'To:', 'Prepared', 'Approved', 'Date', 'Meeting', 'Subject:', 'RECOMMENDED', 'DISCUSSION:', 'Capital Improvement', 'Page', '(', '•']):
            continue
        if 'cid:' in line:
            continue
            
        # Check if disaster-related
        is_disaster = any(marker in line_lower for marker in ['fema', 'caljpia', 'caloes', 'fire', 'disaster', 'emergency'])
        
        # Look ahead for schedule/updates to confirm it's a project
        has_updates = False
        has_schedule = False
        for j in range(i+1, min(i+6, len(lines))):
            next_line = lines[j].strip()
            if 'Updates:' in next_line or 'Updates' in next_line:
                has_updates = True
            if 'Schedule:' in next_line or 'Project Schedule:' in next_line:
                has_schedule = True
        
        if has_updates or has_schedule:
            current_project = line
            
            # If disaster project, look for 2022 start date
            if is_disaster:
                start_date = None
                for j in range(i+1, min(i+20, len(lines))):
                    schedule_line = lines[j].strip()
                    if 'Begin Construction:' in schedule_line or 'Advertise:' in schedule_line:
                        date_match = re.search(r'(\d{4}|Spring \d{4}|Summer \d{4}|Fall \d{4}|Winter \d{4}|\d{4}-[A-Za-z]+)', schedule_line)
                        if date_match:
                            start_date = date_match.group(1)
                            break
                
                if start_date and '2022' in str(start_date):
                    disaster_projects_2022.append({
                        'name': line,
                        'start_date': start_date
                    })

# Find matching funding
total_funding = 0
matched = []

for proj in disaster_projects_2022:
    proj_name = proj['name'].lower()
    
    # Try exact match
    if proj_name in funding_lookup:
        amount = funding_lookup[proj_name]
        total_funding += amount
        matched.append({"project": proj['name'], "amount": amount, "start_date": proj['start_date']})
    else:
        # Try fuzzy match
        for funding_name, amount in funding_lookup.items():
            if (proj_name in funding_name or funding_name in proj_name):
                total_funding += amount
                matched.append({"project": proj['name'], "funding_name": funding_name, "amount": amount, "start_date": proj['start_date']})
                break

final_result = json.dumps({
    "total_funding": total_funding,
    "matched_projects": matched,
    "total_disaster_projects_2022": len(disaster_projects_2022)
})

print('__RESULT__:')
print(final_result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
