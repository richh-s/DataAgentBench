code = """import json
import re
from collections import Counter

file_path = locals()['var_function-call-4943697616696163916']
with open(file_path, 'r') as f:
    papers = json.load(f)

years = []
years_empirical = []

for p in papers:
    text = p.get('text', '')
    header = text[:1000]
    match = re.search(r'20[0-9]{2}', header)
    if match:
        y = int(match.group(0))
        years.append(y)
        if y > 2016 and 'empirical' in text.lower():
            years_empirical.append(y)

print("__RESULT__:")
print(json.dumps({
    "years_counts": dict(Counter(years)),
    "empirical_after_2016_count": len(years_empirical)
}))"""

env_args = {'var_function-call-9891317091661830869': 'file_storage/function-call-9891317091661830869.json', 'var_function-call-10963661510414454345': ['paper_docs'], 'var_function-call-5664922713276342655': [], 'var_function-call-4943697616696163916': 'file_storage/function-call-4943697616696163916.json', 'var_function-call-14589379518527739272': [], 'var_function-call-18205085577768064644': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'extracted_year': 'None', 'has_empirical': False, 'header_snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n"}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'extracted_year': 'None', 'has_empirical': False, 'header_snippet': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Hum'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'extracted_year': 'None', 'has_empirical': True, 'header_snippet': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Anima'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'extracted_year': 'None', 'has_empirical': True, 'header_snippet': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n '}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'extracted_year': 'None', 'has_empirical': False, 'header_snippet': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation '}], 'var_function-call-1755271744771540989': {'header_repr': '"UBICOMP \'15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\\n\\nA Lived Informatics Model of Personal Informatics \\n\\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \\n1Computer Science & Engineering, 2Human Centered Design & Engineering \\nDUB Group, University of Washington \\n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \\n\\nABSTRACT \\nCurrent  models  of  how  people  use  personal  informatics \\nsystems are largely based in behavior change goals. They do \\nnot  adequately  characteriz"', 'match_simple': '2015', 'match_boundary': 'No match'}, 'var_function-call-5879411163879530965': []}

exec(code, env_args)
