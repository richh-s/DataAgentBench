code = """import json
import re

file_path = locals()['var_function_call_4943697616696163916']
with open(file_path, 'r') as f:
    papers = json.load(f)

# If papers is just a list of dicts
results = []
years_found = set()

for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    
    # Extract year: look for year in first 2000 chars
    # Regex for years 2017-2029
    # We look for a standalone year
    header_text = text[:2000]
    match = re.search(r'\b(201[7-9]|202[0-9])\b', header_text)
    
    year = None
    if match:
        year = int(match.group(1))
        
    # Check empirical
    # Check if "empirical" is in the full text (or maybe first 5000 chars to be safe/faster?)
    # "empirical" usually appears in abstract or introduction if it's the contribution type.
    # But let's check full text to be safe, searching case-insensitive.
    is_empirical = 'empirical' in text.lower()
    
    if year and year > 2016 and is_empirical:
        title = filename.replace('.txt', '')
        results.append({'title': title, 'year': year})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-9891317091661830869': 'file_storage/function-call-9891317091661830869.json', 'var_function-call-10963661510414454345': ['paper_docs'], 'var_function-call-5664922713276342655': [], 'var_function-call-4943697616696163916': 'file_storage/function-call-4943697616696163916.json'}

exec(code, env_args)
