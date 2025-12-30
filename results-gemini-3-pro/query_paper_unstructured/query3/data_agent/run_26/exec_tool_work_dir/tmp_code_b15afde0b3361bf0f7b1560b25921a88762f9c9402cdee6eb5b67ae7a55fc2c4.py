code = """import json
import re

with open(locals()['var_function-call-1844431421063330575'], 'r') as f:
    paper_docs = json.load(f)

target_title = "A Quantified-Self Framework for Exploring and Enhancing Personal Productivity"

found = False
for doc in paper_docs:
    if target_title in doc['filename']:
        text = doc.get('text', '')
        head = text[:3000]
        print(f"TITLE: {doc['filename']}")
        print(f"HEAD: {repr(head)}")
        found = True
        break

if not found:
    print(f"Paper '{target_title}' not found in docs.")

print("__RESULT__:")
print("done")"""

env_args = {'var_function-call-14741953591797828167': ['paper_docs'], 'var_function-call-14741953591797829382': ['Citations', 'sqlite_sequence'], 'var_function-call-2114113704500066494': 'file_storage/function-call-2114113704500066494.json', 'var_function-call-2114113704500064987': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-1844431421063330575': 'file_storage/function-call-1844431421063330575.json', 'var_function-call-11864637065263499194': 'file_storage/function-call-11864637065263499194.json', 'var_function-call-3352296089699517802': [], 'var_function-call-7894072423861374024': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'has_empirical': False}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'has_empirical': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'has_empirical': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'has_empirical': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None, 'has_empirical': False}], 'var_function-call-15134506039956552643': {'years': []}, 'var_function-call-4951557483953088360': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citation_count': 266}], 'var_function-call-9153438531013861764': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019, 'empirical': True}]}

exec(code, env_args)
