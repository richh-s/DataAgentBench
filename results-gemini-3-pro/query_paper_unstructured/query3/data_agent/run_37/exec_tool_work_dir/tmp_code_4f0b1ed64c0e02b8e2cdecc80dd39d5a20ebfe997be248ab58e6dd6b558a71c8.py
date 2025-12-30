code = """import json
import re
from collections import Counter

with open(locals()['var_function-call-1188879216130437550'], 'r') as f:
    papers = json.load(f)

paper_years = []

for p in papers:
    text = p.get('text', '')
    title = p.get('filename', '').replace('.txt', '')
    
    scan_text = text[:3000] + "\n" + text[-3000:]
    
    # regex for venue
    # splitting the pattern to avoid long line issues or quote issues
    venues = "CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH"
    # match year: 4 digits OR single quote + 2 digits
    # use ['] to match single quote
    pattern = "(" + venues + ")" + r".*?(\d{4}|[']\d{2})"
    
    venue_match = re.search(pattern, scan_text, re.IGNORECASE)
    
    year = None
    if venue_match:
        y_str = venue_match.group(2)
        if len(y_str) == 4:
            year = int(y_str)
        elif y_str.startswith("'"):
            year = 2000 + int(y_str[1:])
    
    if not year:
        copy_match = re.search(r"Copyright.*?20(\d{2})", scan_text, re.IGNORECASE)
        if copy_match:
            year = 2000 + int(copy_match.group(1))
            
    if not year:
        years = re.findall(r"20\d{2}", scan_text)
        valid_years = [int(y) for y in years if 2010 <= int(y) <= 2025]
        if valid_years:
            c = Counter(valid_years)
            year = c.most_common(1)[0][0]
            
    paper_years.append({"title": title, "year": year})

print("__RESULT__:")
print(json.dumps(paper_years))"""

env_args = {'var_function-call-563988683724796528': 'file_storage/function-call-563988683724796528.json', 'var_function-call-1188879216130437550': 'file_storage/function-call-1188879216130437550.json', 'var_function-call-6926115911538441459': 'file_storage/function-call-6926115911538441459.json', 'var_function-call-11700601508177380664': [], 'var_function-call-15227438266193405659': [{'title': 'A Lived Informatics Model of Personal Informatics', 'extracted_year': None, 'has_empirical': False}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'extracted_year': None, 'has_empirical': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'extracted_year': None, 'has_empirical': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'extracted_year': None, 'has_empirical': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'extracted_year': None, 'has_empirical': False}], 'var_function-call-4638443691179812252': ["Paper 0: matches=['2015']", 'Paper 1: matches=[]', 'Paper 2: matches=[]', 'Paper 3: matches=[]', 'Paper 4: matches=[]'], 'var_function-call-1232675705292650106': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 15213 \nianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu \n\nABSTRACT \nPeople  strive  to  obtain  self-knowledge.  A  class  of  systems \ncalled  personal  informatics  is  appearing  that  help  people \ncollect and reflect on personal information. However, there \nis no comprehensive list of problems that users experience \nusing  these  systems,  and  no  guidance  for  making  these \nsystems  more  effective.  To  address  this,  we  conducted \nsurveys and interviews with people who collect and reflect \non  personal  information.  We  derived  a  stage-based  model \nof  personal  informatics  systems  composed  of  five  stages  \n(preparation, collection, integration, reflection, and action) \nand  identified  barriers  in  each  of  the  stages.  These  stages \nhave  four  essential  properties:  b', 'var_function-call-9291635066695142137': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  condition, \naffecting  20%  of  the  population.  Even  though  it  is  a \ntreatable  condition,  people  often  do  not  seek  treatment.  In \nthis paper, we  describe how we co-designed and evaluated \nwith  30  stakeholders  (9  medical  professionals  and  21  end-\nusers)  an  OAB  mobile  health  application  that  aims  to \nincrease  adherence  to  self-managed  treatment.  Our  results \nsupport previous research that visualizing progress, setting \ngoals, receiving reminders and feedback  increases  use.  We \ndiscovered  that  games  could  be  used  successfully  as  a \ndistraction technique for urge suppression. Contrary to the \ncurrent research direction, automatically calculated features \n', 'var_function-call-12075459260304953316': {'copyright_year': None, 'years_found': []}, 'var_function-call-4736028606523868203': {'len': 74850, 'tail': 'f My Soul – How People Bond with Their \nMobile Phones. In Proc. ACM MobileHCI’08. \n\n[61]   Lois M. Verbrugg 1980. Health diaries. Medical care 18.1: 73-95. \n[62]  Graham  Wilson  and  Stephen  A.  Brewster.  2017.  Multi-Moji: \nCombining  Thermal,  Vibrotactile  &  Visual  Stimuli  to  Expand  the \nAffective Range of Feedback. In Proc. CHI’17. \n\n[63]   2048, https://en.wikipedia.org/wiki/2048_(video_game) \n\nCHI 2019 Paper  CHI 2019, May 4–9, 2019, Glasgow, Scotland, UKPaper 703Page 14 \n \n \n \n \n\x0c'}}

exec(code, env_args)
