code = """import json
import re

# Read the civic documents data from the file
with open('/tmp/tmpyq7d3x4g.json', 'r') as f:
    civic_docs = json.load(f)

# Initialize a list to store extracted projects
all_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Find all projects with their details
    # Look for patterns that indicate project descriptions
    
    # Find Capital Improvement Projects (Design) section
    design_match = re.search(r'Capital Improvement Projects \(Design\)(.*?)(?=\n\nCapital Improvement Projects \(|$)', text, re.DOTALL)
    if design_match:
        design_section = design_match.group(1)
        # Extract individual projects from this section
        # Projects are separated by blank lines and start with project name
        projects_raw = re.split(r'\n\n(?=\w)', design_section)
        for proj in projects_raw:
            proj = proj.strip()
            if proj and len(proj) > 20 and not proj.startswith('('):
                # Extract project name (first line)
                lines = proj.split('\n')
                if lines:
                    project_name = lines[0].strip()
                    # Check if this line looks like a project name (not a header or page marker)
                    if (project_name and not project_name.startswith('Page') and 
                        'Capital Improvement' not in project_name and len(project_name) < 200):
                        
                        # Determine topics
                        lower_proj = proj.lower()
                        topics = []
                        if 'park' in lower_proj:
                            topics.append('park')
                        if 'road' in lower_proj:
                            topics.append('road')
                        if 'storm' in lower_proj or 'drainage' in lower_proj:
                            topics.append('storm drain')
                        if 'emergency' in lower_proj or 'warning' in lower_proj:
                            topics.append('emergency warning')
                        
                        # Check for Spring 2022 dates
                        st = None
                        if 'Spring 2022' in proj or 'spring 2022' in proj:
                            st = '2022-Spring'
                        elif re.search(r'Spring\s+2022', proj, re.IGNORECASE):
                            st = '2022-Spring'
                        
                        all_projects.append({
                            'Project_Name': project_name,
                            'topic': ', '.join(topics),
                            'type': 'capital',
                            'status': 'design',
                            'st': st,
                            'et': None
                        })
    
    # Find Capital Improvement Projects (Construction) section
    construction_match = re.search(r'Capital Improvement Projects \(Construction\)(.*?)(?=\n\nCapital Improvement Projects \(|$)', text, re.DOTALL)
    if construction_match:
        construction_section = construction_match.group(1)
        projects_raw = re.split(r'\n\n(?=\w)', construction_section)
        for proj in projects_raw:
            proj = proj.strip()
            if proj and len(proj) > 20 and not proj.startswith('('):
                lines = proj.split('\n')
                if lines:
                    project_name = lines[0].strip()
                    if (project_name and not project_name.startswith('Page') and 
                        'Capital Improvement' not in project_name and len(project_name) < 200):
                        
                        lower_proj = proj.lower()
                        topics = []
                        if 'park' in lower_proj:
                            topics.append('park')
                        if 'road' in lower_proj:
                            topics.append('road')
                        if 'storm' in lower_proj or 'drainage' in lower_proj:
                            topics.append('storm drain')
                        
                        st = None
                        if 'Spring 2022' in proj or 'spring 2022' in proj:
                            st = '2022-Spring'
                        elif re.search(r'Spring\s+2022', proj, re.IGNORECASE):
                            st = '2022-Spring'
                        
                        all_projects.append({
                            'Project_Name': project_name,
                            'topic': ', '.join(topics),
                            'type': 'capital',
                            'status': 'completed',
                            'st': st,
                            'et': None
                        })
    
    # Find Capital Improvement Projects (Not Started) section
    notstarted_match = re.search(r'Capital Improvement Projects \(Not Started\)(.*?)$', text, re.DOTALL)
    if notstarted_match:
        notstarted_section = notstarted_match.group(1)
        projects_raw = re.split(r'\n\n(?=\w)', notstarted_section)
        for proj in projects_raw:
            proj = proj.strip()
            if proj and len(proj) > 20 and not proj.startswith('('):
                lines = proj.split('\n')
                if lines:
                    project_name = lines[0].strip()
                    if (project_name and not project_name.startswith('Page') and 
                        'Capital Improvement' not in project_name and len(project_name) < 200):
                        
                        lower_proj = proj.lower()
                        topics = []
                        if 'park' in lower_proj:
                            topics.append('park')
                        if 'road' in lower_proj:
                            topics.append('road')
                        if 'storm' in lower_proj or 'drainage' in lower_proj:
                            topics.append('storm drain')
                        
                        st = None
                        if 'Spring 2022' in proj or 'spring 2022' in proj:
                            st = '2022-Spring'
                        elif re.search(r'Spring\s+2022', proj, re.IGNORECASE):
                            st = '2022-Spring'
                        
                        all_projects.append({
                            'Project_Name': project_name,
                            'topic': ', '.join(topics),
                            'type': 'capital',
                            'status': 'not started',
                            'st': st,
                            'et': None
                        })
    
    # Find Disaster Recovery Projects (look for FEMA/Disaster keywords)
    if re.search(r'Disaster Recovery|FEMA|Woolsey Fire', text):
        # Extract potential disaster projects
        # These often have (FEMA Project) or similar in the name
        disaster_matches = re.finditer(r'\n\n([^\n]+?FEMA[^\n]*)', text)
        for match in disaster_matches:
            project_name = match.group(1).strip()
            if project_name and len(project_name) < 200:
                topics = ['FEMA', 'disaster']
                
                st = None
                if 'Spring 2022' in text:
                    st = '2022-Spring'
                
                all_projects.append({
                    'Project_Name': project_name,
                    'topic': ', '.join(topics),
                    'type': 'disaster',
                    'status': 'design',
                    'st': st,
                    'et': None
                })

# Filter for Spring 2022 projects
spring_2022_projects = [p for p in all_projects if p['st'] == '2022-Spring']

print('Total projects extracted:', len(all_projects))
print('Spring 2022 projects found:', len(spring_2022_projects))

# Save projects to files
with open('/tmp/all_projects.json', 'w') as f:
    json.dump(all_projects, f, indent=2)

with open('/tmp/spring_2022_projects.json', 'w') as f:
    json.dump(spring_2022_projects, f, indent=2)

print('__RESULT__:')
print(json.dumps({
    'total_projects': len(all_projects),
    'spring_2022_count': len(spring_2022_projects),
    'spring_2022_projects': spring_2022_projects
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:12': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
