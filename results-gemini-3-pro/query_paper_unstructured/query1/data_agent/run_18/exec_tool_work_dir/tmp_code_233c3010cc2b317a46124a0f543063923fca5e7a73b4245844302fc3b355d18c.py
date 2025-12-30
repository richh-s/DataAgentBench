code = """import json
import re

papers_path = locals()['var_function-call-12584433843491866597']
with open(papers_path, 'r') as f:
    paper_docs = json.load(f)

count_title = 0
count_keywords = 0
count_abstract = 0
count_text = 0

sample_text_match = None

for doc in paper_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Title
    if 'food' in title.lower():
        count_title += 1
        
    # Keywords
    pattern_kw = r"Author Keywords(.*?)(?=ACM Classification|INTRODUCTION|General Terms|Index Terms)"
    match_kw = re.search(pattern_kw, text, re.DOTALL | re.IGNORECASE)
    kw = match_kw.group(1).lower() if match_kw else ""
    if 'food' in kw:
        count_keywords += 1
        
    # Abstract
    # Between ABSTRACT and Author Keywords/INTRODUCTION
    pattern_abs = r"ABSTRACT(.*?)(?=Author Keywords|INTRODUCTION|ACM Classification)"
    match_abs = re.search(pattern_abs, text, re.DOTALL | re.IGNORECASE)
    abstract = match_abs.group(1).lower() if match_abs else ""
    if 'food' in abstract:
        count_abstract += 1
        
    # Text
    if 'food' in text.lower():
        count_text += 1
        if not sample_text_match and not ('food' in title.lower() or 'food' in kw):
            sample_text_match = title

print("__RESULT__:")
print(json.dumps({
    "count_title": count_title,
    "count_keywords": count_keywords,
    "count_abstract": count_abstract,
    "count_text": count_text,
    "sample_text_match_title": sample_text_match
}))"""

env_args = {'var_function-call-3783672913394696319': ['paper_docs'], 'var_function-call-3783672913394696700': ['Citations', 'sqlite_sequence'], 'var_function-call-272073867596597133': 'file_storage/function-call-272073867596597133.json', 'var_function-call-272073867596596742': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-9679994414761045024': 'file_storage/function-call-9679994414761045024.json', 'var_function-call-12584433843491866400': 'file_storage/function-call-12584433843491866400.json', 'var_function-call-12584433843491866597': 'file_storage/function-call-12584433843491866597.json', 'var_function-call-3836062097239578025': {'food_paper_count': 0, 'total_citations': 0, 'sample_titles': []}, 'var_function-call-1933883333484097501': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'keywords_found': 'Lived Informatics; Personal Informatics; Self-Tracking;  Lapsing; Physical Activity; Finances; Locat', 'is_food': False}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'keywords_found': 'Personal informatics, collection, reflection, model, barriers', 'is_food': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'keywords_found': 'Personalization; animation; emotion; engagement; empathy; self-reﬂection.', 'is_food': False}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'keywords_found': 'None', 'is_food': False}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'keywords_found': 'Wearable technology; dashboard; information visualization;  stroke rehabilitation; occupational ther', 'is_food': False}], 'var_function-call-15046315751179438460': {'food_paper_count': 0, 'total_citations': 0, 'sample_titles': []}}

exec(code, env_args)
