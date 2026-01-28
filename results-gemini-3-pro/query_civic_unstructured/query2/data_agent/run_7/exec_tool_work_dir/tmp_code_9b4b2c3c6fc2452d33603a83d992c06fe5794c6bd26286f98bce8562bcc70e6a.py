code = """import json
import re

# Get filenames from variables
filename_funding = locals()['var_function-call-17324143026383402211']
filename_civic = locals()['var_function-call-17324143026383404966']

# Load Funding Data
with open(filename_funding, 'r') as f:
    funding_data = json.load(f)

# Load Civic Docs
with open(filename_civic, 'r') as f:
    civic_docs = json.load(f)

# Filter Park Projects
park_projects = []
for record in funding_data:
    name = record.get('Project_Name', '')
    if 'park' in name.lower() or 'playground' in name.lower():
        park_projects.append(name)

print("Park Projects (Funding):", park_projects)

completed_2022_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    # Normalize: remove multiple spaces and newlines
    text = re.sub(r'\s+', ' ', text)
    
    for proj in park_projects:
        # Find project name in text
        pattern = re.escape(proj)
        for match in re.finditer(pattern, text, re.IGNORECASE):
            # Get context: next 500 chars
            start = match.end()
            context = text[start:start+500].lower()
            
            # Check 1: "Construction was completed [Month] 2022"
            if re.search(r'construction was completed [a-z]+ 2022', context):
                completed_2022_projects.add(proj)
                continue
            
            # Check 2: "Complete Construction: [Month/Season] 2022"
            if re.search(r'complete construction:? [a-z]+ 2022', context):
                completed_2022_projects.add(proj)
                continue

            # Check 3: "completed in 2022"
            if re.search(r'completed in [a-z]* ?2022', context):
                 completed_2022_projects.add(proj)
                 continue

print("Completed Park Projects in 2022:", list(completed_2022_projects))

total_funding = 0
for record in funding_data:
    if record['Project_Name'] in completed_2022_projects:
        val = record.get('Amount', 0)
        total_funding += int(val)

print('__RESULT__:')
print(json.dumps(total_funding))"""

env_args = {'var_function-call-5219184128043879497': ['Funding'], 'var_function-call-5219184128043880064': ['civic_docs'], 'var_function-call-17324143026383402211': 'file_storage/function-call-17324143026383402211.json', 'var_function-call-17324143026383404966': 'file_storage/function-call-17324143026383404966.json'}

exec(code, env_args)
