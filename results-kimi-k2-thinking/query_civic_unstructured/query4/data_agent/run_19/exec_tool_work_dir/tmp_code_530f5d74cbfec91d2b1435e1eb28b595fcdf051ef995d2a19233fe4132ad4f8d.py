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
    
    # Patterns to find projects and their details
    # Capital Improvement Projects (Design)
    design_section = re.search(r'Capital Improvement Projects \(Design\)(.*?)(?=\n\n[A-Z]|\n\nCapital Improvement Projects \(|$)', text, re.DOTALL)
    
    # Capital Improvement Projects (Construction)
    construction_section = re.search(r'Capital Improvement Projects \(Construction\)(.*?)(?=\n\n[A-Z]|$)', text, re.DOTALL)
    
    # Capital Improvement Projects (Not Started)
    not_started_section = re.search(r'Capital Improvement Projects \(Not Started\)(.*?)(?=\n\n[A-Z]|$)', text, re.DOTALL)
    
    # Also look for Disaster Recovery Projects specifically
    disaster_section = re.search(r'Disaster Recovery Projects(.*?)($|\n\n[A-Z])', text, re.DOTALL)
    
    def extract_projects_from_section(section_text, status, project_type='capital'):
        if not section_text:
            return []
        
        projects = []
        # Split by project names (typically followed by updates or schedule)
        # Look for patterns like "Project Name\n\n( updates or schedule marks"
        project_splits = re.split(r'\n\n(?=\w.*?\n\n\(cid:\d+\))', section_text)
        
        for proj_text in project_splits:
            proj_text = proj_text.strip()
            if not proj_text or len(proj_text) < 30:
                continue
            
            # Extract project name (first line or two)
            lines = proj_text.split('\n')
            project_name = lines[0].strip()
            
            if project_name and not project_name.startswith('(') and not project_name.startswith('Page'):
                # Determine project type based on content
                topics = []
                if 'park' in proj_text.lower():
                    topics.append('park')
                if 'road' in proj_text.lower():
                    topics.append('road')
                if 'FEMA' in proj_text.upper() or 'disaster' in proj_text.lower() or 'fire' in proj_text.lower():
                    topics.append('FEMA')
                    topics.append('disaster')
                    project_type = 'disaster'
                if 'storm' in proj_text.lower() or 'drainage' in proj_text.lower():
                    topics.append('storm drain')
                if 'emergency' in proj_text.lower() or 'warning' in proj_text.lower():
                    topics.append('emergency warning')
                
                # Extract dates
                st_match = None
                et_match = None
                
                # Look for schedule information
                schedule_match = re.search(r'Project Schedule.*?(?=\n\n|$)', proj_text, re.DOTALL)
                if not schedule_match:
                    schedule_match = re.search(r'Estimated Schedule.*?(?=\n\n|$)', proj_text, re.DOTALL)
                
                if schedule_match:
                    schedule_text = schedule_match.group()
                    
                    # Look for specific date references
                    spring_matches = re.findall(r'(?:Spring|spring)\s+2022', schedule_text)
                    if spring_matches:
                        st_match = '2022-Spring'
                    
                    # Look for other seasons/years
                    if not st_match:
                        for season in ['Spring', 'Summer', 'Fall', 'Winter']:
                            season_match = re.search(season + r'\s+(20\d{2})', schedule_text)
                            if season_match:
                                year = season_match.group(1)
                                st_match = year + '-' + season
                                break
                
                # If no schedule found, check if the document filename suggests a timeframe
                if not st_match and doc_year:
                    # Check if project is mentioned as starting or being scheduled
                    if '2022' in doc_year and any(keyword in proj_text.lower() for keyword in ['2022', 'advertise', 'design']):
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
        
        return projects
    
    # Extract from different sections
    all_projects.extend(extract_projects_from_section(
        design_section.group(1) if design_section else '', 
        'design', 'capital'
    ))
    all_projects.extend(extract_projects_from_section(
        construction_section.group(1) if construction_section else '', 
        'completed', 'capital'
    ))
    all_projects.extend(extract_projects_from_section(
        not_started_section.group(1) if not_started_section else '', 
        'not started', 'capital'
    ))
    all_projects.extend(extract_projects_from_section(
        disaster_section.group(1) if disaster_section else '', 
        'design', 'disaster'
    ))

# Count total projects extracted
print('Total projects extracted: ' + str(len(all_projects)))

# Debug: Print a few projects
for i, proj in enumerate(all_projects[:5]):
    print('Project ' + str(i+1) + ': ' + str(proj))

# Save all projects to a file for next steps
with open('/tmp/all_projects.json', 'w') as f:
    json.dump(all_projects, f, indent=2)

print('__RESULT__:')
print(json.dumps({'num_projects': len(all_projects), 'sample_projects': all_projects[:5]}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
