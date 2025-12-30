code = """import json

with open(locals()['var_function-call-7711183651007727056'], 'r') as f:
    citations_data = json.load(f)

with open(locals()['var_function-call-4121090962908109712'], 'r') as f:
    paper_docs_data = json.load(f)

cit_titles = [r['title'] for r in citations_data]
doc_titles = [d['filename'].replace('.txt', '') for d in paper_docs_data if 'filename' in d]

intersection = set(cit_titles).intersection(set(doc_titles))

debug_info = {
    "num_citations": len(cit_titles),
    "num_docs": len(doc_titles),
    "intersection_count": len(intersection),
    "sample_cit_titles": cit_titles[:5],
    "sample_doc_titles": doc_titles[:5]
}

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-7711183651007727056': 'file_storage/function-call-7711183651007727056.json', 'var_function-call-4121090962908109712': 'file_storage/function-call-4121090962908109712.json', 'var_function-call-5326245820750148638': 16, 'var_function-call-17055580434800668848': {'total_citations': 0, 'chi_papers_count': 0, 'matched_titles_preview': []}, 'var_function-call-1860412936554148787': {'venue_counts': {'CHI': 0, 'Ubicomp': 0, 'CSCW': 0, 'Other': 4}, 'chi_citations': 0}}

exec(code, env_args)
