code = """import json
import re

# Load the paper docs
# The previous tool call stored the result in a file.
# The key is var_function-call-12545833755252698609
file_path = locals()['var_function-call-12545833755252698609']

with open(file_path, 'r') as f:
    papers = json.load(f)

food_papers = []

for p in papers:
    filename = p.get('filename', '')
    text = p.get('text', '')
    title = filename.replace('.txt', '')
    
    # Check title
    if 'food' in title.lower():
        food_papers.append(title)
        continue
        
    # Check keywords
    # Look for "Author Keywords" or just "Keywords"
    # and take the text until the next section (often "ACM Classification" or "Introduction")
    # A simple regex to grab the block:
    match = re.search(r'(?:Author Keywords|Keywords)([\s\S]{1,500}?)(?:ACM Classification|INTRODUCTION|ABSTRACT)', text, re.IGNORECASE)
    if match:
        keywords_block = match.group(1).lower()
        if 'food' in keywords_block:
            food_papers.append(title)
            continue
            
    # As a fallback, maybe check if "food" appears frequently? 
    # But let's verify with just Title and Keywords first.
    # The prompt lists "food" as a domain, so it should be prominent.

print("__RESULT__:")
print(json.dumps(food_papers))"""

env_args = {'var_function-call-2991259327904718266': ['paper_docs'], 'var_function-call-2991259327904718481': ['Citations', 'sqlite_sequence'], 'var_function-call-10512507186521432510': 'file_storage/function-call-10512507186521432510.json', 'var_function-call-12545833755252698609': 'file_storage/function-call-12545833755252698609.json'}

exec(code, env_args)
