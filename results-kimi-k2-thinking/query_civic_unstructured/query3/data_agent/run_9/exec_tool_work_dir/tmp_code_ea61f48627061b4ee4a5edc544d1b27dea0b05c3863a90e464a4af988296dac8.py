code = """import json
import re

# Read the stored query results
civic_docs_raw = var_functions.query_db_5
funding_raw = var_functions.query_db_6

# Parse JSON data
civic_docs = json.loads(civic_docs_raw)
funding = json.loads(funding_raw)

print("Loaded %d civic documents" % len(civic_docs))
print("Loaded %d funding records" % len(funding))

# Step 1: Filter funding records for FEMA/Emergency projects
fema_funding = []
for rec in funding:
    pname = rec['Project_Name'].upper()
    if 'FEMA' in pname or 'EMERGENCY' in pname:
        fema_funding.append({
            'Project_Name': rec['Project_Name'],
            'Funding_Source': rec['Funding_Source'],
            'Amount': int(rec['Amount']),
            'Status': 'Unknown'
        })

print("\nFound %d FEMA/emergency funding records" % len(fema_funding))

# Step 2: Extract project status information from civic documents
# Create a mapping of project base names to status
status_map = {}

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project = None
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Look for project name lines (not bullet points, not page numbers)
        if not line.startswith('(') and not line.startswith('Page') and not line.startswith('Agenda') and len(line) > 5:
            # Store as potential project name
            current_project = line
        
        # If we have a current project, look for status indicators
        if current_project:
            lower_line = line.lower()
            if 'complete design:' in lower_line or 'advertise:' in lower_line:
                status_map[current_project] = 'Design'
            elif 'under construction' in lower_line or 'begin construction' in lower_line:
                status_map[current_project] = 'Construction'
            elif 'construction was completed' in lower_line or 'completed' in lower_line:
                status_map[current_project] = 'Completed'
            elif 'not started' in lower_line:
                status_map[current_project] = 'Not Started'

# Step 3: Match funding records with status information
results = []
for project in fema_funding:
    project_name = project['Project_Name']
    base_name = project_name.split(' (')[0]
    
    # Look for status match
    status = 'Unknown'
    for doc_project, doc_status in status_map.items():
        if base_name.upper() in doc_project.upper() or doc_project.upper() in base_name.upper():
            status = doc_status
            break
    
    project['Status'] = status
    results.append(project)

# Step 4: Sort by amount descending
results.sort(key=lambda x: x['Amount'], reverse=True)

print("\nTop 15 FEMA/Emergency projects:")
for r in results[:15]:
    print("- %s: $%d (%s) [%s]" % (r['Project_Name'], r['Amount'], r['Funding_Source'], r['Status']))

# Prepare final output
__RESULT__ = json.dumps(results, indent=2)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
