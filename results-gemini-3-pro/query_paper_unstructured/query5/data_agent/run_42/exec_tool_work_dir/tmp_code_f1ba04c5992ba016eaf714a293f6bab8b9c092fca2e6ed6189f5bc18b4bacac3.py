code = """import json
import re

citations_path = locals()['var_function-call-9827945916294781673']
with open(citations_path, 'r') as f:
    citations = json.load(f)
citation_titles = set(rec['title'] for rec in citations)

papers_path = locals()['var_function-call-15113855768220925357']
with open(papers_path, 'r') as f:
    papers = json.load(f)

print("__RESULT__:")
debug_info = []
matched_chi = []

count = 0
for paper in papers:
    title = paper.get('filename', '').replace('.txt', '')
    if title in citation_titles:
        text = paper.get('text', '')
        header = text[:300].replace('\n', ' ')
        
        is_chi = False
        if "Conference on Human Factors in Computing Systems" in text[:5000]:
            is_chi = True
        elif re.search(r"\bCHI\s+'?\d{2,4}", text[:5000]):
            is_chi = True
        elif "CHI Conference" in text[:5000]:
            is_chi = True
        elif re.search(r"\bCHI\s+20\d{2}", text[:5000]):
            is_chi = True
            
        if is_chi:
            matched_chi.append(title)
        else:
            if count < 10:
                debug_info.append({"title": title, "header": header})
                count += 1

print(json.dumps({"matched_chi": matched_chi, "samples_not_matched": debug_info}))"""

env_args = {'var_function-call-9827945916294781673': 'file_storage/function-call-9827945916294781673.json', 'var_function-call-15113855768220925357': 'file_storage/function-call-15113855768220925357.json', 'var_function-call-14723286786793106195': {'total_citations': 16, 'paper_count': 1}}

exec(code, env_args)
