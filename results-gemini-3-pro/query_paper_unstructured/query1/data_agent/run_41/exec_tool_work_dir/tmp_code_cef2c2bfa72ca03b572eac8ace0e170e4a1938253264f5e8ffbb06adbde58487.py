code = """import json
import re

with open(locals()['var_function-call-9278851709122145007'], 'r') as f:
    papers_data = json.load(f)

food_counts = []
activity_counts = []

for paper in papers_data:
    text = paper['text']
    # Substring search
    f_count = text.lower().count('food')
    if f_count > 0:
        food_counts.append({"filename": paper['filename'], "count": f_count})
        
    a_count = text.lower().count('activity')
    if a_count > 0:
        activity_counts.append({"filename": paper['filename'], "count": a_count})

food_counts.sort(key=lambda x: x['count'], reverse=True)
activity_counts.sort(key=lambda x: x['count'], reverse=True)

print("__RESULT__:")
print(json.dumps({
    "food_top_5": food_counts[:5],
    "activity_top_5": activity_counts[:5]
}))"""

env_args = {'var_function-call-10309278563115687463': ['paper_docs'], 'var_function-call-17310270331774513134': 'file_storage/function-call-17310270331774513134.json', 'var_function-call-14859437005275468977': 'file_storage/function-call-14859437005275468977.json', 'var_function-call-9278851709122145007': 'file_storage/function-call-9278851709122145007.json', 'var_function-call-2702061835981032480': 0, 'var_function-call-14459346751113599875': 'Done', 'var_function-call-9639062052083134801': {'food_papers_count': 0, 'food_papers': [], 'debug': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'extracted_keywords': ' \nlived informatics; personal informatics; self-tracking; \nlapsing; physical activity; finances; loc'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'extracted_keywords': ' \npersonal informatics, collection, reflection, model, barriers \n\n'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'extracted_keywords': '\npersonalization; animation; emotion; engagement; empathy;\nself-reﬂection.\n\n'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'extracted_keywords': ' \nmobile  health  applications;  assistive  technology;  co-design; \ninterviews; usability; overacti'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'extracted_keywords': ' \nwearable technology; dashboard; information visualization; \nstroke rehabilitation; occupational th'}]}, 'var_function-call-16481698289397756348': [], 'var_function-call-15906191458607323979': []}

exec(code, env_args)
