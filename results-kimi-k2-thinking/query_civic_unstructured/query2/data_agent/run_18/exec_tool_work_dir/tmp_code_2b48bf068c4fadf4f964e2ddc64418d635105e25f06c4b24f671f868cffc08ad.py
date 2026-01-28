code = """import json
import pandas as pd
import re

# Load funding data
with open('/tmp/tmp8opjs8_m.json', 'r') as f:
    funding_data = json.load(f)

# Load civic documents data
with open('/tmp/tmpg5k2n9mq.json', 'r') as f:
    civic_docs_data = json.load(f)

# Convert funding data to DataFrame
funding_df = pd.DataFrame(funding_data)
print("Total funding records: " + str(len(funding_df)))

# Sample of funding data first few records
print("\nSample funding data:")
print(funding_df.head().to_string())

print("\nTotal civic documents: " + str(len(civic_docs_data)))

# Process civic documents to extract project information
print("\nProcessing civic documents to extract project information...")

# Function to extract project info from text
def extract_projects_from_text(text):
    projects = []
    # Look for project patterns - typically project names followed by status/schedule info
    # This is a simplified extraction - in real scenarios, you'd use more sophisticated NLP
    
    # Split by common section headers
    sections = re.split(r'\n\s*\n', text)
    
    for section in sections:
        lines = section.strip().split('\n')
        if len(lines) < 2:
            continue
            
        # Look for project name patterns (usually first line or bolded)
        project_line = lines[0].strip()
        
        # Skip if it's a header or contains certain keywords
        skip_keywords = ['Agenda', 'Public Works', 'Commission', 'Capital Improvement', 'Disaster Recovery', 'Page', 'Item']
        if any(keyword in project_line for keyword in skip_keywords):
            continue
            
        if len(project_line) > 5 and not project_line.startswith('(') and not project_line.startswith('•'):
            # Check for topic indicators in the text
            topics = []
            if 'park' in section.lower():
                topics.append('park')
            if 'road' in section.lower():
                topics.append('road')
            if 'storm' in section.lower() or 'drain' in section.lower():
                topics.append('drainage')
            if 'FEMA' in section:
                topics.append('FEMA')
            if 'fire' in section.lower():
                topics.append('fire')
            
            # Check for status
            status = None
            if 'completed' in section.lower() or 'Complete Construction' in section:
                # Check for dates
                if '2022' in section or 'November 2022' in section or 'January 2023' in section:
                    status = 'completed'
            elif 'design' in section.lower():
                status = 'design'
            elif 'not started' in section.lower():
                status = 'not started'
            
            # Extract dates
            date_pattern = r'(?:Complete|Construction).*?(2022|2023|2024)'
            dates_found = re.findall(date_pattern, section)
            
            if status and topics:
                projects.append({
                    'Project_Name': project_line,
                    'topic': ','.join(topics),
                    'status': status,
                    'text_preview': section[:200]
                })
    
    return projects

# Extract projects from all documents
all_projects = []
for doc in civic_docs_data[:10]:  # Process first 10 for now
    projects = extract_projects_from_text(doc['text'])
    all_projects.extend(projects)

print("\nExtracted projects (sample):")
for proj in all_projects[:10]:
    print(f"Name: {proj['Project_Name']}")
    print(f"Topic: {proj['topic']}, Status: {proj['status']}")
    print("---")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json'}

exec(code, env_args)
