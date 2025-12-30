code = """import json
import re

with open(locals()['var_function-call-13085037572156381968'], 'r') as f:
    papers = json.load(f)

for p in papers:
    if "A Trip to the Moon" in p['filename']:
        text = p['text'][:5000]
        # Run my regexes to see what year it picked
        venue_pattern = re.compile(r"(CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s*['\u2019]?\s*(\d{2,4})", re.IGNORECASE)
        copyright_pattern = re.compile(r"Copyright\s+.*(20\d{2})", re.IGNORECASE)
        simple_year_pattern = re.compile(r"20[0-2]\d")
        
        y = None
        v = venue_pattern.search(text)
        if v: y = v.group(2)
        elif copyright_pattern.search(text): y = copyright_pattern.search(text).group(1)
        elif simple_year_pattern.search(text[:500]): y = simple_year_pattern.search(text[:500]).group(0)
        
        print("__RESULT__:")
        print(json.dumps({"title": p['filename'], "extracted_year": y, "header_snippet": text[:500]}))
        break"""

env_args = {'var_function-call-7886853940146991682': 'file_storage/function-call-7886853940146991682.json', 'var_function-call-14846085348849016055': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-13085037572156381968': 'file_storage/function-call-13085037572156381968.json', 'var_function-call-1254515193280365466': [{'COUNT(*)': '1405'}], 'var_function-call-13580482470423784099': 'file_storage/function-call-13580482470423784099.json', 'var_function-call-5769832818917747020': [], 'var_function-call-8243376314728765099': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'has_empirical': False, 'header_snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n"}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'has_empirical': False, 'header_snippet': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Hum'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'has_empirical': True, 'header_snippet': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Anima'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'has_empirical': True, 'header_snippet': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n '}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None, 'has_empirical': False, 'header_snippet': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation '}], 'var_function-call-18154700937133714252': [], 'var_function-call-15004411282572223018': {'year_distribution': {'2015': 1}, 'empirical_count': 2, 'total_papers': 5}, 'var_function-call-5830780861978788181': 'file_storage/function-call-5830780861978788181.json', 'var_function-call-14906456097883813854': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citation_count': 265}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citation_count': 266}]}

exec(code, env_args)
