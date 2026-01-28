code = """import json
import re

# Load funding data
with open(var_functions.query_db:18, 'r') as f:
    funding_records = json.load(f)

# Load civic documents
with open(var_functions.query_db:19, 'r') as f:
    civic_docs = json.load(f)

# Create funding dictionary (amount > 50000)
funding_dict = {}
for rec in funding_records:
    try:
        amt = int(rec.get('Amount', 0))
        if amt > 50000:
            name = rec.get('Project_Name', '').strip()
            if name:
                key = re.sub(r'[^\w\s]', '', name.lower())
                funding_dict[key] = {
                    'original_name': name,
                    'amount': amt
                }
    except:
        pass

print('Funding records > $50K: ' + str(len(funding_dict)))

# Extract capital design projects
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    design_match = re.search(r'Capital Improvement Projects \(Design\)(.*?)(?=Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|DISASTER RECOVERY PROJECTS|$)', 
                             text, re.DOTALL | re.IGNORECASE)
    
    if design_match:
        design_text = design_match.group(1)
        lines = design_text.split('\n')
        
        for i, line in enumerate(lines):
            line = line.strip()
            if not line or len(line) < 10:
                continue
            
            # Skip headers and markers
            if any(marker in line for marker in ['cid:', 'Updates:', 'Project Schedule:', 'Complete Design:', 'Advertise:', 'Begin Construction:', 'Page']):
                continue
            
            if line.isupper() and len(line.split()) <= 3:
                continue
            
            # Look for project name lines
            if line[0].isupper() and len(line.split()) >= 2:
                # Verify it's a project by checking following lines
                is_project = False
                for j in range(i+1, min(i+4, len(lines))):
                    next_line = lines[j].lower()
                    if 'updates:' in next_line or 'project schedule:' in next_line:
                        is_project = True
                        break
                
                # Also accept lines that end with common project suffixes
                if (is_project or 
                    line.endswith(('Project', 'Improvements', 'Repairs', 'Drainage', 'Study', 'Upgrades')) or
                    any(keyword in line for keyword in ['Improvements', 'Drainage', 'Repairs', 'Replacement', 'System'])):
                    
                    if line not in design_projects:
                        design_projects.append(line)

print('Capital design projects found: ' + str(len(design_projects)))

# Match projects with funding
matched = []
for project in design_projects:
    proj_key = re.sub(r'[^\w\s]', '', project.lower())
    
    if proj_key in funding_dict:
        matched.append(project)
    else:
        # Fuzzy matching
        for fund_key, fund_info in funding_dict.items():
            # Check if project name is contained in funded name or vice versa
            if (proj_key in fund_key or fund_key in proj_key):
                # Share at least 2 words
                proj_words = set(proj_key.split())
                fund_words = set(fund_key.split())
                if len(proj_words.intersection(fund_words)) >= 2:
                    matched.append(project)
                    break

unique_matches = list(set(matched))
print('Matched projects: ' + str(len(unique_matches)))

if unique_matches:
    print('\nSample matches:')
    for i, proj in enumerate(unique_matches[:5]):
        print(str(i+1) + '. ' + proj)

result = len(unique_matches)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:19': 'file_storage/functions.query_db:19.json'}

exec(code, env_args)
