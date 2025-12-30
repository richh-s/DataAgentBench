code = """import json

file_path = locals()['var_function-call-454889790813745050']
with open(file_path, 'r') as f:
    docs = json.load(f)

inspection = []
for doc in docs[:10]:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    found_lines = []
    
    # Check for specific prefixes
    lines = text.split('\n')
    for line in lines:
        if line.strip().startswith('Contribution:') or line.strip().startswith('Year:') or line.strip().startswith('Venue:'):
            found_lines.append(line.strip())
            
    inspection.append({
        "filename": filename,
        "found_lines": found_lines,
        "first_100": text[:100],
        "last_100": text[-100:]
    })

print("__RESULT__:")
print(json.dumps(inspection))"""

env_args = {'var_function-call-454889790813745050': 'file_storage/function-call-454889790813745050.json'}

exec(code, env_args)
