code = """import json

# Read the file containing the papers
with open(locals()['var_function-call-1502338921683613399'], 'r') as f:
    papers = json.load(f)

matching_titles = []

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    
    # Extract Title
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
        
    # Extract Year
    # Look for 2016 in the first 1000 characters to be safe
    header = text[:1000]
    if '2016' in header:
        year = 2016
    else:
        year = None
        
    # Check Domain
    # Check if 'physical activity' is in the text (case insensitive)
    if 'physical activity' in text.lower():
        domain_match = True
    else:
        domain_match = False
        
    if year == 2016 and domain_match:
        matching_titles.append(title)

print("__RESULT__:")
print(json.dumps(matching_titles))"""

env_args = {'var_function-call-18065361926361048824': 'file_storage/function-call-18065361926361048824.json', 'var_function-call-1502338921683613399': 'file_storage/function-call-1502338921683613399.json'}

exec(code, env_args)
