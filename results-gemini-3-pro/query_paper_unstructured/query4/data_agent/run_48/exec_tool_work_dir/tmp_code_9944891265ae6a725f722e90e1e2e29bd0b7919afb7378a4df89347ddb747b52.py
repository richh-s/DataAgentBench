code = """import json
import re

# Load the documents
with open(locals()['var_function-call-11583602006326947447'], 'r') as f:
    # The file might contain a list of dicts. The output from query_db is a list.
    docs = json.load(f)

# If the result is wrapped in a list (which query_db usually returns), use it.
if isinstance(docs, dict) and 'results' in docs:
    docs = docs['results']

filtered_titles = []

for doc in docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check for Year 2016
    # Look for "2016" in the first 2000 characters.
    # Common formats: "CHI '16", "CHI 2016", "Copyright 2016", "September 2016"
    # To be safe, just checking if "2016" is present in the header area seems reasonable for this task.
    # However, a paper published in 2016 might have references to 2016, but usually the publication date is prominent.
    # The example showed "UBICOMP '15... 2015". So searching for 2016 in the beginning is good.
    header_text = text[:3000]
    if '2016' in header_text:
        # Check for Domain 'physical activity'
        # Domain matching should be case-insensitive substring
        if 'physical activity' in text.lower():
            filtered_titles.append(title)
            
print("__RESULT__:")
print(json.dumps(filtered_titles))"""

env_args = {'var_function-call-7152381321579556689': 'file_storage/function-call-7152381321579556689.json', 'var_function-call-11583602006326947447': 'file_storage/function-call-11583602006326947447.json'}

exec(code, env_args)
