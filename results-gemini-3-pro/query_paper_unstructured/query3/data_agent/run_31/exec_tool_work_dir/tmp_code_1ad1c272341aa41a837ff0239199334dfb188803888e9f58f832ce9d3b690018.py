code = """import json
import re

papers_path = locals()['var_function-call-10894468654798374866']
with open(papers_path, 'r') as f:
    papers_data = json.load(f)

debug_info = []
for i, paper in enumerate(papers_data[:20]):
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    header_text = text[:2000]
    years = re.findall(r"20[12]\d", header_text)
    is_empirical = "empirical" in text[:10000].lower()
    
    debug_info.append({
        "filename": filename,
        "years_found": years,
        "is_empirical": is_empirical
    })

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-5623558947517056704': 'file_storage/function-call-5623558947517056704.json', 'var_function-call-4507795440507618758': 'file_storage/function-call-4507795440507618758.json', 'var_function-call-10894468654798374866': 'file_storage/function-call-10894468654798374866.json', 'var_function-call-7275202975009130922': [], 'var_function-call-8227419315527480326': 'Debug Complete'}

exec(code, env_args)
