code = """import json
import re

file_path = locals()['var_function-call-2573740285369106607']

with open(file_path, 'r') as f:
    docs = json.load(f)

papers = []
for doc in docs:
    text = doc['text']
    filename = doc['filename']
    
    # Year
    # Find all 20xx
    years = re.findall(r'20\d\d', text[:2000]) # check first 2000 chars
    # Also 'xx
    short_years = re.findall(r"'\d{2}", text[:500])
    
    candidates = []
    for y in years:
        if 2000 <= int(y) <= 2024:
            candidates.append(int(y))
    for sy in short_years:
        y = int(sy[1:])
        if 10 <= y <= 24:
             candidates.append(2000 + y)
    
    # Heuristic: The earliest year >= 2000 in the header is usually the pub year (or copyright).
    # Sometimes header has "Since 2000".
    # Let's pick the most common one in the header? Or the first one?
    # Usually "CHI 2019" is at the top.
    if candidates:
        # Take the first one?
        year = candidates[0]
    else:
        year = None
        
    # Empirical
    # Keywords
    text_lower = text.lower()
    keywords = ["participants", "user study", "interviews", "interviewed", "recruited", "empirical"]
    is_empirical = False
    for kw in keywords:
        if kw in text_lower:
            is_empirical = True
            break
            
    papers.append({
        "title": filename.replace(".txt", ""),
        "year": year,
        "is_empirical": is_empirical
    })

print("__RESULT__:")
print(json.dumps(papers))"""

env_args = {'var_function-call-7387203186474718594': 'file_storage/function-call-7387203186474718594.json', 'var_function-call-9551476032774433042': ['paper_docs'], 'var_function-call-7392786003504292061': {'explicit_contribution': '', 'empirical_context': '', 'years': ['2015', '2015', '2015', '2015', '2015', '2015', '2015', '2015', '2014', '2013']}, 'var_function-call-16070472679849682591': 'file_storage/function-call-16070472679849682591.json', 'var_function-call-14838569663088297683': 'file_storage/function-call-14838569663088297683.json', 'var_function-call-2573740285369106607': 'file_storage/function-call-2573740285369106607.json', 'var_function-call-17192200102339754629': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'year': 2015, 'contrib_context': 'contributions  through  survey  design  and  parti', 'has_empirical': False}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'year': None, 'contrib_context': 'contributions  in  this  paper:  1)  we  identify ', 'has_empirical': False}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'year': None, 'contrib_context': '', 'has_empirical': True}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'year': None, 'contrib_context': 'contribution “I like drawing!” (UP4),  some  did n', 'has_empirical': True}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'year': None, 'contrib_context': 'contribution of this research is  a  system  desig', 'has_empirical': False}], 'var_function-call-8037773018140063796': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'header_snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN  A Lived Informatics Model of Personal Informatics  ", 'contribution_snippet': 'contributions  through  survey  design  and  participant  interviews.  We  also  thank  Elena  Agapie,  Elizabeth  Bales,  Lucas  Franco  Colusso, Felicia Cordeiro, and Ravi Karkar for early feedback '}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'header_snippet': 'A Stage-Based Model of Personal Informatics Systems  Ian Li1, Anind Dey1, and Jodi Forlizzi1,2  1Hum', 'contribution_snippet': 'contributions  in  this  paper:  1)  we  identify  problems  across  personal  informatics  tools,  2)  we  introduce and discuss a model that improves the diagnosis,  in  personal  assessment,  and  '}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'header_snippet': 'Fengjiao Peng MIT Media Lab Cambridge, MA, USA fpeng@mit.edu  A Trip to the Moon: Personalized Anima', 'contribution_snippet': ''}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'header_snippet': 'A Wee Bit More Interaction: Designing and Evaluating   an Overactive Bladder App  Ana-Maria Salai   ', 'contribution_snippet': 'contribution “I like drawing!” (UP4),  some  did not like  drawing: “I don’t like drawing things.” (UP9).   3.3  Design Decisions   Based on the design findings from this study, we developed  the  fir'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'header_snippet': 'ArmSleeve: a Patient Monitoring System to Support  Occupational Therapists in Stroke Rehabilitation ', 'contribution_snippet': 'contribution of this research is  a  system  designed  to  support  the  work  of  occupational  therapists.    This  research  describes  the  design  of  the  ArmSleeve  system,  a  patient  monitor'}]}

exec(code, env_args)
