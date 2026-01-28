code = """import json
import re

civic_docs_path = locals()['var_functions.query_db:2']
with open(civic_docs_path, 'r') as f:
    civic_docs_data = json.load(f)

# Extract projects with timeline information from civic documents
projects_with_timeline = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    doc_id = doc.get('_id', '')
    
    # Find project sections by looking for patterns like "2022 Project Name" or "Project Name\nUpdates:" 
    # and extracting the timeline info that follows
    
    # Look for lines containing years that might be project names
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 5:
            continue
        
        # Skip header/footer lines
        if any(skip in line for skip in ['Page', 'Agenda Item', 'Public Works', 'Commission']):
            continue
        
        # Look for project names (often on their own line, not starting with bullet points)
        if (not line.startswith('(') and not line.startswith('•') and not line.startswith('-') and
            not line.startswith('Complete') and not line.startswith('Advertise') and not line.startswith('Begin') and
            'Updates:' not in line and 'Project Schedule:' not in line and 'Project Description:' not in line):
            
            # Check if line contains a year (potential start date in project name)
            year_match = re.search(r'(20\d{2})', line)
            if year_match:
                project_name = line.strip()
                year = year_match.group(1)
                
                # Check for disaster indicators
                is_disaster = any(keyword in project_name.lower() for keyword in ['fema', 'caloes', 'caljpia', 'fire', 'disaster', 'recovery'])
                
                # Try to find more timeline details in following lines
                status = ''
                end_year = year
                
                # Look ahead for status and end dates
                for j in range(i+1, min(i+10, len(lines))):
                    next_line = lines[j].strip()
                    if not next_line:
                        continue
                    
                    next_line_lower = next_line.lower()
                    if 'design' in next_line_lower:
                        status = 'design'
                    elif 'construction' in next_line_lower:
                        status = 'construction'
                    elif 'not started' in next_line_lower:
                        status = 'not started'
                    elif 'completed' in next_line_lower:
                        status = 'completed'
                    
                    # Look for end year
                    year_match_2 = re.search(r'(20\d{2})', next_line)
                    if year_match_2:
                        end_year = year_match_2.group(1)
                
                projects_with_timeline.append({
                    'Project_Name': project_name,
                    'st': year,
                    'et': end_year,
                    'status': status,
                    'is_disaster': is_disaster,
                    '_id': doc_id
                })

print("__RESULT__:")
print(json.dumps({
    "timeline_projects_count": len(projects_with_timeline),
    "disaster_projects_2022": [p for p in projects_with_timeline if p['is_disaster'] and '2022' in p['st']],
    "all_2022_projects": [p for p in projects_with_timeline if '2022' in p['st']],
    "sample": projects_with_timeline[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'total_records': 500, 'sample_records': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}, 'var_functions.execute_python:12': {'civic_docs_count': 5, 'first_doc_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.execute_python:22': {'total_funding_records': 500, 'total_funding_amount': 28094000, 'disaster_projects_count': 27, 'disaster_projects': [['Birdview Avenue Improvements (CalOES Project)', 85000], ['Birdview Avenue Improvements (FEMA/CalOES Project)', 14000], ['Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 81000], ['Clover Heights Storm Drain (FEMA Project)', 21000], ['Corral Canyon Culvert Repairs (FEMA Project)', 43000], ['Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 15000], ['Corral Canyon Road Bridge Repairs (FEMA Project)', 25000], ['Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 58000], ['Encinal Canyon Road Drainage Improvements (CalOES Project)', 18000], ['Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 94000], ['Guardrail Replacement Citywide (FEMA Project)', 22000], ['Guardrail Replacement Citywide (FEMA/CalOES Project)', 45000], ['Latigo Canyon Road Culvert Repairs (FEMA Project)', 36000], ['Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 44000], ['Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 91000], ['Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 78000], ['Malibu Road Slope Repairs (CalOES Project)', 37000], ['Outdoor Warning Sirens (FEMA Project)', 27000], ['Outdoor Warning Sirens (FEMA)', 81000], ['Outdoor Warning Sirens - Design (FEMA Project)', 43000]]}}

exec(code, env_args)
