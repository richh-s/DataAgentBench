code = """import json
import re

with open(locals()['var_function-call-18231062501554874953'], 'r') as f:
    docs = json.load(f)

# Analyze first 10 docs
results = []
for doc in docs[:10]:
    text = doc['text']
    # Find all occurrences of 2016
    indices_2016 = [m.start() for m in re.finditer('2016', text)]
    # Find all occurrences of '16
    indices_16 = [m.start() for m in re.finditer(r"'16", text)]
    
    # Check for specific conference patterns
    conf_2016 = re.search(r"(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH).*?2016", text, re.IGNORECASE)
    conf_16 = re.search(r"(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH).*?'16", text, re.IGNORECASE)
    
    res = {
        "filename": doc['filename'],
        "indices_2016_first_5": indices_2016[:5],
        "indices_16_first_5": indices_16[:5],
        "conf_match": conf_2016.group(0) if conf_2016 else (conf_16.group(0) if conf_16 else None)
    }
    results.append(res)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-15828363465301237669': 'file_storage/function-call-15828363465301237669.json', 'var_function-call-5049852519434866755': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-18231062501554874953': 'file_storage/function-call-18231062501554874953.json', 'var_function-call-4823252345665697145': [], 'var_function-call-4264647216091307837': ['Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard Unive', 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  conditi', 'Beyond Abandonment to Next Steps: Understanding and \nDesigning for Life after Personal Informatics Tool Use \n\nDaniel A. Epstein1, Monica Caraway2, Chuck Johnston2, \nAn Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University', 'Beyond Behavior: The Coach’s Perspective \n on Technology in Health Coaching \n\nHeleen Rutjes \n Human-Technology Interaction \n Eindhoven University of Technology \n Eindhoven, the Netherlands \n H.Rutjes@tue.nl \n\nMartijn C. Willemsen \n Human-Technology Interaction \n Eindhoven University of Technology \n ', 'Charting Design Preferences on Wellness Wearables  \n\nJuho Rantakari1, Virve Inget2, Ashley Colley1, Jonna Häkkilä1 \n\n1University of Lapland \nYliopistokatu 8 \n96400 Rovaniemi, Finland \nfirstname.lastname@ulapland.fi \n\n2Center for Ubiquitous Computing \nP.O Box 4500 \n90014 University of Oulu, Finland \n']}

exec(code, env_args)
