code = """import json
import re

file_path = locals()['var_function-call-2573740285369106607']

with open(file_path, 'r') as f:
    docs = json.load(f)

result_list = []
debug = []

for doc in docs:
    text = doc['text']
    filename = doc['filename']
    title = filename.replace(".txt", "")
    
    # YEAR
    # Look for 20xx
    # We use a pattern without single quotes to avoid parser issues if any
    # Just look for 4 digits
    years = re.findall(r"20[1-2][0-9]", text[:2000])
    
    # Try to find 'xx (apostrophe followed by 2 digits)
    # We'll rely on 4-digit years first.
    # Most papers have "20xx" in the copyright line or conference line.
    
    valid_years = []
    for y in years:
        yi = int(y)
        if 2010 <= yi <= 2024:
            valid_years.append(yi)
            
    # If no 4-digit year found, look for pattern like " '17 " or similar?
    # Skipping for now to avoid syntax errors.
    
    year = None
    if valid_years:
        # Heuristic: usually the first one is correct
        year = valid_years[0]
        
    # EMPIRICAL
    is_empirical = False
    # Check keywords
    kw = ["participants", "user study", "interviews", "recruited", "empirical"]
    if any(k in text.lower() for k in kw):
        is_empirical = True
        
    if year and year > 2016 and is_empirical:
        result_list.append({"title": title, "year": year})
    elif year is None:
        # Save title to check if we missed any
        debug.append(title)

print("__RESULT__:")
print(json.dumps({"matches": result_list, "missing_year": debug}))"""

env_args = {'var_function-call-7387203186474718594': 'file_storage/function-call-7387203186474718594.json', 'var_function-call-9551476032774433042': ['paper_docs'], 'var_function-call-7392786003504292061': {'explicit_contribution': '', 'empirical_context': '', 'years': ['2015', '2015', '2015', '2015', '2015', '2015', '2015', '2015', '2014', '2013']}, 'var_function-call-16070472679849682591': 'file_storage/function-call-16070472679849682591.json', 'var_function-call-14838569663088297683': 'file_storage/function-call-14838569663088297683.json', 'var_function-call-2573740285369106607': 'file_storage/function-call-2573740285369106607.json', 'var_function-call-17192200102339754629': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'year': 2015, 'contrib_context': 'contributions  through  survey  design  and  parti', 'has_empirical': False}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'year': None, 'contrib_context': 'contributions  in  this  paper:  1)  we  identify ', 'has_empirical': False}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'year': None, 'contrib_context': '', 'has_empirical': True}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'year': None, 'contrib_context': 'contribution “I like drawing!” (UP4),  some  did n', 'has_empirical': True}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'year': None, 'contrib_context': 'contribution of this research is  a  system  desig', 'has_empirical': False}], 'var_function-call-8037773018140063796': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'header_snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN  A Lived Informatics Model of Personal Informatics  ", 'contribution_snippet': 'contributions  through  survey  design  and  participant  interviews.  We  also  thank  Elena  Agapie,  Elizabeth  Bales,  Lucas  Franco  Colusso, Felicia Cordeiro, and Ravi Karkar for early feedback '}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'header_snippet': 'A Stage-Based Model of Personal Informatics Systems  Ian Li1, Anind Dey1, and Jodi Forlizzi1,2  1Hum', 'contribution_snippet': 'contributions  in  this  paper:  1)  we  identify  problems  across  personal  informatics  tools,  2)  we  introduce and discuss a model that improves the diagnosis,  in  personal  assessment,  and  '}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'header_snippet': 'Fengjiao Peng MIT Media Lab Cambridge, MA, USA fpeng@mit.edu  A Trip to the Moon: Personalized Anima', 'contribution_snippet': ''}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'header_snippet': 'A Wee Bit More Interaction: Designing and Evaluating   an Overactive Bladder App  Ana-Maria Salai   ', 'contribution_snippet': 'contribution “I like drawing!” (UP4),  some  did not like  drawing: “I don’t like drawing things.” (UP9).   3.3  Design Decisions   Based on the design findings from this study, we developed  the  fir'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'header_snippet': 'ArmSleeve: a Patient Monitoring System to Support  Occupational Therapists in Stroke Rehabilitation ', 'contribution_snippet': 'contribution of this research is  a  system  designed  to  support  the  work  of  occupational  therapists.    This  research  describes  the  design  of  the  ArmSleeve  system,  a  patient  monitor'}], 'var_function-call-1979176044345138821': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': 2015, 'is_empirical': True}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'is_empirical': True}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'is_empirical': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019, 'is_empirical': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None, 'is_empirical': True}]}

exec(code, env_args)
