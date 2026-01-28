code = """import json
import re

# Load the civic documents data from the file path in storage
file_path = '/tmp/tmp_civic_docs.json'

# Read the JSON file
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

print(f'Loaded {len(civic_docs)} documents')

# Function to extract project information
def extract_emergency_fema_projects(text, filename):
    projects = []
    
    # Split text into sections based on common document structure
    sections = re.split(r'\n\s*\n', text)
    
    for section in sections:
        section = section.strip()
        if not section:
            continue
            
        # Convert to lowercase for keyword matching
        section_lower = section.lower()
        
        # Check if section contains emergency/fema/fire keywords
        if ('emergency' in section_lower or 'fema' in section_lower or 
            'fire' in section_lower or 'warning' in section_lower):
            
            # Extract project name (typically the first line or title)
            lines = section.split('\n')
            project_name = None
            
            for line in lines[:3]:  # Look at first few lines
                line = line.strip()
                if line and len(line) > 5 and not line.startswith(('(', '•', '-', '◦')):
                    # Check if line looks like a project name
                    project_indicators = ['Project', 'Road', 'Park', 'Bridge', 'Facility', 
                                        'Study', 'Improvements', 'Repairs', 'System', 'Plan']
                    if any(indicator in line for indicator in project_indicators) or len(line) < 80:
                        project_name = line
                        break
            
            # If we found a project name
            if project_name:
                # Determine type
                project_type = 'unknown'
                if 'FEMA' in section:
                    project_type = 'disaster'
                elif any(kw in section_lower for kw in ['road', 'bridge', 'park', 'facility']):
                    project_type = 'capital'
                
                # Determine status
                status = 'unknown'
                if 'completed' in section_lower:
                    status = 'completed'
                elif 'construction' in section_lower and ('under construction' in section_lower or 'begin construction' in section_lower):
                    status = 'construction'
                elif 'design' in section_lower or 'complete design' in section_lower:
                    status = 'design'
                elif 'not started' in section_lower:
                    status = 'not started'
                
                # Extract topics
                topics = []
                if 'emergency' in section_lower:
                    topics.append('emergency')
                if 'fema' in section_lower:
                    topics.append('FEMA')
                if 'fire' in section_lower:
                    topics.append('fire')
                if 'warning' in section_lower or 'siren' in section_lower:
                    topics.append('emergency warning')
                if 'drainage' in section_lower or 'storm' in section_lower:
                    topics.append('drainage')
                    topics.append('storm drain')
                
                if topics:
                    projects.append({
                        'Project_Name': project_name,
                        'topic': ', '.join(topics),
                        'type': project_type,
                        'status': status,
                        'source_file': filename
                    })
    
    return projects

# Extract all emergency/FEMA related projects
all_projects = []
for doc in civic_docs:
    if isinstance(doc, dict) and 'text' in doc:
        projects = extract_emergency_fema_projects(doc['text'], doc.get('filename', ''))
        all_projects.extend(projects)

print(f'Extracted {len(all_projects)} emergency/FEMA related projects')

# Remove duplicates based on project name
unique_projects = {}
for proj in all_projects:
    name = proj['Project_Name']
    if name not in unique_projects or len(proj['topic']) > len(unique_projects[name]['topic']):
        unique_projects[name] = proj

projects_list = list(unique_projects.values())
print(f'After deduplication: {len(projects_list)} projects')

# Create result
result = {
    'projects': projects_list,
    'count': len(projects_list)
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.execute_python:16': {'test': 'data'}, 'var_functions.query_db:18': [{'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
