code = """import json
import re
from collections import Counter

file_path = locals()['var_function-call-4728077729145465214']
with open(file_path, 'r') as f:
    papers = json.load(f)

matching_titles = []
years_found = []

for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    
    # Year extraction
    header = text[:1000]
    match = re.search(r'20[0-9]{2}', header)
    
    if match:
        year = int(match.group(0))
        years_found.append(year)
        
        # Check > 2016 and empirical
        if year > 2016:
            if 'empirical' in text.lower():
                title = filename.replace('.txt', '')
                matching_titles.append(title)

print("__RESULT__:")
print(json.dumps({
    "matching_titles": matching_titles,
    "year_distribution": dict(Counter(years_found))
}))"""

env_args = {'var_function-call-9891317091661830869': 'file_storage/function-call-9891317091661830869.json', 'var_function-call-10963661510414454345': ['paper_docs'], 'var_function-call-5664922713276342655': [], 'var_function-call-4943697616696163916': 'file_storage/function-call-4943697616696163916.json', 'var_function-call-14589379518527739272': [], 'var_function-call-18205085577768064644': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'extracted_year': 'None', 'has_empirical': False, 'header_snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n"}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'extracted_year': 'None', 'has_empirical': False, 'header_snippet': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Hum'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'extracted_year': 'None', 'has_empirical': True, 'header_snippet': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Anima'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'extracted_year': 'None', 'has_empirical': True, 'header_snippet': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n '}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'extracted_year': 'None', 'has_empirical': False, 'header_snippet': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation '}], 'var_function-call-1755271744771540989': {'header_repr': '"UBICOMP \'15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\\n\\nA Lived Informatics Model of Personal Informatics \\n\\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \\n1Computer Science & Engineering, 2Human Centered Design & Engineering \\nDUB Group, University of Washington \\n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \\n\\nABSTRACT \\nCurrent  models  of  how  people  use  personal  informatics \\nsystems are largely based in behavior change goals. They do \\nnot  adequately  characteriz"', 'match_simple': '2015', 'match_boundary': 'No match'}, 'var_function-call-5879411163879530965': [], 'var_function-call-18008899165245471905': {'years_counts': {'2015': 1}, 'empirical_after_2016_count': 0}, 'var_function-call-14889316983934402817': [{'_id': '694f5530284b10b11dc0a869'}, {'_id': '694f5530284b10b11dc0a86a'}, {'_id': '694f5530284b10b11dc0a86b'}, {'_id': '694f5530284b10b11dc0a86c'}, {'_id': '694f5530284b10b11dc0a86d'}], 'var_function-call-10527428186343621801': [{'_id': '694f5530284b10b11dc0a869'}, {'_id': '694f5530284b10b11dc0a86a'}, {'_id': '694f5530284b10b11dc0a86b'}, {'_id': '694f5530284b10b11dc0a86c'}, {'_id': '694f5530284b10b11dc0a86d'}, {'_id': '694f5530284b10b11dc0a86e'}, {'_id': '694f5530284b10b11dc0a86f'}, {'_id': '694f5530284b10b11dc0a870'}, {'_id': '694f5530284b10b11dc0a871'}, {'_id': '694f5530284b10b11dc0a872'}, {'_id': '694f5530284b10b11dc0a873'}, {'_id': '694f5530284b10b11dc0a874'}, {'_id': '694f5530284b10b11dc0a875'}, {'_id': '694f5530284b10b11dc0a876'}, {'_id': '694f5530284b10b11dc0a877'}, {'_id': '694f5530284b10b11dc0a878'}, {'_id': '694f5530284b10b11dc0a879'}, {'_id': '694f5530284b10b11dc0a87a'}, {'_id': '694f5530284b10b11dc0a87b'}, {'_id': '694f5530284b10b11dc0a87c'}, {'_id': '694f5530284b10b11dc0a87d'}, {'_id': '694f5530284b10b11dc0a87e'}, {'_id': '694f5530284b10b11dc0a87f'}, {'_id': '694f5530284b10b11dc0a880'}, {'_id': '694f5530284b10b11dc0a881'}, {'_id': '694f5530284b10b11dc0a882'}, {'_id': '694f5530284b10b11dc0a883'}, {'_id': '694f5530284b10b11dc0a884'}, {'_id': '694f5530284b10b11dc0a885'}, {'_id': '694f5530284b10b11dc0a886'}, {'_id': '694f5530284b10b11dc0a887'}, {'_id': '694f5530284b10b11dc0a888'}, {'_id': '694f5530284b10b11dc0a889'}, {'_id': '694f5530284b10b11dc0a88a'}, {'_id': '694f5530284b10b11dc0a88b'}, {'_id': '694f5530284b10b11dc0a88c'}, {'_id': '694f5530284b10b11dc0a88d'}, {'_id': '694f5530284b10b11dc0a88e'}, {'_id': '694f5530284b10b11dc0a88f'}, {'_id': '694f5530284b10b11dc0a890'}, {'_id': '694f5530284b10b11dc0a891'}, {'_id': '694f5530284b10b11dc0a892'}, {'_id': '694f5530284b10b11dc0a893'}, {'_id': '694f5530284b10b11dc0a894'}, {'_id': '694f5530284b10b11dc0a895'}, {'_id': '694f5530284b10b11dc0a896'}, {'_id': '694f5530284b10b11dc0a897'}, {'_id': '694f5530284b10b11dc0a898'}, {'_id': '694f5530284b10b11dc0a899'}, {'_id': '694f5530284b10b11dc0a89a'}, {'_id': '694f5530284b10b11dc0a89b'}, {'_id': '694f5530284b10b11dc0a89c'}, {'_id': '694f5530284b10b11dc0a89d'}, {'_id': '694f5530284b10b11dc0a89e'}, {'_id': '694f5530284b10b11dc0a89f'}, {'_id': '694f5530284b10b11dc0a8a0'}, {'_id': '694f5530284b10b11dc0a8a1'}, {'_id': '694f5530284b10b11dc0a8a2'}, {'_id': '694f5530284b10b11dc0a8a3'}, {'_id': '694f5530284b10b11dc0a8a4'}, {'_id': '694f5530284b10b11dc0a8a5'}, {'_id': '694f5530284b10b11dc0a8a6'}, {'_id': '694f5530284b10b11dc0a8a7'}, {'_id': '694f5530284b10b11dc0a8a8'}, {'_id': '694f5530284b10b11dc0a8a9'}, {'_id': '694f5530284b10b11dc0a8aa'}, {'_id': '694f5530284b10b11dc0a8ab'}, {'_id': '694f5530284b10b11dc0a8ac'}, {'_id': '694f5530284b10b11dc0a8ad'}, {'_id': '694f5530284b10b11dc0a8ae'}, {'_id': '694f5530284b10b11dc0a8af'}, {'_id': '694f5530284b10b11dc0a8b0'}, {'_id': '694f5530284b10b11dc0a8b1'}, {'_id': '694f5530284b10b11dc0a8b2'}, {'_id': '694f5530284b10b11dc0a8b3'}, {'_id': '694f5530284b10b11dc0a8b4'}, {'_id': '694f5530284b10b11dc0a8b5'}, {'_id': '694f5530284b10b11dc0a8b6'}, {'_id': '694f5530284b10b11dc0a8b7'}, {'_id': '694f5530284b10b11dc0a8b8'}, {'_id': '694f5530284b10b11dc0a8b9'}, {'_id': '694f5530284b10b11dc0a8ba'}, {'_id': '694f5530284b10b11dc0a8bb'}, {'_id': '694f5530284b10b11dc0a8bc'}, {'_id': '694f5530284b10b11dc0a8bd'}, {'_id': '694f5530284b10b11dc0a8be'}, {'_id': '694f5530284b10b11dc0a8bf'}, {'_id': '694f5530284b10b11dc0a8c0'}, {'_id': '694f5530284b10b11dc0a8c1'}, {'_id': '694f5530284b10b11dc0a8c2'}, {'_id': '694f5530284b10b11dc0a8c3'}, {'_id': '694f5530284b10b11dc0a8c4'}, {'_id': '694f5530284b10b11dc0a8c5'}, {'_id': '694f5530284b10b11dc0a8c6'}, {'_id': '694f5530284b10b11dc0a8c7'}, {'_id': '694f5530284b10b11dc0a8c8'}, {'_id': '694f5530284b10b11dc0a8c9'}, {'_id': '694f5530284b10b11dc0a8ca'}, {'_id': '694f5530284b10b11dc0a8cb'}], 'var_function-call-4728077729145465214': 'file_storage/function-call-4728077729145465214.json'}

exec(code, env_args)
