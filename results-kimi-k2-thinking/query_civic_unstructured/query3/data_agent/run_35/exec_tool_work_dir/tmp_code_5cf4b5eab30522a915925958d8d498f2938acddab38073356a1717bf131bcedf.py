code = """import json
import re

# Get the MongoDB documents that contain emergency/FEMA references
civic_docs = var_functions.query_db_6

# Get the funding data
funding_data = var_functions.query_db_4

print("Documents:", len(civic_docs))
print("Funding records:", len(funding_data))

# Create funding map
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

# Extract projects from documents
all_projects = []

for doc in civic_docs:
    text = doc['text']
    filename = doc['filename']
    
    # Find sections that mention projects with emergency/FEMA
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Look for project names (title case or uppercase, not too short)
        if len(line) > 15 and (line.istitle() or line.isupper()):
            if 'PROJECT' not in line and 'COMMISSION' not in line and 'MEETING' not in line:
                # Check if it contains project-related keywords
                lower_line = line.lower()
                if any(word in lower_line for word in ['project', 'repairs', 'improvements', 'road', 'drainage', 'sirens', 'warning', 'canyon', 'bridge']):
                    
                    # Look for status in nearby lines
                    status = None
                    for j in range(max(0, i-5), min(len(lines), i+10)):
                        check_line = lines[j].lower()
                        if 'design' in check_line or 'finalizing' in check_line:
                            status = 'design'
                            break
                        elif 'construction' in check_line or 'under construction' in check_line:
                            status = 'construction'
                            break
                        elif 'completed' in check_line or 'completion' in check_line:
                            status = 'completed'
                            break
                        elif 'not started' in check_line or 'waiting for' in check_line:
                            status = 'not started'
                            break
                    
                    if status:
                        clean_name = re.sub(r'\s*\([^)]*\)\s*$', '', line).strip()
                        all_projects.append({
                            'Project_Name': line,
                            'Clean_Name': clean_name,
                            'Status': status
                        })

# Match with funding data
results = []
seen_projects = set()

for proj in all_projects:
    clean_name = proj['Clean_Name']
    matched = False
    
    # Direct match
    if clean_name in funding_map:
        for funding in funding_map[clean_name]:
            project_key = clean_name + '_' + proj['Status']
            if project_key not in seen_projects:
                seen_projects.add(project_key)
                results.append({
                    'Project_Name': proj['Project_Name'],
                    'Status': proj['Status'],
                    'Funding_Source': funding['Funding_Source'],
                    'Amount': funding['Amount'],
                    'Funding_Details': funding['Full_Project_Name']
                })
            matched = True
    
    # Partial match if not already matched
    if not matched:
        for funded_name in funding_map:
            if clean_name.lower() in funded_name.lower() or funded_name.lower() in clean_name.lower():
                for funding in funding_map[funded_name]:
                    project_key = clean_name + '_' + proj['Status']
                    if project_key not in seen_projects:
                        seen_projects.add(project_key)
                        results.append({
                            'Project_Name': proj['Project_Name'],
                            'Status': proj['Status'],
                            'Funding_Source': funding['Funding_Source'],
                            'Amount': funding['Amount'] 
                        })
                break

print("Results:", len(results))

# Format output
output = []
for r in results:
    output.append({
        'Project_Name': r['Project_Name'],
        'Status': r['Status'],
        'Funding_Source': r['Funding_Source'],
        'Amount': r['Amount']
    })

print("__RESULT__:")
print(json.dumps(output, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': [{'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '34', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Funding_Source': 'Educational Sponsorship', 'Amount': '18000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '59', 'Project_Name': 'Malibu Road Slope Repairs (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '37000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}, {'Funding_ID': '92', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Funding_Source': 'International Organization Grant', 'Amount': '32000'}, {'Funding_ID': '99', 'Project_Name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Funding_Source': 'Local Business Support', 'Amount': '77000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
