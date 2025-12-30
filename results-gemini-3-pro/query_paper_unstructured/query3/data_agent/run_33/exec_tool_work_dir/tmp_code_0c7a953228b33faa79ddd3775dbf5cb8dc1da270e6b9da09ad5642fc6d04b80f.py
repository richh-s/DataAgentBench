code = """import json
import re

path = locals()['var_function-call-454889790813745050']
with open(path, 'r') as f:
    docs = json.load(f)

extracted = []
venues = ["CHI", "Ubicomp", "CSCW", "DIS", "PervasiveHealth", "WWW", "IUI", "OzCHI", "TEI", "AH"]

for doc in docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Extract Year
    # Look for year associated with venue or just appearing in header
    # Search for 2016-2025
    year = None
    # Check first 1000 chars for a year
    header = text[:1000]
    years = re.findall(r'(201[6-9]|202[0-4])', header)
    if years:
        year = int(years[0]) # Take the first one found
    else:
        # Fallback: check specifically for "2015" etc just to see
        # But query asks for > 2016.
        pass
        
    # Check Contribution
    # Check for line "Contribution: ..."
    contribution_text = ""
    has_empirical_kw = "empirical" in text.lower()
    
    # Try to find specific metadata line
    for line in text.split('\n'):
        if "contribution" in line.lower() and ":" in line:
            contribution_text += line + " "
    
    extracted.append({
        "title": title,
        "year": year,
        "has_empirical_kw": has_empirical_kw,
        "contrib_line": contribution_text
    })

print("__RESULT__:")
print(json.dumps(extracted))"""

env_args = {'var_function-call-454889790813745050': 'file_storage/function-call-454889790813745050.json', 'var_function-call-2725923968047008507': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-7236080537222007473': {'start': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \n\nABSTRACT \nCurrent  models  of  how  people  use  personal  informatics \nsystems are largely based in behavior change goals. They do \nnot  adequately  characteriz", 'end': '\nInferring Meal Eating Activities in Real World Settings \nfrom Ambient Sounds: A Feasibility Study. IUI 2015, \n427-431. \n\n40.  Toscos, T., Faber, A., Connelly, K., and Upoma, A.M. \n\nEncouraging Physical Activity in Teens: Can \nTechnology Help Reduce Barriers to Physical Activity \nin Adolescent Girls? PervasiveHealth 2008, 218-221. \n41.  Whooley, M., Gray, K., Ploderer, B., and Gray, K. On \n\nthe Integration of Self-tracking Data amongst \nQuantified Self Members. HCI 2014, 151-160.  \n\n742\n\n \n \n \n\x0c'}, 'var_function-call-13029464252544165405': 'file_storage/function-call-13029464252544165405.json', 'var_function-call-7875787986985144672': 'Success', 'var_function-call-14039091801293034967': ['2015', 'None', 'None', 'None', 'None'], 'var_function-call-5957332521816669202': [{'y': '2015', 'emp': False, 'head': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA"}, {'y': 'None', 'emp': False, 'head': 'A Stage-Based Model of Personal Informatics System'}, {'y': 'None', 'emp': True, 'head': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpe'}, {'y': 'None', 'emp': True, 'head': 'A Wee Bit More Interaction: Designing and Evaluati'}, {'y': 'None', 'emp': False, 'head': 'ArmSleeve: a Patient Monitoring System to Support '}]}

exec(code, env_args)
