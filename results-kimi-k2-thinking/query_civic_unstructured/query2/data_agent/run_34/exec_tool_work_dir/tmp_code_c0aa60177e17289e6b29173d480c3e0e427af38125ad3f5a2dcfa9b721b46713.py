code = """import json
import re

# Read the civic documents from the file
civic_docs_file = var_functions.query_db:0
civic_docs = []

with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

print(f"Total civic documents: {len(civic_docs)}")

# Initialize list to store extracted project information
projects = []

# Iterate through each document
for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Split text into lines for easier processing
    lines = text.split('\n')
    
    # Look for lines containing "park" and check surrounding context for completion in 2022
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Check if this line looks like a project name (not empty, reasonable length, contains park)
        if (line and len(line) > 5 and 'park' in line.lower() and 
            not line.startswith('(') and not line.startswith('-') and 
            'updates' not in line.lower() and 'schedule' not in line.lower()):
            
            # Look ahead for completion information
            for j in range(i, min(i+10, len(lines))):
                next_line = lines[j].strip().lower()
                
                # Check if completed in 2022
                if 'construction was completed' in next_line and '2022' in next_line:
                    # Extract completion date
                    date_match = re.search(r'(\w+\s+2022)', next_line, re.IGNORECASE)
                    if date_match:
                        completion_date = date_match.group(1)
                        projects.append({
                            'project_name': line.strip(),
                            'completion_date': completion_date,
                            'filename': filename,
                            'topic': 'park',
                            'status': 'completed',
                            'et': completion_date
                        })
                        break

# Remove duplicates
unique_projects = []
seen_names = set()

for proj in projects:
    clean_name = proj['project_name'].strip()
    if clean_name not in seen_names:
        unique_projects.append(proj)
        seen_names.add(clean_name)

print(f"Found {len(unique_projects)} unique park-related projects completed in 2022:")
for proj in unique_projects:
    print(f"  - {proj['project_name']} ({proj['completion_date']})")

# Also check for any other patterns in the documents
print("\nSearching for additional park projects...")
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for any mention of park projects with 2022 completion
    if 'park' in text.lower() and '2022' in text:
        # Check for completion patterns
        completion_patterns = [
            r'Completed[^\n]*2022[^\n]*park[^\n]*',
            r'park[^\n]*Completed[^\n]*2022',
            r'Construction[^\n]*completed[^\n]*2022[^\n]*park'
        ]
        
        for pattern in completion_patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            for match in matches:
                print(f"Potential match: {match[:100]}...")

print('__RESULT__:')
print(json.dumps(unique_projects))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:8': ['Funding'], 'var_functions.query_db:10': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}]}

exec(code, env_args)
