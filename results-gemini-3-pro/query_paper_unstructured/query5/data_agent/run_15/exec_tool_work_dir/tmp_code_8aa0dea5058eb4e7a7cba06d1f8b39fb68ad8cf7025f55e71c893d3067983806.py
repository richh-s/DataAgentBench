code = """import json
import re

# Load citations
with open(locals()['var_function-call-15646429060027290344'], 'r') as f:
    citations = json.load(f)

# Load papers
with open(locals()['var_function-call-5884279522157261639'], 'r') as f:
    papers = json.load(f)

citation_titles = set(c['title'] for c in citations)
paper_titles = set()
for p in papers:
    if 'filename' in p:
        paper_titles.add(p['filename'][:-4])

intersection = citation_titles.intersection(paper_titles)

debug_info = {
    "num_citations": len(citations),
    "num_papers": len(papers),
    "num_intersection": len(intersection),
    "sample_paper_titles": list(paper_titles)[:5],
    "sample_citation_titles": list(citation_titles)[:5]
}

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-173807103424142885': ['Citations', 'sqlite_sequence'], 'var_function-call-173807103424140732': ['paper_docs'], 'var_function-call-173807103424142675': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-173807103424140522': 'file_storage/function-call-173807103424140522.json', 'var_function-call-17670429279864850901': [{'COUNT(*)': '188'}], 'var_function-call-5884279522157261639': 'file_storage/function-call-5884279522157261639.json', 'var_function-call-15646429060027290344': 'file_storage/function-call-15646429060027290344.json', 'var_function-call-6914183761872541415': 'file_storage/function-call-6914183761872541415.json', 'var_function-call-14650497424767224127': 0}

exec(code, env_args)
