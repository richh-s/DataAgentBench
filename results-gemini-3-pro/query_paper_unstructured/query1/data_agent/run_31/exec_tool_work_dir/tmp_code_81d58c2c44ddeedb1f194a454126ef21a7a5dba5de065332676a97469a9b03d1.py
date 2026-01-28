code = """import json
import re
from collections import Counter

papers_path = locals()['var_function-call-5874155478376628757']
with open(papers_path, 'r') as f:
    papers = json.load(f)

print(f"Total papers: {len(papers)}")

all_keywords = []

for paper in papers:
    text = paper.get('text', '').lower()
    
    match = re.search(r'(author keywords|keywords)\s*[:\s](.*?)(?=acm classification|introduction)', text, re.DOTALL)
    
    if match:
        kws = match.group(2)
        # Handle newlines without using backslash n in string
        kws = ' '.join(kws.splitlines())
        
        # Split by ; or ,
        # We can Iterate and split manually or use regex if safe
        # let's use re.split with [;,]
        parts = re.split(r'[;,]', kws)
        for k in parts:
            k = k.strip()
            if k:
                all_keywords.append(k)

cnt = Counter(all_keywords)
print("__RESULT__:")
print(json.dumps(cnt.most_common(50)))"""

env_args = {'var_function-call-853909438841445340': 'file_storage/function-call-853909438841445340.json', 'var_function-call-1978902813264061650': 'file_storage/function-call-1978902813264061650.json', 'var_function-call-99245770254800995': 'file_storage/function-call-99245770254800995.json', 'var_function-call-5874155478376628757': 'file_storage/function-call-5874155478376628757.json', 'var_function-call-1098255190598746852': {'total_citations': 0, 'food_papers': []}, 'var_function-call-17104759845065888599': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'keyword_snippet': 'Keywords \nLived Informatics; Personal Informatics; Self-Tracking; \nLapsing; Physical Activity; Finances; Location. \n\nACM Classification Keywords \nH.5.m. Information interfaces and presentation (e.g., '}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'keyword_snippet': 'Keywords \nPersonal informatics, collection, reflection, model, barriers \n\nACM Classification Keywords \nH5.m.  Information  interfaces  and  presentation  (e.g.,  HCI): \nMiscellaneous.  \n\nGeneral Terms'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'keyword_snippet': 'Keywords\nH.5.1. Information interfaces and presentation (e.g., HCI):\nAnimations.\n\nAuthor Keywords\nPersonalization; animation; emotion; engagement; empathy;\nself-reﬂection.\n\nINTRODUCTION\nThe developmen'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'keyword_snippet': 'KEYWORDS \nMobile  Health  Applications;  Assistive  Technology;  Co-Design; \nInterviews; Usability; Overactive Bladder \n\nACM Reference format: \n\nAna-Maria  Salai  and  Lynne  Baillie.  2019.  A  Wee  '}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'keyword_snippet': 'Keywords \nWearable technology; dashboard; information visualization; \nstroke rehabilitation; occupational therapy  \n\nACM Classification Keywords \nH.5.m. Information interfaces and presentation (e.g., '}], 'var_function-call-4974837685350385437': {'total_citations': 0, 'food_papers': []}, 'var_function-call-5389726838473826471': {'A Lived Informatics Model of Personal Informatics': 'lived informatics; personal informatics; self-tracking; \nlapsing; physical activity; finances; location. \n\n', 'A Stage-based Model of Personal Informatics Systems': 'personal informatics, collection, reflection, model, barriers \n\n', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection': 'h.5.1. information interfaces and presentation (e.g., hci):\nanimations.\n\nauthor keywords\npersonalization; animation; emotion; engagement; empathy;\nself-reﬂection.\n\n', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App': 'mobile  health  applications;  assistive  technology;  co-design; \ninterviews; usability; overactive bladder \n\nacm reference format: \n\nana-maria  salai  and  lynne  baillie.  2019.  a  wee  bit  more ', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation': 'wearable technology; dashboard; information visualization; \nstroke rehabilitation; occupational therapy  \n\n'}, 'var_function-call-11652074379122659369': [{'title': 'A Lived Informatics Model of Personal Informatics', 'keywords': 'lived informatics; personal informatics; self-tracking; \nlapsing; physical activity; finances; location. \n\n'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'keywords': 'personal informatics, collection, reflection, model, barriers \n\n'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'keywords': 'mobile  health  applications;  assistive  technology;  co-design; \ninterviews; usability; overactive bladder \n\nacm reference format: \n\nana-maria  salai  and  lynne  baillie.  2019.  a  wee  bit  more  interaction: \ndesigning  and  evaluating  an  overactive  bladder  app.  in  2019  chi \nconference '}]}

exec(code, env_args)
