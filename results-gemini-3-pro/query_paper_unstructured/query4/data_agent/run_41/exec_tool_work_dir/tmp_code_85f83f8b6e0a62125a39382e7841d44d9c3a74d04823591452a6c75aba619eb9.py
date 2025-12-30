code = """import json
import re

file_path = locals()['var_function-call-16322124554372865657']
with open(file_path, 'r') as f:
    papers = json.load(f)

titles_2016 = []

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    
    # Check for publication year 2016
    # Search in the first 3000 and last 3000 characters
    # (Metadata often at the start or end)
    
    region_of_interest = text[:3000] + "\n" + text[-3000:]
    
    is_2016 = False
    
    # Check for Copyright 2016
    if re.search(r'Copyright\s+(?:©|\\u00a9|\(c\))?\s*2016', region_of_interest, re.IGNORECASE):
        is_2016 = True
    
    # Check for Conference header/footer with 2016
    # Matches: "CHI 2016", "UbiComp '16", "September 2016"
    elif re.search(r'(?:CHI|UbiComp|CSCW|DIS|IUI|PervasiveHealth|WWW|OzCHI|TEI|AH)\s*(?:[\w\s,.-]+)?(?:2016|\'16)', region_of_interest, re.IGNORECASE):
        is_2016 = True
        
    # Check for "Permission ... 2016"
    elif re.search(r'Permission.*2016', region_of_interest, re.IGNORECASE):
        is_2016 = True
        
    # Check for specific date format "Month DD-DD, 2016"
    elif re.search(r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}[–-]\d{1,2},?\s+2016', region_of_interest, re.IGNORECASE):
        is_2016 = True
        
    if is_2016:
        # Check domain "physical activity" (case insensitive)
        if "physical activity" in text.lower():
            titles_2016.append(filename.replace('.txt', ''))

print("__RESULT__:")
print(json.dumps(titles_2016))"""

env_args = {'var_function-call-4836586951926601287': ['paper_docs'], 'var_function-call-4836586951926600548': 'file_storage/function-call-4836586951926600548.json', 'var_function-call-218136711215706544': 'file_storage/function-call-218136711215706544.json', 'var_function-call-16322124554372865657': 'file_storage/function-call-16322124554372865657.json', 'var_function-call-805702450646494683': [], 'var_function-call-10525079842332072840': ['Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard University\nCambridge, MA, USA\neyue@college.harvard.edu\n\nABSTRACT\nSelf-tracking physiological and psychological data poses the\nchallenge of presentation and interpretation. Insightful nar-\nratives for self-', 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  condition, \naffecting  20%  of  the  population.  Even  though  it  is  a \ntreatable  condition,  people  often  do  not  seek  treatment.  In \nthis paper, we  describe how we co-designed and evaluated \nwith', 'Beyond Abandonment to Next Steps: Understanding and \nDesigning for Life after Personal Informatics Tool Use \n\nDaniel A. Epstein1, Monica Caraway2, Chuck Johnston2, \nAn Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {mcaraway, chuck2, anping, smunson}@uw.edu \n\nABSTRACT \nRecent  research  examines  how  and  why  people  abandon \nself-tracking tools. We exten']}

exec(code, env_args)
