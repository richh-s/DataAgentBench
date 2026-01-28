code = """import json
import re
from datetime import datetime

# Load the MongoDB documents
mongo_file = locals()['var_functions.query_db:2']
with open(mongo_file, 'r') as f:
    docs = json.load(f)

print(f"Loaded {len(docs)} documents")

# Function to extract projects and their dates from text
def extract_projects_from_text(text, filename):
    projects = []
    
    # Look for project sections - typically project names are on their own line or follow a pattern
    # Common patterns: project name followed by schedule/updates
    
    # Split text by common project delimiters
    sections = re.split(r'\n\s*\n', text)
    
    for section in sections:
        section = section.strip()
        if not section or len(section) < 20:
            continue
            
        # Look for likely project names - these are typically title-like lines
        lines = section.split('\n')
        
        for i, line in enumerate(lines):
            line = line.strip()
            # Skip empty lines, common headers
            if not line or line.startswith('(') or line in ['Public Works Commission', 'Agenda Report', 
                                                           'Item', 'To:', 'Prepared by:', 'Approved by:',
                                                           'Date prepared:', 'Meeting date:', 'Subject:',
                                                           'RECOMMENDED ACTION:', 'DISCUSSION:']:
                continue
                
            # Look for lines that look like project names (not bullet points, not dates)
            # Project names are typically longer and descriptive
            if (len(line) > 10 and 
                not line.startswith('•') and 
                not line.startswith('-') and
                not line.startswith('●') and
                not line.startswith('□') and
                not line.startswith('(') and
                not line.startswith('Page') and
                not ':' in line[:15] and  # Avoid "Complete Design:"
                not any(keyword in line.lower() for keyword in ['updates', 'schedule', 'advertise', 
                                                               'begin construction', 'complete design']),
                not line.isupper()):  # Avoid ALL CAPS headings
                
                # Look for date mentions in subsequent lines
                project_name = line.strip()
                start_date = None
                
                # Search the rest of the section for schedule info
                subsequent_text = '\n'.join(lines[i:])
                
                # Look for start dates in various formats
                # Pattern 1: "Advertise: Spring 2022"
                # Pattern 2: "Begin Construction: Spring 2022"
                # Pattern 3: "2022-Spring" mention
                
                # Check for Spring 2022 mentions
                spring_patterns = [
                    r'(?:advertise|begin construction|start|commence).*?[:\-]\s*(2022[-\s]spring|spring[-\s]2022)',
                    r'(2022[-\s]march|march[-\s]2022)',
                    r'(2022[-\s]april|april[-\s]2022)',
                    r'(2022[-\s]may|may[-\s]2022)',
                    r'(2022[-\s]0[3-5]|0[3-5][-\s]2022)',  # 2022-03, 2022-04, 2022-05
                ]
                
                for pattern in spring_patterns:
                    match = re.search(pattern, subsequent_text, re.IGNORECASE)
                    if match:
                        start_date = match.group(1)
                        break
                
                if start_date:
                    projects.append({
                        'project_name': project_name,
                        'start_date': start_date,
                        'filename': filename
                    })
                    print(f"Found project: {project_name} - {start_date}")
                
    return projects

# Extract projects from all documents
all_projects = []
for doc in docs:
    projects = extract_projects_from_text(doc.get('text', ''), doc.get('filename', ''))
    all_projects.extend(projects)

print(f"\nTotal projects with Spring 2022 start dates found: {len(all_projects)}")
for proj in all_projects:
    print(f"- {proj['project_name']}: {proj['start_date']}")

result = {
    "projects_found": all_projects,
    "count": len(all_projects)
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:16': {'key': 'var_functions.query_db:2', 'type': "<class 'str'>", 'length': 38}, 'var_functions.execute_python:18': {'total_docs': 5, 'sample_keys': ['_id', 'filename', 'text'], 'doc_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 202'}, 'var_functions.query_db:20': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}]}

exec(code, env_args)
