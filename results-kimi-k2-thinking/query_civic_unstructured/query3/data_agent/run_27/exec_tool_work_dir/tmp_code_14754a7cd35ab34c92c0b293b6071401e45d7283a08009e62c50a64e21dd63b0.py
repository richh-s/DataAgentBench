code = """import json
import re

# Read civic documents data
civic_file = locals()['var_functions.query_db:10']
with open(civic_file, 'r') as f:
    civic_data = json.load(f)

# Extract project information from all civic documents
all_projects = []

for doc in civic_data:
    text = doc.get('text', '')
    
    # Split by project sections - look for patterns like project names followed by updates/status
    # Look for capital projects and disaster recovery projects
    
    # Find sections with project names
    lines = text.split('\n')
    current_project = None
    project_info = {}
    
    for line in lines:
        line = line.strip()
        
        # Look for project names (typically on their own line, title case)
        if line and not line.startswith('(') and not line.startswith('•') and not line.startswith('◦'):
            # Skip common headers
            skip_patterns = ['Capital Improvement Projects', 'Disaster Recovery Projects', 'RECOMMENDED ACTION:', 
                           'DISCUSSION:', 'To:', 'Prepared by:', 'Approved by:', 'Date prepared:', 'Meeting date:',
                           'Subject:', 'Page', 'Agenda Item', 'Public Works Commission', 'CITY OF', 'Malibu']
            
            if any(pattern in line for pattern in skip_patterns):
                continue
                
            # If line is likely a project name (not too short, not too long, contains project terms)
            project_indicators = ['Project', 'Improvements', 'Repairs', 'Replacement', 'Drainage', 'Road', 'Street',
                                'Siren', 'Warning', 'Culvert', 'Bridge', 'Guardrail', 'Resurfacing', 'Maintenance']
            
            if len(line) > 10 and len(line) < 150 and any(indicator.lower() in line.lower() for indicator in project_indicators):
                # Save previous project if exists
                if current_project and project_info:
                    all_projects.append({**project_info, 'Project_Name': current_project, 'source_doc': doc['filename']})
                    
                # Start new project
                current_project = line
                project_info = {'status': '', 'topic': '', 'type': ''}
        
        # Look for status information
        if current_project:
            status_patterns = [
                (r'Updates?\s*:\s*(.+?)(?:\n|$)', 'status'),
                (r'Project Schedule\s*:\s*(.+?)(?:\n|$)', 'status'),
                (r'(?:Completed|Complete|Construction was completed)', 'status', 'completed'),
                (r'(?:Design|Under Design|Complete Design)', 'status', 'design'),
                (r'(?:Not Started|Not Begun|Identified but not begun)', 'status', 'not started'),
                (r'(?:Under construction|Construction)', 'status', 'construction'),
                (r'(?:Advertise|Bids)', 'status', 'advertising')
            ]
            
            for pattern in status_patterns:
                if len(pattern) == 3:
                    if re.search(pattern[0], line, re.I):
                        project_info[pattern[1]] = pattern[2]
                else:
                    match = re.search(pattern[0], line, re.I)
                    if match:
                        project_info[pattern[1]] = match.group(1).strip()[:200]  # Limit length
    
    # Add last project
    if current_project and project_info:
        all_projects.append({**project_info, 'Project_Name': current_project, 'source_doc': doc['filename']})

# Filter projects related to FEMA/emergency
emergency_projects = []
for proj in all_projects:
    name = proj['Project_Name'].lower()
    if 'fema' in name or 'emergency' in name or 'warning' in name or 'siren' in name or 'disaster' in name:
        emergency_projects.append(proj)
    # Also include infrastructure/response projects
    elif any(term in name for term in ['guardrail', 'culvert', 'storm drain', 'bridge']):
        emergency_projects.append(proj)

print('__RESULT__:')
print(json.dumps({
    'total_projects_found': len(all_projects),
    'emergency_projects_count': len(emergency_projects),
    'emergency_projects': emergency_projects
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.execute_python:5': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'funding_count': 500, 'civic_count': 5, 'sample_funding': [{'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}], 'sample_civic_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.execute_python:18': {'emergency_related_count': 27, 'fema_count': 20, 'emergency_count': 0, 'fema_projects': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'emergency_projects': [], 'combined_related': [{'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Project_Name': 'Citywide Guardrail Replacement', 'Funding_Source': 'Infrastructure Bond', 'Amount': '30000'}, {'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Clover Heights Storm Drainage Improvements', 'Funding_Source': 'Development Bank Loan', 'Amount': '22000'}, {'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Encinal Canyon 60-inch Storm Drain Repairs', 'Funding_Source': 'Municipal Fund', 'Amount': '56000'}, {'Project_Name': 'Guardrail Replacement Citywide', 'Funding_Source': 'International Aid', 'Amount': '39000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs', 'Funding_Source': 'Community Fund', 'Amount': '57000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Malibu Park Storm Drain Repairs', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '50000'}, {'Project_Name': 'Outdoor Warning Signs', 'Funding_Source': 'Urban Renewal Fund', 'Amount': '92000'}, {'Project_Name': 'Outdoor Warning Sirens', 'Funding_Source': 'Social Impact Investment', 'Amount': '28000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}]}}

exec(code, env_args)
