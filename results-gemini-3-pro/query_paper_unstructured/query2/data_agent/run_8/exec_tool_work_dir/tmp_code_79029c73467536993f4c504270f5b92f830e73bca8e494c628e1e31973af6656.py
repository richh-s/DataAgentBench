code = """import json

# Load citations
file_path_cit = locals()['var_function-call-17666330447833607191']
with open(file_path_cit, 'r') as f:
    citations_list = json.load(f)
citation_titles = set(c['title'] for c in citations_list)

# Load docs
file_path_docs = locals()['var_function-call-3540073977128497152']
with open(file_path_docs, 'r') as f:
    docs = json.load(f)
doc_titles = set(d['filename'].replace('.txt', '') for d in docs)

# Check intersection
intersection = citation_titles.intersection(doc_titles)
missing_docs = citation_titles - doc_titles
extra_docs = doc_titles - citation_titles

print("__RESULT__:")
print(json.dumps({
    "intersection_count": len(intersection),
    "missing_docs_count": len(missing_docs),
    "extra_docs_count": len(extra_docs),
    "sample_missing": list(missing_docs)[:5],
    "sample_extra": list(extra_docs)[:5]
}))"""

env_args = {'var_function-call-17666330447833607191': 'file_storage/function-call-17666330447833607191.json', 'var_function-call-11031819639720739797': 'file_storage/function-call-11031819639720739797.json', 'var_function-call-11580890549591616551': 158, 'var_function-call-15015239705628452412': 'file_storage/function-call-15015239705628452412.json', 'var_function-call-12301809577552988153': 'file_storage/function-call-12301809577552988153.json', 'var_function-call-291982586650051971': 'file_storage/function-call-291982586650051971.json', 'var_function-call-7820464138049076348': 5, 'var_function-call-3540073977128497152': 'file_storage/function-call-3540073977128497152.json', 'var_function-call-16924924423564672170': 60.092592592592595, 'var_function-call-2801795861932674547': {'total_cited_papers': 158, 'papers_found_in_docs': 55, 'acm_papers_count': 54, 'avg': 60.092592592592595}, 'var_function-call-11335091958675771062': 99}

exec(code, env_args)
