code = """import json
import re

with open(locals()['var_function-call-15772907393576741835'], 'r') as f:
    papers_data = json.load(f)

# Subset to candidates
candidates = [
    "A Trip to the Moon: Personalized Animated Movies for Self-reflection",
    "A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App"
]

info = []
for p in papers_data:
    title = p['filename'].replace('.txt', '')
    if title in candidates:
        text = p['text']
        # Find all years
        years = re.findall(r'20\d{2}', text)
        # Context around years? Too much output.
        # Just distinct years and count.
        from collections import Counter
        year_counts = Counter(years)
        
        info.append({
            "title": title,
            "years_found": dict(year_counts),
            "head": text[:500],
            "tail": text[-500:]
        })

print("__RESULT__:")
print(json.dumps(info))"""

env_args = {'var_function-call-11810081531988972241': ['paper_docs'], 'var_function-call-10291775221222249891': 'file_storage/function-call-10291775221222249891.json', 'var_function-call-15772907393576741835': 'file_storage/function-call-15772907393576741835.json', 'var_function-call-6342000761403970921': 'file_storage/function-call-6342000761403970921.json', 'var_function-call-809378135484135581': [], 'var_function-call-7140887120610556425': {'total_papers': 5, 'papers_with_empirical': 2, 'papers_post_2016': 0, 'matched_titles': 5, 'sample_years': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': 0, 'has_empirical': False}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': 0, 'has_empirical': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 0, 'has_empirical': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 0, 'has_empirical': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': 0, 'has_empirical': False}]}, 'var_function-call-14761232112250728850': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'post_2016_match': None, 'empirical': False}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'post_2016_match': None, 'empirical': False}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'post_2016_match': None, 'empirical': True}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'post_2016_match': None, 'empirical': True}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'post_2016_match': None, 'empirical': False}], 'var_function-call-10247718206001386956': [{'id': '47', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '16', 'citation_year': '2020'}, {'id': '48', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '49', 'citation_year': '2021'}, {'id': '49', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '11', 'citation_year': '2022'}, {'id': '50', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '71', 'citation_year': '2023'}, {'id': '51', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '38', 'citation_year': '2024'}, {'id': '52', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '81', 'citation_year': '2025'}], 'var_function-call-12682327022870390596': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  condition, \naffecting  20%  of  the  population.  Even  though  it  is  a \ntreatable  condition,  people  often  do  not  seek  treatment.  In \nthis paper, we  describe how we co-designed and evaluated \nwith  30  stakeholders  (9  medical  professionals  and  21  end-\nusers)  an  OAB  mobile  health  application  that  aims  to \nincrease  adherence  to  self-managed  treatment.  Our  results \nsupport previous research that visualizing progress, setting \ngoals, receiving reminders and feedback  increases  use.  We \ndiscovered  that  games  could  be  used  successfully  as  a \ndistraction technique for urge suppression. Contrary to the \ncurrent research direction, automatically calculated features \n', 'var_function-call-5797733396096891655': 'file_storage/function-call-5797733396096891655.json'}

exec(code, env_args)
