code = """import json
import re

# Load the civic documents
civic_docs_path = var_functions.query_db:0
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Load the funding data
funding_data = var_functions.query_db:5  # Already filtered for FEMA/emergency

# Parse civic documents to extract project information
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for project sections
    # Projects often appear with patterns like:
    # Project Name
    # (cid:190) Updates:
    # (cid:190) Project Schedule:
    # etc.
    
    # Split by common project delimiters
    sections = re.split(r'\n\s*\n', text)
    
    for section in sections:
        section = section.strip()
        if not section:
            continue
            
        # Look for project indicators
        lines = section.split('\n')
        project_name = None
        project_status = None
        project_type = None
        project_topic = []
        
        # Check if section contains project-like content
        if len(lines) > 2:
            # First line might be project name
            candidate_name = lines[0].strip()
            
            # Check if it's a likely project name (not a header)
            if (len(candidate_name) < 150 and 
                not candidate_name.startswith('Public Works') and
                not candidate_name.startswith('Agenda') and
                not candidate_name.startswith('To:') and
                not candidate_name.startswith('Prepared') and
                not candidate_name.startswith('Approved') and
                not candidate_name.startswith('Date') and
                not candidate_name.startswith('Meeting') and
                not candidate_name.startswith('Subject') and
                not candidate_name.startswith('RECOMMENDED') and
                not candidate_name.startswith('DISCUSSION') and
                not candidate_name.startswith('Capital Improvement') and
                not candidate_name.startswith('Page') and
                not candidate_name.startswith('----')):
                
                project_name = candidate_name
                
                # Determine status based on keywords
                if 'Updates:' in section:
                    if 'not started' in section.lower() or 'identified' in section.lower():
                        project_status = 'not started'
                    elif 'completed' in section.lower() or 'construction was completed' in section.lower():
                        project_status = 'completed'
                    elif 'design' in section.lower() or 'construction' in section.lower() or 'under construction' in section.lower():
                        # Check if it's in design phase
                        if 'Complete Design:' in section or 'design' in section.lower():
                            if 'construction' not in section.lower() or 'under construction' not in section.lower():
                                project_status = 'design'
                            else:
                                project_status = 'in progress'
                        else:
                            project_status = 'in progress'
                
                # Determine type based on content
                if 'FEMA' in section or 'disaster' in section.lower() or 'recovery' in section.lower():
                    project_type = 'disaster'
                elif 'capital' in section.lower() or 'improvement' in section.lower():
                    project_type = 'capital'
                elif any(word in section.lower() for word in ['park', 'road', 'drainage', 'bridge', 'highway']):
                    project_type = 'capital'
                
                # Extract topics
                if 'FEMA' in project_name or 'FEMA' in section:
                    project_topic.append('FEMA')
                if 'emergency' in section.lower() or 'warning' in section.lower():
                    project_topic.append('emergency warning')
                if 'drainage' in section.lower():
                    project_topic.append('drainage')
                if 'park' in section.lower():
                    project_topic.append('park')
                if 'road' in section.lower():
                    project_topic.append('road')
                if 'fire' in section.lower():
                    project_topic.append('fire')
                
                # Only add if we found meaningful data
                if project_name and (project_status or project_type or project_topic):
                    projects.append({
                        'Project_Name': project_name,
                        'Status': project_status,
                        'Type': project_type,
                        'Topic': ', '.join(project_topic) if project_topic else ''
                    })

# Now match with funding data
results = []

for funding in funding_data:
    fund_project_name = funding['Project_Name']
    funding_source = funding['Funding_Source']
    amount = funding['Amount']
    
    # Find matching project info from civic docs
    matched = False
    for project in projects:
        proj_name = project['Project_Name']
        
        # Check for direct match or partial match
        if (proj_name.lower() in fund_project_name.lower() or 
            fund_project_name.lower() in proj_name.lower()):
            results.append({
                'Project_Name': fund_project_name,
                'Funding_Source': funding_source,
                'Amount': amount,
                'Status': project['Status'],
                'Type': project['Type'],
                'Topic': project['Topic']
            })
            matched = True
            break
    
    # If no match found in extracted projects, add with available data
    if not matched:
        # Try to infer from project name
        topic = []
        if 'FEMA' in fund_project_name:
            topic.append('FEMA')
        if 'emergency' in fund_project_name.lower():
            topic.append('emergency warning')
        
        p_type = 'disaster' if 'FEMA' in fund_project_name else None
        
        results.append({
            'Project_Name': fund_project_name,
            'Funding_Source': funding_source,
            'Amount': amount,
            'Status': None,
            'Type': p_type,
            'Topic': ', '.join(topic)
        })

# Output results
print('__RESULT__:')
print(json.dumps(results, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
