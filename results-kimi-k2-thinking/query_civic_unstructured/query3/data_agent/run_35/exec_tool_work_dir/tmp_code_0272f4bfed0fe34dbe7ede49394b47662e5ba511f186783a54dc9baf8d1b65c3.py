code = """import json
import re

# Get the MongoDB documents that contain emergency/FEMA references
civic_docs = var_functions.query_db_6

# Get the funding data
funding_data = var_functions.query_db_4

print(f"Found {len(civic_docs)} civic documents")
print(f"Found {len(funding_data)} funding records")

# Process funding data to map project names
funding_map = {}
for record in funding_data:
    project_name = record['Project_Name']
    clean_name = re.sub(r'\s*\([^)]*\)\s*$', '', project_name).strip()
    if clean_name not in funding_map:
        funding_map[clean_name] = []
    funding_map[clean_name].append({
        'Funding_ID': record['Funding_ID'],
        'Funding_Source': record['Funding_Source'],
        'Amount': int(record['Amount']),
        'Full_Project_Name': project_name
    })

print(f"Mapped {len(funding_map)} unique project names in funding data")

# Extract project information from civic documents
project_info = []

for doc in civic_docs:
    text = doc['text']
    filename = doc['filename']
    
    # Look for project patterns in the text
    # Common patterns: project names followed by descriptions
    lines = text.split('\n')
    
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Look for project names (typically title case or uppercase at start of lines)
        if (len(line) > 10 and 
            (line.istitle() or line.isupper()) and 
            not line.startswith('(') and 
            not line.startswith('Page') and
            'PROJECT' not in line and
            'COMMISSION' not in line and
            'MEETING' not in line):
            
            # Check if this looks like a project name
            if any(keyword in line.lower() for keyword in ['project', 'repairs', 'improvements', 'road', 'avenue', 'canyon', 'drainage', 'sirens', 'warning']):
                current_project = line.strip()
                continue
        
        # If we have a current project, look for status and other info
        if current_project:
            # Look for status indicators
            status = None
            if 'design' in line.lower() or 'finalizing' in line.lower():
                status = 'design'
            elif 'construction' in line.lower() or 'under construction' in line.lower():
                status = 'construction'
            elif 'completed' in line.lower() or 'completion' in line.lower():
                status = 'completed'
            elif 'not started' in line.lower() or 'waiting for' in line.lower():
                status = 'not started'
            
            if status:
                clean_name = re.sub(r'\s*\([^)]*\)\s*$', '', current_project).strip()
                project_info.append({
                    'Project_Name': current_project,
                    'Clean_Name': clean_name,
                    'Status': status,
                    'Source_File': filename
                })
                current_project = None

print(f"Extracted {len(project_info)} project status entries")

# Match projects with funding data
matched_projects = []

for proj in project_info:
    clean_name = proj['Clean_Name']
    
    # Direct match
    if clean_name in funding_map:
        for funding in funding_map[clean_name]:
            matched_projects.append({
                'Project_Name': proj['Project_Name'],
                'Status': proj['Status'],
                'Funding_Source': funding['Funding_Source'],
                'Amount': funding['Amount'],
                'Full_Funding_Name': funding['Full_Project_Name']
            })
    else:
        # Try fuzzy matching
        for funded_name, funding_list in funding_map.items():
            if (clean_name.lower() in funded_name.lower() or 
                funded_name.lower() in clean_name.lower()):
                for funding in funding_list:
                    matched_projects.append({
                        'Project_Name': proj['Project_Name'],
                        'Status': proj['Status'],
                        'Funding_Source': funding['Funding_Source'],
                        'Amount': funding['Amount'],
                        'Full_Funding_Name': funding['Full_Project_Name']
                    })
                break

print(f"Matched {len(matched_projects)} projects with funding data")

# Aggregate results by project
project_summary = {}
for proj in matched_projects:
    name = proj['Project_Name']
    if name not in project_summary:
        project_summary[name] = {
            'Status': proj['Status'],
            'Funding_Sources': set(),
            'Total_Amount': 0,
            'Funding_Records': []
        }
    project_summary[name]['Funding_Sources'].add(proj['Funding_Source'])
    project_summary[name]['Total_Amount'] += proj['Amount']
    project_summary[name]['Funding_Records'].append(proj['Full_Funding_Name'])

# Convert sets to lists for JSON serialization
for name in project_summary:
    project_summary[name]['Funding_Sources'] = list(project_summary[name]['Funding_Sources'])

print("__RESULT__:")
print(json.dumps(project_summary, indent=2, default=str))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': [{'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '34', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Funding_Source': 'Educational Sponsorship', 'Amount': '18000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '59', 'Project_Name': 'Malibu Road Slope Repairs (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '37000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}, {'Funding_ID': '92', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Funding_Source': 'International Organization Grant', 'Amount': '32000'}, {'Funding_ID': '99', 'Project_Name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Funding_Source': 'Local Business Support', 'Amount': '77000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
