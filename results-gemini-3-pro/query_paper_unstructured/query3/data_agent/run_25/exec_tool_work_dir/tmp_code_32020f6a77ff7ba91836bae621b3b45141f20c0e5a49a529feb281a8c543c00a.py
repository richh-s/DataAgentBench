code = """import json
import re

with open(locals()['var_function-call-15606477523093127544'], 'r') as f:
    docs = json.load(f)

papers_metadata = []

for doc in docs:
    text = doc['text']
    filename = doc['filename']
    title = filename.replace('.txt', '')
    
    # Year extraction
    # Look for 2017, 2018, 2019, 2020... in the first 1000 chars
    header = text[:1000]
    years = re.findall(r"20(1[7-9]|2[0-9])", header) # Matches 2017-2029
    if years:
        year = int("20" + years[0])
    else:
        # Check if 2015, 2016 exist to be sure
        all_years = re.findall(r"20\d{2}", header)
        if all_years:
            year = int(all_years[0])
        else:
            year = 0

    # Contribution check
    text_lower = text.lower()
    # Broad empirical check
    is_empirical = False
    if "empirical" in text_lower:
        is_empirical = True
    elif "study" in text_lower and ("participant" in text_lower or "interview" in text_lower or "survey" in text_lower):
        is_empirical = True
    elif "user study" in text_lower:
        is_empirical = True
        
    if year > 2016 and is_empirical:
        papers_metadata.append(title)

print("__RESULT__:")
print(json.dumps(papers_metadata))"""

env_args = {'var_function-call-4403390195297864469': 'file_storage/function-call-4403390195297864469.json', 'var_function-call-5079307557547688021': ['paper_docs'], 'var_function-call-3097430276196367090': 'file_storage/function-call-3097430276196367090.json', 'var_function-call-5206321841837773326': {'has_empirical': False, 'has_survey': True, 'has_interview': True, 'has_study': True}, 'var_function-call-3687296208506163854': [], 'var_function-call-5857355116469077971': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-4539730163481461020': 'file_storage/function-call-4539730163481461020.json', 'var_function-call-10637637580937536300': {'total_docs': 5, 'docs_after_2016': 0, 'docs_after_2016_with_empirical': 0, 'docs_after_2016_with_study': 0, 'examples_empirical': []}, 'var_function-call-15606477523093127544': 'file_storage/function-call-15606477523093127544.json'}

exec(code, env_args)
