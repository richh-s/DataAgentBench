code = """import json
import re
import pandas as pd

# Load files
with open(locals()['var_function-call-13085037572156381968'], 'r') as f:
    papers = json.load(f)

with open(locals()['var_function-call-13580482470423784099'], 'r') as f:
    citations = json.load(f)

citations_df = pd.DataFrame(citations)
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'])

def normalize_year(y_str):
    if len(y_str) == 2:
        return 2000 + int(y_str)
    return int(y_str)

results = []
venues_regex = r"(CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s*['\u2019]?\s*(\d{2,4})"

for p in papers:
    title = p['filename'].replace('.txt', '')
    text = p['text']
    
    pub_year = None
    
    # Strategy 1: Venue + Year in header
    header = text[:1000]
    venue_match = re.search(venues_regex, header, re.IGNORECASE)
    if venue_match:
        pub_year = normalize_year(venue_match.group(2))
    
    # Strategy 2: Copyright year
    if not pub_year:
        copy_match = re.search(r"Copyright\s+.*(20\d{2})", header, re.IGNORECASE)
        if copy_match:
            pub_year = int(copy_match.group(1))
            
    # Strategy 3: Any 4 digit year in first 200 chars
    if not pub_year:
        y_match = re.search(r"\b(20[0-2]\d)\b", text[:200])
        if y_match:
            pub_year = int(y_match.group(1))
            
    # Check Empirical
    is_empirical = "empirical" in text.lower()
    
    if pub_year and pub_year > 2016 and is_empirical:
        paper_cits = citations_df[citations_df['title'] == title]
        if not paper_cits.empty:
            total = paper_cits['citation_count'].sum()
            results.append({
                "title": title,
                "total_citation_count": int(total)
            })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-7886853940146991682': 'file_storage/function-call-7886853940146991682.json', 'var_function-call-14846085348849016055': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-13085037572156381968': 'file_storage/function-call-13085037572156381968.json', 'var_function-call-1254515193280365466': [{'COUNT(*)': '1405'}], 'var_function-call-13580482470423784099': 'file_storage/function-call-13580482470423784099.json', 'var_function-call-5769832818917747020': [], 'var_function-call-8243376314728765099': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'has_empirical': False, 'header_snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n"}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'has_empirical': False, 'header_snippet': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Hum'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'has_empirical': True, 'header_snippet': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Anima'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'has_empirical': True, 'header_snippet': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n '}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None, 'has_empirical': False, 'header_snippet': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation '}]}

exec(code, env_args)
