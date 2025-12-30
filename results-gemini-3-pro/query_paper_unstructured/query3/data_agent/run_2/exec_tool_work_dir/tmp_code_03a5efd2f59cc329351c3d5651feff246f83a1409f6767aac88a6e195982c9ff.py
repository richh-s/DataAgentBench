code = """import json
import re
from collections import Counter

with open(locals()['var_function-call-13085037572156381968'], 'r') as f:
    papers = json.load(f)

extracted_years = []
empirical_count = 0
venues_regex = r"(CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s*['\u2019]?\s*(\d{2,4})"

for p in papers:
    text = p['text']
    header = text[:1000]
    
    pub_year = None
    venue_match = re.search(venues_regex, header, re.IGNORECASE)
    if venue_match:
        y_str = venue_match.group(2)
        pub_year = 2000 + int(y_str) if len(y_str) == 2 else int(y_str)
    
    if not pub_year:
        copy_match = re.search(r"Copyright\s+.*(20\d{2})", header, re.IGNORECASE)
        if copy_match:
            pub_year = int(copy_match.group(1))
            
    if not pub_year:
        y_match = re.search(r"\b(20[0-2]\d)\b", text[:200])
        if y_match:
            pub_year = int(y_match.group(1))
            
    if pub_year:
        extracted_years.append(pub_year)
    
    if "empirical" in text.lower():
        empirical_count += 1

print("__RESULT__:")
print(json.dumps({
    "year_distribution": dict(Counter(extracted_years)),
    "empirical_count": empirical_count,
    "total_papers": len(papers)
}))"""

env_args = {'var_function-call-7886853940146991682': 'file_storage/function-call-7886853940146991682.json', 'var_function-call-14846085348849016055': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-13085037572156381968': 'file_storage/function-call-13085037572156381968.json', 'var_function-call-1254515193280365466': [{'COUNT(*)': '1405'}], 'var_function-call-13580482470423784099': 'file_storage/function-call-13580482470423784099.json', 'var_function-call-5769832818917747020': [], 'var_function-call-8243376314728765099': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'has_empirical': False, 'header_snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n"}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'has_empirical': False, 'header_snippet': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Hum'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'has_empirical': True, 'header_snippet': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Anima'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'has_empirical': True, 'header_snippet': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n '}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None, 'has_empirical': False, 'header_snippet': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation '}], 'var_function-call-18154700937133714252': []}

exec(code, env_args)
