code = """import json
import re

# Read the civic documents
civic_docs_file = 'var_functions.query_db:8'
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Read the funding data
funding_file = 'var_functions.query_db:5'
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

print(f"Number of civic documents: {len(civic_docs)}")
print(f"Number of funding records: {len(funding_data)}")

# Let's examine the structure of the data
print("\nFirst civic doc keys:", list(civic_docs[0].keys()))
print("First funding record:", funding_data[0])

# Function to extract projects from civic doc text
def extract_projects_from_text(text):
    projects = []
    
    # Look for patterns that indicate project listings
    # Pattern 1: Project name on its own line, followed by updates
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Check if this looks like a project name (not a heading, not a bullet)
        # Project names are typically descriptive and don't start with common headings
        if (line and 
            not line.startswith('To:') and 
            not line.startswith('From:') and 
            not line.startswith('Subject:') and
            not line.startswith('Public Works') and
            not line.startswith('Commission') and
            not line.startswith('Agenda') and
            not line.startswith('Page') and
            not line.startswith('Item') and
            not line.startswith('RECOMMENDED') and
            not line.startswith('DISCUSSION:') and
            not line.startswith('Capital Improvement') and
            not line.startswith('Disaster Recovery') and
            not line.startswith('Prepared by:') and
            not line.startswith('Approved by:') and
            not line.startswith('Date prepared:') and
            not line.startswith('Meeting date:') and
            len(line) > 10 and  # Reasonably long
            not line.startswith('(') and  # Not a continuation
            not line.startswith('cid:')):  # Not a special character code
            
            # Check if next few lines contain update information
            project_info = {
                'project_name': line,
                'topic': '',
                'status': '',
                'et': '',
                'text_snippet': ''
            }
            
            # Look ahead for status and date information
            snippet_lines = []
            for j in range(i+1, min(i+10, len(lines))):
                next_line = lines[j].strip()
                snippet_lines.append(next_line)
                
                # Look for completion information
                if 'completed' in next_line.lower() and '2022' in next_line:
                    project_info['status'] = 'completed'
                    # Try to extract the date
                    if 'November 2022' in next_line:
                        project_info['et'] = '2022-November'
                    elif '2022' in next_line:
                        project_info['et'] = '2022'
                
                # Look for park-related keywords
                if any(park_word in line.lower() for park_word in ['park', 'playground']):
                    project_info['topic'] = 'park'
                elif any(park_word in next_line.lower() for park_word in ['park', 'playground']):
                    if project_info['topic'] == '':
                        project_info['topic'] = 'park'
            
            project_info['text_snippet'] = ' '.join(snippet_lines[:5])
            
            # Check if this project is park-related AND completed in 2022
            if project_info['topic'] == 'park' and project_info['status'] == 'completed':
                projects.append(project_info)
    
    return projects

# Extract projects from all documents
all_projects = []
for doc in civic_docs:
    projects = extract_projects_from_text(doc['text'])
    all_projects.extend(projects)

print(f"\nFound {len(all_projects)} park-related projects completed in 2022")
for proj in all_projects:
    print(f"- {proj['project_name']}: {proj['et']}")

# Now let's also look at funding data to see what park-related projects we have
park_funding = [f for f in funding_data if 'park' in f['Project_Name'].lower()]
print(f"\nFound {len(park_funding)} park-related projects in funding data")
for f in park_funding[:10]:
    print(f"- {f['Project_Name']}: ${f['Amount']}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
