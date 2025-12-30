code = """import json

# Load papers from the stored file
# The key for the file path is var_function-call-1860394560099388718
file_path = locals()['var_function-call-1860394560099388718']

with open(file_path, 'r') as f:
    papers = json.load(f)

matched_titles = []

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check Year 2016
    # Look for 2016 in the first 2000 chars
    header = text[:2000]
    
    # Simple check for 2016 in header/metadata area
    if '2016' in header:
        # Check Domain 'physical activity' in the full text
        if 'physical activity' in text.lower():
            matched_titles.append(title)

print("__RESULT__:")
print(json.dumps(matched_titles))"""

env_args = {'var_function-call-10819517614772727470': 'file_storage/function-call-10819517614772727470.json', 'var_function-call-1860394560099388718': 'file_storage/function-call-1860394560099388718.json'}

exec(code, env_args)
