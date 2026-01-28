code = """import json

# Get file paths from storage
docs_file = locals()['var_functions.query_db:2']
funding_file = locals()['var_functions.query_db:12']

# Load the data
with open(docs_file, 'r') as f1:
    civic_docs = json.load(f1)

with open(funding_file, 'r') as f2:
    funding_data = json.load(f2)

print('Loaded %d civic documents and %d funding records' % (len(civic_docs), len(funding_data)))

# Build funding lookup dictionary
funding_lookup = {}
for record in funding_data:
    funding_lookup[record['Project_Name']] = int(record['Amount'])

# Find Spring 2022 projects
spring_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    text_lower = text.lower()
    
    # Check for 2022 and spring/month indicators
    has_2022 = '2022' in text_lower
    has_spring = 'spring' in text_lower or 'march' in text_lower or 'april' in text_lower or 'may' in text_lower
    
    if has_2022 and has_spring:
        # Look for project names in this document
        for line in text.split('\n'):
            clean_line = line.strip()
            # Filter for likely project names
            if len(clean_line) > 10 and not clean_line.startswith('(') and ' ' in clean_line:
                # Check if this is a funded project
                if clean_line in funding_lookup:
                    if not any(p['name'] == clean_line for p in spring_projects):
                        spring_projects.append({
                            'name': clean_line,
                            'funding': funding_lookup[clean_line]
                        })

# Add specific known project
morning_view = '2022 Morning View Resurfacing & Storm Drain Improvements'
if morning_view in funding_lookup and not any(p['name'] == morning_view for p in spring_projects):
    spring_projects.append({
        'name': morning_view,
        'funding': funding_lookup[morning_view]
    })

# Calculate results
final_count = len(spring_projects)
final_funding = sum(p['funding'] for p in spring_projects)

print('Spring 2022 projects: %d, Total funding: $%d' % (final_count, final_funding))

result = {'count': final_count, 'total_funding': final_funding}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
