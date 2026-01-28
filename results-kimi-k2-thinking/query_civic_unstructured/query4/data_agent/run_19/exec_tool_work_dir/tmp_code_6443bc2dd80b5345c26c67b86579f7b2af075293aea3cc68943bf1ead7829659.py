code = """import os
import json
import re

# Read the data from storage
with open('/tmp/tmpyq7d3x4g.json', 'r') as f:
    civic_docs = json.load(f)

# Initialize a list to store all projects
all_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Extract year from filename
    year_match = re.search(r'(?:20\d{2})', filename)
    doc_year = year_match.group() if year_match else None
    
    # Find different project sections using simpler patterns
    # Look for Capital Improvement Projects sections
    capital_sections = []
    
    # Find projects in Capital Improvement Projects (Design) section
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start >= 0:
        next_section = text.find('Capital Improvement Projects (', design_start + 1)
        if next_section < 0:
            next_section = len(text)
        section_text = text[design_start:next_section]
        capital_sections.append(('design', section_text, 'capital'))
    
    # Find projects in Capital Improvement Projects (Construction) section
    construction_start = text.find('Capital Improvement Projects (Construction)')
    if construction_start >= 0:
        next_section = text.find('Capital Improvement Projects (', construction_start + 1)
        if next_section < 0:
            next_section = len(text)
        section_text = text[construction_start:next_section]
        capital_sections.append(('completed', section_text, 'capital'))
    
    # Find projects in Capital Improvement Projects (Not Started) section
    notstarted_start = text.find('Capital Improvement Projects (Not Started)')
    if notstarted_start >= 0:
        next_section = text.find('\n\n', notstarted_start + 50)
        if next_section < 0:
            next_section = len(text)
        section_text = text[notstarted_start:next_section]
        capital_sections.append(('not started', section_text, 'capital'))
    
    # Find Disaster Recovery Projects section
    disaster_start = text.find('Disaster Recovery Projects')
    if disaster_start >= 0:
        next_section = text.find('\n\n', disaster_start + 50)
        if next_section < 0:
            next_section = len(text)
        section_text = text[disaster_start:next_section]
        capital_sections.append(('design', section_text, 'disaster'))
    
    def extract_projects_from_section(section_text, status, project_type):
        if not section_text or len(section_text) < 30:
            return []
        
        projects = []
        # Split by lines that look like project names
        # Project names are typically followed by content with (cid: markers
        lines = section_text.split('\n')
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if line and not line.startswith('(') and not line.startswith('Page') and len(line) > 5 and 'Capital Improvement' not in line and 'Disaster Recovery' not in line:
                # This might be a project name
                project_name = line
                # Collect the content for this project until next project or end
                project_content = []
                i += 1
                while i < len(lines):
                    next_line = lines[i].strip()
                    if next_line and (next_line.startswith('(') or 'Project Schedule' in next_line or 'Updates:' in next_line or 'Project Description:' in next_line):
                        project_content.append(next_line)
                        i += 1
                    elif next_line and len(next_line) > 5 and not next_line.startswith('(') and 'Capital Improvement' not in next_line and 'Page' not in next_line and 'Project Schedule' not in next_line:
                        # Likely next project
                        break
                    else:
                        i += 1
                
                proj_text = '\\n'.join(project_content)
                
                # Determine project type based on content
                topics = []
                lower_text = proj_text.lower()
                if 'park' in lower_text:
                    topics.append('park')
                if 'road' in lower_text:
                    topics.append('road')
                if 'FEMA' in proj_text.upper() or 'disaster' in lower_text or 'fire' in lower_text:
                    topics.append('FEMA')
                    topics.append('disaster')
                    project_type = 'disaster'
                if 'storm' in lower_text or 'drainage' in lower_text:
                    topics.append('storm drain')
                if 'emergency' in lower_text or 'warning' in lower_text:
                    topics.append('emergency warning')
                
                # Extract dates
                st_match = None
                et_match = None
                
                # Look for Spring 2022 reference
                if 'Spring 2022' in proj_text or 'spring 2022' in proj_text:
                    st_match = '2022-Spring'
                elif 'Spring 2022' in project_content.__str__():
                    st_match = '2022-Spring'
                elif doc_year and '2022' in doc_year and ('2022' in proj_text or '2022' in project_content.__str__()):
                    # Check if it mentions being scheduled or designed in 2022
                    combined = project_name + ' ' + proj_text
                    if any(keyword in combined.lower() for keyword in ['advertise', 'design', 'schedule', 'complete']):
                        st_match = doc_year
                
                project_data = {
                    'Project_Name': project_name[:200],
                    'topic': ', '.join(topics) if topics else '',
                    'type': project_type,
                    'status': status,
                    'st': st_match,
                    'et': et_match,
                    'source_file': filename
                }
                projects.append(project_data)
            else:
                i += 1
        
        return projects
    
    # Extract projects from all sections
    for status, section_text, project_type in capital_sections:
        all_projects.extend(extract_projects_from_section(section_text, status, project_type))

# Count total projects extracted
print('Total projects extracted: ' + str(len(all_projects)))

# Save all projects to a file for next steps
with open('/tmp/all_projects.json', 'w') as f:
    json.dump(all_projects, f, indent=2)

# Now filter for Spring 2022 projects
spring_2022_projects = [p for p in all_projects if p['st'] and '2022-Spring' in p['st']]

print('Found ' + str(len(spring_2022_projects)) + ' Spring 2022 projects:')
for proj in spring_2022_projects:
    print('  - ' + proj['Project_Name'] + ' (' + proj['type'] + ', ' + proj['status'] + ')')

print('__RESULT__:')
print(json.dumps({
    'total_extracted': len(all_projects),
    'spring_2022_count': len(spring_2022_projects),
    'spring_2022_projects': spring_2022_projects
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
