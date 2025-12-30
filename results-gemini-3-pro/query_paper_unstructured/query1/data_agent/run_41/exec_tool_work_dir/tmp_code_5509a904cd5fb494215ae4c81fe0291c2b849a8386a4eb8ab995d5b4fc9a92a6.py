code = """import json
import pandas as pd
import re

# Load the large dataset
with open(locals()['var_function-call-15588185410019799743'], 'r') as f:
    papers_data = json.load(f)

# Load citations
with open(locals()['var_function-call-14859437005275468977'], 'r') as f:
    citations_data = json.load(f)

df_papers = pd.DataFrame(papers_data)
df_citations = pd.DataFrame(citations_data)

# Extract domain and filter
def is_food_paper(text):
    # Find Keywords
    patterns = [r"Author Keywords", r"Keywords"]
    start_idx = -1
    for p in patterns:
        match = re.search(p, text, re.IGNORECASE)
        if match:
            start_idx = match.end()
            break
            
    if start_idx == -1:
        # Fallback: Check first 5000 chars for "food" near "Index Terms" or similar?
        # Or just return False?
        # Let's check strictly for Keywords first.
        return False
        
    sub_text = text[start_idx:]
    
    # End markers
    end_markers = ["ACM Classification Keywords", "INTRODUCTION", "ABSTRACT", "\n\n\n"]
    end_idx = len(sub_text)
    
    for marker in end_markers:
        marker_match = re.search(marker, sub_text, re.IGNORECASE)
        if marker_match:
            end_idx = min(end_idx, marker_match.start())
            
    if end_idx > 2000: # Safety
        end_idx = 2000
        
    keywords = sub_text[:end_idx].lower()
    
    # Check for 'food'
    if 'food' in keywords:
        return True
    return False

# Normalize filename to title
df_papers['title_join'] = df_papers['filename'].str.replace('.txt', '', regex=False)
df_papers['is_food'] = df_papers['text'].apply(is_food_paper)

food_papers = df_papers[df_papers['is_food']]
food_titles = food_papers['title_join'].tolist()

# Join with citations
df_citations['citation_count'] = pd.to_numeric(df_citations['citation_count'])
merged = pd.merge(df_citations, food_papers, left_on='title', right_on='title_join')

total_citations = merged['citation_count'].sum()

print(f"Found {len(food_papers)} food papers.")
print(f"Titles: {food_titles}")

print("__RESULT__:")
print(json.dumps(int(total_citations)))"""

env_args = {'var_function-call-10309278563115687463': ['paper_docs'], 'var_function-call-17310270331774513134': 'file_storage/function-call-17310270331774513134.json', 'var_function-call-14859437005275468977': 'file_storage/function-call-14859437005275468977.json', 'var_function-call-9278851709122145007': 'file_storage/function-call-9278851709122145007.json', 'var_function-call-2702061835981032480': 0, 'var_function-call-14459346751113599875': 'Done', 'var_function-call-9639062052083134801': {'food_papers_count': 0, 'food_papers': [], 'debug': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'extracted_keywords': ' \nlived informatics; personal informatics; self-tracking; \nlapsing; physical activity; finances; loc'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'extracted_keywords': ' \npersonal informatics, collection, reflection, model, barriers \n\n'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'extracted_keywords': '\npersonalization; animation; emotion; engagement; empathy;\nself-reﬂection.\n\n'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'extracted_keywords': ' \nmobile  health  applications;  assistive  technology;  co-design; \ninterviews; usability; overacti'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'extracted_keywords': ' \nwearable technology; dashboard; information visualization; \nstroke rehabilitation; occupational th'}]}, 'var_function-call-16481698289397756348': [], 'var_function-call-15906191458607323979': [], 'var_function-call-11201761744589980479': {'food_top_5': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'count': 13}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'count': 13}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'count': 1}], 'activity_top_5': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'count': 56}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'count': 31}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'count': 11}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'count': 2}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'count': 2}]}, 'var_function-call-12615532098506666424': 5, 'var_function-call-15588185410019799743': 'file_storage/function-call-15588185410019799743.json', 'var_function-call-9865040666208107031': 'file_storage/function-call-9865040666208107031.json', 'var_function-call-6725474295619689306': 'Done', 'var_function-call-7473176720608438589': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'], 'var_function-call-7344836607993902723': [], 'var_function-call-5322295408034049035': ['Citations', 'sqlite_sequence'], 'var_function-call-10911347694363360162': 99}

exec(code, env_args)
