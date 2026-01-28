code = """import json
import re

# Load the data properly
civic_docs_path = var_functions.query_db:10
if isinstance(civic_docs_path, str) and civic_docs_path.endswith('.json'):
    with open(civic_docs_path, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_docs_path

# Load funding data
funding_data = var_functions.query_db:2

print('=== DATA LOADED ===')
print(f'Loaded {len(civic_docs)} civic documents')
print(f'Loaded {len(funding_data)} funding records')

# Extract projects with simpler pattern matching
projects_from_docs = []
emergency_fema_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Check if document mentions emergency or FEMA
    has_emergency = 'emergency' in text.lower()
    has_fema = 'fema' in text.lower()
    
    if has_emergency or has_fema:
        # Split text into lines to find project names
        lines = text.split('\n')
        project_candidates = []
        
        for i, line in enumerate(lines):
            line = line.strip()
            # Look for lines that look like project names (uppercase, not empty, not dates)
            if (len(line) > 10 and len(line) < 150 and 
                (line[0].isupper() or line.isupper()) and 
                not line.startswith('Page') and
                not line.startswith('Agenda') and
                'cid:' not in line.lower()):
                # Check if next line has updates or status
                if i + 1 < len(lines):
                    next_line = lines[i+1].lower()
                    if 'updates' in next_line or 'status' in next_line:
                        project_candidates.append(line)
        
        # Add unique project candidates
        for proj in set(project_candidates):
            if proj:
                # Determine status
                status = 'not started'
                if 'design' in text.lower() and proj.lower() in text.lower():
                    status = 'design'
                if 'construction' in text.lower() or 'under construction' in text.lower():
                    if proj.lower() in text.lower():
                        status = 'construction'
                if 'completed' in text.lower():
                    if proj.lower() in text.lower():
                        status = 'completed'
                
                # Determine topics
                topics = []
                if 'fema' in text.lower():
                    topics.append('FEMA')
                if 'emergency' in text.lower():
                    topics.append('emergency')
                if 'fire' in text.lower():
                    topics.append('fire')
                if 'warning' in text.lower():
                    topics.append('emergency warning')
                if 'storm drain' in text.lower():
                    topics.append('storm drain')
                if 'drainage' in text.lower():
                    topics.append('drainage')
                
                projects_from_docs.append({
                    'Project_Name': proj,
                    'topics': topics,
                    'status': status,
                    'source': 'civic_doc'
                })
                
                # Filter for emergency/FEMA specific projects
                if has_fema or ('emergency' in text.lower() and ('warning' in text.lower() or 'siren' in text.lower())):
                    emergency_fema_projects.append(proj)

print(f'Found {len(projects_from_docs)} projects in civic docs')
print(f'Found {len(emergency_fema_projects)} emergency/FEMA focused projects')
print(f'Emergency/FEMA project names: {list(set(emergency_fema_projects))[:10]}')

# Process funding data to match with projects
funding_matches = []

for record in funding_data:
    proj_name = record.get('Project_Name', '')
    funding_source = record.get('Funding_Source', '')
    amount = int(record.get('Amount', 0))
    
    # Check if this is a FEMA/emergency project from name
    is_fema = 'fema' in proj_name.lower()
    is_emergency = 'emergency' in proj_name.lower()
    
    if is_fema or is_emergency:
        funding_matches.append({
            'Project_Name': proj_name,
            'Funding_Source': funding_source,
            'Amount': amount,
            'topics': ['FEMA'] if is_fema else ['emergency'],
            'status': 'unknown'
        })

print(f'Found {len(funding_matches)} funding records for emergency/FEMA projects')

# Match projects between funding and civic docs
matched_projects = []

for fund_proj in funding_matches:
    fund_name = fund_proj['Project_Name'].lower()
    
    # Find matching project in civic docs
    matching_doc_proj = None
    for doc_proj in projects_from_docs:
        doc_name = doc_proj['Project_Name'].lower()
        
        # Simple matching: check if one name contains the other
        if (fund_name in doc_name or doc_name in fund_name or
            any(word in doc_name for word in fund_name.split() if len(word) > 5)):
            matching_doc_proj = doc_proj
            break
    
    if matching_doc_proj:
        matched_projects.append({
            'Project_Name': fund_proj['Project_Name'],
            'Funding_Source': fund_proj['Funding_Source'],
            'Amount': fund_proj['Amount'],
            'topics': list(set(fund_proj['topics'] + matching_doc_proj['topics'])),
            'status': matching_doc_proj['status']
        })
    else:
        # Use funding data only
        matched_projects.append(fund_proj)

print(f'Matched {len(matched_projects)} projects with funding information')

# Format the output
result_lines = []
for proj in matched_projects[:20]:  # Limit to prevent too large output
    result_lines.append(f"Project: {proj['Project_Name']}")
    result_lines.append(f"  Funding Source: {proj['Funding_Source']}")
    result_lines.append(f"  Amount: ${proj['Amount']:,}")
    result_lines.append(f"  Status: {proj['status']}")
    result_lines.append(f"  Topics: {', '.join(proj['topics']) if proj['topics'] else 'N/A'}")
    result_lines.append("")

output = '\n'.join(result_lines)
print('__RESULT__:')
print(output)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
