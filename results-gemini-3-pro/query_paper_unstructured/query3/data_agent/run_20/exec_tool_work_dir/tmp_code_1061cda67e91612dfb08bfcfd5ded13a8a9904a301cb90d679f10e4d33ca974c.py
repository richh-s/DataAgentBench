code = """import json
import re

with open(locals()['var_function-call-14157823481537147433'], 'r') as f:
    papers_data = json.load(f)

debug_info = []

for i, paper in enumerate(papers_data[:20]):
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    match = re.search(r'20\d{2}', text[:1000])
    year = int(match.group(0)) if match else 0
    has_empirical = 'empirical' in text.lower()
    
    debug_info.append({
        "title": filename,
        "year": year,
        "has_empirical": has_empirical
    })

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-11261961701334828073': ['paper_docs'], 'var_function-call-11261961701334829364': 'file_storage/function-call-11261961701334829364.json', 'var_function-call-11261961701334830655': ['Citations', 'sqlite_sequence'], 'var_function-call-11261961701334827850': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}], 'var_function-call-8802837961524065341': 'file_storage/function-call-8802837961524065341.json', 'var_function-call-389901141376174398': 'file_storage/function-call-389901141376174398.json', 'var_function-call-389901141376172653': 'file_storage/function-call-389901141376172653.json', 'var_function-call-8584235094798493494': [], 'var_function-call-10819417574072414189': [], 'var_function-call-18354289230382980981': ['Num citations: 259', 'Num papers: 5', {'title': 'A Lived Informatics Model of Personal Informatics', 'year': 2015, 'has_empirical': False, 'snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n"}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': 0, 'has_empirical': False, 'snippet': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Hum'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 0, 'has_empirical': True, 'snippet': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Anima'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 0, 'has_empirical': True, 'snippet': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n '}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': 0, 'has_empirical': False, 'snippet': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation '}], 'var_function-call-14157823481537147433': 'file_storage/function-call-14157823481537147433.json', 'var_function-call-3479710015239140496': []}

exec(code, env_args)
