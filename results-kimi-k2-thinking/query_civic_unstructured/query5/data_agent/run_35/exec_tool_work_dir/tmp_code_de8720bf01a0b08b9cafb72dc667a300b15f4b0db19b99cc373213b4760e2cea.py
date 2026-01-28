code = """import json
import re

# Read the full civic documents data
file_path = '/tmp/tmpxm85f67u.json'
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

print(f"Loaded {len(civic_docs)} documents")

# Function to extract project information
def extract_disaster_projects_starting_in_2022(docs):
    """Extract disaster projects with start dates in 2022"""
    projects = []
    
    for doc in docs:
        text = doc.get('text', '')
        lines = text.split('\n')
        
        for i, line in enumerate(lines):
            line = line.strip()
            
            # Look for disaster project indicators
            # Pattern 1: Explicit disaster keywords
            disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'disaster', 'recovery', 'fire']
            
            # Pattern 2: Look for project names followed by status/schedule info
            # Projects often have schedule info after them
            
            # Common ways projects are listed in these documents:
            # - Project name on one line
            # - Updates/Schedule on following lines
            
            # Check if line looks like a project name (not too long, doesn't start with common markers)
            if (len(line) > 5 and len(line) < 200 and 
                not line.startswith('(') and 
                not line.startswith('•') and
                not line.startswith('■') and
                not line.startswith('Page') and
                not line.startswith('Agenda') and
                not 'Prepared by' in line and
                not 'Approved by' in line and
                not 'Subject' in line):
                
                # Look ahead for schedule/status info that contains 2022 dates
                project_start_2022 = False
                status = 'unknown'
                
                # Look ahead up to 8 lines for date/schedule info
                for j in range(i, min(len(lines), i+10)):
                    next_line = lines[j].strip()
                    
                    # Check for 2022 dates associated with start/begin/advertise
                    if '2022' in next_line:
                        if any(keyword in next_line.lower() for keyword in ['begin', 'start', 'advertise', 'design']):
                            project_start_2022 = True
                    
                    # Check for status information
                    if 'Updates:' in next_line or 'Status:' in next_line:
                        # Look for status in subsequent lines
                        for k in range(j+1, min(len(lines), j+5)):
                            status_line = lines[k].lower()
                            if 'design' in status_line:
                                status = 'design'
                                break
                            elif 'construction' in status_line or 'completed' in status_line:
                                status = 'completed' if 'completed' in status_line else 'construction'
                                break
                            elif 'not started' in status_line:
                                status = 'not started'
                                break
                
                # If this project starts in 2022, check if it's disaster-related
                if project_start_2022:
                    is_disaster = False
                    
                    # Check the line itself for disaster indicators
                    line_lower = line.lower()
                    if any(kw in line_lower for kw in disaster_keywords):
                        is_disaster = True
                    
                    # Check nearby lines for disaster context
                    if not is_disaster:
                        for j in range(max(0, i-5), min(len(lines), i+15)):
                            check_line = lines[j].lower()
                            if any(kw in check_line for kw in disaster_keywords):
                                is_disaster = True
                                break
                    
                    if is_disaster:
                        projects.append({
                            'Project_Name': line,
                            'type': 'disaster',
                            'status': status,
                            'st': '2022'
                        })
    
    return projects

# Extract disaster projects starting in 2022
disaster_projects_2022 = extract_disaster_projects_starting_in_2022(civic_docs)

print(f"Found {len(disaster_projects_2022)} disaster projects starting in 2022")

# Display them
for proj in disaster_projects_2022:
    print(f"- {proj['Project_Name']} (Status: {proj['status']})")

# Save results
result = {
    'disaster_projects_2022': disaster_projects_2022,
    'count': len(disaster_projects_2022)
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
