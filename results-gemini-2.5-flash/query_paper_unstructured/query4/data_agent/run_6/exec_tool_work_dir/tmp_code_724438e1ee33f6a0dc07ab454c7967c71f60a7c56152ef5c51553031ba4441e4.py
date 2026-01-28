code = """import json
import re

file_path = locals()['var_function-call-4575013761380349714']
with open(file_path, 'r') as f:
    physical_activity_papers = json.load(f)

filtered_papers_info = []
for paper in physical_activity_papers:
    text = paper['text']
    filename = paper['filename']
    title = filename.replace('.txt', '')

    year_match = re.search(r'year: (\\d{4})', text)
    domain_match = re.search(r'domain: (.*?)\n', text)

    year = int(year_match.group(1)) if year_match else None
    domain = domain_match.group(1).strip() if domain_match else None

    if year == 2016 and domain and 'physical activity' in domain:
        filtered_papers_info.append({'title': title, 'year': year, 'domain': domain})

print('__RESULT__:')
print(json.dumps(filtered_papers_info))"""

env_args = {'var_function-call-3967600453842721378': [], 'var_function-call-8271451008217141183': [], 'var_function-call-5153703013806353214': [], 'var_function-call-12010824351002747580': [], 'var_function-call-4575013761380349714': 'file_storage/function-call-4575013761380349714.json'}

exec(code, env_args)
