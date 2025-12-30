code = """import json
import re

path_papers = locals()['var_function-call-15302473096394275436']
with open(path_papers, 'r') as f:
    papers = json.load(f)

years_found = []
empirical_count = 0
total_papers = len(papers)

for p in papers[:20]:
    title = p['filename'].replace('.txt', '')
    text = p['text']
    m = re.search(r'(20\d{2})', text[:1000])
    y = int(m.group(1)) if m else None
    years_found.append(y)
    if 'empirical' in text.lower():
        empirical_count += 1

print("__RESULT__:")
print(json.dumps({
    "years_preview": years_found,
    "total_papers": total_papers,
    "empirical_in_first_20": empirical_count
}))"""

env_args = {'var_function-call-3735696705524140447': 'file_storage/function-call-3735696705524140447.json', 'var_function-call-8426954921484076460': ['paper_docs'], 'var_function-call-8432852988790509735': [{'COUNT(*)': '1405'}], 'var_function-call-15575652384849502838': [], 'var_function-call-76014379587843141': 'file_storage/function-call-76014379587843141.json', 'var_function-call-15302473096394275436': 'file_storage/function-call-15302473096394275436.json', 'var_function-call-13901182043948570327': []}

exec(code, env_args)
