code = """import json
import re

# Read the funding data
with open('var_functions.query_db:6', 'r') as f:
    funding_data = json.load(f)

# Read the civic documents
with open('var_functions.query_db:5', 'r') as f:
    civic_docs = json.load(f)

print(f"Number of funding records: {len(funding_data)}")
print(f"Number of civic documents: {len(civic_docs)}")
print(f"First funding record: {funding_data[0]}")
print(f"First civic doc keys: {list(civic_docs[0].keys())}")

# Let's try to extract project information from the text
# Looking at the pattern in the text, projects seem to be listed with names and schedules

def extract_projects_from_text(text):
    projects = []
    
    # Patterns to look for project names and their schedules
    # Common patterns like "Project Name\n\n(updates)\n\nProject Schedule:\n\nComplete Design: Summer 2023"
    
    # Look for project names that are typically title case lines followed by updates/schedule
    lines = text.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Skip empty lines and lines that look like headers/footers
        if not line or line.startswith('Page') or line.startswith('Agenda Item'):
            i += 1
            continue
            
        # Look for potential project names (title case, not too short, not common headers)
        # Project names are usually multiple words and start with capital letters
        if (len(line) > 10 and 
            line[0].isupper() and 
            not any(keyword in line.lower() for keyword in ['commission', 'meeting', 'agenda', 'report', 'public works', 'capital improvement', 'disaster recovery']):
            
            project_name = line
            
            # Look for schedule information after the project name
            st = None
            et = None
            status = None
            type_val = None
            
            # Scan ahead for schedule info
            j = i + 1
            while j < min(i + 20, len(lines)):
                next_line = lines[j].strip()
                
                # Look for start/completion dates
                if 'Complete Design:' in next_line or 'Begin Construction:' in next_line or 'Complete Construction:' in next_line:
                    # Extract year and season
                    if '2022' in next_line:
                        if 'Spring' in next_line:
                            st = '2022-Spring'
                        elif 'Summer' in next_line:
                            st = '2022-Summer'
                        elif 'Fall' in next_line:
                            st = '2022-Fall'
                        elif 'Winter' in next_line:
                            st = '2022-Winter'
                        else:
                            st = '2022'
                    
                if 'Project Schedule:' in next_line:
                    # Check next few lines for dates
                    k = j + 1
                    while k < min(j + 5, len(lines)):
                        schedule_line = lines[k].strip()
                        if '2022' in schedule_line:
                            if 'Spring' in schedule_line:
                                if not st:
                                    st = '2022-Spring'
                                else:
                                    et = '2022-Spring'
                            elif 'Complete' in schedule_line and '2022' in schedule_line:
                                if not et:
                                    et = '2022'
                        k += 1
                
                j += 1
            
            # Determine type based on project name
            if any(keyword in project_name.lower() for keyword in ['fema', 'fire', 'disaster']):
                type_val = 'disaster'
            else:
                type_val = 'capital'
            
            # Add project if it has a start time in 2022
            if st and '2022' in st:
                projects.append({
                    'Project_Name': project_name,
                    'st': st,
                    'et': et,
                    'status': status,
                    'type': type_val,
                    'topic': ''  # Would need more sophisticated parsing
                })
        
        i += 1
    
    return projects

# Extract projects from all documents
all_projects = []
for doc in civic_docs:
    projects = extract_projects_from_text(doc.get('text', ''))
    all_projects.extend(projects)

print(f"Extracted {len(all_projects)} projects with 2022 dates")
for p in all_projects[:10]:
    print(f"  {p['Project_Name']}: {p['st']}")

# Now filter for Spring 2022
spring_2022_projects = [p for p in all_projects if '2022-Spring' in p['st'] or '2022-03' in p['st'] or '2022-04' in p['st'] or '2022-05' in p['st']]
print(f"\nProjects in Spring 2022: {len(spring_2022_projects)}")
for p in spring_2022_projects:
    print(f"  {p['Project_Name']}")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
