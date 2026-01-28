code = """import json

with open(locals()['var_function-call-8384665205253997752'], 'r') as f:
    paper_docs = json.load(f)

print("__RESULT__:")
print(json.dumps({
    "total_papers": len(paper_docs),
    "papers_with_food_in_text": [d['filename'] for d in paper_docs if 'food' in d['text'].lower()]
}))"""

env_args = {'var_function-call-5922621878014711528': ['paper_docs'], 'var_function-call-11455490410163430330': 'file_storage/function-call-11455490410163430330.json', 'var_function-call-8384665205253997752': 'file_storage/function-call-8384665205253997752.json', 'var_function-call-10278166770112498048': 'file_storage/function-call-10278166770112498048.json', 'var_function-call-2640047506381148300': {'food_titles': [], 'total_citations': 0, 'count_of_citation_records': 0}, 'var_function-call-515143036915456539': {'titles': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'], 'keywords_extraction_sample': 'Author Keywords \nLived Informatics; Personal Informatics; Self-Tracking; \nLapsing; Physical Activity; Finances; Location. \n\nACM Classification', 'papers_with_food_in_text': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'], 'count_food_in_text': 3}}

exec(code, env_args)
