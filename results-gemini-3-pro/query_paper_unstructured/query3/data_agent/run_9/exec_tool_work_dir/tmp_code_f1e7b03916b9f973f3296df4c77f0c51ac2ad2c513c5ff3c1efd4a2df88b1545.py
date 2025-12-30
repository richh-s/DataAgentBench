code = """import json
import re

paper_docs_path = locals()['var_function-call-15160889356619040949']

with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

stats = {
    "total_docs": len(paper_docs),
    "count_year_found": 0,
    "count_year_gt_2016": 0,
    "count_empirical": 0,
    "samples": []
}

for i, doc in enumerate(paper_docs):
    text = doc.get('text', '')
    header_text = text[:2000]
    match = re.search(r'\b(20[0-2][0-9])\b', header_text) # Broaden to check all 2000s
    
    year = None
    if match:
        year = int(match.group(1))
        stats["count_year_found"] += 1
        if year > 2016:
            stats["count_year_gt_2016"] += 1
            
    is_empirical = 'empirical' in text.lower()
    if is_empirical:
        stats["count_empirical"] += 1

    if i < 10:
        stats["samples"].append({
            "title": doc.get('filename'),
            "extracted_year": year,
            "is_empirical": is_empirical,
            "snippet": header_text[:100].replace('\n', ' ')
        })

print("__RESULT__:")
print(json.dumps(stats))"""

env_args = {'var_function-call-15160889356619040949': 'file_storage/function-call-15160889356619040949.json', 'var_function-call-14370993471195573993': 'file_storage/function-call-14370993471195573993.json', 'var_function-call-3936278199097246076': [], 'var_function-call-845286639558883186': 'Done'}

exec(code, env_args)
