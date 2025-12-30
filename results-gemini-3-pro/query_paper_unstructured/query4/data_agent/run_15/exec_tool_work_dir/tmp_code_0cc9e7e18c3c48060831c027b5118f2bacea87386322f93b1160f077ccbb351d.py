code = """import json
import re

with open(locals()['var_function-call-18231062501554874953'], 'r') as f:
    docs = json.load(f)

titles = []
for doc in docs:
    text = doc['text']
    # Check domain
    if 'physical activity' not in text.lower():
        continue
        
    # Check year 2016 in first 5000 chars
    head = text[:5000]
    
    # Patterns for 2016 publication
    patterns = [
        r"Copyright.*?2016",
        r"©.*?2016",
        r"(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH).*?(2016|'16)",
        r"2016\s*ACM",
        r"ACM\s*.*?2016",
        r"Permission.*?2016",
        r"January.*?2016", r"February.*?2016", r"March.*?2016", r"April.*?2016",
        r"May.*?2016", r"June.*?2016", r"July.*?2016", r"August.*?2016",
        r"September.*?2016", r"October.*?2016", r"November.*?2016", r"December.*?2016"
    ]
    
    is_2016 = False
    for pat in patterns:
        if re.search(pat, head, re.IGNORECASE | re.DOTALL):
            is_2016 = True
            break
            
    if is_2016:
        titles.append(doc['filename'].replace('.txt', ''))

print("__RESULT__:")
print(json.dumps(titles))"""

env_args = {'var_function-call-15828363465301237669': 'file_storage/function-call-15828363465301237669.json', 'var_function-call-5049852519434866755': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-18231062501554874953': 'file_storage/function-call-18231062501554874953.json', 'var_function-call-4823252345665697145': [], 'var_function-call-4264647216091307837': ['Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard Unive', 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  conditi', 'Beyond Abandonment to Next Steps: Understanding and \nDesigning for Life after Personal Informatics Tool Use \n\nDaniel A. Epstein1, Monica Caraway2, Chuck Johnston2, \nAn Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University', 'Beyond Behavior: The Coach’s Perspective \n on Technology in Health Coaching \n\nHeleen Rutjes \n Human-Technology Interaction \n Eindhoven University of Technology \n Eindhoven, the Netherlands \n H.Rutjes@tue.nl \n\nMartijn C. Willemsen \n Human-Technology Interaction \n Eindhoven University of Technology \n ', 'Charting Design Preferences on Wellness Wearables  \n\nJuho Rantakari1, Virve Inget2, Ashley Colley1, Jonna Häkkilä1 \n\n1University of Lapland \nYliopistokatu 8 \n96400 Rovaniemi, Finland \nfirstname.lastname@ulapland.fi \n\n2Center for Ubiquitous Computing \nP.O Box 4500 \n90014 University of Oulu, Finland \n'], 'var_function-call-15351404564757081740': [{'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'indices_2016_first_5': [49375, 49488, 52909], 'indices_16_first_5': [], 'conf_match': None}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'indices_2016_first_5': [65587, 66348, 68096, 69324, 70495], 'indices_16_first_5': [], 'conf_match': None}, {'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt', 'indices_2016_first_5': [3015, 3043, 5791, 12655, 19408], 'indices_16_first_5': [2999], 'conf_match': "CHI'16, May 07-12, 2016"}, {'filename': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching.txt", 'indices_2016_first_5': [13642, 28433, 41103, 71704, 72660], 'indices_16_first_5': [], 'conf_match': 'teijn.  2016'}, {'filename': 'Charting Design Preferences on Wellness Wearables.txt', 'indices_2016_first_5': [3195, 3217, 3246], 'indices_16_first_5': [], 'conf_match': 'AH 2016'}]}

exec(code, env_args)
