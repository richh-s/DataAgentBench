code = """import json
import re

with open(locals()['var_function-call-4358244583942540599'], 'r') as f:
    papers = json.load(f)

print("__RESULT__:")
output = []

for p in papers:
    text = p['text']
    title = p['filename']
    output.append(f"--- {title} ---")
    
    # Find all occurrences of "food"
    matches = [m.start() for m in re.finditer(r'food', text, re.IGNORECASE)]
    if not matches:
        output.append("No 'food' found.")
    else:
        for m in matches:
            start = max(0, m - 50)
            end = min(len(text), m + 50)
            snippet = text[start:end]
            # simple replace of newline with space
            snippet = snippet.replace('\n', ' ').replace('\r', ' ')
            output.append(f"...{snippet}...")
    output.append("")

print(json.dumps(output))"""

env_args = {'var_function-call-4625483642172775665': 'file_storage/function-call-4625483642172775665.json', 'var_function-call-4600237865366959545': [{'_id': '694f5530284b10b11dc0a869'}, {'_id': '694f5530284b10b11dc0a86a'}, {'_id': '694f5530284b10b11dc0a86b'}, {'_id': '694f5530284b10b11dc0a86c'}, {'_id': '694f5530284b10b11dc0a86d'}], 'var_function-call-5959858908206975424': 'file_storage/function-call-5959858908206975424.json', 'var_function-call-4358244583942540599': 'file_storage/function-call-4358244583942540599.json', 'var_function-call-1694766061137811147': {'food_papers_found': ['A Lived Informatics Model of Personal Informatics'], 'total_citations': 390}, 'var_function-call-9988489539688869624': [{'title': 'A Lived Informatics Model of Personal Informatics', 'snippet': 'Author Keywords \nLived Informatics; Personal Informatics; Self-Tracking; \nLapsing; Physical Activity; Finances; Location. \n\nACM Classification Keywords \nH.5.m. Information interfaces and presentation (e.g., HCI). \n\nINTRODUCTION \nPersonal informatics, or collecting and reflecting on personal \ninformation,  has  become  increasingly  prevalent.  Personal \ninformatics can serve a goal-driven purpose, such as tracking \nweight loss, increasing physical activity, having a record of \nplaces  visited,  '}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'snippet': 'Author Keywords \nPersonal informatics, collection, reflection, model, barriers \n\nACM Classification Keywords \nH5.m.  Information  interfaces  and  presentation  (e.g.,  HCI): \nMiscellaneous.  \n\nGeneral Terms \nDesign, Human Factors \n\nINTRODUCTION AND MOTIVATION \nThe  importance  of  knowing  oneself  has  been  known  since \nancient  times.  Ancient  Greeks  who  pilgrimaged  to  the \nTemple  of  Apollo  at  Delphi  to  find  answers  were  greeted \nwith  the  inscription  “Gnothi  seauton”  or  '}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'snippet': 'Author Keywords\nPersonalization; animation; emotion; engagement; empathy;\nself-reﬂection.\n\nINTRODUCTION\nThe development of mobile phone technology and biological\nsensors is enabling individuals to self-track biological, phys-\nical and environmental information. From rich self-tracking\ndata, individuals can interpret and infer the patterns, correla-\ntions and causal relations in their own behavior and wellbeing.\nRecent HCI research attempts to help users build up a critical\nunderstanding of their'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'snippet': ''}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'snippet': 'Author Keywords \nWearable technology; dashboard; information visualization; \nstroke rehabilitation; occupational therapy  \n\nACM Classification Keywords \nH.5.m. Information interfaces and presentation (e.g., HCI): \nMiscellaneous.  \n\nINTRODUCTION \nStroke  is  the  leading  cause  of  disability  in  high-income \nthe  most  common  resulting \ncountries,  with  one  of \n\nPermission to make digital or hard copies of all or part of this work for personal\nor  classroom  use  is  granted  without  fee  '}], 'var_function-call-11451954240526920658': 'file_storage/function-call-11451954240526920658.json'}

exec(code, env_args)
