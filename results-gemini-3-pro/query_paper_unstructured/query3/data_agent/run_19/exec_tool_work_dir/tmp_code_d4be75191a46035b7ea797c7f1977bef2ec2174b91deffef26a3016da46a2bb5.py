code = """import json
import re

# Load data
with open(locals()['var_function-call-8795539412435626401'], 'r') as f:
    citations_data = json.load(f)

with open(locals()['var_function-call-4477812079734102671'], 'r') as f:
    papers_data = json.load(f)

# Process citations
citations_map = {}
for item in citations_data:
    t = item['title'].strip()
    c = int(item['citation_count'])
    citations_map[t] = citations_map.get(t, 0) + c

# Process papers
results = []
empirical_keywords = ["empirical", "user study", "participants", "interview", "survey", "field study", "controlled experiment", "quantitative", "qualitative", "recruited", "n ="]

for paper in papers_data:
    title = paper['filename'].replace('.txt', '').strip()
    text = paper['text']
    header_text = text[:1000]
    
    # Extract year
    # Look for 4 digit year in first 1000 chars
    years = re.findall(r'\b(20\d{2})\b', header_text)
    # Also look for 'YY format e.g. '17, '18
    short_years = re.findall(r"'\d{2}", header_text)
    
    # Heuristic: Pick the earliest year found that is reasonable (e.g. 2010-2025)
    # Actually, the copyright year is usually the publication year.
    # Or conference year.
    # The sample had "UBICOMP '15 ... 2015".
    # Let's take the first 20xx found.
    pub_year = None
    if years:
        # Filter years to be within range [2000, 2025]
        valid_years = [int(y) for y in years if 2000 <= int(y) <= 2025]
        if valid_years:
            pub_year = min(valid_years) # Usually the first one is the conference year
    
    # Check contribution
    is_empirical = False
    lower_text = text.lower()
    # Check explicitly for "empirical"
    if "empirical" in lower_text:
        is_empirical = True
    else:
        # Check for other keywords
        for kw in empirical_keywords:
            if kw in lower_text:
                is_empirical = True
                break
    
    if pub_year and pub_year > 2016 and is_empirical:
        count = citations_map.get(title, 0)
        results.append({"title": title, "citation_count": count, "year": pub_year})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-1144598558241376863': ['paper_docs'], 'var_function-call-12352843097856726104': 'file_storage/function-call-12352843097856726104.json', 'var_function-call-6179476248442941554': ['Citations', 'sqlite_sequence'], 'var_function-call-16625066116565131687': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-2869416645867630841': {'contains_empirical': False, 'contains_contribution': True, 'first_500': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \n\nABSTRACT \nCurrent  models  of  how  people  use  personal  informatics \nsystems are largely based in behavior change goals. They do \nnot  adequately  characteriz"}, 'var_function-call-3359098311945883536': [{'_id': '694f5530284b10b11dc0a869'}, {'_id': '694f5530284b10b11dc0a86a'}, {'_id': '694f5530284b10b11dc0a86b'}, {'_id': '694f5530284b10b11dc0a86c'}, {'_id': '694f5530284b10b11dc0a86d'}], 'var_function-call-4477812079734102671': 'file_storage/function-call-4477812079734102671.json', 'var_function-call-8795539412435626401': 'file_storage/function-call-8795539412435626401.json'}

exec(code, env_args)
