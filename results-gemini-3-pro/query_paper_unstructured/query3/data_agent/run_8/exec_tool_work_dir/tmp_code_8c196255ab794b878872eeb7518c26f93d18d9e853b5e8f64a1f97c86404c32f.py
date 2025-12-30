code = """import json
import re

with open(locals()['var_function-call-15080538060224287608'], 'r') as f:
    papers = json.load(f)

with open(locals()['var_function-call-7203993170122994378'], 'r') as f:
    citations = json.load(f)

citation_sums = {}
for c in citations:
    t = c['title']
    count = int(c['citation_count'])
    citation_sums[t] = citation_sums.get(t, 0) + count

results = []
debug_years = []

for p in papers:
    text = p['text']
    filename = p['filename']
    title = filename.replace('.txt', '')
    
    # Year Extraction
    # Heuristic 1: Look for 4 digits 20xx in first 1000 chars
    header = text[:1000]
    years = re.findall(r'20[0-2][0-9]', header)
    year = None
    if years:
        # Pick the one that appears most or is earliest/latest?
        # Usually the publication year is the one that appears in the copyright or venue string.
        # Often it's the first one.
        year = int(years[0])
    
    # Heuristic 2: 'xx
    if not year:
        match_short = re.search(r"[A-Z]+ '[0-9]{2}", header)
        if match_short:
             yy = int(match_short.group(0).split("'")[1])
             year = 2000 + yy
    
    # Empirical Extraction
    is_empirical = "empirical" in text.lower()
    
    if is_empirical and year and year > 2016:
        total_c = citation_sums.get(title, 0)
        results.append({"title": title, "total_citation_count": total_c})
    
    if is_empirical and (not year or year <= 2016):
        debug_years.append({"title": title, "year": year})

print("__RESULT__:")
print(json.dumps(results))
# print(json.dumps(debug_years[:5])) # Debug if needed"""

env_args = {'var_function-call-1382832429316452546': ['paper_docs'], 'var_function-call-1382832429316454187': ['Citations', 'sqlite_sequence'], 'var_function-call-12576902616845472384': 'file_storage/function-call-12576902616845472384.json', 'var_function-call-9106356078782033053': 'file_storage/function-call-9106356078782033053.json', 'var_function-call-7203993170122994378': 'file_storage/function-call-7203993170122994378.json', 'var_function-call-9603352317542376889': [], 'var_function-call-10921488412089867487': {'total_papers': 5, 'sample_debug': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': 2015, 'is_empirical': False, 'in_citations': True}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'is_empirical': False, 'in_citations': True}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'is_empirical': True, 'in_citations': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'is_empirical': True, 'in_citations': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None, 'is_empirical': False, 'in_citations': True}], 'stats': {'count_empirical': 2, 'count_year_found': 1, 'count_year_gt_2016': 0, 'count_matched_title': 5}}, 'var_function-call-15080538060224287608': 'file_storage/function-call-15080538060224287608.json'}

exec(code, env_args)
