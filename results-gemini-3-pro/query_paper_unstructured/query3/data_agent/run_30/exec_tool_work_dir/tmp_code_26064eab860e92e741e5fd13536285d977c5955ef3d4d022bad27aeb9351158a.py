code = """import json
import re

# Load papers
with open(locals()['var_function-call-12945244942482490428'], 'r') as f:
    papers = json.load(f)

debug_info = []

for p in papers:
    text = p['text']
    title = p['filename']
    
    # Try multiple year extraction strategies
    # Strategy 1: "Copyright 20xx"
    m1 = re.search(r'Copyright\s+(?:©|\(c\))?\s*(20\d{2})', text, re.IGNORECASE)
    # Strategy 2: "Conference 'xx" -> 20xx
    m2 = re.search(r"'\d{2}", text) # '15 -> 2015. Risky.
    # Strategy 3: Just the first 20xx number
    years = re.findall(r'20\d{2}', text[:3000])
    
    y = None
    if m1:
        y = int(m1.group(1))
    elif years:
        y = int(years[0])
        
    if y is None:
        debug_info.append({"title": title, "preview": text[:200]})

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-12710699781919047137': 'file_storage/function-call-12710699781919047137.json', 'var_function-call-4291090424664498879': ['paper_docs'], 'var_function-call-15848114717037089156': [{'cid': '0', 'name': 'id', 'type': 'INTEGER', 'notnull': '0', 'dflt_value': 'None', 'pk': '1'}, {'cid': '1', 'name': 'title', 'type': 'TEXT', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'citation_count', 'type': 'INTEGER', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'citation_year', 'type': 'INTEGER', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}], 'var_function-call-6799070853489164674': 'file_storage/function-call-6799070853489164674.json', 'var_function-call-17861381846449372899': [], 'var_function-call-2694959544840446415': 'file_storage/function-call-2694959544840446415.json', 'var_function-call-8715248679689147439': 'file_storage/function-call-8715248679689147439.json', 'var_function-call-411178734668789802': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'contribution_contexts': ['rdi,  Megan  Taylor,  and  Frank  Xu  for  their  contributions  through  survey  design  and  parti'], 'empirical_contexts': []}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'contribution_contexts': ['informatics systems.    We  provide  three  main  contributions  in  this  paper:  1)  we  identify '], 'empirical_contexts': []}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'contribution_contexts': [], 'empirical_contexts': ['cal effects on the user.  SYSTEM OVERVIEW Several empirical principles in animated ﬁlm making provid']}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'contribution_contexts': [' although  some  UPs  were  pleased  with  their  contribution “I like drawing!” (UP4),  some  did n'], 'empirical_contexts': ['  T.  Kortum  and  James  T.  Miller.  2008.  An  Empirical  Evaluation  of  the  System  Usability ', ' Susanna  Raj.  2018.  Circles  vs.  scales:  an  empirical  evaluation  of  emotional assessment GU']}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'contribution_contexts': ['s  focus  on  the  patient is important, the main contribution of this research is  a  system  desig', 'atients’ activities outside therapy.   A  second  contribution  is  offered  through  the  design  o'], 'empirical_contexts': []}], 'var_function-call-15082852831104243869': ['Citations', 'sqlite_sequence'], 'var_function-call-12945244942482490428': 'file_storage/function-call-12945244942482490428.json', 'var_function-call-6020655889257574954': 'file_storage/function-call-6020655889257574954.json', 'var_function-call-14298331136714285140': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '164911713881'}], 'var_function-call-11370626618227578168': {'matches': [], 'debug': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': 2015, 'is_empirical': False}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'is_empirical': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'is_empirical': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'is_empirical': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None, 'is_empirical': False}]}}

exec(code, env_args)
