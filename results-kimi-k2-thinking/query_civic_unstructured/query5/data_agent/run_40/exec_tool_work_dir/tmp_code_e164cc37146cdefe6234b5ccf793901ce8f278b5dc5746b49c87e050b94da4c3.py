code = """import json

# Load data
civic_docs_file = open('/tmp/tmp2d2u8k1a.json', 'r')
civic_docs = json.load(civic_docs_file)
civic_docs_file.close()

funding_file = open('/tmp/tmp0k5s9q8h.json', 'r')
funding_data = json.load(funding_file)
funding_file.close()

# Build funding lookup
funding_lookup = {}
for rec in funding_data:
    funding_lookup[rec.get('Project_Name','')] = int(rec.get('Amount',0))

# Process documents
total = 0
count = 0
projects = []

for doc in civic_docs:
    text = doc.get('text','')
    lines = text.split('\n')
    
    for i,line in enumerate(lines):
        line = line.strip()
        
        # Check for disaster project markers
        if line.find('(FEMA Project)') >= 0 or \
           line.find('(CalJPIA Project)') >= 0 or \
           line.find('(CalOES Project)') >= 0 or \
           line.find('FEMA/CalOES Project') >= 0:
            
            # Look for start date
            start = ''
            for j in range(i+1, min(i+6, len(lines))):
                nxt = lines[j].strip().lower()
                if nxt.find('st:') >= 0 or nxt.find('start:') >= 0:
                    start = lines[j].strip()
                    break
            
            # Check for 2022
            if start.find('2022') >= 0:
                amt = funding_lookup.get(line, 0)
                if amt > 0:
                    total += amt
                    count += 1
                    projects.append({'name': line, 'amount': amt})

# Output
output = {'total_funding': total, 'project_count': count, 'projects': projects}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
