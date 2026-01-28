code = """import json
import re

file_path = locals()['var_function-call-4943697616696163916']
with open(file_path, 'r') as f:
    papers = json.load(f)

debug_info = []

for p in papers[:5]:
    text = p.get('text', '')
    filename = p.get('filename', '')
    header_text = text[:500]
    
    match = re.search(r'\b(201[0-9]|202[0-9])\b', header_text) # broader year range for debug
    year = match.group(1) if match else "None"
    
    is_empirical = 'empirical' in text.lower()
    
    debug_info.append({
        'filename': filename,
        'extracted_year': year,
        'has_empirical': is_empirical,
        'header_snippet': header_text[:100]
    })

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-9891317091661830869': 'file_storage/function-call-9891317091661830869.json', 'var_function-call-10963661510414454345': ['paper_docs'], 'var_function-call-5664922713276342655': [], 'var_function-call-4943697616696163916': 'file_storage/function-call-4943697616696163916.json', 'var_function-call-14589379518527739272': []}

exec(code, env_args)
