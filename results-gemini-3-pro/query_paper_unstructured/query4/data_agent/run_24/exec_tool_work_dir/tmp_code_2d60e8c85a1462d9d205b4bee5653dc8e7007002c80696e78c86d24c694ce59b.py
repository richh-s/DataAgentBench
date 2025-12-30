code = """import json
import re

try:
    with open(locals()['var_function-call-18233020040394176288'], 'r') as f:
        papers = json.load(f)
except:
    papers = []

titles = []
relevant_papers = []

for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    
    # Domain check
    if 'physical activity' not in text.lower():
        continue
        
    # Year check
    # Check first 1000 chars
    header = text[:1000]
    
    is_2016 = False
    
    # 1. Look for explicit conference year like CHI '16, UbiComp '16
    if re.search(r"(?:CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s*'?16", header, re.IGNORECASE):
        is_2016 = True
    # 2. Look for date line with 2016
    elif re.search(r"(?:January|February|March|April|May|June|July|August|September|October|November|December).{0,20}2016", header, re.IGNORECASE):
        is_2016 = True
    # 3. Look for Copyright 2016
    elif re.search(r"(?:Copyright|©).{0,20}2016", header, re.IGNORECASE):
        is_2016 = True
    # 4. Look for ACM/IEEE 2016 or just 2016 in the very top part (first 300 chars) usually indicates year
    elif re.search(r"2016", header[:300]):
        # Check if it's not part of a DOI or something unrelated? 
        # But top 300 is usually safe.
        is_2016 = True
        
    # Exclusion: If Copyright/Conference says 2015, 2017, etc., it overrides weak matches.
    if re.search(r"(?:Copyright|©).{0,20}(?:2015|2014|2013|2017|2018|2019)", header, re.IGNORECASE):
        # Unless we also found a strong 2016 indicator? 
        # Usually copyright year is definitive.
        if not re.search(r"(?:Copyright|©).{0,20}2016", header, re.IGNORECASE):
            is_2016 = False
            
    if is_2016:
        title = filename.replace('.txt', '')
        titles.append(title)

print("__RESULT__:")
print(json.dumps(titles))"""

env_args = {'var_function-call-13566097313952112574': 'file_storage/function-call-13566097313952112574.json', 'var_function-call-5276622005229675102': 'file_storage/function-call-5276622005229675102.json', 'var_function-call-15838140455159973064': [], 'var_function-call-16252018297350116542': 'Debug info printed', 'var_function-call-18172961170683457814': ['Total papers: 5', {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'header_snippet': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard University\nCambridge, MA, USA\neyue@college.harvard.edu\n\nABSTRACT\nSelf-tracking physiological and psychological data poses the\nchallenge of presentation and interpretation. Insightful nar-\nratives for self-', 'has_physical_activity': True, 'has_2016_header': False}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'header_snippet': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  condition, \naffecting  20%  of  the  population.  Even  though  it  is  a \ntreatable  condition,  people  often  do  not  seek  treatment.  In \nthis paper, we  describe how we co-designed and evaluated \nwith', 'has_physical_activity': True, 'has_2016_header': False}, {'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt', 'header_snippet': 'Beyond Abandonment to Next Steps: Understanding and \nDesigning for Life after Personal Informatics Tool Use \n\nDaniel A. Epstein1, Monica Caraway2, Chuck Johnston2, \nAn Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {mcaraway, chuck2, anping, smunson}@uw.edu \n\nABSTRACT \nRecent  research  examines  how  and  why  people  abandon \nself-tracking tools. We exten', 'has_physical_activity': True, 'has_2016_header': False}, {'filename': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching.txt", 'header_snippet': 'Beyond Behavior: The Coach’s Perspective \n on Technology in Health Coaching \n\nHeleen Rutjes \n Human-Technology Interaction \n Eindhoven University of Technology \n Eindhoven, the Netherlands \n H.Rutjes@tue.nl \n\nMartijn C. Willemsen \n Human-Technology Interaction \n Eindhoven University of Technology \n Eindhoven, the Netherlands \n M.C.Willemsen@tue.com \n\nWijnand A. IJsselsteijn  \nHuman-Technology Interaction \n Eindhoven University of Technology \n Eindhoven, the Netherlands \n W.A.IJsselsteijn@tue.com', 'has_physical_activity': True, 'has_2016_header': False}, {'filename': 'Charting Design Preferences on Wellness Wearables.txt', 'header_snippet': 'Charting Design Preferences on Wellness Wearables  \n\nJuho Rantakari1, Virve Inget2, Ashley Colley1, Jonna Häkkilä1 \n\n1University of Lapland \nYliopistokatu 8 \n96400 Rovaniemi, Finland \nfirstname.lastname@ulapland.fi \n\n2Center for Ubiquitous Computing \nP.O Box 4500 \n90014 University of Oulu, Finland \nfirstname.lastname@oulu.fi \n\nABSTRACT \nThis paper presents a study on people’s preferences with wearable \nwellness  devices.  The  results  are  based  on  an  online  survey \n(n=84),  where  people  ', 'has_physical_activity': True, 'has_2016_header': False}], 'var_function-call-18233020040394176288': 'file_storage/function-call-18233020040394176288.json'}

exec(code, env_args)
