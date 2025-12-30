code = """import json
import re

citations_file_path = locals()['var_function-call-8765785804266823925']
papers_file_path = locals()['var_function-call-10316404265600385483']

with open(citations_file_path, 'r') as f:
    citations_data = json.load(f)
citation_titles = set(c['title'] for c in citations_data)

with open(papers_file_path, 'r') as f:
    papers_data = json.load(f)

debug_info = []
for paper in papers_data[:10]:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    text = paper.get('text', '')[:1000]
    
    years = re.findall(r'\b(20\d{2})\b', text)
    year = int(years[0]) if years else 0
    
    is_empirical = "empirical" in paper.get('text', '').lower()
    
    in_citations = title in citation_titles
    
    debug_info.append({
        "title": title,
        "extracted_year": year,
        "is_empirical": is_empirical,
        "in_citations": in_citations
    })

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-2080358657401428239': 'file_storage/function-call-2080358657401428239.json', 'var_function-call-4922993133298785860': ['paper_docs'], 'var_function-call-4922993133298782503': ['Citations', 'sqlite_sequence'], 'var_function-call-15480292294165083401': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-10316404265600385483': 'file_storage/function-call-10316404265600385483.json', 'var_function-call-8350695654712224507': [{'count(*)': '1405'}], 'var_function-call-8765785804266825960': 'file_storage/function-call-8765785804266825960.json', 'var_function-call-8765785804266823925': 'file_storage/function-call-8765785804266823925.json', 'var_function-call-5730915488565907792': []}

exec(code, env_args)
