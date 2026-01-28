code = """import json

# Load the paper docs from the previous tool output
file_path = locals()['var_function-call-16535487898167590868']
with open(file_path, 'r') as f:
    papers = json.load(f)

relevant_titles = []

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    
    # Check for Year 2016
    # Heuristic: Look for "2016" in the first 2000 characters (header/abstract/copyright)
    header_text = text[:3000]
    if '2016' in header_text:
        # Check for Domain 'physical activity'
        # Heuristic: simple substring search in the full text (or maybe first 3000 to be safer against references?)
        # The prompt says "Fields like domain... may contain multiple values". 
        # But references might contain "physical activity".
        # However, usually the domain is mentioned in Abstract, Keywords, or Introduction.
        # Let's search in the whole text as "physical activity" is a specific phrase.
        if 'physical activity' in text.lower():
            title = filename.replace('.txt', '')
            relevant_titles.append(title)

print("__RESULT__:")
print(json.dumps(relevant_titles))"""

env_args = {'var_function-call-9156106444127035660': 'file_storage/function-call-9156106444127035660.json', 'var_function-call-16535487898167590868': 'file_storage/function-call-16535487898167590868.json'}

exec(code, env_args)
