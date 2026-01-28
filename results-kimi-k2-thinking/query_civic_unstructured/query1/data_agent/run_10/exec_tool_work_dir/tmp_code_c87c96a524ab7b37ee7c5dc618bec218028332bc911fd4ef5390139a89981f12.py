code = """import json
import re

# Load the MongoDB documents (civic project information)
civic_docs_file = var_functions.query_db:2
if isinstance(civic_docs_file, str) and civic_docs_file.endswith('.json'):
    with open(civic_docs_file, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = var_functions.query_db:2

# Load the funding data
funding_file = var_functions.query_db:5
if isinstance(funding_file, str) and funding_file.endswith('.json'):
    with open(funding_file, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = var_functions.query_db:5

# First, let's extract all project names from funding data for projects > $50,000
funding_projects = set()
for item in funding_data:
    if int(item['Amount']) > 50000:
        funding_projects.add(item['Project_Name'])

# Now, parse civic documents to find capital projects with 'design' status
# We'll look for patterns in the text that indicate project sections

capital_design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for "Capital Improvement Projects (Design)" section
    # This appears to be the pattern in the documents
    design_section = re.search(r'Capital Improvement Projects \(Design\)(.*?)(?=Capital Improvement Projects \(Construction\)|Disaster Recovery Projects|END OF SECTION|$)', 
                               text, re.DOTALL|re.IGNORECASE)
    
    if design_section:
        section_text = design_section.group(1)
        
        # Extract project names from this section
        # Projects appear to be listed with names, sometimes followed by updates and schedules
        # Look for patterns like project names at the beginning of lines or after bullet points
        
        # Split by common project delimiters
        lines = section_text.split('\n')
        
        current_project = None
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            # Skip common headers/footers
            if any(skip in line for skip in ['Page', 'Agenda Item', 'Public Works Commission', 'RECOMMENDED ACTION:', 'DISCUSSION:', 'To:', 'Prepared by:', 'Approved by:', 'Date prepared:', 'Meeting date:', 'Subject:']):
                continue
            
            # Look for project names - typically not indented or with minimal indentation
            # and not containing typical directive words
            if (len(line) > 10 and 
                not line.startswith('(') and 
                not line.startswith('•') and 
                not line.startswith('-') and
                'Updates:' not in line and
                'Project Schedule:' not in line and
                'Estimated Schedule:' not in line and
                not any(keyword in line for keyword in ['Staff is', 'City is', 'City has', 'Complete Design:', 'Advertise:', 'Begin Construction:', 'cid:', 'Project is'])):
                
                # This looks like a project name
                # Clean up the project name
                project_name = line.strip()
                
                # Remove common suffixes that might be part of the name in funding data
                # Keep the original but also add version without suffixes for matching
                capital_design_projects.append(project_name)

# Also check for projects listed with bullet points or other formats
# Let's try a more comprehensive extraction

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find all sections that mention "Design" and are part of capital projects
    # Look for headings first
    headings = re.findall(r'^(.*?(?:Capital|Design|Project).*?)$', text, re.MULTILINE)
    
    # Look for the capital design section more broadly
    if 'Capital Improvement Projects (Design)' in text:
        start_idx = text.index('Capital Improvement Projects (Design)')
        
        # Find where this section ends (when next major section begins)
        end_markers = [
            'Capital Improvement Projects (Construction)',
            'Capital Improvement Projects (Not Started)',
            'Disaster Recovery Projects',
            'DISASTER RECOVERY PROJECTS',
            'PUBLIC WORKS QUARTERLY UPDATE'
        ]
        
        end_idx = len(text)
        for marker in end_markers:
            if marker in text[start_idx:]:
                idx = text.index(marker, start_idx)
                end_idx = min(end_idx, idx)
        
        section_text = text[start_idx:end_idx]
        
        # Extract what look like project names (lines that are likely titles)
        lines = section_text.split('\n')
        for line in lines:
            line = line.strip()
            if (len(line) > 8 and 
                not any(skip in line for skip in ['(', ')', 'Updates:', 'Schedule:', 'Staff', 'City', 'Project', 'Complete', 'Advertise', 'Begin', 'RECOMMENDED', 'DISCUSSION', 'Page', 'Agenda']) and
                not line.isupper()):  # Avoid all-caps headers
                
                # More cleaning
                project_name = line.strip('•-– ')
                if project_name and len(project_name) > 8:
                    capital_design_projects.append(project_name)

# Clean up and deduplicate
capital_design_projects = list(set([p.strip() for p in capital_design_projects if p.strip()]))

# Now match with funding projects
matched_projects = []
for design_project in capital_design_projects:
    # Try to find matches in funding projects
    # Use flexible matching - check if design project name is contained in funding project name or vice versa
    design_lower = design_project.lower()
    
    for funding_project in funding_projects:
        funding_lower = funding_project.lower()
        
        # Check for containment in either direction
        if (design_lower in funding_lower or funding_lower in design_lower or
            # Check for key name matches (simplified)
            any(word in funding_lower for word in design_lower.split() if len(word) > 4)):
            matched_projects.append({
                'design_project': design_project,
                'funding_project': funding_project
            })

# Remove duplicates
unique_matches = []
seen = set()
for match in matched_projects:
    key = (match['design_project'], match['funding_project'])
    if key not in seen:
        seen.add(key)
        unique_matches.append(match)

# Count the results
count = len(unique_matches)

print('__RESULT__:')
print(json.dumps({
    'count': count,
    'matches': unique_matches,
    'capital_design_projects_extracted': capital_design_projects,
    'funding_projects_over_50k': list(funding_projects)
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
