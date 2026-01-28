code = """import json
import re

# Load funding data
funding_file = var_functions.query_db:1
if isinstance(funding_file, str) and funding_file.endswith('.json'):
    with open(funding_file, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = var_functions.query_db:1

# Load civic documents
civic_file = var_functions.query_db:2
if isinstance(civic_file, str) and civic_file.endswith('.json'):
    with open(civic_file, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = var_functions.query_db:2

# Extract projects from civic documents with their status and type
extracted_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for Capital Improvement Projects sections with Design status
    # Pattern to find Design section
    design_section_pattern = r'Capital Improvement Projects \(Design\)(.*?)(?=Capital Improvement Projects \((Construction|Not Started)\)|Disaster Recovery Projects|\Z)'
    design_match = re.search(design_section_pattern, text, re.DOTALL)
    
    if design_match:
        design_section = design_match.group(1)
        
        # Extract project names from the design section
        # Look for patterns like project names followed by updates or schedule
        project_patterns = [
            r'([A-Z][^\n]+?(?:Project|Improvements|Repairs|Infrastructure|Study|Master Plan|Facility|Center|Replacement))\s*\n',
            r'([A-Z][^\n]+?(?:Road|Drive|Avenue|Beach|Park|Highway|Lane|Way)[^\n]*?(?:Project|Improvements|Repairs|Infrastructure|Study|Master Plan|Facility|Center|Replacement)?)\s*\n'
        ]
        
        # Find all potential project names
        lines = design_section.split('\n')
        for line in lines:
            line = line.strip()
            # Skip empty lines, update lines, schedule lines, etc.
            if (line and 
                not line.startswith('(') and 
                not line.startswith('•') and 
                not line.startswith('●') and 
                not line.startswith('cid:') and
                'Updates:' not in line and
                'Schedule:' not in line and
                'Complete Design:' not in line and
                'Advertise:' not in line and
                'Begin Construction:' not in line and
                'Project Description:' not in line and
                len(line) > 10):
                
                # Check if it looks like a project name
                if any(keyword in line for keyword in ['Project', 'Improvements', 'Repairs', 'Infrastructure', 'Master Plan', 'Study', 'Replacement', 'Facility']):
                    # Clean up the project name
                    project_name = line.strip()
                    # Remove bullet points and special characters at start
                    project_name = re.sub(r'^[^a-zA-Z]*', '', project_name)
                    
                    if project_name and len(project_name) > 5:
                        extracted_projects.append({
                            'Project_Name': project_name,
                            'type': 'capital',
                            'status': 'design',
                            'source_doc': doc.get('filename', '')
                        })

# Also look for other patterns where projects might be mentioned with their status
# Look for "2022 Morning View Resurfacing & Storm Drain Improvements" pattern
year_project_pattern = r'(\d{4}\s+[A-Z][^\n]+?(?:Project|Improvements|Repairs|Infrastructure|Study|Master Plan|Facility|Center|Replacement))'
year_matches = re.findall(year_project_pattern, text)
for match in year_matches:
    if 'design' in text.lower() or 'Design' in text:
        extracted_projects.append({
            'Project_Name': match.strip(),
            'type': 'capital',
            'status': 'design',
            'source_doc': doc.get('filename', '')
        })

# Remove duplicates based on project name
unique_projects = {}
for proj in extracted_projects:
    name = proj['Project_Name']
    if name not in unique_projects:
        unique_projects[name] = proj

extracted_projects = list(unique_projects.values())

# Now match with funding data
funding_project_names = [f['Project_Name'] for f in funding_data]

# For each extracted project, check if it has funding > 50000
matched_projects = []

for proj in extracted_projects:
    proj_name = proj['Project_Name']
    
    # Direct match
    if proj_name in funding_project_names:
        matched_projects.append(proj)
    else:
        # Fuzzy match - check if project name contains key parts
        # This handles cases where the name might be slightly different
        for funding_proj in funding_data:
            funding_name = funding_proj['Project_Name']
            
            # Check for substring matches in both directions
            if (proj_name in funding_name or 
                funding_name in proj_name or
                # Check for key word matches
                any(keyword in funding_name and keyword in proj_name 
                    for keyword in ['Road', 'Park', 'Beach', 'Highway', 'Bridge', 
                                   'Drain', 'Storm', 'Canyon', 'Malibu', 'Replacement',
                                   'Improvements', 'Repairs', 'Project'])):
                
                # Additional check: at least 3 words match
                proj_words = set(re.findall(r'\b\w+\b', proj_name.lower()))
                funding_words = set(re.findall(r'\b\w+\b', funding_name.lower()))
                
                common_words = proj_words.intersection(funding_words)
                if len(common_words) >= 3:
                    proj['Matched_Funding_Name'] = funding_name
                    matched_projects.append(proj)
                    break

# Count matched projects
count = len(matched_projects)

print('__RESULT__:')
print(json.dumps({
    'count': count,
    'matched_projects': matched_projects[:10],  # Show first 10 for verification
    'total_extracted': len(extracted_projects),
    'total_funding_over_50k': len(funding_data)
}))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
