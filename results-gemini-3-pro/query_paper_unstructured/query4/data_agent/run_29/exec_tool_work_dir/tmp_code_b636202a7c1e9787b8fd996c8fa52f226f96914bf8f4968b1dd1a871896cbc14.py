code = """import json

with open(locals()['var_function-call-9551284447428775563'], 'r') as f:
    papers = json.load(f)

with open(locals()['var_function-call-4736821834278124027'], 'r') as f:
    citations = json.load(f)

debug_info = {}
debug_info["total_papers"] = len(papers)
debug_info["total_citations"] = len(citations)

pa_count = 0
year_2016_count = 0
match_count = 0
matches = []

for p in papers:
    text = p.get('text', '').lower()
    header = p.get('text', '')[:2000]
    
    has_pa = 'physical activity' in text
    has_2016 = '2016' in header
    
    if has_pa:
        pa_count += 1
    if has_2016:
        year_2016_count += 1
    if has_pa and has_2016:
        match_count += 1
        matches.append(p['filename'])

debug_info["pa_count"] = pa_count
debug_info["year_2016_count"] = year_2016_count
debug_info["match_count"] = match_count
debug_info["sample_matches"] = matches[:5]

citation_titles = set(c['title'] for c in citations)
debug_info["sample_citation_titles"] = list(citation_titles)[:5]

# Check if matches exist in citations
if matches:
    test_title = matches[0].replace('.txt', '')
    debug_info["test_title_in_citations"] = test_title in citation_titles
else:
    debug_info["test_title_in_citations"] = False

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-524279506149407119': ['paper_docs'], 'var_function-call-524279506149405588': 'file_storage/function-call-524279506149405588.json', 'var_function-call-524279506149408153': ['Citations', 'sqlite_sequence'], 'var_function-call-524279506149406622': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-9551284447428774224': [{'count(*)': '1405'}], 'var_function-call-9551284447428775563': 'file_storage/function-call-9551284447428775563.json', 'var_function-call-4736821834278124027': 'file_storage/function-call-4736821834278124027.json', 'var_function-call-1276767600603300389': [], 'var_function-call-8853061178265091948': 'debug_done'}

exec(code, env_args)
