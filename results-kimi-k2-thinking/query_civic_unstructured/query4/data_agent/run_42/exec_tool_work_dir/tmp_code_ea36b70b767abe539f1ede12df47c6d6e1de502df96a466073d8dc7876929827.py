code = """import json

# Get the actual file paths
mongo_path = locals()['var_functions.query_db:42']
funding_path = locals()['var_functions.query_db:4']

# Read the data
with open(mongo_path) as f:
    mongo_docs = json.load(f)

with open(funding_path) as f:
    funding_recs = json.load(f)

# Build funding lookup
d = {}
for r in funding_recs:
    d[r['Project_Name']] = int(r['Amount'])

# Extract Spring 2022 projects
spring = set()

for doc in mongo_docs:
    text = doc.get('text', '')
    if 'Spring' in text and '2022' in text:
        lines = text.split('\n')
        for i in range(len(lines)):
            line = lines[i]
            if 'Begin Construction' in line and '2022' in line:
                # Look back to find project name
                for j in range(i-1, max(i-8, -1), -1):
                    candidate = lines[j].strip()
                    if candidate and not candidate.startswith('(') and 'Schedule' not in candidate:
                        if len(candidate) > 5:
                            spring.add(candidate)
                            break

# Match with funding
matches = []
for proj in spring:
    if proj in d:
        matches.append({'name': proj, 'funding': d[proj]})

# Calculate totals
count = len(matches)
total_funding = sum(m['funding'] for m in matches)

# Create output string
output = 'COUNT=' + str(count) + ', TOTAL_FUNDING=$' + str(total_funding)

# Print in required format
print('__RESULT__:')
print(output)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
