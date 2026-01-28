code = """import json

# Load paper docs
with open(locals()['var_function-call-6784004311963359326'], 'r') as f:
    paper_docs = json.load(f)

target_title = "TastyBeats: Designing Palatable Representations of Physical Activity"
found_doc = None

for doc in paper_docs:
    if target_title in doc['filename']:
        found_doc = doc
        break

if found_doc:
    text = found_doc['text']
    lower_text = text.lower()
    start_idx = lower_text.find("author keywords")
    if start_idx == -1:
        start_idx = lower_text.find("keywords")
    
    snippet = ""
    if start_idx != -1:
        snippet = text[start_idx:start_idx+500]

    print("__RESULT__:")
    print(json.dumps({"title": target_title, "snippet": snippet}))
else:
    print("__RESULT__:")
    print(json.dumps({"error": "Doc not found"}))"""

env_args = {'var_function-call-2084014560423739449': 'file_storage/function-call-2084014560423739449.json', 'var_function-call-11352259319045470857': 'file_storage/function-call-11352259319045470857.json', 'var_function-call-9528525890526779817': 'file_storage/function-call-9528525890526779817.json', 'var_function-call-11391268532651985749': 'file_storage/function-call-11391268532651985749.json', 'var_function-call-4893813044392379918': {'food_papers_count': 0, 'total_citations': 0, 'sample_food_papers': []}, 'var_function-call-10781200927220455236': ['Author Keywords \nLived Informatics; Personal Informatics; Self-Tracking; \nLapsing; Physical Activity; Finances; Location. \n\nACM Classification Keywords \nH.5.m. Information interfaces and presentation (e.g., HCI). \n\nINTRODUCTION \nPersonal informatics, or collecting and reflecting on personal \ninforma', 'Author Keywords \nPersonal informatics, collection, reflection, model, barriers \n\nACM Classification Keywords \nH5.m.  Information  interfaces  and  presentation  (e.g.,  HCI): \nMiscellaneous.  \n\nGeneral Terms \nDesign, Human Factors \n\nINTRODUCTION AND MOTIVATION \nThe  importance  of  knowing  oneself ', 'Author Keywords\nPersonalization; animation; emotion; engagement; empathy;\nself-reﬂection.\n\nINTRODUCTION\nThe development of mobile phone technology and biological\nsensors is enabling individuals to self-track biological, phys-\nical and environmental information. From rich self-tracking\ndata, individu', 'KEYWORDS \nMobile  Health  Applications;  Assistive  Technology;  Co-Design; \nInterviews; Usability; Overactive Bladder \n\nACM Reference format: \n\nAna-Maria  Salai  and  Lynne  Baillie.  2019.  A  Wee  Bit  More  Interaction: \nDesigning  and  Evaluating  an  Overactive  Bladder  App.  In  2019  CHI \nC', 'Author Keywords \nWearable technology; dashboard; information visualization; \nstroke rehabilitation; occupational therapy  \n\nACM Classification Keywords \nH.5.m. Information interfaces and presentation (e.g., HCI): \nMiscellaneous.  \n\nINTRODUCTION \nStroke  is  the  leading  cause  of  disability  in  h'], 'var_function-call-7825954886258194997': {'filename_food': 0, 'keywords_food': 0, 'keywords_activity': 1, 'food_in_text_count': 3, 'total_docs': 5}, 'var_function-call-6784004311963359326': 'file_storage/function-call-6784004311963359326.json', 'var_function-call-8157847343566696553': {'food_papers_count': 9, 'matched_citation_records': 53, 'total_citations': 2531, 'sample_food_papers': ['Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture', 'When Personal Tracking Becomes Social: Examining the Use of Instagram for Healthy Eating', 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'TastyBeats: Designing Palatable Representations of Physical Activity', 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling'], 'total_docs_processed': 99}}

exec(code, env_args)
