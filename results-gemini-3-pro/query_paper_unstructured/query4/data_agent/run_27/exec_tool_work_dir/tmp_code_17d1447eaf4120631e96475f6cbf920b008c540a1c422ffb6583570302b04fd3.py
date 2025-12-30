code = """import json
import re
from collections import Counter

with open(locals()['var_function-call-14323313354234643834'], 'r') as f:
    papers = json.load(f)

venues = "CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH"

debug_pa_papers = []

for p in papers:
    text = p.get('text', '')
    title = p.get('filename', '')
    
    # Domain check
    if 'physical activity' in text.lower():
        # Extract year
        y_cop = re.findall(r'Copyright.*?(\d{4})', text, re.IGNORECASE)
        y_acm = re.findall(r'(\d{4})\s*ACM', text)
        y_conf = re.findall(r'(?:' + venues + r').*?(\d{4})', text, re.IGNORECASE)
        
        candidates = y_cop + y_acm + y_conf
        valid_years = [y for y in candidates if 2000 <= int(y) <= 2024]
        
        best_year = "None"
        if valid_years:
            best_year = Counter(valid_years).most_common(1)[0][0]
        
        debug_pa_papers.append({"title": title, "year": best_year, "years_found": valid_years})

print("__RESULT__:")
print(json.dumps(debug_pa_papers))"""

env_args = {'var_function-call-8814252410451424238': ['paper_docs'], 'var_function-call-5259206578733669392': 'file_storage/function-call-5259206578733669392.json', 'var_function-call-14323313354234643834': 'file_storage/function-call-14323313354234643834.json', 'var_function-call-12161874527337870347': ['Citations', 'sqlite_sequence'], 'var_function-call-7764328309385985012': 'file_storage/function-call-7764328309385985012.json', 'var_function-call-3369097710081167039': [], 'var_function-call-6510332609486320018': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'years': [], 'has_pa': True}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'years': [], 'has_pa': True}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'years': [], 'has_pa': False}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'years': [], 'has_pa': False}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'years': [], 'has_pa': False}], 'var_function-call-5498128891951429973': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \n\nABSTRACT \nCurrent  models  of  how  people  use  personal  informatics \nsystems are largely based in behavior change goals. They do \nnot  adequately  characteriz", 'var_function-call-2372319320552918241': [], 'var_function-call-3375896330272505398': [], 'var_function-call-4716451782019835983': {'2015': 1, "'15": 1}, 'var_function-call-7959346322132370818': ["UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu", 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 152', 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali', 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n E', 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent C'], 'var_function-call-17428978023062246028': {'count': 3, 'examples': ['ng, François\n\nGuimbetiere, and Tanzeem Choudhury. 2016.\nEmotionCheck: leveraging bodily signals and ', 'Paul  Dendale,  Kris  Luyten  and  Karin \nConinx. 2016. Back on bike: the BoB mobile cycling app for', 'quest  permissions\nfrom Permissions@acm.org. \nDIS 2016, June 04 - 08, 2016, Brisbane, QLD, Australia']}, 'var_function-call-6568798951610469619': {'2015': 3, '2016': 3}, 'var_function-call-16268306268256240637': {'2015': 1}, 'var_function-call-14696234152299367750': [['A Lived Informatics Model of Personal Informatics.txt', '2015'], ['A Stage-based Model of Personal Informatics Systems.txt', '2010'], ['A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', '2018'], ['A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', '2019'], ['ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'None']], 'var_function-call-5460376318601530807': [], 'var_function-call-2519719532387138222': {'papers_2016': [], 'papers_pa': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': '2015'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': '2010'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': '2018'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': '2019'}]}, 'var_function-call-15740013008563417737': {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'header_snippet': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent Crocher1,3, Frank Vetere1, Suranga Nanayakkara1,4 \n1Microsoft Research Centre for SocialNUI, The University of Melbourne, Australia \n2Queensland University of Technology, Brisbane, Australia \n3Department of Mechanical Engineering, The University of Melbourne, Australia \n4Augmented Human Lab, Singapore University of Technology and Design, Singapore \n5The Royal Melbourne Hospital, Australia \n{ploderer, vincent.crocher, f.vetere}@unimelb.edu.au, {justinf, siddharthn}@student.unimelb.edu.au, \n{anusha, suranga}@ahlab.org, marlena.klaic@mh.org.au \n\nthrough \n\nABSTRACT \nThis  paper  describes  the  design  of  “ArmSleeve”,  a  patient \nmonitoring  system  to  support  occupational  therapists  in \ntheir  upper  limb  rehabilitation  work  with  stroke  patients. \nOccupational therapists can provide', 'index_of_dis_2016': 2943}, 'var_function-call-7796914705444684450': []}

exec(code, env_args)
