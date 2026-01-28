code = """import json
import re

# Read the civic_docs result from storage
civic_docs_data = locals()['var_functions.query_db:2']

# If it's a file path (string), load it
if isinstance(civic_docs_data, str):
    with open(civic_docs_data, 'r') as f:
        civic_docs = json.load(f)
else:
    # It's already the data
    civic_docs = civic_docs_data

print(f"Number of documents: {len(civic_docs)}")
print("\nFirst document keys:")
first_doc = civic_docs[0]
print(list(first_doc.keys()))

# Show a preview of the text
print("\nText preview (first 300 chars):")
text_preview = first_doc.get('text', '')[:300]
print(text_preview)

# Look for Spring 2022 projects
spring_2022_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find project names and their details
    # Looking for patterns that indicate projects with Spring 2022 timeline
    if 'Spring 2022' in text or '2022-Spring' in text or ('2022' in text and 'Spring' in text):
        # Extract project information around these mentions
        lines = text.split('\n')
        for i, line in enumerate(lines):
            if 'Spring 2022' in line or '2022-Spring' in line or ('2022' in line and 'Spring' in line):
                # Look for project name (usually above or is the line itself)
                project_name = line.strip()
                if i > 0 and (len(line.strip()) < 50 or 'Project' not in line):
                    # Try to get project name from previous lines
                    for j in range(max(0, i-5), i):
                        prev_line = lines[j].strip()
                        if prev_line and len(prev_line) > 10 and not prev_line.startswith('('):
                            if 'project' in prev_line.lower() or len(prev_line.split()) < 10:
                                project_name = prev_line
                                if len(prev_line) > 3:
                                    break
                
                spring_2022_projects.append({
                    'project_name': project_name,
                    'context': f"{lines[max(0,i-2)]}...{line}...{lines[min(len(lines)-1,i+2)]}"
                })

print(f"\nFound {len(spring_2022_projects)} potential Spring 2022 mentions")
for proj in spring_2022_projects[:5]:
    print(f"- {proj['project_name']}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
