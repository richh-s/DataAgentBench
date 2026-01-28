code = """import json
import re

# Read MongoDB results
mongo_file = open(var_functions.query_db:14, 'r')
mongo_docs = json.load(mongo_file)
mongo_file.close()

# Read funding data
funding_file = open(var_functions.query_db:4, 'r')
funding_records = json.load(funding_file)
funding_file.close()

# Create lookup for funding amounts
funding_lookup = {}
for rec in funding_records:
    funding_lookup[rec['Project_Name']] = int(rec['Amount'])

print('MongoDB documents: ' + str(len(mongo_docs)))
print('Funding records: ' + str(len(funding_records)))

# Extract projects starting in Spring 2022
spring_projects = []

for doc in mongo_docs:
    text = doc.get('text', '')
    # Simple pattern: look for Spring 2022 mentions
    if 'Spring 2022' in text or 'Spring/Summer 2022' in text:
        # Extract project names from sections
        sections = text.split('\n\n')
        for section in sections:
            if 'Spring' in section and '2022' in section:
                # Try to find project name in this section
                lines = section.split('\n')
                for line in lines:
                    # Project names are often capitalized and descriptive
                    if len(line.strip()) > 10 and not line.startswith('(') and not line.startswith('Page'):
                        clean_line = line.strip()
                        if clean_line.isupper() or (clean_line[0].isupper() and sum(c.isupper() for c in clean_line) > len(clean_line)/3):
                            if clean_line not in spring_projects:
                                spring_projects.append(clean_line)

print('Potential Spring 2022 projects: ' + str(len(spring_projects)))
for proj in spring_projects[:10]:
    print('  ' + proj)

# Cross-reference with funding
matched_projects = []
for proj in spring_projects:
    if proj in funding_lookup:
        matched_projects.append({'name': proj, 'amount': funding_lookup[proj]})
        
print('Projects with funding data: ' + str(len(matched_projects)))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
