code = """import json
import re

# Load data from stored variables
funding_data = locals()["var_functions.query_db:0"]
civic_docs_data = locals()["var_functions.query_db:4"]

# Handle file paths if needed
if isinstance(funding_data, str):
    with open(funding_data) as f:
        funding_data = json.load(f)
if isinstance(civic_docs_data, str):
    with open(civic_docs_data) as f:
        civic_docs_data = json.load(f)

print(f"Loaded {len(funding_data)} funding records and {len(civic_docs_data)} civic documents")

# Step 1: Extract projects from civic documents with emergency/FEMA context
projects_from_docs = []

for doc in civic_docs_data:
    text = doc['text']
    
    # Split into project sections - look for headings that are project names
    # Common patterns: lines that are mostly uppercase or Title Case, followed by status updates
    lines = text.split('\n')
    
    current_project = None
    current_status = 'unknown'
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Look for project names (typically not bullet points, not too short)
        if (len(line) > 15 and 
            not line.startswith('(') and 
            not line.startswith('•') and
            not line.startswith('·') and
            not line.startswith('cid:') and
            'Project' not in line and
            'COMM' not in line[:4] and
            'CAPITAL' not in line.upper() and
            'DISASTER' not in line.upper() and
            'STATUS' not in line.upper()):
            
            # Check if next lines contain status indicators
            next_lines = '\n'.join(lines[i:i+20]).lower()
            if 'updates:' in next_lines or 'schedule:' in next_lines:
                # This is likely a project name
                if current_project:
                    projects_from_docs.append({
                        'Project_Name': current_project,
                        'status': current_status,
                        'source_doc': doc['filename']
                    })
                
                current_project = line
                current_status = 'unknown'
        
        # Extract status from content
        line_lower = line.lower()
        if current_project:
            if 'complete design:' in line_lower or 'final design:' in line_lower:
                current_status = 'design'
            elif 'under construction' in line_lower or 'begin construction' in line_lower:
                current_status = 'construction'
            elif 'construction was completed' in line_lower or 'notice of completion' in line_lower:
                current_status = 'completed'
            elif 'not started' in line_lower:
                current_status = 'not started'
    
    # Add last project
    if current_project:
        projects_from_docs.append({
            'Project_Name': current_project,
            'status': current_status,
            'source_doc': doc['filename']
        })

print(f"\nExtracted {len(projects_from_docs)} projects from civic docs")

# Step 2: Get all emergency/FEMA projects from funding data
emergency_fema_projects = []
for record in funding_data:
    project_name = record['Project_Name']
    if 'emergency' in project_name.lower() or 'fema' in project_name.lower():
        emergency_fema_projects.append(record)

print(f"Found {len(emergency_fema_projects)} emergency/FEMA projects in funding data")

# Step 3: Match funding data with status information
final_results = []

for funding_proj in emergency_fema_projects:
    project_name = funding_proj['Project_Name']
    best_match = None
    best_score = 0
    
    # Find matching project in civic docs
    for doc_proj in projects_from_docs:
        doc_name = doc_proj['Project_Name']
        
        # Calculate similarity score
        score = 0
        funding_words = set(project_name.lower().replace('(', '').replace(')', '').split())
        doc_words = set(doc_name.lower().replace('(', '').replace(')', '').split())
        
        # Count matching words (excluding common words)
        common_words = {'project', 'repairs', 'repair', 'improvements', 'and', 'or', 'the', 'a', 'an', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'canyon', 'road', 'storm', 'drain'}
        matching_words = funding_words.intersection(doc_words) - common_words
        
        if len(matching_words) > best_score:
            best_score = len(matching_words)
            best_match = doc_proj
    
    # Determine status based on match
    status = 'unknown'
    if best_match and best_score >= 2:  # At least 2 matching keywords
        status = best_match['status']
    else:
        # Try simpler matching
        for doc_proj in projects_from_docs:
            doc_name = doc_proj['Project_Name'].lower()
            # Check if key parts of the name match
            if (project_name.split()[0].lower() in doc_name and 
                any(keyword in doc_name for keyword in ['canyon', 'road', 'drain', 'bridge', 'culvert', 'guardrail', 'siren'])):
                status = doc_proj['status']
                break
    
    final_results.append({
        'Project_Name': project_name,
        'Funding_Source': funding_proj['Funding_Source'],
        'Amount': funding_proj['Amount'],
        'Status': status
    })

# Sort by amount descending
final_results.sort(key=lambda x: int(x['Amount']), reverse=True)

print(f"\nFinal results: {len(final_results)} projects")
for i, result in enumerate(final_results):
    print(f"{i+1}. {result['Project_Name']}")
    print(f"   Funding: {result['Funding_Source']} - ${result['Amount']}")
    print(f"   Status: {result['Status']}")
    print()

result_json = json.dumps(final_results, indent=2)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:24': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_functions.execute_python:28': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
