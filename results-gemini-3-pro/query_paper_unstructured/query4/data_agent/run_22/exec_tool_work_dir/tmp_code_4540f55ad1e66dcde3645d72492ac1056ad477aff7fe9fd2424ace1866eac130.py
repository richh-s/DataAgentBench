code = """import json
import re

with open(locals()['var_function-call-4161258242438240829'], 'r') as f:
    papers = json.load(f)

paper_info = []

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Try to find year
    year = None
    if '2016' in text[:2000]:
        year = 2016
    elif "'16" in text[:500]: # Check header for '16
        year = 2016
    elif "2015" in text[:2000]:
        year = 2015
    elif "'15" in text[:500]:
        year = 2015
    # Check for other years
    else:
        # scan for any year-like pattern
        m = re.search(r'20\d\d', text[:2000])
        if m:
            year = int(m.group(0))
            
    # Check domain
    has_pa = 'physical activity' in text.lower()
    
    paper_info.append({
        'title': title,
        'detected_year': year,
        'has_physical_activity': has_pa
    })

print("__RESULT__:")
print(json.dumps(paper_info))"""

env_args = {'var_function-call-18065361926361048824': 'file_storage/function-call-18065361926361048824.json', 'var_function-call-1502338921683613399': 'file_storage/function-call-1502338921683613399.json', 'var_function-call-4041748401913796717': [], 'var_function-call-2901872464972295904': [], 'var_function-call-12598558614972453544': ["UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.wash", 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 15213 \nianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu \n\nABSTRACT \nPeople  strive  to  obtain  self-knowled', 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard Unive', 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  conditi', 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent Crocher1,3, Frank Vetere1, Suranga Nanayakkara1,4 \n1Microsoft Research Centre for SocialNUI, The Univ'], 'var_function-call-5379995669479938539': [], 'var_function-call-3504084481303803347': ['A Lived Informatics Model of Personal Informatics.txt'], 'var_function-call-964086390390166412': {'2015': 1, '2019': 4}, 'var_function-call-15929576778750581044': 5, 'var_function-call-4161258242438240829': 'file_storage/function-call-4161258242438240829.json'}

exec(code, env_args)
