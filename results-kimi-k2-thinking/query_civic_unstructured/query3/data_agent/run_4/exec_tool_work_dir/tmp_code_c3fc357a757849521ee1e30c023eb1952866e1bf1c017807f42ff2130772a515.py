code = """import json
import re

# Read the full MongoDB results
with open('/var_functions.query_db:9', 'r') as f:
    mongo_docs = json.load(f)

# Read the funding data  
with open('/var_functions.query_db:10', 'r') as f:
    funding_data = json.load(f)

# Create funding lookup dictionary
funding_lookup = {}
for record in funding_data:
    funding_lookup[record['Project_Name']] = {
        'Funding_Source': record['Funding_Source'],
        'Amount': int(record['Amount'])
    }

# Extract projects mentioning emergency or FEMA
results = []

for doc in mongo_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_section = None
    current_status = None
    
    for line in lines:
        line = line.strip()
        
        # Skip empty lines and headers
        if not line or any(header in line for header in ['Public Works', 'Commission', 'Agenda Item', 'Page', 'To:', 'Prepared by:', 'Approved by:', 'Date prepared:', 'Meeting date:', 'Subject:', 'RECOMMENDED ACTION:', 'DISCUSSION:']):
            continue
            
        # Identify project sections and statuses
        if 'Design' in line and 'Capital' in line:
            current_status = 'design'
            continue
        elif 'Construction' in line and 'Capital' in line:
            current_status = 'construction'
            continue
        elif 'Not Started' in line and 'Capital' in line:
            current_status = 'not started'
            continue
        elif 'Design' in line and 'Disaster' in line:
            current_status = 'design'
            continue
        elif 'Construction' in line and 'Disaster' in line:
            current_status = 'construction'  
            continue
        elif 'Not Started' in line and 'Disaster' in line:
            current_status = 'not started'
            continue
            
        # Look for project names (lines that don't start with special characters and contain project keywords)
        if (line and not line.startswith('(') and not line.startswith('•') and not line.startswith('-') and 
            not line.startswith('□') and 'Updates:' not in line and 'Schedule:' not in line and 
            'Project Description:' not in line and 'Project Schedule:' not in line and
            any(keyword in line for keyword in ['Project', 'Improvements', 'Repair', 'Maintenance', 'Drainage', 
                                               'Road', 'Bridge', 'Culvert', 'Park', 'Sirens', 'Signs', 'System']) and
            len(line) < 150):
            
            project_name = line
            
            # Check if this project is related to emergency or FEMA
            if 'emergency' in project_name.lower() or 'fema' in project_name.lower():
                # Determine project type
                if any(fema_type in project_name for fema_type in ['(FEMA Project)', '(CalOES Project)', '(FEMA/CalOES Project)']):
                    project_type = 'disaster'
                else:
                    project_type = 'capital'
                    
                # Find funding info
                funding_info = funding_lookup.get(project_name)
                
                if funding_info:
                    results.append({
                        'Project_Name': project_name,
                        'Funding_Source': funding_info['Funding_Source'],
                        'Amount': funding_info['Amount'],
                        'Status': current_status,
                        'Type': project_type
                    })

# Sort results by Amount descending
results.sort(key=lambda x: x['Amount'], reverse=True)

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
