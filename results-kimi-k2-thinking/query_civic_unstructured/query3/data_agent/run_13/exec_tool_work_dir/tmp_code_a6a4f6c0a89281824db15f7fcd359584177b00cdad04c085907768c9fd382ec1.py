code = """import json
import re

# Load the data again
civic_docs_path = locals()['var_functions.query_db:2']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

funding_path = locals()['var_functions.query_db:5']  
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Step 1: Filter funding for emergency/FEMA projects
emergency_funding = []
for rec in funding_data:
    project_name = rec.get('Project_Name', '').lower()
    if 'emergency' in project_name or 'fema' in project_name:
        emergency_funding.append(rec)

print("Emergency/FEMA funding records:", len(emergency_funding))

# Step 2: Parse civic documents to extract project details
projects_from_docs = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    current_project = None
    in_project_section = False
    
    # Look for project sections
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
            
        # Look for project names (typically capitalized, sometimes with special characters)
        # Projects often have distinctive patterns
        
        # Check if this looks like a project name
        if (line.isupper() or 
            (len(line) > 10 and not line.startswith(('(', '•', '-', '◦', '◊', '◄', '▪', '■', '□'))) or
            line.endswith('Project') or
            line.endswith('Improvements') or
            line.endswith('Repairs')):
            
            # Check if this is a project section header
            if ('Updates:' in lines[i+1:i+4] or 
                'Project Schedule:' in lines[i+1:i+4] or
                'Project Description:' in lines[i+1:i+4]):
                
                current_project = line
                
                # Determine status based on nearby keywords
                status = None
                project_type = None
                
                # Look ahead for status indicators
                next_lines = '\n'.join(lines[i:i+10])
                next_text_lower = next_lines.lower()
                
                # Determine status (design, completed, not started, construction)
                if 'complete design' in next_text_lower or 'finalize design' in next_text_lower:
                    status = 'design' 
                elif 'under construction' in next_text_lower or 'construction was completed' in next_text_lower:
                    if 'construction was completed' in next_text_lower:
                        status = 'completed'
                    else:
                        status = 'construction'
                elif 'not started' in next_text_lower or 'identified' in next_text_lower:
                    status = 'not started'
                elif 'awaiting' in next_text_lower or 'pending' in next_text_lower:
                    status = 'design'
                    
                # Determine type based on context
                if any(x in line.lower() for x in ['drainage', 'storm drain', 'culvert', 'bridge', 'road', 'street', 'park', 'highway']):
                    if 'fema' in line.lower() or 'disaster' in line.lower():
                        project_type = 'disaster'
                    else:
                        project_type = 'capital'
                
                # Check if this is emergency/FEMA related
                if 'emergency' in line.lower() or 'fema' in line.lower():
                    projects_from_docs.append({
                        'Project_Name': current_project,
                        'status': status,
                        'type': project_type,
                        'topic': 'emergency, FEMA, ' + line.lower().replace(current_project.lower(), ''),
                        'source_doc': doc.get('filename', '')
                    })

print("Projects extracted from docs:", len(projects_from_docs))
for proj in projects_from_docs[:10]:
    print(proj)

# Step 3: Create a mapping of project names to find matches
project_name_map = {}
for rec in emergency_funding:
    name = rec['Project_Name']
    # Create variations for matching (base name without suffixes)
    base_name = name
    for suffix in [' (FEMA Project)', ' (CalJPIA Project)', ' (CalOES Project)', 
                   ' (FEMA/CalOES Project)', ' (CalJPIA/FEMA Project)']:
        if name.endswith(suffix):
            base_name = name.replace(suffix, '')
            break
    
    if base_name not in project_name_map:
        project_name_map[base_name] = []
    project_name_map[base_name].append(rec)

print("\nProject names in funding map:", len(project_name_map))

# Step 4: Try to match projects from docs with funding
matched_projects = []

# For each project in our funding data, try to find status/details
for base_name, funding_records in project_name_map.items():
    found_match = False
    
    # Check if we have this project in our parsed docs
    for proj in projects_from_docs:
        doc_name = proj['Project_Name'].lower()
        funding_name_lower = base_name.lower()
        
        # Check for direct match or partial match
        if (funding_name_lower in doc_name or 
            doc_name in funding_name_lower or
            'emergency' in doc_name):
            
            # Found a match, combine the info
            for funding_rec in funding_records:
                matched_projects.append({
                    'Project_Name': funding_rec['Project_Name'],
                    'Funding_Source': funding_rec['Funding_Source'],
                    'Amount': funding_rec['Amount'],
                    'Status': proj['status'],
                    'Type': proj['type'],
                    'Topic': proj['topic']
                })
            found_match = True
            break
    
    # If no document match, still include the funding record
    if not found_match:
        for funding_rec in funding_records:
            matched_projects.append({
                'Project_Name': funding_rec['Project_Name'],
                'Funding_Source': funding_rec['Funding_Source'],
                'Amount': funding_rec['Amount'],
                'Status': 'Unknown',
                'Type': 'disaster',  # Likely disaster if FEMA-related
                'Topic': 'emergency, FEMA'
            })

print("\nTotal matched projects:", len(matched_projects))

# Output the results
import json as js
print('__RESULT__:')
print(js.dumps(matched_projects))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:18': {'relevant_funding': [{'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'civic_docs_count': 5}}

exec(code, env_args)
