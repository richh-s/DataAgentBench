code = """import json
import re

file_path = locals()['var_function-call-15853476606945075848']
with open(file_path, 'r') as f:
    papers = json.load(f)

matching_titles = []

nl = chr(10)
# Start pattern: Author Keywords, Keywords, Index Terms followed by colon or newline
start_regex = r'(?:Author Keywords|Keywords|Index Terms)\s*[:' + nl + ']'
start_pattern = re.compile(start_regex, re.IGNORECASE)

# End pattern
end_regex = r'(?:ACM Classification|INTRODUCTION|ABSTRACT|General Terms|' + nl + nl + nl + ')'
end_pattern = re.compile(end_regex, re.IGNORECASE)

for paper in papers:
    text = paper.get('text', '')
    title = paper.get('filename', '').replace('.txt', '')
    
    match_start = start_pattern.search(text)
    if match_start:
        start_idx = match_start.end()
        
        match_end = end_pattern.search(text, pos=start_idx)
        if match_end:
            end_idx = match_end.start()
        else:
            end_idx = min(len(text), start_idx + 500)
            
        keywords_section = text[start_idx:end_idx].strip().lower()
        
        if 'food' in keywords_section:
            matching_titles.append(title)

print("__RESULT__:")
print(json.dumps(matching_titles))"""

env_args = {'var_function-call-2030052539716132653': ['paper_docs'], 'var_function-call-2030052539716130606': ['Citations', 'sqlite_sequence'], 'var_function-call-10436001229395050788': 'file_storage/function-call-10436001229395050788.json', 'var_function-call-14775446657247865324': 'file_storage/function-call-14775446657247865324.json', 'var_function-call-17848564962204727189': 'file_storage/function-call-17848564962204727189.json', 'var_function-call-15853476606945075848': 'file_storage/function-call-15853476606945075848.json', 'var_function-call-16520379867273674583': [], 'var_function-call-12529024315606180287': {'food_in_text_count': 3, 'debug_output': ["Paper 'A Lived Informatics Model of Personal Informatics.txt' has 'food' in text.", 'Paper: A Lived Informatics Model of Personal Informatics.txt, Marker: Author Keywords, Extracted: Lived Informatics; Personal Informatics; Self-Tracking; \nLapsing; Physical Activity; Finances; Locat...', "Paper 'A Stage-based Model of Personal Informatics Systems.txt' has 'food' in text.", 'Paper: A Stage-based Model of Personal Informatics Systems.txt, Marker: Author Keywords, Extracted: Personal informatics, collection, reflection, model, barriers...', 'Paper: A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt, Marker: Author Keywords, Extracted: Personalization; animation; emotion; engagement; empathy;\nself-reﬂection....', "Paper 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt' has 'food' in text.", 'Paper: A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt, No keyword marker found.', 'Paper: ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt, Marker: Author Keywords, Extracted: Wearable technology; dashboard; information visualization; \nstroke rehabilitation; occupational ther...']}, 'var_function-call-12043749988653774284': 'file_storage/function-call-12043749988653774284.json', 'var_function-call-4226476911779009528': [{'title': 'A Lived Informatics Model of Personal Informatics', 'keywords': 'Lived Informatics; Personal Informatics; Self-Tracking; \nLapsing; Physical Activity; Finances; Location.'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'keywords': 'Personal informatics, collection, reflection, model, barriers'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'keywords': 'Personalization; animation; emotion; engagement; empathy;\nself-reﬂection.'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'keywords': 'NOT FOUND'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'keywords': 'Wearable technology; dashboard; information visualization; \nstroke rehabilitation; occupational therapy'}]}

exec(code, env_args)
