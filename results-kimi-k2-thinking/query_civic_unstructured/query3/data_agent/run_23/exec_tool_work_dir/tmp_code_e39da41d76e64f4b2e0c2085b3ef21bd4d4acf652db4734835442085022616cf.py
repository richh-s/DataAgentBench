code = """import json
import re

# Get the funding data
funding_results = var_functions.query_db:24

# Get civic documents data (it's stored in a string path)
civic_docs_path = var_functions.query_db:4

# Load the civic documents
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

print(f"Found {len(funding_results)} FEMA-related funding records")
print(f"Found {len(civic_docs)} civic documents to search for statuses")

# Extract project names from funding results
fema_project_names = [record['Project_Name'] for record in funding_results]
print(f"\nFEMA project names: {fema_project_names[:5]}...")  # Show first 5

# Let's look for project patterns in the civic documents
# Common patterns: Project_Name followed by Updates/Status
project_info = {}

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for project sections
    # Pattern: Project name followed by updates/status
    lines = text.split('\n')
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Look for project names (usually bold or title case)
        # Skip empty lines and common headers
        if line and len(line) > 10 and not line.startswith('(') and not any(header in line for header in ['Item', 'To:', 'Prepared by:', 'Approved by:', 'Date prepared:', 'Meeting date:', 'Subject:', 'RECOMMENDED ACTION:', 'DISCUSSION:', 'Capital Improvement Projects', 'Disaster Recovery Projects']):
            
            # Check if this looks like a project name (doesn't end with period, not a bullet)
            if not line.endswith('.') and not line.startswith('•') and not line.startswith('-') and not line.startswith('□'):
                # Check if next few lines contain Updates or Status
                next_lines = '\n'.join(lines[i+1:i+4])
                if 'Updates:' in next_lines or 'Status:' in next_lines or 'Project Schedule' in next_lines:
                    current_project = line
                    
                    # Extract status from following lines
                    status = "Unknown"
                    if 'Project is currently under construction' in next_lines:
                        status = "Construction"
                    elif 'Construction was completed' in next_lines or 'Complete Construction' in next_lines:
                        status = "Completed"
                    elif 'Complete Design:' in next_lines or 'Staff is working' in next_lines:
                        status = "Design"
                    elif 'Advertise:' in next_lines or 'out to bid' in next_lines.lower():
                        status = "Bidding"
                    elif 'not started' in next_lines.lower() or 'identified' in next_lines.lower():
                        status = "Not Started"
                    elif 'Awaiting' in next_lines:
                        status = "Awaiting Approval"
                    
                    if current_project:
                        project_info[current_project] = status

print(f"\nExtracted {len(project_info)} project statuses from documents")
print(f"Sample project statuses: {list(project_info.items())[:5]}")

# Try to match funding records with extracted statuses
matched_projects = []

for funding_record in funding_results:
    proj_name = funding_record['Project_Name']
    matched = False
    
    # Direct match
    if proj_name in project_info:
        status = project_info[proj_name]
        matched = True
    else:
        # Try partial match (base name without suffix)
        base_name = proj_name.replace(' (FEMA Project)', '').replace(' (CalOES Project)', '').replace(' (FEMA/CalOES Project)', '').replace(' (CalJPIA Project)', '')
        
        for extracted_name, status in project_info.items():
            if base_name.lower() in extracted_name.lower() or extracted_name.lower() in base_name.lower():
                matched_projects.append({
                    'Project_Name': proj_name,
                    'Funding_Source': funding_record['Funding_Source'],
                    'Amount': funding_record['Amount'],
                    'Status': status,
                    'Extracted_Name': extracted_name
                })
                matched = True
                break
    
    if not matched:
        # Assign unknown status if no match found
        matched_projects.append({
            'Project_Name': proj_name,
            'Funding_Source': funding_record['Funding_Source'],
            'Amount': funding_record['Amount'],
            'Status': 'Unknown'
        })

print(f"\nMatched {len(matched_projects)} projects with funding and status info")
print("\nFirst 10 matched projects:")
for proj in matched_projects[:10]:
    print(f"  {proj['Project_Name'][:60]}... - ${proj['Amount']} - {proj['Status']}")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:20': {'mongo_type': "<class 'str'>", 'funding_type': "<class 'str'>", 'mongo_is_list': False, 'funding_is_list': False}, 'var_functions.query_db:24': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
