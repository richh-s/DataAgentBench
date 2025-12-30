code = """import json
import re

papers_file = locals()['var_function-call-3120307728303997294']

with open(papers_file, 'r') as f:
    papers_data = json.load(f)

analysis = []

for paper in papers_data:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Extract year candidates from first 2000 chars
    header = text[:2000]
    years_found = re.findall(r'20\d{2}', header)
    # Also look for '16 
    short_year = re.search(r"'\d{2}", header)
    
    # Check physical activity
    phy_act = 'physical activity' in text.lower()
    
    analysis.append({
        "title": filename,
        "years_in_header": years_found,
        "short_year": short_year.group(0) if short_year else None,
        "phy_act": phy_act,
        "header_snippet": header[:300].replace('\n', ' ')
    })

print("__RESULT__:")
print(json.dumps(analysis))"""

env_args = {'var_function-call-14316968101871802559': ['paper_docs'], 'var_function-call-14316968101871802262': ['Citations', 'sqlite_sequence'], 'var_function-call-637640979100223299': 'file_storage/function-call-637640979100223299.json', 'var_function-call-1625396781395039115': 'file_storage/function-call-1625396781395039115.json', 'var_function-call-3120307728303997294': 'file_storage/function-call-3120307728303997294.json', 'var_function-call-14472908731975527772': [], 'var_function-call-2932303628757857075': {'total_papers': 5, 'count_2016_header': 0, 'count_phy_act': 4, 'samples': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'header_preview': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN  A Lived Informatics Model of Personal Informatics  ", 'has_2016': False, 'has_phy_act': True}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'header_preview': 'A Stage-Based Model of Personal Informatics Systems  Ian Li1, Anind Dey1, and Jodi Forlizzi1,2  1Hum', 'has_2016': False, 'has_phy_act': True}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'header_preview': 'Fengjiao Peng MIT Media Lab Cambridge, MA, USA fpeng@mit.edu  A Trip to the Moon: Personalized Anima', 'has_2016': False, 'has_phy_act': True}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'header_preview': 'A Wee Bit More Interaction: Designing and Evaluating   an Overactive Bladder App  Ana-Maria Salai   ', 'has_2016': False, 'has_phy_act': True}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'header_preview': 'ArmSleeve: a Patient Monitoring System to Support  Occupational Therapists in Stroke Rehabilitation ', 'has_2016': False, 'has_phy_act': False}]}, 'var_function-call-3261606002053340868': [{'_id': '694f5530284b10b11dc0a869'}, {'_id': '694f5530284b10b11dc0a86a'}, {'_id': '694f5530284b10b11dc0a86b'}, {'_id': '694f5530284b10b11dc0a86c'}, {'_id': '694f5530284b10b11dc0a86d'}], 'var_function-call-3261606002053341073': 'file_storage/function-call-3261606002053341073.json'}

exec(code, env_args)
