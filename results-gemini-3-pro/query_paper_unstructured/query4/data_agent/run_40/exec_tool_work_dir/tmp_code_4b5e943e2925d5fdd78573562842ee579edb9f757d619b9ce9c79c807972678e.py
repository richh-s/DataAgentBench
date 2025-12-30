code = """import json
import re

with open(locals()['var_function-call-17095788158205138574'], 'r') as f:
    papers = json.load(f)

print("__RESULT__:")
# Debug: find papers that have 'physical activity' and '2016' in text but failed the strict header check
missed = []
for p in papers:
    text = p['text']
    title = p['filename'].replace('.txt', '')
    
    if 'physical activity' in text.lower():
        # strict check
        check_text = text[:5000]
        pattern = r"(?:CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s*(?:'16|2016)|Copyright\s+(?:©\s*)?2016|Permission\s+to\s+make\s+digital.*?2016"
        if not re.search(pattern, check_text, re.IGNORECASE | re.DOTALL):
            # Check if 2016 is mentioned nearby in a way that suggests publication
            # just print title and first 200 chars to check
            missed.append({"title": title, "snippet": text[:200]})

print(json.dumps(missed))"""

env_args = {'var_function-call-16853199496411036361': 'file_storage/function-call-16853199496411036361.json', 'var_function-call-17095788158205138574': 'file_storage/function-call-17095788158205138574.json', 'var_function-call-7387633955592090896': 'file_storage/function-call-7387633955592090896.json', 'var_function-call-11266484425143730548': [], 'var_function-call-5358281181828038604': ['Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard Unive', 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  conditi', 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent Crocher1,3, Frank Vetere1, Suranga Nanayakkara1,4 \n1Microsoft Research Centre for SocialNUI, The Univ', 'Beyond Abandonment to Next Steps: Understanding and \nDesigning for Life after Personal Informatics Tool Use \n\nDaniel A. Epstein1, Monica Caraway2, Chuck Johnston2, \nAn Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University', 'Beyond Behavior: The Coach’s Perspective \n on Technology in Health Coaching \n\nHeleen Rutjes \n Human-Technology Interaction \n Eindhoven University of Technology \n Eindhoven, the Netherlands \n H.Rutjes@tue.nl \n\nMartijn C. Willemsen \n Human-Technology Interaction \n Eindhoven University of Technology \n '], 'var_function-call-9795341655051111948': [{'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'citation_count': 636}]}

exec(code, env_args)
