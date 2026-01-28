code = """import json
import re
import os

# Load the data files
civic_docs_path = 'results/query_db_5.json'
funding_path = 'results/query_db_6.json'

# Load civic documents
civic_docs_file = open(civic_docs_path, 'r')
civic_docs_data = json.load(civic_docs_file)
civic_docs_file.close()

# Load funding records
funding_file = open(funding_path, 'r')
funding_data = json.load(funding_file)
funding_file.close()

print("Loaded", len(civic_docs_data), "civic documents")
print("Loaded", len(funding_data), "funding records")

# First, identify FEMA/emergency projects from funding data
fema_keywords = ['FEMA', 'EMERGENCY']
fema_funding_records = []

for record in funding_data:
    project_name = record['Project_Name']
    if any(keyword in project_name.upper() for keyword in fema_keywords):
        fema_funding_records.append(record)

print("\nFound", len(fema_funding_records), "FEMA/emergency funding records")

# Get unique project names from funding data
fema_project_names = [r['Project_Name'] for r in fema_funding_records]
print("Project names:", fema_project_names[:10])

# Find status information from civic documents
projects_with_status = []

for doc in civic_docs_data:
    text = doc['text']
    
    # Look for project sections in the text
    # Standard format appears to be:
    # Project Name
    # (cid:190) Updates: ...
    # (cid:190) Project Schedule: ...
    
    # Find project names and their status
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Look for project names (typically on their own line, title case)
        if len(line) > 10 and not line.startswith('(') and not line.startswith('Page') and not line.startswith('Agenda'):
            # Check if this is a project name we're tracking
            for project_name in fema_project_names:
                # Match if the line is similar to project name (ignore case and extra suffixes)
                base_name = project_name.split(' (')[0]  # Remove parenthetical suffixes
                if base_name.upper() in line.upper() or line.upper() in base_name.upper():
                    # Found a project, now look for its status
                    status = "Unknown"
                    
                    # Look ahead for status indicators
                    for j in range(i+1, min(i+10, len(lines))):
                        next_line = lines[j].strip()
                        
                        # Check for status keywords
                        if 'Advertise:' in next_line or 'Complete Design:' in next_line:
                            status = "Design"
                            break
                        elif 'Begin construction:' in next_line or 'Complete Construction:' in next_line or 'Project is currently under construction' in next_line:
                            status = "Construction"
                            break
                        elif 'Construction was completed' in next_line or 'completed' in next_line.lower():
                            status = "Completed"
                            break
                        elif 'not started' in next_line.lower() or 'preliminary design' in next_line.lower():
                            status = "Not Started"
                            break
                    
                    projects_with_status.append({
                        'Project_Name': project_name,
                        'Status': status,
                        'Status_Source': line
                    })

print("\nFound status info for", len(projects_with_status), "projects")

# Create a dictionary to store final results
final_results = []

# For each FEMA/emergency project in funding data
for funding_rec in fema_funding_records:
    project_name = funding_rec['Project_Name']
    
    # Find matching status record
    status = "Unknown"
    for ps in projects_with_status:
        if ps['Project_Name'] == project_name:
            status = ps['Status']
            break
    
    final_results.append({
        'Project_Name': project_name,
        'Funding_Source': funding_rec['Funding_Source'],
        'Amount': int(funding_rec['Amount']),
        'Status': status
    })

print("\nFinal results compiled for", len(final_results), "projects")
for r in final_results[:10]:
    print(f"- {r['Project_Name']}: ${r['Amount']} ({r['Funding_Source']}) - Status: {r['Status']}")

# Prepare JSON output
output = json.dumps(final_results, indent=2)

__RESULT__ = output"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
