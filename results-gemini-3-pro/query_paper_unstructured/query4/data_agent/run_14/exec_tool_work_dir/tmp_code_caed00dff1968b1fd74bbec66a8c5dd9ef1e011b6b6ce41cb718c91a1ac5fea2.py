code = """import json

# Load the paper docs
with open(locals()['var_function-call-1932226808801670089'], 'r') as f:
    papers = json.load(f)

filtered_titles = []

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    
    # 1. Check Year 2016
    # Check first 2000 chars for "2016"
    # Also check for conference patterns if possible, but "2016" is a strong indicator in the header.
    # The example had "UBICOMP '15, ... 2015" in the first line.
    header_text = text[:1000]
    is_2016 = "2016" in header_text
    
    # 2. Check Domain "physical activity"
    # Case insensitive
    is_physical_activity = "physical activity" in text.lower()
    
    if is_2016 and is_physical_activity:
        # Extract title
        if filename.endswith('.txt'):
            title = filename[:-4]
        else:
            title = filename
        filtered_titles.append(title)

print("__RESULT__:")
print(json.dumps(filtered_titles))"""

env_args = {'var_function-call-1702073112922347921': 'file_storage/function-call-1702073112922347921.json', 'var_function-call-1932226808801670089': 'file_storage/function-call-1932226808801670089.json'}

exec(code, env_args)
