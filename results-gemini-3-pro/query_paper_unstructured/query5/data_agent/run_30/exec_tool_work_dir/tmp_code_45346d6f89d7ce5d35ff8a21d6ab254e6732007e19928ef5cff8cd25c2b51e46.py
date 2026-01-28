code = """import json
import re

with open(locals()['var_function-call-7711183651007727056'], 'r') as f:
    citations_data = json.load(f)

with open(locals()['var_function-call-4121090962908109712'], 'r') as f:
    paper_docs_data = json.load(f)

paper_map = {d['filename'].replace('.txt', ''): d['text'] for d in paper_docs_data if 'filename' in d}

venue_counts = {"CHI": 0, "Ubicomp": 0, "CSCW": 0, "Other": 0}
chi_citations = 0

for record in citations_data:
    title = record['title']
    if title in paper_map:
        text = paper_map[title]
        header = text[:1000]
        
        found = False
        if re.search(r'\bCHI\b', header) or "Human Factors in Computing Systems" in header:
            venue_counts["CHI"] += 1
            chi_citations += int(record['citation_count'])
            found = True
        elif re.search(r'\bUbiComp\b', header, re.IGNORECASE):
            venue_counts["Ubicomp"] += 1
            found = True
        elif re.search(r'\bCSCW\b', header):
            venue_counts["CSCW"] += 1
            found = True
        
        if not found:
            venue_counts["Other"] += 1

print("__RESULT__:")
print(json.dumps({"venue_counts": venue_counts, "chi_citations": chi_citations}))"""

env_args = {'var_function-call-7711183651007727056': 'file_storage/function-call-7711183651007727056.json', 'var_function-call-4121090962908109712': 'file_storage/function-call-4121090962908109712.json', 'var_function-call-5326245820750148638': 16, 'var_function-call-17055580434800668848': {'total_citations': 0, 'chi_papers_count': 0, 'matched_titles_preview': []}}

exec(code, env_args)
