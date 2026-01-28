code = """import json
import re

# Load data from storage
mongo_path = locals().get('var_functions.query_db:10')
funding_path = locals().get('var_functions.query_db:22')

# Load MongoDB documents
mongo_docs = []
if isinstance(mongo_path, str) and mongo_path.endswith('.json'):
    with open(mongo_path, 'r') as f:
        mongo_docs = json.load(f)
else:
    mongo_docs = mongo_path or []

# Load funding records with amount > 50000
funding_records = []
if isinstance(funding_path, str) and funding_path.endswith('.json'):
    with open(funding_path, 'r') as f:
        funding_records = json.load(f)
else:
    funding_records = funding_path or []

print('Loaded {0} documents and {1} funding records'.format(len(mongo_docs), len(funding_records)))

# Extract design project names from MongoDB documents
all_design_project_names = []

for doc in mongo_docs:
    text = doc.get('text', '')
    
    # Look for the Design section
    design_marker = 'Capital Improvement Projects (Design)'
    construct_marker = 'Capital Improvement Projects (Construction)'
    
    if design_marker in text:
        # Find the start of design section
        design_start = text.index(design_marker)
        construct_start = text.index(construct_marker) if construct_marker in text else len(text)
        
        # Extract the design section
        design_section = text[design_start:construct_start]
        
        # Split into lines and extract project names
        for line in design_section.split('\n'):
            line = line.strip()
            # Simple heuristics for project names
            if line and len(line) > 10 and not line.startswith('(') and not line.endswith(':'):
                # Skip header/footer lines
                skip_words = ['Page', 'Item', 'Agenda', 'Public Works', 'Commission', 'Subject:', 'To:', 'From:', 'Updates:', 'Schedule:', 'Complete Design']
                should_skip = any(word in line for word in skip_words)
                if not should_skip and line not in all_design_project_names:
                    all_design_project_names.append(line)

print('Found {0} potential design projects'.format(len(all_design_project_names)))

# Build funding lookup
funding_lookup = {}
for rec in funding_records:
    name = rec.get('Project_Name', '')
    amount = int(rec.get('Amount', 0))
    if name:
        funding_lookup[name] = amount

# Match design projects with funding
matched_count = 0
matched_list = []

for design_proj in all_design_project_names:
    design_lower = design_proj.lower()
    
    for funded_name in funding_lookup:
        funded_lower = funded_name.lower()
        
        # Remove common words
        common_terms = {'project', 'improvements', 'repair', 'repairs', 'road', 'and', 'the', 'improvement'}
        
        design_words = set(design_lower.split()) - common_terms
        funded_words = set(funded_lower.split()) - common_terms
        
        # Check for significant overlap
        overlap = design_words.intersection(funded_words)
        
        if len(overlap) >= 2:  # At least 2 significant words match
            matched_count += 1
            if len(matched_list) < 3:  # Store a few examples
                matched_list.append({
                    'design_name': design_proj,
                    'funded_name': funded_name,
                    'amount': funding_lookup[funded_name]
                })
            break

# Create the final result
result_dict = {
    'count': matched_count,
    'sample_matches': matched_list
}

print('__RESULT__:')
print(json.dumps(result_dict))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
