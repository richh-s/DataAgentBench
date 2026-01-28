code = """import json
import re

# Load funding data
funding_file = locals()['var_functions.query_db:6']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
civic_file = locals()['var_functions.query_db:2']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Extract project information from civic documents
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for project patterns in the text
    # Common patterns include bullet points with project names
    lines = text.split('\n')
    
    for line in lines:
        # Look for lines that might contain project names
        # These often start with project names or have specific markers
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
            
        # Look for disaster-related keywords and project names
        # Disaster projects often mention FEMA, CalOES, CalJPIA, fire, etc.
        disaster_indicators = ['FEMA', 'CalOES', 'CalJPIA', 'disaster', 'fire', 'emergency', 'recovery']
        
        # Check if this line might be a project name
        # Project names are often title case or have specific suffixes
        if (any(indicator in line for indicator in disaster_indicators) or
            '(FEMA Project)' in line or
            '(CalOES Project)' in line or
            '(CalJPIA Project)' in line):
            
            # Clean up the project name
            project_name = line.strip()
            
            # Skip very short lines that are likely not project names
            if len(project_name) < 10:
                continue
                
            # Remove leading bullet points or numbering
            project_name = re.sub(r'^[\d\s\-\•\.]+', '', project_name)
            project_name = re.sub(r'^[\s]+', '', project_name)
            
            # Remove common prefixes that aren't part of project names
            project_name = re.sub(r'^(?:Updates?|Status|Project|Description|Schedule|Recommended Action|Discussion|To:|Prepared by|Approved by|Date prepared|Meeting date|Subject|RECOMMENDED ACTION|DISCUSSION|Item|Agenda|Public Works|Commission|Prepared by):.*$', '', project_name, flags=re.IGNORECASE)
            
            if not project_name:
                continue
                
            # Look for dates in the surrounding context
            # Search nearby lines for date patterns
            context_window = 10
            idx = lines.index(line)
            start_idx = max(0, idx - context_window)
            end_idx = min(len(lines), idx + context_window)
            context = '\n'.join(lines[start_idx:end_idx])
            
            # Look for start dates
            start_date = None
            date_patterns = [
                r'(?:Start|Begin|Schedule|Timeline).*(?:2022[\-\s]?(?:Spring|Fall|Summer|Winter|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|\d{1,2}))',
                r'2022[\-\s]?(?:Spring|Fall|Summer|Winter|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|\d{1,2})',
                r'(?:Spring|Fall|Summer|Winter)[\-\s]?2022'
            ]
            
            for pattern in date_patterns:
                matches = re.findall(pattern, context, re.IGNORECASE)
                if matches:
                    start_date = matches[0]
                    break
            
            # If we have what looks like a valid project name for a disaster-related project
            if (len(project_name) > 10 and 
                (any(indicator in project_name for indicator in disaster_indicators) or
                 '(FEMA Project)' in project_name or
                 '(CalOES Project)' in project_name or
                 '(CalJPIA Project)' in project_name)):
                
                projects.append({
                    'Project_Name': project_name,
                    'Type': 'disaster',
                    'Start_Date': start_date,
                    'Has_2022_Start': '2022' in str(start_date) if start_date else False
                })

# Debug info
print(f"Found {len(projects)} potential disaster projects in civic docs")
print(f"Sample projects: {[p['Project_Name'] for p in projects[:10]]}")

# Now match with funding data and filter for 2022 start dates
total_funding = 0
matched_projects = []

for project in projects:
    if project['Has_2022_Start']:
        project_name = project['Project_Name']
        
        # Look for matching funding records
        for funding in funding_data:
            funding_project = funding.get('Project_Name', '')
            
            # Check for exact match or partial match
            if (project_name == funding_project or
                funding_project.startswith(project_name) or
                project_name.startswith(funding_project)):
                
                amount = int(funding.get('Amount', 0))
                total_funding += amount
                matched_projects.append({
                    'Project': project_name,
                    'Funding_Project': funding_project,
                    'Amount': amount
                })
                break

# Alternative approach: Look for disaster projects directly in funding data
# Some projects in funding data have clear disaster indicators in their names

for funding in funding_data:
    funding_project = funding.get('Project_Name', '')
    
    disaster_indicators = ['FEMA', 'CalOES', 'CalJPIA', 'disaster', 'fire', 'emergency']
    
    if any(indicator in funding_project for indicator in disaster_indicators):
        # Check if this project started in 2022 by looking for it in civic docs
        amount = int(funding.get('Amount', 0))
        
        # For now, include all disaster projects (we can refine further)
        # We'll add this amount if we couldn't find it through the main matching
        found_in_match = any(mp['Funding_Project'] == funding_project for mp in matched_projects)
        
        if not found_in_match:
            # Look for date info in civic docs for this specific project
            for doc in civic_docs:
                text = doc.get('text', '')
                if funding_project in text:
                    # Check for 2022 date references
                    if re.search(r'2022.*' + re.escape(funding_project)[:30], text) or \
                       re.search(re.escape(funding_project)[:30] + r'.*2022', text):
                        total_funding += amount
                        matched_projects.append({
                            'Project': funding_project,
                            'Funding_Project': funding_project,
                            'Amount': amount
                        })
                        break

result = f"Total funding for disaster-related projects that started in 2022: ${total_funding:,}"

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
