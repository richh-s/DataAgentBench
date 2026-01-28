code = """import json
import re

# Load the file path from the previous step
file_path = locals()['var_function-call-8411561626965281580']

with open(file_path, 'r') as f:
    papers = json.load(f)

matching_titles = []

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check domain
    if 'physical activity' in text.lower():
        # Check year 2016 in the beginning of the text (metadata usually at top)
        # We look for "2016" or "'16" in the first 1000 characters.
        header = text[:1000]
        
        # Check for explicit 2016
        if re.search(r'\b2016\b', header):
            matching_titles.append(title)
        # Check for '16 convention (e.g. CHI '16)
        elif re.search(r"'\s?16\b", header): 
            matching_titles.append(title)

print("__RESULT__:")
print(json.dumps(matching_titles))"""

env_args = {'var_function-call-14900117783735274401': 'file_storage/function-call-14900117783735274401.json', 'var_function-call-8411561626965281580': 'file_storage/function-call-8411561626965281580.json'}

exec(code, env_args)
