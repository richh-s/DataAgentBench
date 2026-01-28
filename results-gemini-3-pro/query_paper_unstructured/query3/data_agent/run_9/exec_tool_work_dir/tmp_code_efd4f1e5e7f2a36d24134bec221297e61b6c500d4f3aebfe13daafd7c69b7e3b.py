code = """import json
import re

paper_docs_path = locals()['var_function-call-15160889356619040949']
citations_path = locals()['var_function-call-14370993471195573993']

with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

with open(citations_path, 'r') as f:
    citations_data = json.load(f)
    
citation_counts = {}
for record in citations_data:
    title = record['title']
    count = int(record['citation_count'])
    citation_counts[title] = citation_counts.get(title, 0) + count

debug_results = []
final_results = []

for doc in paper_docs:
    filename = doc.get('filename', '')
    title = filename[:-4] if filename.endswith('.txt') else filename
    text = doc.get('text', '')
    
    # Extract years
    # Check first 2000 chars
    header_text = text[:2000]
    years = re.findall(r'20[0-9]{2}', header_text)
    
    # Heuristic: First year found is usually the publication year
    # Or filter years that are likely publication years (e.g. >= 2000)
    # Be careful of "Copyright 20xx"
    valid_years = [int(y) for y in years if 2000 <= int(y) <= 2025]
    
    year = valid_years[0] if valid_years else None
    
    is_empirical = 'empirical' in text.lower()
    
    debug_results.append({
        "title": title,
        "years_found": years,
        "chosen_year": year,
        "is_empirical": is_empirical
    })
    
    if year and year > 2016 and is_empirical:
        count = citation_counts.get(title, 0)
        final_results.append({
            "title": title,
            "citation_count": count
        })

print("DEBUG:")
print(json.dumps(debug_results, indent=2))
print("__RESULT__:")
print(json.dumps(final_results))"""

env_args = {'var_function-call-15160889356619040949': 'file_storage/function-call-15160889356619040949.json', 'var_function-call-14370993471195573993': 'file_storage/function-call-14370993471195573993.json', 'var_function-call-3936278199097246076': [], 'var_function-call-845286639558883186': 'Done', 'var_function-call-9568601149975010194': {'total_docs': 5, 'count_year_found': 0, 'count_year_gt_2016': 0, 'count_empirical': 2, 'samples': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'extracted_year': None, 'is_empirical': False}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'extracted_year': None, 'is_empirical': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'extracted_year': None, 'is_empirical': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'extracted_year': None, 'is_empirical': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'extracted_year': None, 'is_empirical': False}]}, 'var_function-call-10596429833444850584': {'snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \n\nABSTRACT \nCurrent  models  of  how  people  use  personal  informatics \nsystems are largely based in behavior change goals. They do \nnot  adequately  characteriz"}, 'var_function-call-5184517715911920305': {'matches': ['2015'], 'has_empirical': False, 'snippet_len': 68339}, 'var_function-call-2563683768028750558': 'file_storage/function-call-2563683768028750558.json'}

exec(code, env_args)
