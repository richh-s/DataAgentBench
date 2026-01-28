code = """import json
import re

# Load data files
civic_file = var_functions.query_db:2
funding_file = var_functions.query_db:5

if isinstance(civic_file, str) and civic_file.endswith('.json'):
    with open(civic_file, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_file

if isinstance(funding_file, str) and funding_file.endswith('.json'):
    with open(funding_file, 'r') as f:
        funding_records = json.load(f)
else:
    funding_records = funding_file

# Get funding projects > $50k as a dictionary
funding_projects = {}
for rec in funding_records:
    try:
        if int(rec['Amount']) > 50000:
            funding_projects[rec['Project_Name']] = int(rec['Amount'])
    except:
        pass

# Extract capital projects with design status from civic docs
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find capital improvement projects in design phase
    if 'Capital Improvement Projects (Design)' not in text:
        continue
    
    # Extract section for design projects
    start = text.find('Capital Improvement Projects (Design)')
    end_pos = len(text)
    
    # Look for where this section ends
    end_markers = [
        'Capital Improvement Projects (Construction)',
        'Capital Improvement Projects (Not Started)', 
        'Disaster Recovery Projects',
        'FEMA PROJECTS'
    ]
    
    for marker in end_markers:
        pos = text.find(marker, start + 50)
        if pos > 0:
            end_pos = min(end_pos, pos)
    
    section = text[start:end_pos]
    
    # Look for project name patterns - typically bold or standalone lines
    # Split by newlines and look for lines that could be project names
    lines = section.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Skip headers and metadata
        skip_terms = ['Page', 'Agenda Item', 'RECOMMENDED ACTION', 'DISCUSSION', 'To:', 'Prepared by', 'Approved by', 'Updates:', 'Project Schedule', 'Estimated Schedule', 'Complete Design', 'Advertise:', 'Begin Construction', 'Staff is', 'City is', 'Project is', 'Subject:']
        if any(term in line for term in skip_terms):
            continue
        
        # Skip all-caps short headers
        if line.isupper() and len(line) < 60:
            continue
        
        # Skip lines starting with symbols or parens
        if line[0] in ['•', '-', '–', '◦', '■', '(', ')']:
            continue
        
        # Skip very short lines
        if len(line) < 10:
            continue
        
        # Skip lines that are mostly dates/numbers
        if re.match(r'^[A-Za-z]+ \d{4}$', line):
            continue
        
        # Clean up and add
        cleaned = line.strip('•-– ')
        
        # Filter out update lines
        update_words = ['Staff', 'City', 'Project', 'Complete', 'Advertise', 'Begin', 'Working', 'Submitted', 'Schedule']
        if any(word in cleaned for word in update_words) and len(cleaned.split()) < 4:
            continue
        
        if cleaned:
            design_projects.append(cleaned)

# Remove exact duplicates
design_projects = list(set(design_projects))

# Now match with funding data using flexible string matching
counted_projects = []

for design in design_projects:
    design_lc = design.lower().replace('project', '').strip()
    
    # Try several matching strategies
    for funding in funding_projects:
        funding_lc = funding.lower().replace('project', '').strip()
        
        # Strategy 1: Direct containment
        if design_lc in funding_lc or funding_lc in design_lc:
            counted_projects.append({
                'design': design,
                'funding': funding,
                'amount': funding_projects[funding]
            })
            break
        
        # Strategy 2: Remove common suffixes/prefixes and match
        d_clean = re.sub(r'\s*\([^)]*\)$', '', design_lc)
        f_clean = re.sub(r'\s*\([^)]*\)$', '', funding_lc)
        
        if d_clean in f_clean or f_clean in d_clean:
            counted_projects.append({
                'design': design,
                'funding': funding,
                'amount': funding_projects[funding]
            })
            break
        
        # Strategy 3: Word overlap for longer names
        if len(design_lc) > 15 and len(funding_lc) > 15:
            design_words = set([w for w in re.findall(r'\b\w{4,}\b', design_lc)])
            funding_words = set([w for w in re.findall(r'\b\w{4,}\b', funding_lc)])
            
            if len(design_words.intersection(funding_words)) >= 2:
                counted_projects.append({
                    'design': design,
                    'funding': funding,
                    'amount': funding_projects[funding]
                })
                break

# Final count
count = len(counted_projects)

result = {
    'count': count,
    'matches': counted_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
