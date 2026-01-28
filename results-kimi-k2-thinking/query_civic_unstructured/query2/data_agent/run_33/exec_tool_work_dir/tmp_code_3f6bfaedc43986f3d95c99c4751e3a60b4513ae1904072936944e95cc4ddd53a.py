code = """import json
import re
from collections import defaultdict

# Load funding data from file
funding_file = locals()['var_functions.query_db:8']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic documents from file
civic_file = locals()['var_functions.query_db:2']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Extract project information from civic documents
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find project sections
    # Look for patterns like "Project Name" followed by updates and schedule
    project_patterns = [
        r'([A-Z][a-zA-Z\s&\-]+?)(?=\(cid:\d+\)\s+Updates:)',
        r'([A-Z][a-zA-Z\s&\-]+?)(?=\(cid:\d+\)\s+Project Schedule:)',
        r'([A-Z][a-zA-Z\s&\-]+?)(?=\(cid:\d+\)\s+Estimated Schedule:)',
        r'([A-Z][a-zA-Z\s&\-]+?)(?=\(cid:\d+\)\s+Complete Construction:)',
        r'([A-Z][a-zA-Z\s&\-]+?)(?=\(cid:\d+\)\s+Construction was completed)'
    ]
    
    for pattern in project_patterns:
        matches = re.finditer(pattern, text)
        for match in matches:
            project_name = match.group(1).strip()
            if project_name and len(project_name) < 200:  # Filter out noise
                # Extract status information
                status = None
                completed_2022 = False
                
                # Look for completion info
                completion_pattern = project_name + r'.*?Construction was completed[^,]*?(?=\n)'
                completion_match = re.search(completion_pattern, text, re.DOTALL | re.IGNORECASE)
                if completion_match:
                    completion_text = completion_match.group(0)
                    if '2022' in completion_text or 'November 2022' in completion_text:
                        completed_2022 = True
                        status = 'completed'
                
                # Look for status in section headers
                if 'Construction)' in text and project_name in text:
                    if 'Construction)' in text.split(project_name)[0].split('\n')[-5:]:
                        status = 'construction'
                elif 'Design)' in text and project_name in text:
                    if 'Design)' in text.split(project_name)[0].split('\n')[-5:]:
                        status = 'design'
                elif 'Not Started)' in text and project_name in text:
                    if 'Not Started)' in text.split(project_name)[0].split('\n')[-5:]:
                        status = 'not started'
                
                # Determine if park-related
                is_park = 'park' in project_name.lower() or 'playground' in project_name.lower()
                
                projects.append({
                    'Project_Name': project_name,
                    'status': status,
                    'completed_2022': completed_2022,
                    'is_park': is_park
                })

# Debug info
park_projects_2022 = [p for p in projects if p['is_park'] and p['completed_2022']]

print('__RESULT__:')
print(json.dumps({
    'total_projects_found': len(projects),
    'park_projects_completed_2022': len(park_projects_2022),
    'sample_park_projects': park_projects_2022[:5]
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
