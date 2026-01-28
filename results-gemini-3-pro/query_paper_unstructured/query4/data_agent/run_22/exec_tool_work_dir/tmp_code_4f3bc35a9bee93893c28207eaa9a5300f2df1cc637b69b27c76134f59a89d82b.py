code = """import json

with open(locals()['var_function-call-1502338921683613399'], 'r') as f:
    papers = json.load(f)

debug_info = []
count_physical_activity = 0
for i, paper in enumerate(papers[:10]):
    text = paper.get('text', '')
    header = text[:500].replace('\n', ' ')
    has_pa = 'physical activity' in text.lower()
    if has_pa:
        count_physical_activity += 1
    debug_info.append({
        'filename': paper.get('filename'),
        'header_preview': header,
        'has_physical_activity': has_pa
    })

print("__RESULT__:")
print(json.dumps(debug_info, indent=2))"""

env_args = {'var_function-call-18065361926361048824': 'file_storage/function-call-18065361926361048824.json', 'var_function-call-1502338921683613399': 'file_storage/function-call-1502338921683613399.json', 'var_function-call-4041748401913796717': []}

exec(code, env_args)
