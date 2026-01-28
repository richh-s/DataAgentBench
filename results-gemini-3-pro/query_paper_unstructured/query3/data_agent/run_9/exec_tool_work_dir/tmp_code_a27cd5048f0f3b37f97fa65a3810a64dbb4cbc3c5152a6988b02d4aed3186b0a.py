code = """import json
import re

paper_docs_path = locals()['var_function-call-15160889356619040949']

with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

print(f"Total docs: {len(paper_docs)}")

count_year_found = 0
count_year_gt_2016 = 0
count_empirical = 0
debug_info = []

for i, doc in enumerate(paper_docs):
    text = doc.get('text', '')
    header_text = text[:2000]
    match = re.search(r'\b(201[7-9]|202[0-9])\b', header_text)
    
    year = None
    if match:
        year = int(match.group(1))
        count_year_found += 1
        if year > 2016:
            count_year_gt_2016 += 1
            
    is_empirical = 'empirical' in text.lower()
    if is_empirical:
        count_empirical += 1

    if i < 5:
        debug_info.append({
            "title": doc.get('filename'),
            "extracted_year": year,
            "is_empirical": is_empirical,
            "snippet": header_text[:200]
        })

print(f"Year found: {count_year_found}")
print(f"Year > 2016: {count_year_gt_2016}")
print(f"Empirical found: {count_empirical}")
print("Debug samples:")
print(json.dumps(debug_info, indent=2))

print("__RESULT__:")
print(json.dumps("Done"))"""

env_args = {'var_function-call-15160889356619040949': 'file_storage/function-call-15160889356619040949.json', 'var_function-call-14370993471195573993': 'file_storage/function-call-14370993471195573993.json', 'var_function-call-3936278199097246076': []}

exec(code, env_args)
