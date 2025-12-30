code = """import json

file_path = locals()['var_function-call-15853476606945075848']
with open(file_path, 'r') as f:
    papers = json.load(f)

extracted_info = []

keyword_markers = ["Author Keywords", "Keywords", "Index Terms"]
nl = chr(10)
end_markers = ["ACM Classification", "INTRODUCTION", "ABSTRACT", "General Terms", nl+nl+nl]

for paper in papers:
    text = paper.get('text', '')
    title = paper.get('filename', '').replace('.txt', '')
    
    keywords_section = "NOT FOUND"
    
    start_idx = -1
    for marker in keyword_markers:
        idx = text.find(marker)
        if idx != -1:
            start_idx = idx + len(marker)
            break
            
    if start_idx != -1:
        end_idx = len(text)
        for marker in end_markers:
            idx = text.find(marker, start_idx)
            if idx != -1 and idx < end_idx:
                end_idx = idx
        
        # Limit length
        if end_idx - start_idx > 500:
             end_idx = start_idx + 500
        
        keywords_section = text[start_idx:end_idx].strip()
        
    extracted_info.append({"title": title, "keywords": keywords_section})

print("__RESULT__:")
print(json.dumps(extracted_info))"""

env_args = {'var_function-call-2030052539716132653': ['paper_docs'], 'var_function-call-2030052539716130606': ['Citations', 'sqlite_sequence'], 'var_function-call-10436001229395050788': 'file_storage/function-call-10436001229395050788.json', 'var_function-call-14775446657247865324': 'file_storage/function-call-14775446657247865324.json', 'var_function-call-17848564962204727189': 'file_storage/function-call-17848564962204727189.json', 'var_function-call-15853476606945075848': 'file_storage/function-call-15853476606945075848.json', 'var_function-call-16520379867273674583': [], 'var_function-call-12529024315606180287': {'food_in_text_count': 3, 'debug_output': ["Paper 'A Lived Informatics Model of Personal Informatics.txt' has 'food' in text.", 'Paper: A Lived Informatics Model of Personal Informatics.txt, Marker: Author Keywords, Extracted: Lived Informatics; Personal Informatics; Self-Tracking; \nLapsing; Physical Activity; Finances; Locat...', "Paper 'A Stage-based Model of Personal Informatics Systems.txt' has 'food' in text.", 'Paper: A Stage-based Model of Personal Informatics Systems.txt, Marker: Author Keywords, Extracted: Personal informatics, collection, reflection, model, barriers...', 'Paper: A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt, Marker: Author Keywords, Extracted: Personalization; animation; emotion; engagement; empathy;\nself-reﬂection....', "Paper 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt' has 'food' in text.", 'Paper: A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt, No keyword marker found.', 'Paper: ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt, Marker: Author Keywords, Extracted: Wearable technology; dashboard; information visualization; \nstroke rehabilitation; occupational ther...']}, 'var_function-call-12043749988653774284': 'file_storage/function-call-12043749988653774284.json'}

exec(code, env_args)
