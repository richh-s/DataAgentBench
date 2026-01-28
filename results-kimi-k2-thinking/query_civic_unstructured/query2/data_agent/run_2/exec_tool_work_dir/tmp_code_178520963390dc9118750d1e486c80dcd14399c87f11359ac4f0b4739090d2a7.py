code = """import json
import re

# Load the civic documents data
with open(var_functions.query_db:0, 'r') as f:
    civic_docs = json.load(f)

# Load the funding data
with open(var_functions.query_db:2, 'r') as f:
    funding_data = json.load(f)

# Create a list to store extracted projects
extracted_projects = []

# Function to extract project information from document text
def extract_projects_from_text(text):
    projects = []
    # Split by common project section headers
    sections = re.split(r'\n\s*\n', text)
    
    current_project = None
    
    for section in sections:
        # Look for project names (typically bold or title case)
        # Patterns like "Project Name:\n" or just standalone project names
        lines = section.strip().split('\n')
        
        for line in lines:
            line = line.strip()
            if not line or line.startswith('(') or line.startswith('•') or line.startswith('■'):
                continue
                
            # Look for indicators of project sections
            if any(keyword in line.lower() for keyword in ['project', 'updates:', 'schedule:', 'description:']):
                continue
                
            # Check if this looks like a project name (not too long, starts with capital, no colon at end)
            if (len(line) < 100 and 
                line and 
                line[0].isupper() and 
                not line.endswith(':') and 
                not line.startswith('To:') and
                not line.startswith('From:') and
                not line.startswith('Date:') and
                not line.startswith('Subject:') and
                not 'Commission' in line and
                not 'Prepared by' in line and
                not 'Approved by' in line):  
                
                # Check if line contains topic indicators
                has_topic_indicators = False
                for topic in ['park', 'road', 'storm', 'drainage', 'bridge', 'playground', 'FEMA', 'fire']:
                    if topic.lower() in line.lower():
                        has_topic_indicators = True
                        break
                
                if has_topic_indicators:
                    current_project = line
                    
                    # Try to find status and dates in nearby text
                    status = None
                    st = None
                    et = None
                    topics = []
                    
                    # Check if it's park-related
                    if 'park' in line.lower():
                        topics.append('park')
                    if 'playground' in line.lower():
                        topics.append('playground')
                    if 'storm' in line.lower() or 'drainage' in line.lower():
                        topics.append('storm drain')
                    if 'road' in line.lower():
                        topics.append('road')
                    if 'FEMA' in line.lower():
                        topics.append('FEMA')
                    
                    # Look for status indicators
                    section_lower = section.lower()
                    if 'completed' in section_lower:
                        status = 'completed'
                    elif 'construction' in section_lower and ('begin' in section_lower or 'under construction' in section_lower):
                        status = 'construction'
                    elif 'design' in section_lower:
                        status = 'design'
                    elif 'not started' in section_lower:
                        status = 'not started'
                    
                    # Look for date patterns like "2022", "2022-Fall", "November 2022", etc.
                    date_patterns = [
                        r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{4})',
                        r'(\d{4})-(?:Spring|Summer|Fall|Winter)',
                        r'(\d{4})-(?:0[1-9]|1[0-2])',
                        r'(\d{4})'
                    ]
                    
                    for pattern in date_patterns:
                        matches = re.findall(pattern, section)
                        if matches:
                            for year in matches:
                                if year == '2022':
                                    et = '2022'
                                    break
                                    
                    if current_project and status == 'completed' and et == '2022' and 'park' in topics:
                        projects.append({
                            'Project_Name': current_project,
                            'topic': ','.join(topics),
                            'status': status,
                            'st': None,
                            'et': et
                        })
    
    return projects

# Process all documents
for doc in civic_docs:
    if 'text' in doc:
        projects = extract_projects_from_text(doc['text'])
        extracted_projects.extend(projects)

# Print extracted park projects completed in 2022
print("EXTRACTED PARK PROJECTS COMPLETED IN 2022:")
for proj in extracted_projects:
    print(f"- {proj['Project_Name']}: {proj['topic']}, {proj['status']}, {proj['et']}")

print(f"\nTotal extracted: {len(extracted_projects)}")

# Create a set of project names from funding data
funding_project_names = set()
for fund in funding_data:
    if 'Project_Name' in fund:
        funding_project_names.add(fund['Project_Name'].lower())

# Match extracted projects with funding data
matched_projects = []
total_funding = 0

for proj in extracted_projects:
    proj_name = proj['Project_Name']
    proj_name_lower = proj_name.lower()
    
    # Look for exact or close matches in funding data
    for fund in funding_data:
        fund_name = fund.get('Project_Name', '')
        fund_name_lower = fund_name.lower()
        
        # Direct match or project name is subset of funding name
        if proj_name_lower in fund_name_lower or fund_name_lower in proj_name_lower:
            amount = int(fund.get('Amount', 0))
            matched_projects.append({
                'project_name': proj_name,
                'funding_name': fund_name,
                'amount': amount
            })
            total_funding += amount

# Print matches
print("\nMATCHED PROJECTS WITH FUNDING:")
for match in matched_projects:
    print(f"- {match['project_name']} -> {match['funding_name']}: ${match['amount']:,}")

print(f"\nTOTAL FUNDING: ${total_funding:,}")

# Return the result in the required format
result = {
    'total_funding': total_funding,
    'matched_projects': matched_projects,
    'count': len(matched_projects)
}

print("\n__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
