code = """import json
import re

# Load civic documents
civic_docs = []
with open('var_functions.query_db:20', 'r') as f:
    civic_docs = json.load(f)

# Load funding data
funding_data = []
with open('var_functions.query_db:5', 'r') as f:
    funding_data = json.load(f)

print(f"Number of civic documents: {len(civic_docs)}")
print(f"Number of funding records: {len(funding_data)}")

# Build funding lookup map
funding_map = {}
for record in funding_data:
    proj_name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    funding_map[proj_name] = amount

# Function to extract park projects completed in 2022 from text
def extract_park_projects_2022(text):
    projects = []
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 10:
            continue
            
        # Skip headings and metadata
        skip_patterns = [
            'capital improvement', 'disaster recovery', 'prepared by', 
            'approved by', 'recommended action', 'discussion:', 'to:', 
            'subject:', 'public works', 'commission', 'agenda', 'page', 
            'item', 'date prepared:', 'meeting date:'
        ]
        
        if any(pattern in line.lower() for pattern in skip_patterns):
            continue
            
        # Clean line
        line_clean = re.sub(r'\(cid:\d+\)', '', line).strip()
        
        # Check if it's park-related
        is_park = 'park' in line_clean.lower() or 'playground' in line_clean.lower()
        
        if is_park:
            # Look for completion status in context
            context_start = max(0, i-10)
            context_end = min(len(lines), i+15)
            context = ' '.join(lines[context_start:context_end])
            
            # Check if completed in 2022
            if re.search(r'completed.*2022|2022.*completed|completion.*2022|november 2022', context, re.IGNORECASE):
                projects.append(line_clean)
    
    return projects

# Extract projects from all documents
all_park_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    projects = extract_park_projects_2022(text)
    all_park_projects.extend(projects)

# Remove duplicates
unique_projects = list(set(all_park_projects))
print(f"\nFound {len(unique_projects)} park projects completed in 2022")
for proj in unique_projects:
    print(f"- {proj}")

# Match with funding data
matched_projects = []
total_funding = 0

for proj_name in unique_projects:
    best_match = None
    best_score = 0
    
    for funded_name in funding_map.keys():
        # Calculate match score based on word overlap
        proj_words = set(proj_name.lower().replace('(', '').replace(')', '').split())
        funded_words = set(funded_name.lower().replace('(', '').replace(')', '').split())
        
        common_words = proj_words.intersection(funded_words)
        score = len(common_words)
        
        # Prefer longer matches
        if score > best_score:
            best_match = funded_name
            best_score = score
    
    funding_amount = 0
    if best_match and best_score >= 2:  # At least 2 matching words
        funding_amount = funding_map[best_match]
        matched_projects.append({
            'project_name': proj_name,
            'funded_name': best_match,
            'funding': funding_amount
        })
        total_funding += funding_amount

print(f"\nMatched {len(matched_projects)} projects with funding:")
for proj in matched_projects:
    print(f"- {proj['project_name']}: ${proj['funding']}")

print(f"\nTotal funding: ${total_funding}")

# Return result
result = str(total_funding)
print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
