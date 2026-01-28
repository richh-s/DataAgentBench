code = """import json

with open(locals()['var_function-call-1518864463960469704'], 'r') as f:
    papers = json.load(f)

keywords_counter = {}

for p in papers:
    text = p.get('text', '')
    text_lower = text.lower()
    
    start_idx = -1
    # Check headers
    for h in ["author keywords", "keywords"]:
        idx = text_lower.find(h)
        if idx != -1:
            start_idx = idx + len(h)
            break
            
    if start_idx != -1:
        snippet = text[start_idx:start_idx+800]
        
        stop_markers = ["ACM Classification", "INTRODUCTION", "ABSTRACT", "General Terms"]
        
        min_stop = len(snippet)
        for marker in stop_markers:
            s_idx = snippet.find(marker)
            if s_idx != -1 and s_idx < min_stop:
                min_stop = s_idx
        
        raw_kws = snippet[:min_stop]
        
        # Replace semicolon and newline with comma
        clean_kws = raw_kws.replace(chr(59), chr(44)).replace(chr(10), chr(44))
        parts = clean_kws.split(chr(44))
        
        for t in parts:
            t = t.strip().lower()
            if len(t) > 2:
                # Remove trailing dots if any
                if t.endswith('.'):
                    t = t[:-1]
                keywords_counter[t] = keywords_counter.get(t, 0) + 1

sorted_kws = sorted(keywords_counter.items(), key=lambda x: x[1], reverse=True)[:50]

print("__RESULT__:")
print(json.dumps(sorted_kws))"""

env_args = {'var_function-call-13263841084100216715': ['paper_docs'], 'var_function-call-2979229897755399322': 'file_storage/function-call-2979229897755399322.json', 'var_function-call-1518864463960469704': 'file_storage/function-call-1518864463960469704.json', 'var_function-call-16808733530214175810': 'file_storage/function-call-16808733530214175810.json', 'var_function-call-8705897625478698375': {'total_citations': 0, 'paper_count': 0, 'matched_titles': []}, 'var_function-call-8492066724070141824': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'keywords_snippet': 'research.  \n\nAuthor Keywords \nLived Informatics; Personal Informatics; Self-Tracking; \nLapsing; Physical Activity; Finances; Location. \n\nACM Classification Keywords \nH.5.m. Information interfaces and presentation (e.g., '}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'keywords_snippet': ' recommend \n\nAuthor Keywords \nPersonal informatics, collection, reflection, model, barriers \n\nACM Classification Keywords \nH5.m.  Information  interfaces  and  presentation  (e.g.,  HCI): \nMiscellaneous.  \n\nGeneral Terms'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'keywords_snippet': '\n\nACM Classiﬁcation Keywords\nH.5.1. Information interfaces and presentation (e.g., HCI):\nAnimations.\n\nAuthor Keywords\nPersonalization; animation; emotion; engagement; empathy;\nself-reﬂection.\n\nINTRODUCTION\nThe developmen'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'keywords_snippet': 'g; \nField Studies \n\nKEYWORDS \nMobile  Health  Applications;  Assistive  Technology;  Co-Design; \nInterviews; Usability; Overactive Bladder \n\nACM Reference format: \n\nAna-Maria  Salai  and  Lynne  Baillie.  2019.  A  Wee  '}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'keywords_snippet': 'therapists \n\nAuthor Keywords \nWearable technology; dashboard; information visualization; \nstroke rehabilitation; occupational therapy  \n\nACM Classification Keywords \nH.5.m. Information interfaces and presentation (e.g., '}]}

exec(code, env_args)
