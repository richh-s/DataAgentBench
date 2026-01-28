code = """import json
import re

citation_file = locals()['var_function-call-5680722423366516433']
with open(citation_file, 'r') as f:
    citations = json.load(f)

cited_papers = {c['title'] for c in citations}

paper_file = locals()['var_function-call-1166448778177815195']
with open(paper_file, 'r') as f:
    papers = json.load(f)

matched_count = 0
skipped_samples = []

def is_chi(text):
    header = text[:2000]
    if re.search(r"\bCHI\s*['\u2019]?\s*\d{2,4}\b", header, re.IGNORECASE):
        return True
    if re.search(r"Conference on Human Factors in Computing Systems", header, re.IGNORECASE):
        return True
    return False

for p in papers:
    title = p['filename'].replace('.txt', '')
    if title in cited_papers:
        matched_count += 1
        if not is_chi(p['text']):
            if len(skipped_samples) < 3:
                skipped_samples.append({"title": title, "header": p['text'][:300]})

debug_info = {
    "total_cited_titles": len(cited_papers),
    "papers_found_in_mongo": matched_count,
    "skipped_samples": skipped_samples
}

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-5680722423366514432': ['Citations', 'sqlite_sequence'], 'var_function-call-5680722423366516433': 'file_storage/function-call-5680722423366516433.json', 'var_function-call-5680722423366514338': 'file_storage/function-call-5680722423366514338.json', 'var_function-call-1825670630710000632': 'file_storage/function-call-1825670630710000632.json', 'var_function-call-1380767849587936819': 188, 'var_function-call-5679032680150065306': 'file_storage/function-call-5679032680150065306.json', 'var_function-call-15107492987324530466': 'file_storage/function-call-15107492987324530466.json', 'var_function-call-1166448778177815195': 'file_storage/function-call-1166448778177815195.json', 'var_function-call-9559692353416114931': 16}

exec(code, env_args)
