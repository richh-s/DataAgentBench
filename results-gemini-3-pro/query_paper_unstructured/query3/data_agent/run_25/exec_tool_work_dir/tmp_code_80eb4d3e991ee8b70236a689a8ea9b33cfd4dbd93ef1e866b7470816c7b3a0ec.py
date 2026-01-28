code = """import json
import re

with open(locals()['var_function-call-15606477523093127544'], 'r') as f:
    docs = json.load(f)

matching_titles = []

for doc in docs:
    text = doc['text']
    filename = doc['filename']
    title = filename.replace('.txt', '')
    
    # Year Extraction
    year = 0
    # Search in header (first 500) and footer (last 500)
    snippet = text[:500] + " " + text[-500:]
    
    # 1. Conference + Year (e.g., CHI 2017, CHI '17)
    # Matches: CHI 2017, UbiComp '18
    conf_matches = re.findall(r"(?:CHI|UbiComp|CSCW|DIS|IUI|ISWC)\s+(?:'|20)?(\d{2})", snippet, re.IGNORECASE)
    if conf_matches:
        year = int("20" + conf_matches[0])
    
    # 2. Copyright 20xx
    if year == 0:
        copy_matches = re.findall(r"Copyright\s+(?:20)(\d{2})", snippet, re.IGNORECASE)
        if copy_matches:
            year = int("20" + copy_matches[0])
            
    # 3. Simple 20xx in header
    if year == 0:
        simple_matches = re.findall(r"20(\d{2})", text[:200])
        if simple_matches:
            year = int("20" + simple_matches[0])

    # Empirical Check
    text_lower = text.lower()
    is_empirical = False
    
    if "empirical" in text_lower:
        is_empirical = True
    elif "user study" in text_lower:
        is_empirical = True
    elif "participants" in text_lower and ("study" in text_lower or "interview" in text_lower or "survey" in text_lower):
        is_empirical = True
    
    if year > 2016 and is_empirical:
        matching_titles.append(title)

print("__RESULT__:")
print(json.dumps(matching_titles))"""

env_args = {'var_function-call-4403390195297864469': 'file_storage/function-call-4403390195297864469.json', 'var_function-call-5079307557547688021': ['paper_docs'], 'var_function-call-3097430276196367090': 'file_storage/function-call-3097430276196367090.json', 'var_function-call-5206321841837773326': {'has_empirical': False, 'has_survey': True, 'has_interview': True, 'has_study': True}, 'var_function-call-3687296208506163854': [], 'var_function-call-5857355116469077971': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-4539730163481461020': 'file_storage/function-call-4539730163481461020.json', 'var_function-call-10637637580937536300': {'total_docs': 5, 'docs_after_2016': 0, 'docs_after_2016_with_empirical': 0, 'docs_after_2016_with_study': 0, 'examples_empirical': []}, 'var_function-call-15606477523093127544': 'file_storage/function-call-15606477523093127544.json', 'var_function-call-6095849557644838005': [], 'var_function-call-835920876180923776': 'file_storage/function-call-835920876180923776.json'}

exec(code, env_args)
