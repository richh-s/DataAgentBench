code = """import json
import re

with open(locals()['var_function-call-9106356078782033053'], 'r') as f:
    papers = json.load(f)

with open(locals()['var_function-call-7203993170122994378'], 'r') as f:
    citations = json.load(f)

citation_titles = set(c['title'] for c in citations)

debug_info = []
count_empirical = 0
count_year_found = 0
count_year_gt_2016 = 0
count_matched_title = 0

for p in papers[:20]: # Check first 20 papers
    text = p['text']
    filename = p['filename']
    title = filename.replace('.txt', '')
    
    header = text[:1000]
    match_year = re.search(r'20[0-2][0-9]', header)
    year = None
    if match_year:
        year = int(match_year.group(0))
    
    is_empirical = "empirical" in text.lower()
    
    if is_empirical: count_empirical += 1
    if year: count_year_found += 1
    if year and year > 2016: count_year_gt_2016 += 1
    if title in citation_titles: count_matched_title += 1
    
    debug_info.append({
        "title": title,
        "year": year,
        "is_empirical": is_empirical,
        "in_citations": title in citation_titles
    })

print("__RESULT__:")
print(json.dumps({
    "total_papers": len(papers),
    "sample_debug": debug_info,
    "stats": {
        "count_empirical": count_empirical,
        "count_year_found": count_year_found,
        "count_year_gt_2016": count_year_gt_2016,
        "count_matched_title": count_matched_title
    }
}))"""

env_args = {'var_function-call-1382832429316452546': ['paper_docs'], 'var_function-call-1382832429316454187': ['Citations', 'sqlite_sequence'], 'var_function-call-12576902616845472384': 'file_storage/function-call-12576902616845472384.json', 'var_function-call-9106356078782033053': 'file_storage/function-call-9106356078782033053.json', 'var_function-call-7203993170122994378': 'file_storage/function-call-7203993170122994378.json', 'var_function-call-9603352317542376889': []}

exec(code, env_args)
