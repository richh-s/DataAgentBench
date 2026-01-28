code = """import json
import re

# Load funding data
funding_file = locals()['var_functions.query_db:38']
with open(funding_file) as f:
    funding_data = json.load(f)

# Load civic documents
civic_file = locals()['var_functions.query_db:40']
with open(civic_file) as f:
    civic_documents = json.load(f)

# Create sets for comparison
high_funding_set = set()
for record in funding_data:
    if int(record['Amount']) > 50000:
        high_funding_set.add(record['Project_Name'])

design_set = set()

# Process each document
for doc in civic_documents:
    text_content = doc.get('text', '')
    
    # Find design projects section
    design_start = text_content.find('Capital Improvement Projects (Design)')
    if design_start > 0:
        construction_start = text_content.find('Capital Improvement Projects (Construction)', design_start)
        if construction_start == -1:
            section_text = text_content[design_start:]
        else:
            section_text = text_content[design_start:construction_start]
        
        # Extract lines that look like project names
        for line in section_text.split('\n'):
            line = line.strip()
            if len(line) > 15 and not line.startswith('('):
                if 'Updates:' not in line and 'Schedule:' not in line:
                    clean_line = line.replace('(cid:190)', '').replace('(cid:131)', '').strip()
                    design_set.add(clean_line)

# Count matches
exact_matches = high_funding_set.intersection(design_set)
match_count = len(exact_matches)

# If no exact matches, try normalized matching
if match_count == 0:
    norm_funding = {name.lower().strip() for name in high_funding_set}
    for design_name in design_set:
        if design_name.lower().strip() in norm_funding:
            match_count += 1

result = {
    'total_high_funding': len(high_funding_set),
    'total_design_projects': len(design_set),
    'matching_projects': match_count
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:32': [{'count': '276'}], 'var_functions.query_db:36': [], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json'}

exec(code, env_args)
