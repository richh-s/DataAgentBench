code = """import json
import re

# Load the data
civic_docs_file = var_functions.query_db:2
if isinstance(civic_docs_file, str) and civic_docs_file.endswith('.json'):
    with open(civic_docs_file, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_docs_file

funding_file = var_functions.query_db:5
if isinstance(funding_file, str) and funding_file.endswith('.json'):
    with open(funding_file, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = funding_file

# Extract funding projects > $50,000
funding_projects = {}
for item in funding_data:
    try:
        amount = int(item['Amount'])
        if amount > 50000:
            funding_projects[item['Project_Name']] = amount
    except:
        continue

# Extract capital design projects from civic documents
capital_design_projects = []
skip_phrases = [
    'Page', 'Agenda Item', 'RECOMMENDED ACTION', 'DISCUSSION:',
    'To:', 'Prepared by:', 'Approved by:', 'Date prepared:',
    'Meeting date:', 'Subject:', 'Updates:', 'Project Schedule:',
    'Estimated Schedule:', 'Complete Design:', 'Advertise:',
    'Begin Construction:', 'Staff is', 'City is', 'City has',
    'Project is', 'Staff has', 'Public Works Commission'
]

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section start
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start == -1:
        continue
    
    # Find where design section ends
    end_markers = [
        'Capital Improvement Projects (Construction)',
        'Capital Improvement Projects (Not Started)',
        'Disaster Recovery Projects'
    ]
    
    design_end = len(text)
    for marker in end_markers:
        pos = text.find(marker, design_start + 50)
        if pos > 0:
            design_end = min(design_end, pos)
    
    design_section = text[design_start:design_end]
    lines = design_section.split('\n')
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Skip unwanted lines
        if any(phrase in line for phrase in skip_phrases):
            continue
        
        # Skip all caps short lines (headers)
        if line.isupper() and len(line) < 60:
            continue
        
        # Skip lines starting with symbols
        if line[0] in ['•', '-', '–', '(', ')', '◦', '■']:
            continue
        
        # Skip very short lines
        if len(line) < 10:
            continue
        
        # Clean and add project name
        project_name = line.strip('•-– ')
        
        # Additional filter: skip if it looks like a status update
        update_words = ['Staff', 'City', 'Project', 'Complete', 'Advertise', 'Begin']
        if any(word in project_name for word in update_words) and len(project_name.split()) < 5:
            continue
        
        if project_name:
            capital_design_projects.append(project_name)

# Remove duplicates
capital_design_projects = list(set(capital_design_projects))

# Match design projects with funding projects
def get_simple_name(name):
    # Convert to lowercase and remove common words and suffixes
    simple = name.lower()
    simple = simple.replace('project', '').replace('improvements', '').replace('improvement', '')
    simple = simple.replace('repairs', '').replace('repair', '').replace('replacement', '')
    
    # Remove parenthetical suffixes like (FEMA Project)
    simple = re.sub(r'\s*\([^)]*\)\s*$', '', simple)
    
    # Remove extra whitespace
    simple = ' '.join(simple.split())
    
    return simple

# Build a mapping of simple names to original names
funding_simple_map = {}
for funding_name in funding_projects:
    simple = get_simple_name(funding_name)
    funding_simple_map[simple] = funding_name

# Count matches
count = 0
matched_pairs = []

for design_project in capital_design_projects:
    design_simple = get_simple_name(design_project)
    
    # Try exact simple match first
    if design_simple in funding_simple_map:
        count += 1
        matched_pairs.append({
            'design': design_project,
            'funding': funding_simple_map[design_simple],
            'amount': funding_projects[funding_simple_map[design_simple]]
        })
        continue
    
    # Try partial matching for longer names
    if len(design_simple) > 15:
        design_words = set([w for w in design_simple.split() if len(w) > 3])
        
        for funding_simple, funding_name in funding_simple_map.items():
            if len(funding_simple) > 15:
                funding_words = set([w for w in funding_simple.split() if len(w) > 3])
                
                # If they share at least 3 key words, consider it a match
                common = design_words.intersection(funding_words)
                if len(common) >= 3:
                    count += 1
                    matched_pairs.append({
                        'design': design_project,
                        'funding': funding_name,
                        'amount': funding_projects[funding_name]
                    })
                    break

print('__RESULT__:')
print(json.dumps({
    'count': count,
    'matched_pairs': matched_pairs
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
