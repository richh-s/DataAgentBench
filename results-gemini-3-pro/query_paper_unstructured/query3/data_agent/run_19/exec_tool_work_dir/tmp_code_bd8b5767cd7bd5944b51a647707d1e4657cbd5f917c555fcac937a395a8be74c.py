code = """import json
import re

# Load data
with open(locals()['var_function-call-8795539412435626401'], 'r') as f:
    citations_data = json.load(f)

with open(locals()['var_function-call-4477812079734102671'], 'r') as f:
    papers_data = json.load(f)

debug_info = []
empirical_keywords = ["empirical", "user study", "participants", "interview", "survey", "field study", "controlled experiment", "quantitative", "qualitative", "recruited", "n =", "findings", "method"]

for paper in papers_data:
    title = paper['filename'].replace('.txt', '').strip()
    text = paper['text']
    header_text = text[:1000]
    
    # Extract year
    years = re.findall(r'\b(20\d{2})\b', header_text)
    pub_year = None
    if years:
        valid_years = [int(y) for y in years if 2000 <= int(y) <= 2025]
        if valid_years:
            pub_year = min(valid_years)
            
    # Check contribution
    lower_text = text.lower()
    found_keywords = [kw for kw in empirical_keywords if kw in lower_text]
    is_empirical = len(found_keywords) > 0
    
    debug_info.append({
        "title": title,
        "extracted_year": pub_year,
        "is_empirical": is_empirical,
        "keywords_found": found_keywords[:5],
        "header_snippet": header_text[:200].replace('\n', ' ')
    })

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-1144598558241376863': ['paper_docs'], 'var_function-call-12352843097856726104': 'file_storage/function-call-12352843097856726104.json', 'var_function-call-6179476248442941554': ['Citations', 'sqlite_sequence'], 'var_function-call-16625066116565131687': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-2869416645867630841': {'contains_empirical': False, 'contains_contribution': True, 'first_500': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \n\nABSTRACT \nCurrent  models  of  how  people  use  personal  informatics \nsystems are largely based in behavior change goals. They do \nnot  adequately  characteriz"}, 'var_function-call-3359098311945883536': [{'_id': '694f5530284b10b11dc0a869'}, {'_id': '694f5530284b10b11dc0a86a'}, {'_id': '694f5530284b10b11dc0a86b'}, {'_id': '694f5530284b10b11dc0a86c'}, {'_id': '694f5530284b10b11dc0a86d'}], 'var_function-call-4477812079734102671': 'file_storage/function-call-4477812079734102671.json', 'var_function-call-8795539412435626401': 'file_storage/function-call-8795539412435626401.json', 'var_function-call-2769620379183319788': []}

exec(code, env_args)
