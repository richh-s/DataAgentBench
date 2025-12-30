code = """import json
import re

with open(locals()['var_function-call-1188879216130437550'], 'r') as f:
    papers = json.load(f)

p = papers[3] # "A Wee Bit More Interaction..."
text = p.get('text', '')

# Search for Copyright
match = re.search(r'Copyright.*?(20\d\d)', text, re.IGNORECASE)
copyright_year = match.group(1) if match else None

# Search for all years in text
years = re.findall(r'\b20\d\d\b', text)

print("__RESULT__:")
print(json.dumps({"copyright_year": copyright_year, "years_found": years[:20]}))"""

env_args = {'var_function-call-563988683724796528': 'file_storage/function-call-563988683724796528.json', 'var_function-call-1188879216130437550': 'file_storage/function-call-1188879216130437550.json', 'var_function-call-6926115911538441459': 'file_storage/function-call-6926115911538441459.json', 'var_function-call-11700601508177380664': [], 'var_function-call-15227438266193405659': [{'title': 'A Lived Informatics Model of Personal Informatics', 'extracted_year': None, 'has_empirical': False}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'extracted_year': None, 'has_empirical': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'extracted_year': None, 'has_empirical': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'extracted_year': None, 'has_empirical': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'extracted_year': None, 'has_empirical': False}], 'var_function-call-4638443691179812252': ["Paper 0: matches=['2015']", 'Paper 1: matches=[]', 'Paper 2: matches=[]', 'Paper 3: matches=[]', 'Paper 4: matches=[]'], 'var_function-call-1232675705292650106': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 15213 \nianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu \n\nABSTRACT \nPeople  strive  to  obtain  self-knowledge.  A  class  of  systems \ncalled  personal  informatics  is  appearing  that  help  people \ncollect and reflect on personal information. However, there \nis no comprehensive list of problems that users experience \nusing  these  systems,  and  no  guidance  for  making  these \nsystems  more  effective.  To  address  this,  we  conducted \nsurveys and interviews with people who collect and reflect \non  personal  information.  We  derived  a  stage-based  model \nof  personal  informatics  systems  composed  of  five  stages  \n(preparation, collection, integration, reflection, and action) \nand  identified  barriers  in  each  of  the  stages.  These  stages \nhave  four  essential  properties:  b', 'var_function-call-9291635066695142137': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  condition, \naffecting  20%  of  the  population.  Even  though  it  is  a \ntreatable  condition,  people  often  do  not  seek  treatment.  In \nthis paper, we  describe how we co-designed and evaluated \nwith  30  stakeholders  (9  medical  professionals  and  21  end-\nusers)  an  OAB  mobile  health  application  that  aims  to \nincrease  adherence  to  self-managed  treatment.  Our  results \nsupport previous research that visualizing progress, setting \ngoals, receiving reminders and feedback  increases  use.  We \ndiscovered  that  games  could  be  used  successfully  as  a \ndistraction technique for urge suppression. Contrary to the \ncurrent research direction, automatically calculated features \n'}

exec(code, env_args)
