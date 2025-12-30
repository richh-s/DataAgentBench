code = """import json

with open(locals()['var_function-call-11391268532651985749'], 'r') as f:
    paper_docs = json.load(f)

filename_food = 0
keywords_food = 0
keywords_activity = 0
food_in_text_count = 0

for doc in paper_docs:
    filename = doc['filename']
    text = doc['text']
    lower_text = text.lower()
    
    if "food" in filename.lower():
        filename_food += 1
        
    if "food" in lower_text:
        food_in_text_count += 1
    
    start_idx = lower_text.find("author keywords")
    if start_idx == -1:
        start_idx = lower_text.find("keywords")
    
    if start_idx != -1:
        snippet = lower_text[start_idx:start_idx+500]
        if "food" in snippet:
            keywords_food += 1
        if "physical activity" in snippet:
            keywords_activity += 1

print("__RESULT__:")
print(json.dumps({
    "filename_food": filename_food,
    "keywords_food": keywords_food,
    "keywords_activity": keywords_activity,
    "food_in_text_count": food_in_text_count,
    "total_docs": len(paper_docs)
}))"""

env_args = {'var_function-call-2084014560423739449': 'file_storage/function-call-2084014560423739449.json', 'var_function-call-11352259319045470857': 'file_storage/function-call-11352259319045470857.json', 'var_function-call-9528525890526779817': 'file_storage/function-call-9528525890526779817.json', 'var_function-call-11391268532651985749': 'file_storage/function-call-11391268532651985749.json', 'var_function-call-4893813044392379918': {'food_papers_count': 0, 'total_citations': 0, 'sample_food_papers': []}, 'var_function-call-10781200927220455236': ['Author Keywords \nLived Informatics; Personal Informatics; Self-Tracking; \nLapsing; Physical Activity; Finances; Location. \n\nACM Classification Keywords \nH.5.m. Information interfaces and presentation (e.g., HCI). \n\nINTRODUCTION \nPersonal informatics, or collecting and reflecting on personal \ninforma', 'Author Keywords \nPersonal informatics, collection, reflection, model, barriers \n\nACM Classification Keywords \nH5.m.  Information  interfaces  and  presentation  (e.g.,  HCI): \nMiscellaneous.  \n\nGeneral Terms \nDesign, Human Factors \n\nINTRODUCTION AND MOTIVATION \nThe  importance  of  knowing  oneself ', 'Author Keywords\nPersonalization; animation; emotion; engagement; empathy;\nself-reﬂection.\n\nINTRODUCTION\nThe development of mobile phone technology and biological\nsensors is enabling individuals to self-track biological, phys-\nical and environmental information. From rich self-tracking\ndata, individu', 'KEYWORDS \nMobile  Health  Applications;  Assistive  Technology;  Co-Design; \nInterviews; Usability; Overactive Bladder \n\nACM Reference format: \n\nAna-Maria  Salai  and  Lynne  Baillie.  2019.  A  Wee  Bit  More  Interaction: \nDesigning  and  Evaluating  an  Overactive  Bladder  App.  In  2019  CHI \nC', 'Author Keywords \nWearable technology; dashboard; information visualization; \nstroke rehabilitation; occupational therapy  \n\nACM Classification Keywords \nH.5.m. Information interfaces and presentation (e.g., HCI): \nMiscellaneous.  \n\nINTRODUCTION \nStroke  is  the  leading  cause  of  disability  in  h']}

exec(code, env_args)
