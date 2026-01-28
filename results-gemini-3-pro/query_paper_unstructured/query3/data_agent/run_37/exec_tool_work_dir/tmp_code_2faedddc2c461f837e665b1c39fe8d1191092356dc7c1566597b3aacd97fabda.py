code = """import json
import re
from collections import Counter

with open(locals()['var_function-call-1188879216130437550'], 'r') as f:
    papers = json.load(f)

with open(locals()['var_function-call-6926115911538441459'], 'r') as f:
    citations_data = json.load(f)

citation_map = {}
for entry in citations_data:
    t = entry['title']
    c = int(entry['citation_count'])
    if t not in citation_map:
        citation_map[t] = 0
    citation_map[t] += c

results = []
for p in papers:
    text = p.get('text', '')
    title = p.get('filename', '').replace('.txt', '')
    
    # Check empirical
    if 'empirical' not in text.lower():
        continue
        
    # Extract year
    years = re.findall(r'20\d\d', text)
    valid_years = [int(y) for y in years if 2010 <= int(y) <= 2025]
    
    pub_year = 0
    if valid_years:
        c = Counter(valid_years)
        # Get the most common year
        pub_year = c.most_common(1)[0][0]
        
    if pub_year > 2016:
        results.append({
            "title": title,
            "total_citation_count": citation_map.get(title, 0)
        })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-563988683724796528': 'file_storage/function-call-563988683724796528.json', 'var_function-call-1188879216130437550': 'file_storage/function-call-1188879216130437550.json', 'var_function-call-6926115911538441459': 'file_storage/function-call-6926115911538441459.json', 'var_function-call-11700601508177380664': [], 'var_function-call-15227438266193405659': [{'title': 'A Lived Informatics Model of Personal Informatics', 'extracted_year': None, 'has_empirical': False}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'extracted_year': None, 'has_empirical': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'extracted_year': None, 'has_empirical': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'extracted_year': None, 'has_empirical': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'extracted_year': None, 'has_empirical': False}], 'var_function-call-4638443691179812252': ["Paper 0: matches=['2015']", 'Paper 1: matches=[]', 'Paper 2: matches=[]', 'Paper 3: matches=[]', 'Paper 4: matches=[]'], 'var_function-call-1232675705292650106': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 15213 \nianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu \n\nABSTRACT \nPeople  strive  to  obtain  self-knowledge.  A  class  of  systems \ncalled  personal  informatics  is  appearing  that  help  people \ncollect and reflect on personal information. However, there \nis no comprehensive list of problems that users experience \nusing  these  systems,  and  no  guidance  for  making  these \nsystems  more  effective.  To  address  this,  we  conducted \nsurveys and interviews with people who collect and reflect \non  personal  information.  We  derived  a  stage-based  model \nof  personal  informatics  systems  composed  of  five  stages  \n(preparation, collection, integration, reflection, and action) \nand  identified  barriers  in  each  of  the  stages.  These  stages \nhave  four  essential  properties:  b', 'var_function-call-9291635066695142137': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  condition, \naffecting  20%  of  the  population.  Even  though  it  is  a \ntreatable  condition,  people  often  do  not  seek  treatment.  In \nthis paper, we  describe how we co-designed and evaluated \nwith  30  stakeholders  (9  medical  professionals  and  21  end-\nusers)  an  OAB  mobile  health  application  that  aims  to \nincrease  adherence  to  self-managed  treatment.  Our  results \nsupport previous research that visualizing progress, setting \ngoals, receiving reminders and feedback  increases  use.  We \ndiscovered  that  games  could  be  used  successfully  as  a \ndistraction technique for urge suppression. Contrary to the \ncurrent research direction, automatically calculated features \n', 'var_function-call-12075459260304953316': {'copyright_year': None, 'years_found': []}, 'var_function-call-4736028606523868203': {'len': 74850, 'tail': 'f My Soul – How People Bond with Their \nMobile Phones. In Proc. ACM MobileHCI’08. \n\n[61]   Lois M. Verbrugg 1980. Health diaries. Medical care 18.1: 73-95. \n[62]  Graham  Wilson  and  Stephen  A.  Brewster.  2017.  Multi-Moji: \nCombining  Thermal,  Vibrotactile  &  Visual  Stimuli  to  Expand  the \nAffective Range of Feedback. In Proc. CHI’17. \n\n[63]   2048, https://en.wikipedia.org/wiki/2048_(video_game) \n\nCHI 2019 Paper  CHI 2019, May 4–9, 2019, Glasgow, Scotland, UKPaper 703Page 14 \n \n \n \n \n\x0c'}}

exec(code, env_args)
