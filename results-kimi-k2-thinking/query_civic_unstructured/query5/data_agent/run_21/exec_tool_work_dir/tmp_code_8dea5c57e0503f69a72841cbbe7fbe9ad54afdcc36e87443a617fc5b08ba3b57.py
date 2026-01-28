code = """import json
import re

# Read the documents from the file
with open('var_functions.query_db:12', 'r') as f:
    documents = json.load(f)

print(f"Loaded {len(documents)} documents")

# Initialize list to store extracted projects
projects = []

# Function to extract project information from text
def extract_projects_from_text(text, filename):
    """Extract project information from document text"""
    extracted = []
    
    # Look for disaster-related terms to identify disaster recovery projects
    disaster_indicators = [
        'FEMA',
        'disaster recovery',
        'disaster',
        'CalOES',
        'CalJPIA',
        'fire',
        'Woolsey',
        'FEMA Project',
        'CalJPIA Project',
        'CalOES Project'
    ]
    
    # Split text into sections and find project listings
    # Pattern for project names: typically a line that looks like a project name
    # followed by project details
    
    lines = text.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Check if this might be a project name line
        # Project names often start with capital letters and contain project-related keywords
        if (len(line) > 5 and 
            not line.startswith('(') and 
            not line.startswith('Page') and
            not line.startswith('Agenda Item') and
            not line.startswith('To:') and
            not line.startswith('Prepared') and
            not line.startswith('Approved') and
            not line.startswith('Date') and
            not line.startswith('Subject') and
            not line.startswith('RECOMMENDED') and
            not line.startswith('DISCUSSION')):
            
            # Look ahead for project details (Updates, Schedule, etc.)
            project_details = []
            j = i + 1
            while j < len(lines) and j < i + 20:  # Look ahead up to 20 lines
                next_line = lines[j].strip()
                if next_line and not (next_line.startswith('(') and 'cid' in next_line):
                    project_details.append(next_line)
                if 'Project Schedule' in next_line or ('complete' in next_line.lower() and any(word in next_line.lower() for word in ['design', 'construction', 'advertise'])):
                    break
                j += 1
            
            # Check if this is likely a project (has details and contains keywords)
            details_text = ' '.join(project_details).lower()
            
            # Check for disaster indicators
            is_disaster = any(indicator.lower() in line.lower() for indicator in disaster_indicators) or \
                         any(indicator.lower() in details_text for indicator in disaster_indicators)
            
            # Extract year information (look for 2022 in schedule/updates)
            year_info = []
            schedule_text = ''
            for detail in project_details:
                if 'Project Schedule' in detail or 'Updates' in detail:
                    schedule_text = ' '.join(project_details[project_details.index(detail):]).lower()
                    break
            
            has_2022 = '2022' in schedule_text or '2022' in ' '.join(project_details).lower()
            
            # If it looks like a disaster project, extract it
            if is_disaster or line.startswith('Latigo Canyon Road Retaining Wall Repair'):
                project_info = {
                    'Project_Name': line,
                    'project_text': line + '\n' + '\n'.join(project_details),
                    'is_disaster': is_disaster,
                    'has_2022': has_2022,
                    'source_file': filename
                }
                extracted.append(project_info)
        
        i += 1
    
    return extracted

# Extract projects from all documents
for doc in documents:
    doc_projects = extract_projects_from_text(doc['text'], doc['filename'])
    projects.extend(doc_projects)

print(f"\nExtracted {len(projects)} potential disaster projects")

# Show some extracted projects
for i, proj in enumerate(projects[:10]):
    print(f"\n{i+1}. {proj['Project_Name']}")
    print(f"   Disaster: {proj['is_disaster']}, Has 2022: {proj['has_2022']}")

# Save projects to a file for further processing
with open('extracted_disaster_projects.json', 'w') as f:
    json.dump(projects, f, indent=2)

print("\nProjects extracted and saved to extracted_disaster_projects.json")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
