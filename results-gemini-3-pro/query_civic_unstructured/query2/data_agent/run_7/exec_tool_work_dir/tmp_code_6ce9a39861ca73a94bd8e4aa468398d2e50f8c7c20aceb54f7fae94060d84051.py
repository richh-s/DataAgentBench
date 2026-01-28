code = """import json
import re

# Load Funding Data
with open('var_function-call-17324143026383402211.json', 'r') as f:
    funding_data = json.load(f)

# Load Civic Docs
with open('var_function-call-17324143026383404966.json', 'r') as f:
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
    # Normalize a bit: remove multiple spaces
    text = re.sub(r'\s+', ' ', text)
    
    for proj in park_projects:
        # Find project name in text
        # Use re.escape to handle special chars in name
        pattern = re.escape(proj)
        for match in re.finditer(pattern, text, re.IGNORECASE):
            # Get context: next 1000 chars
            start = match.end()
            context = text[start:start+1000].lower()
            
            # Check 1: "Construction was completed [Month] 2022"
            # Regex: construction was completed \w+ 2022
            if re.search(r'construction was completed \w+ 2022', context):
                completed_2022_projects.add(proj)
                continue
            
            # Check 2: "Complete Construction: [Month/Season] 2022"
            # Regex: complete construction:? \w+ 2022
            if re.search(r'complete construction:? \w+ 2022', context):
                completed_2022_projects.add(proj)
                continue

            # Check 3: "completed in 2022" (generic)
            if re.search(r'completed in \w* ?2022', context):
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
