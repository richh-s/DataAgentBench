code = """import json

with open(locals()['var_function-call-9551284447428775563'], 'r') as f:
    papers = json.load(f)

with open(locals()['var_function-call-4736821834278124027'], 'r') as f:
    citations = json.load(f)

print("Total papers:", len(papers))
print("Total citations:", len(citations))

pa_count = 0
year_2016_count = 0
match_count = 0

sample_titles_papers = []
sample_titles_citations = list(set(c['title'] for c in citations))[:5]

for p in papers:
    text = p.get('text', '').lower()
    header = p.get('text', '')[:2000]
    
    if 'physical activity' in text:
        pa_count += 1
        
    if '2016' in header:
        year_2016_count += 1
        
    if 'physical activity' in text and '2016' in header:
        match_count += 1
        sample_titles_papers.append(p['filename'])

print(f"Papers with 'physical activity': {pa_count}")
print(f"Papers with '2016' in header: {year_2016_count}")
print(f"Papers matching both: {match_count}")
if match_count > 0:
    print("Sample matching filenames:", sample_titles_papers[:3])

print("Sample citation titles:", sample_titles_citations)

# Check title matching for one case if possible
if match_count > 0:
    test_title = sample_titles_papers[0].replace('.txt', '')
    found = False
    for c in citations:
        if c['title'] == test_title:
            found = True
            break
    print(f"Title '{test_title}' found in citations: {found}")
    
print("__RESULT__:")
print(json.dumps("debug_done"))"""

env_args = {'var_function-call-524279506149407119': ['paper_docs'], 'var_function-call-524279506149405588': 'file_storage/function-call-524279506149405588.json', 'var_function-call-524279506149408153': ['Citations', 'sqlite_sequence'], 'var_function-call-524279506149406622': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-9551284447428774224': [{'count(*)': '1405'}], 'var_function-call-9551284447428775563': 'file_storage/function-call-9551284447428775563.json', 'var_function-call-4736821834278124027': 'file_storage/function-call-4736821834278124027.json', 'var_function-call-1276767600603300389': []}

exec(code, env_args)
