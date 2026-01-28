code = """import json

# Read the file containing paper docs
file_path = locals()['var_function-call-7710092852733637321']
with open(file_path, 'r') as f:
    papers = json.load(f)

matching_titles = []

for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    
    # Extract Title
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename

    # Extract Year
    # Look for 2016 in the first 1000 characters
    header = text[:1000]
    if '2016' in header:
        year_match = True
    else:
        year_match = False
        
    # Extract Domain
    # Check for 'physical activity' in the full text
    if 'physical activity' in text.lower():
        domain_match = True
    else:
        domain_match = False
        
    if year_match and domain_match:
        matching_titles.append(title)

print("__RESULT__:")
print(json.dumps(matching_titles))"""

env_args = {'var_function-call-8028739805573563198': ['paper_docs'], 'var_function-call-8028739805573566195': ['Citations', 'sqlite_sequence'], 'var_function-call-12468047497345130248': 'file_storage/function-call-12468047497345130248.json', 'var_function-call-7710092852733637321': 'file_storage/function-call-7710092852733637321.json'}

exec(code, env_args)
