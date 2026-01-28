code = """import json
import re

with open(locals()['var_function-call-7959841474300951683'], 'r') as f:
    docs = json.load(f)

summary = []

for doc in docs:
    text = doc['text']
    filename = doc['filename']
    title = filename.replace('.txt', '')
    
    # Year extraction
    # 1. Look for 20xx
    years = re.findall(r'20\d{2}', text[:2000]) # Search first 2000 chars
    valid_years = [int(y) for y in years if 2000 <= int(y) <= 2025]
    
    # 2. Look for 'yy (e.g. '17) in the first 500 chars (header)
    # Often "CHI '17"
    short_years = re.findall(r"\b[A-Z]+\s?'(\d{2})", text[:500])
    
    year = 0
    if valid_years:
        year = valid_years[0] # Take first valid 4-digit year
    elif short_years:
        y = int(short_years[0])
        year = 2000 + y
    
    # Contribution extraction
    contribs = []
    keywords = ["empirical", "artifact", "theoretical", "survey", "methodological"]
    for kw in keywords:
        if kw in text.lower():
            contribs.append(kw)
            
    summary.append({"title": title, "year": year, "contribs": contribs})

print("__RESULT__:")
print(json.dumps(summary))"""

env_args = {'var_function-call-14549722995805523735': 'file_storage/function-call-14549722995805523735.json', 'var_function-call-9109662763408237056': ['Citations', 'sqlite_sequence'], 'var_function-call-6745088051019410329': [{'cid': '0', 'name': 'id', 'type': 'INTEGER', 'notnull': '0', 'dflt_value': 'None', 'pk': '1'}, {'cid': '1', 'name': 'title', 'type': 'TEXT', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'citation_count', 'type': 'INTEGER', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'citation_year', 'type': 'INTEGER', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}], 'var_function-call-4015090324283648615': {'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'preview': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \n\nABSTRACT \nCurrent  models  of  how  people  use  personal  informatics \nsystems are largely based in behavior change goals. They do \nnot  adequately  characterize  the  integration  of  self-tracking \ninto  everyday  life  by  people  with  varying  goals.  We  build \nupon  prior  work  by  embracing  the  perspective  of  lived \ninformatics to propose a new model of personal informatics. \nWe examine how lived informatics manifests in the habits of \nself-trackers across a variety of domains, first by surveying \n105, 99, and 83 past and present trackers of physical activity, \nfinances, and location and then by interviewing 22 trackers \nregarding their lived informatics experiences. We develop a \nmodel characterizing tracker processes of deciding to track \nand selecting a tool, elaborate on tool usage during collection, \nintegration,  and  reflection  as  components  of  tracking  and \nacting,  and  discuss  the  lapsing  and  potential  resuming  of \ntracking.  We  use  our  model  to  surface  underexplored \nchallenges  in  lived  informatics,  thus  identifying  future \ndirections for personal informatics design and research.  \n\nAuthor Keywords \nLived Informatics; Personal Informatics; Self-Tracking; \nLapsing; Physical Activity; Finances; Location. \n\nACM Classification Keywords \nH.5.m. Information interfaces and presentation (e.g., HCI). \n\nINTRODUCTION \nPersonal informatics, or collecting and reflecting on personal \ninformation,  has  become  increasingly  prevalent.  Personal \ninformatics can serve a goal-driven purpose, such as tracking \nweight loss, increasing physical activity, having a record of \nplaces  visited,  or  tracking ", 'has_empirical': False, 'has_contribution': True}, 'var_function-call-9146686809165989876': ['rdi,  Megan  Taylor,  and  Frank  Xu  for  their \ncontributions  through  survey  design  and  participant  interviews. \nWe  also  thank  Elena  Agapi'], 'var_function-call-3687810579190322584': 'file_storage/function-call-3687810579190322584.json', 'var_function-call-15667921520154715322': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'year': 'Unknown', 'has_empirical': False, 'contribution_context': 'contributions  through  survey  design  and  parti'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'year': 'Unknown', 'has_empirical': False, 'contribution_context': 'contributions  in  this  paper:  1)  we \nidentify '}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'year': 'Unknown', 'has_empirical': True, 'contribution_context': 'Not found'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'year': 'Unknown', 'has_empirical': True, 'contribution_context': 'contribution “I like drawing!” (UP4),  some  did n'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'year': 'Unknown', 'has_empirical': False, 'contribution_context': 'contribution of this research is \na  system  desig'}], 'var_function-call-7959841474300951683': 'file_storage/function-call-7959841474300951683.json', 'var_function-call-5331781994975001410': {'titles': [], 'debug': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': 0, 'is_empirical': False}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': 0, 'is_empirical': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 0, 'is_empirical': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 0, 'is_empirical': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': 0, 'is_empirical': False}]}, 'var_function-call-9663220193990734771': {'titles': [], 'debug': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': 2015, 'header_snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n", 'years_found': [2015]}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': 0, 'header_snippet': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Hum', 'years_found': []}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 0, 'header_snippet': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Anima', 'years_found': []}]}}

exec(code, env_args)
