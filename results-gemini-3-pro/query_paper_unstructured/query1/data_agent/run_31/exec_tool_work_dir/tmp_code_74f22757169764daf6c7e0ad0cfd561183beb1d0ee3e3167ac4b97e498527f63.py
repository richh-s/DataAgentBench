code = """import json
import re

citations_path = locals()['var_function-call-99245770254800995']
papers_path = locals()['var_function-call-5874155478376628757']

with open(papers_path, 'r') as f:
    papers = json.load(f)

debug_info = {}

for paper in papers[:10]:
    text = paper.get('text', '').lower()
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    match = re.search(r'(author keywords|keywords)\s*[:\s](.*?)(?=acm classification|introduction)', text, re.DOTALL)
    
    if match:
        extracted = match.group(2)[:200] # preview first 200 chars
        debug_info[title] = extracted
    else:
        debug_info[title] = "NO MATCH"

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-853909438841445340': 'file_storage/function-call-853909438841445340.json', 'var_function-call-1978902813264061650': 'file_storage/function-call-1978902813264061650.json', 'var_function-call-99245770254800995': 'file_storage/function-call-99245770254800995.json', 'var_function-call-5874155478376628757': 'file_storage/function-call-5874155478376628757.json', 'var_function-call-1098255190598746852': {'total_citations': 0, 'food_papers': []}, 'var_function-call-17104759845065888599': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'keyword_snippet': 'Keywords \nLived Informatics; Personal Informatics; Self-Tracking; \nLapsing; Physical Activity; Finances; Location. \n\nACM Classification Keywords \nH.5.m. Information interfaces and presentation (e.g., '}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'keyword_snippet': 'Keywords \nPersonal informatics, collection, reflection, model, barriers \n\nACM Classification Keywords \nH5.m.  Information  interfaces  and  presentation  (e.g.,  HCI): \nMiscellaneous.  \n\nGeneral Terms'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'keyword_snippet': 'Keywords\nH.5.1. Information interfaces and presentation (e.g., HCI):\nAnimations.\n\nAuthor Keywords\nPersonalization; animation; emotion; engagement; empathy;\nself-reﬂection.\n\nINTRODUCTION\nThe developmen'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'keyword_snippet': 'KEYWORDS \nMobile  Health  Applications;  Assistive  Technology;  Co-Design; \nInterviews; Usability; Overactive Bladder \n\nACM Reference format: \n\nAna-Maria  Salai  and  Lynne  Baillie.  2019.  A  Wee  '}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'keyword_snippet': 'Keywords \nWearable technology; dashboard; information visualization; \nstroke rehabilitation; occupational therapy  \n\nACM Classification Keywords \nH.5.m. Information interfaces and presentation (e.g., '}], 'var_function-call-4974837685350385437': {'total_citations': 0, 'food_papers': []}}

exec(code, env_args)
