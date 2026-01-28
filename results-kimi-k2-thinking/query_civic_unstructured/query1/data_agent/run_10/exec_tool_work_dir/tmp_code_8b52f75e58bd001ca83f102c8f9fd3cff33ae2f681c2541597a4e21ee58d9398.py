code = """import json
import re

# Load data files
data1 = var_functions.query_db:2
if isinstance(data1, str) and data1.endswith('.json'):
    with open(data1, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = data1

data2 = var_functions.query_db:5
if isinstance(data2, str) and data2.endswith('.json'):
    with open(data2, 'r') as f:
        funding_records = json.load(f)
else:
    funding_records = data2

# Build funding map > $50k
funding_map = {}
for rec in funding_records:
    try:
        amt = int(rec['Amount'])
        if amt > 50000:
            funding_map[rec['Project_Name']] = amt
    except:
        pass

# Find capital projects in design status
all_design_projects = []

for doc in civic_docs:
    content = doc.get('text', '')
    
    if 'Capital Improvement Projects (Design)' not in content:
        continue
    
    start_idx = content.find('Capital Improvement Projects (Design)')
    end_idx = len(content)
    
    # Find end of section
    section_end_markers = ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects', 'PUBLIC WORKS QUARTERLY UPDATE']
    for marker in section_end_markers:
        pos = content.find(marker, start_idx + 50)
        if pos > 0:
            end_idx = min(end_idx, pos)
    
    section = content[start_idx:end_idx]
    lines = section.split('\n')
    
    in_project_list = False
    for line in lines:
        line_clean = line.strip()
        if not line_clean:
            continue
        
        # Skip header/footer lines
        if any(skip in line_clean for skip in ['Page', 'Agenda Item', 'RECOMMENDED ACTION', 'DISCUSSION:', 'To:', 'Prepared by:', 'Approved by:', 'Updates:', 'Project Schedule:', 'Estimated Schedule:']):
            continue
        
        # Skip bullet points, update lines, etc.
        if line_clean[0] in ['•', '-', '◦', '(', ')']:
            continue
        
        if line_clean.isupper() and len(line_clean) < 60:
            continue
        
        if len(line_clean) < 10:
            continue
        
        # Avoid scheduling/update lines
        update_indicators = ['Staff', 'City', 'Complete', 'Advertise', 'Begin', 'Working', 'Submitted']
        if any(indicator in line_clean for indicator in update_indicators) and len(line_clean.split()) < 5:
            continue
        
        cleaned_name = line_clean.strip('•-– ')
        all_design_projects.append(cleaned_name)

# Remove duplicates
all_design_projects = list(set(all_design_projects))

# Match function
def normalize(name):
    n = name.lower()
    n = n.replace('project', '').replace('improvements', '').replace('improvement', '')
    n = n.replace('repairs', '').replace('repair', '').replace('replacement', '')
    n = re.sub(r'\s*\([^)]*\)$', '', n)
    n = re.sub(r'[^a-z0-9\s]', '', n)
    return ' '.join(n.split())

# Build normalized funding lookup
funding_lookup = {}
for proj_name in funding_map:
    normalized = normalize(proj_name)
    funding_lookup[normalized] = proj_name

count = 0
matches = []

for design_proj in all_design_projects:
    norm_design = normalize(design_proj)
    
    # Direct match in normalized map
    if norm_design in funding_lookup:
        count += 1
        matches.append({
            'design': design_proj,
            'funding': funding_lookup[norm_design],
            'amount': funding_map[funding_lookup[norm_design]]
        })
        continue
    
    # Substring matching
    for norm_funding, original_funding in funding_lookup.items():
        if norm_design in norm_funding or norm_funding in norm_design:
            count += 1
            matches.append({
                'design': design_proj,
                'funding': original_funding,
                'amount': funding_map[original_funding]
            })
            break
        
        # Word-level matching for longer names
        if len(norm_design) > 15 and len(norm_funding) > 15:
            design_words = set(norm_design.split())
            funding_words = set(norm_funding.split())
            
            if len(design_words.intersection(funding_words)) >= 3:
                count += 1
                matches.append({
                    'design': design_proj,
                    'funding': original_funding,
                    'amount': funding_map[original_funding]
                })
                break

result = {'count': count, 'matching_projects': matches}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
