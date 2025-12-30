code = """import json
import re

# Load papers
with open(locals()['var_function-call-9482827288994489608'], 'r') as f:
    papers = json.load(f)

debug_info = []
for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    
    # Extract Year
    year_match = re.search(r'\b(20[1-2][0-9])\b', text[:2000])
    year = int(year_match.group(1)) if year_match else None
    
    # Extract Contribution
    is_empirical = 'empirical' in text.lower()
    
    debug_info.append({'filename': filename, 'year': year, 'is_empirical': is_empirical})

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-16968373354653802012': 'file_storage/function-call-16968373354653802012.json', 'var_function-call-12820784951702258902': ['paper_docs'], 'var_function-call-12820784951702258801': [{'cid': '0', 'name': 'id', 'type': 'INTEGER', 'notnull': '0', 'dflt_value': 'None', 'pk': '1'}, {'cid': '1', 'name': 'title', 'type': 'TEXT', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'citation_count', 'type': 'INTEGER', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'citation_year', 'type': 'INTEGER', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}], 'var_function-call-15186585176547387853': 'file_storage/function-call-15186585176547387853.json', 'var_function-call-9482827288994489608': 'file_storage/function-call-9482827288994489608.json', 'var_function-call-9482827288994490825': 'file_storage/function-call-9482827288994490825.json', 'var_function-call-9811688043533249505': []}

exec(code, env_args)
