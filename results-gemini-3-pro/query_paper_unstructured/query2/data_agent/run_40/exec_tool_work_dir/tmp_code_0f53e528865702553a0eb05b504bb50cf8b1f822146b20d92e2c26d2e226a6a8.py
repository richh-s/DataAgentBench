code = """import json

# Load citations
citations_path = locals()['var_function-call-7399957863239035507']
with open(citations_path, 'r') as f:
    citations_data = json.load(f)

# Load paper docs
docs_path = locals()['var_function-call-7399957863239036828']
with open(docs_path, 'r') as f:
    paper_docs = json.load(f)

citation_titles = set(c['title'] for c in citations_data)
doc_titles = set(d['filename'].replace('.txt', '') for d in paper_docs)

matched_titles = citation_titles.intersection(doc_titles)

print(f"Total citations (2018): {len(citations_data)}")
print(f"Total docs: {len(paper_docs)}")
print(f"Matched titles: {len(matched_titles)}")

# Check classification on matched titles
sample_matches = []
acm_matches = []
non_acm_matches = []

for doc in paper_docs:
    t = doc['filename'].replace('.txt', '')
    if t in matched_titles:
        txt = doc['text'][:5000]
        is_acm = "ACM" in txt or "Association for Computing Machinery" in txt
        if is_acm:
            acm_matches.append(t)
        else:
            non_acm_matches.append((t, txt[:200])) # Show start of text for non-matches

print(f"Classified as ACM: {len(acm_matches)}")
print(f"Classified as Non-ACM: {len(non_acm_matches)}")

print("__RESULT__:")
print(json.dumps({
    "num_citations": len(citations_data),
    "num_docs": len(paper_docs),
    "num_matched": len(matched_titles),
    "num_acm": len(acm_matches),
    "sample_non_acm": non_acm_matches[:5]
}))"""

env_args = {'var_function-call-10677751840676979687': ['paper_docs'], 'var_function-call-10677751840676979600': ['Citations', 'sqlite_sequence'], 'var_function-call-7399957863239035507': 'file_storage/function-call-7399957863239035507.json', 'var_function-call-7399957863239036828': 'file_storage/function-call-7399957863239036828.json', 'var_function-call-2139143517697208341': {'average_citation_count': 68.5, 'count_papers': 2}}

exec(code, env_args)
