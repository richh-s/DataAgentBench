code = """import json
import re

# Correct key name with hyphens
file_path = locals()['var_function-call-4943697616696163916']
with open(file_path, 'r') as f:
    papers = json.load(f)

results = []

for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    
    # Extract year from first 2000 chars
    # Regex for years 2017-2029
    header_text = text[:2000]
    match = re.search(r'\b(201[7-9]|202[0-9])\b', header_text)
    
    year = None
    if match:
        year = int(match.group(1))
        
    # Check empirical in full text
    is_empirical = 'empirical' in text.lower()
    
    if year and year > 2016 and is_empirical:
        title = filename.replace('.txt', '')
        results.append({'title': title, 'year': year})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-9891317091661830869': 'file_storage/function-call-9891317091661830869.json', 'var_function-call-10963661510414454345': ['paper_docs'], 'var_function-call-5664922713276342655': [], 'var_function-call-4943697616696163916': 'file_storage/function-call-4943697616696163916.json'}

exec(code, env_args)
