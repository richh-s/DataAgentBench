code = """import json

# Load citations
with open(locals()['var_function-call-7375441648498366517'], 'r') as f:
    citations_data = json.load(f)

titles = [item['title'] for item in citations_data]
matches = [t for t in titles if "Stage-based" in t]

print("__RESULT__:")
print(json.dumps(matches))"""

env_args = {'var_function-call-7375441648498366517': 'file_storage/function-call-7375441648498366517.json', 'var_function-call-12252996319457097106': 'file_storage/function-call-12252996319457097106.json', 'var_function-call-15387915071709340266': 68.5, 'var_function-call-12664133245284043172': {'total_cited_docs': 2, 'acm_count': 2, 'ieee_count': 0}, 'var_function-call-1887023296466281242': {'citations_count': 158, 'paper_docs_count': 5, 'sample_citations': ['Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'Sundroid: Solar Radiation Awareness with Smartphones', 'Why We Use and Abandon Smart Devices', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set'], 'sample_filenames': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt']}, 'var_function-call-5088514035838282492': 'file_storage/function-call-5088514035838282492.json', 'var_function-call-12537123751146832453': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_function-call-8673983059342040096': [{'title': 'A Lived Informatics Model of Personal Informatics', 'cited_count': 50, 'is_acm': True}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'cited_count': None, 'is_acm': True}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'cited_count': None, 'is_acm': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'cited_count': None, 'is_acm': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'cited_count': 87, 'is_acm': True}]}

exec(code, env_args)
