code = """import json
import re

citations_path = locals()['var_function-call-9827945916294781673']
with open(citations_path, 'r') as f:
    citations = json.load(f)

citation_titles = set()
for c in citations:
    citation_titles.add(c['title'])

papers_path = locals()['var_function-call-15113855768220925357']
with open(papers_path, 'r') as f:
    papers = json.load(f)

found_chi = []
samples_others = []
processed_count = 0

for paper in papers:
    title = paper.get('filename', '').replace('.txt', '')
    if title in citation_titles:
        text = paper.get('text', '')
        is_chi = False
        # Regex checks
        if "Conference on Human Factors in Computing Systems" in text[:3000]:
            is_chi = True
        elif re.search(r"CHI\s+\d{4}", text[:3000]):
            is_chi = True
        elif re.search(r"CHI\s+'\d{2}", text[:3000]):
            is_chi = True
        elif re.search(r"Proceedings of the.*CHI", text[:3000], re.IGNORECASE):
            is_chi = True
            
        if is_chi:
            found_chi.append(title)
        else:
            if len(samples_others) < 5:
                samples_others.append({'title': title, 'header': text[:200]})
        
        processed_count += 1

print('__RESULT__:')
print(json.dumps({'found_chi_count': len(found_chi), 'found_chi_titles': found_chi, 'samples_others': samples_others, 'total_matched_papers': processed_count}))"""

env_args = {'var_function-call-9827945916294781673': 'file_storage/function-call-9827945916294781673.json', 'var_function-call-15113855768220925357': 'file_storage/function-call-15113855768220925357.json', 'var_function-call-14723286786793106195': {'total_citations': 16, 'paper_count': 1}}

exec(code, env_args)
