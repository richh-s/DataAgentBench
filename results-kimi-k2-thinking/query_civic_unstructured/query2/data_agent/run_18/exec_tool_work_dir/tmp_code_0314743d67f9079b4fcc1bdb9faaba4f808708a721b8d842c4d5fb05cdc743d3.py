code = """import json

# Load funding data
with open('/tmp/tmp8opjs8_m.json', 'r') as f:
    funding_data = json.load(f)

# Load civic documents data
with open('/tmp/tmpg5k2n9mq.json', 'r') as f:
    civic_docs_data = json.load(f)

print("Funding records loaded:", len(funding_data))
print("Civic documents loaded:", len(civic_docs_data))

# Look at the park-related funding projects first
park_funding = [item for item in funding_data if 'park' in item['Project_Name'].lower() or 'Park' in item['Project_Name']]
print("\nPark-related funding projects found:", len(park_funding))

for item in park_funding[:10]:
    print(f"- {item['Project_Name']}: ${item['Amount']}")

print("\nSearching civic documents for park projects completed in 2022...")

# Search documents for completed park projects in 2022
completed_2022_park = []

for doc in civic_docs_data:
    text = doc['text']
    
    # Look for park mentions
    if 'park' in text.lower():
        # Check if completed in 2022
        if ('completed' in text.lower() or 'construction was completed' in text.lower()) and \
           ('2022' in text or 'November 2022' in text or 'December 2022' in text or 'October 2022' in text):
            
            # Extract project name and details
            lines = text.split('\n')
            for i, line in enumerate(lines):
                line = line.strip()
                if line and len(line) > 5 and not line.startswith('('):
                    # Skip headers
                    if any(skip in line for skip in ['Agenda', 'Public Works', 'Commission', 'Capital Improvement', 'Page', 'Item']):
                        continue
                    
                    # Check context around this line
                    context_start = max(0, i-3)
                    context_end = min(len(lines), i+15)
                    context = '\n'.join(lines[context_start:context_end])
                    
                    # Check if this is a park project completed in 2022
                    lower_context = context.lower()
                    if ('park' in lower_context and 
                        ('completed' in lower_context or 'construction was completed' in lower_context) and
                        ('2022' in context or 'November 2022' in context)):
                        
                        # Clean up project name
                        project_name = line
                        if 'Updates:' in project_name:
                            continue
                        if project_name.startswith('•'):
                            project_name = project_name[1:].strip()
                        
                        completed_2022_park.append({
                            'Project_Name': project_name,
                            'Source': doc['filename']
                        })

print("Park projects completed in 2022 found:", len(completed_2022_park))

for proj in completed_2022_park:
    print(f"- {proj['Project_Name']}")

# Now match with funding data
total_funding = 0
matched_projects = []

for doc_proj in completed_2022_park:
    doc_name = doc_proj['Project_Name']
    
    # Try exact match first
    for fund in park_funding:
        if fund['Project_Name'] == doc_name:
            amount = int(fund['Amount'])
            total_funding += amount
            matched_projects.append({
                'name': doc_name,
                'amount': amount
            })
            print(f"Matched: {doc_name} - ${amount}")
            break
    else:
        # Try partial matching for common variations
        for fund in park_funding:
            fund_name = fund['Project_Name']
            # Check if key words match
            doc_words = set(doc_name.lower().split())
            fund_words = set(fund_name.lower().split())
            
            # Check for significant overlap (excluding common words)
            common_words = {'park', 'project', 'repair', 'repairs', 'improvement', 'improvements', 'and', 'the', 'a', 'an'}
            doc_key = doc_words - common_words
            fund_key = fund_words - common_words
            
            if len(doc_key & fund_key) >= 2:  # At least 2 key words match
                amount = int(fund['Amount'])
                total_funding += amount
                matched_projects.append({
                    'name': doc_name,
                    'funded_name': fund_name,
                    'amount': amount
                })
                print(f"Partial matched: {doc_name} -> {fund_name} - ${amount}")
                break

print(f"\nTotal funding for park projects completed in 2022: ${total_funding:,}")
print(f"Number of projects matched: {len(matched_projects)}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json'}

exec(code, env_args)
