code = """import json

funding_file = 'file_storage/functions.query_db:8.json'
civic_file = 'file_storage/functions.query_db:5.json'

with open(funding_file, 'r') as f:
    all_funding = json.load(f)

with open(civic_file, 'r') as f:
    all_docs = json.load(f)

# Get all FEMA/emergency related projects with full details
fema_emergency_projects = []
for fund in all_funding:
    name = fund.get('Project_Name', '')
    if 'FEMA' in name or 'emergency' in name.lower():
        fema_emergency_projects.append({
            'Project_Name': name,
            'Funding_Source': fund.get('Funding_Source'),
            'Amount': fund.get('Amount'),
            'Status': 'Unknown',  # Will try to find from documents
            'Type': 'Unknown'
        })

# Create a mapping of all project statuses from documents
status_map = {}
type_map = {}

for doc in all_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    current_status = None
    current_type = 'capital'
    
    for line in lines:
        line_clean = line.strip()
        if not line_clean:
            continue
        
        # Determine type
        if 'Disaster Recovery' in text:
            current_type = 'disaster'
        else:
            current_type = 'capital'
        
        # Determine status from section headers
        if 'Capital Improvement Projects (Design)' in line_clean or 'Disaster Recovery Projects (Design)' in line_clean:
            current_status = 'design'
        elif 'Capital Improvement Projects (Construction)' in line_clean or 'Disaster Recovery Projects (Construction)' in line_clean:
            # Check if construction is completed
            if 'Construction was completed' in text:
                current_status = 'completed'
            else:
                current_status = 'construction'
        elif 'Capital Improvement Projects (Not Started)' in line_clean or 'Disaster Recovery Projects (Not Started)' in line_clean:
            current_status = 'not started'
        
        # Map project name to status and type if found
        if current_status:
            status_map[line_clean] = current_status
            type_map[line_clean] = current_type

# Update our projects with status and type from the documents
for proj in fema_emergency_projects:
    project_name = proj['Project_Name']
    
    # Try to find status by checking if project name appears in status_map
    for doc_proj_name, status in status_map.items():
        if project_name in doc_proj_name or doc_proj_name in project_name:
            proj['Status'] = status
            proj['Type'] = type_map.get(doc_proj_name, 'Unknown')
            break
    
    # If not found, try partial matching
    if proj['Status'] == 'Unknown':
        proj_base = project_name.replace(' (FEMA Project)', '').replace(' (CalOES Project)', '').replace(' (FEMA/CalOES Project)', '')
        for doc_proj_name, status in status_map.items():
            if proj_base in doc_proj_name or doc_proj_name in proj_base:
                proj['Status'] = status
                proj['Type'] = type_map.get(doc_proj_name, 'Unknown')
                break

# Filter out any with status still unknown (not in documents)
projects_with_status = [p for p in fema_emergency_projects if p['Status'] != 'Unknown']

print('__RESULT__:')
print(json.dumps({
    'total_fema_emergency_projects': len(fema_emergency_projects),
    'projects_with_status': len(projects_with_status),
    'results': projects_with_status
}))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:6': {'funding_count': 10, 'funding_columns': ['Funding_ID', 'project_name_db', 'Funding_Source', 'Amount']}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'funding_path': 'file_storage/functions.query_db:8.json', 'civic_path': 'file_storage/functions.query_db:5.json', 'funding_exists': True, 'civic_exists': True}, 'var_functions.execute_python:14': {'funding_records': 500, 'civic_docs_count': 5, 'first_doc_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.execute_python:24': {'total_matches': 20, 'projects': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000', 'found_in_docs': True}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000', 'found_in_docs': True}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000', 'found_in_docs': True}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000', 'found_in_docs': True}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000', 'found_in_docs': True}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000', 'found_in_docs': True}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000', 'found_in_docs': True}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000', 'found_in_docs': True}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000', 'found_in_docs': True}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000', 'found_in_docs': True}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000', 'found_in_docs': True}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000', 'found_in_docs': True}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000', 'found_in_docs': True}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000', 'found_in_docs': True}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000', 'found_in_docs': True}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000', 'found_in_docs': True}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000', 'found_in_docs': True}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000', 'found_in_docs': True}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000', 'found_in_docs': True}]}}

exec(code, env_args)
