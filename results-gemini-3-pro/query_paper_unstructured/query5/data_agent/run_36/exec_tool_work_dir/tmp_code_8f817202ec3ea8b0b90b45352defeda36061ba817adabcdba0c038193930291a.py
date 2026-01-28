code = """import json
import re

citations_path = locals()['var_function-call-12939429308500753230']
with open(citations_path, 'r') as f:
    citations = json.load(f)

papers_path = locals()['var_function-call-11830425974286538439']
with open(papers_path, 'r') as f:
    papers = json.load(f)

debug_info = {}
debug_info['total_papers'] = len(papers)
debug_info['total_citations'] = len(citations)

paper_titles = set(p.get('filename', '').replace('.txt', '') for p in papers)
citation_titles = set(c.get('title') for c in citations)
debug_info['overlap_count'] = len(paper_titles.intersection(citation_titles))

# Check for CHI in first few papers
sample_checks = []
for p in papers[:5]:
    text = p.get('text', '')
    title = p.get('filename', '')
    found = "CHI" in text
    idx = text.find("CHI") if found else -1
    snippet = text[idx:idx+50] if found else ""
    sample_checks.append({
        "title": title,
        "found_chi": found,
        "index": idx,
        "snippet": snippet
    })
debug_info['samples'] = sample_checks

# Check specific CHI heuristic
chi_candidates = []
for p in papers:
    text = p.get('text', '')
    if re.search(r'\bCHI\b', text[:500]):
        chi_candidates.append(p.get('filename'))
debug_info['chi_candidates_count'] = len(chi_candidates)
debug_info['chi_candidates_sample'] = chi_candidates[:5]

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-16274009200495380828': 'file_storage/function-call-16274009200495380828.json', 'var_function-call-12939429308500753230': 'file_storage/function-call-12939429308500753230.json', 'var_function-call-13758046956340935094': 0, 'var_function-call-9966761655225880711': [], 'var_function-call-14800163327184198750': ['A Lived Informatics Model of Personal Informatics.txt'], 'var_function-call-11830425974286538439': 'file_storage/function-call-11830425974286538439.json', 'var_function-call-2236700066034859830': 0, 'var_function-call-12172345065077617984': {'status': 'debug complete'}}

exec(code, env_args)
