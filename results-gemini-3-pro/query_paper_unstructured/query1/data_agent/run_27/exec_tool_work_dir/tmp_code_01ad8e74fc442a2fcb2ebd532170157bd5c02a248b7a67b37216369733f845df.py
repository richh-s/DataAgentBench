code = """import json

# Path from the limit:1000 query
papers_path = locals()['var_function-call-9843037980152056802']
citations_path = locals()['var_function-call-1369991432828738488']

with open(papers_path, 'r') as f:
    papers = json.load(f)

with open(citations_path, 'r') as f:
    citations = json.load(f)

print("__RESULT__:")
print(json.dumps({
    "paper_count": len(papers),
    "paper_titles": [p['filename'] for p in papers],
    "citation_titles_sample": [c['title'] for c in citations[:10]]
}))"""

env_args = {'var_function-call-4428152146119552339': 'file_storage/function-call-4428152146119552339.json', 'var_function-call-1279721563085973081': 'file_storage/function-call-1279721563085973081.json', 'var_function-call-10463220630905116945': 'file_storage/function-call-10463220630905116945.json', 'var_function-call-6853165914555926720': {'food_papers': [], 'total_citations': 0}, 'var_function-call-4486819615144744261': 'file_storage/function-call-4486819615144744261.json', 'var_function-call-16923378931810091090': 'file_storage/function-call-16923378931810091090.json', 'var_function-call-10009206756418749160': 'file_storage/function-call-10009206756418749160.json', 'var_function-call-8154133366834530525': {'food_papers': [], 'total_citations': 0}, 'var_function-call-13338059779918874712': 'file_storage/function-call-13338059779918874712.json', 'var_function-call-1369991432828738488': 'file_storage/function-call-1369991432828738488.json', 'var_function-call-8925442921947814693': {'food_papers': [], 'total_citations': 0, 'debug_info': [{'title': 'A Lived Informatics Model of Personal Informatics', 'is_food': False, 'keywords_snippet': '\nlived informatics; personal informatics; self-tracking; \nlapsing; physical activity; finances; loca'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'is_food': False, 'keywords_snippet': '\npersonal informatics, collection, reflection, model, barriers \n\n'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'is_food': False, 'keywords_snippet': 'h.5.1. information interfaces and presentation (e.g., hci):\nanimations.\n\nauthor keywords\npersonaliza'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'is_food': False, 'keywords_snippet': '\nmobile  health  applications;  assistive  technology;  co-design; \ninterviews; usability; overactiv'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'is_food': False, 'keywords_snippet': '\nwearable technology; dashboard; information visualization; \nstroke rehabilitation; occupational the'}]}, 'var_function-call-14775292004750826621': [{'title': 'A Lived Informatics Model of Personal Informatics', 'snippet': 'r  tracking  location  [24,30],  finances  [20],  food  [11],  weight  [19,25],  and  physical  acti'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'snippet': 'projects  on  her  personal  behavior,  such  as  food  consumption  and  sneezes  (http://ellieharr'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'snippet': 'sist  of  avoiding  bladder  irritants  (certain  food  and  drinks)  and  consuming  a  proper  amo'}], 'var_function-call-9618113465213101423': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation'], 'var_function-call-9843037980152056802': 'file_storage/function-call-9843037980152056802.json', 'var_function-call-14722892854605449496': ['paper_docs']}

exec(code, env_args)
