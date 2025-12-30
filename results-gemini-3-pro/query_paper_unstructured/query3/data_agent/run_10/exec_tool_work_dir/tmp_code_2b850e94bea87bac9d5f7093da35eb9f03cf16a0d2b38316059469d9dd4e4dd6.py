code = """import json
import re

file_path = locals()['var_function-call-4943697616696163916']
with open(file_path, 'r') as f:
    papers = json.load(f)

p1 = papers[0]
text = p1.get('text', '')
header_text = text[:500]

print("Header text:", repr(header_text))

# Test regex
match = re.search(r'20[0-9]{2}', header_text)
print("Match simple:", match.group(0) if match else "No match")

match_b = re.search(r'\b20[0-9]{2}\b', header_text)
print("Match boundary:", match_b.group(0) if match_b else "No match")"""

env_args = {'var_function-call-9891317091661830869': 'file_storage/function-call-9891317091661830869.json', 'var_function-call-10963661510414454345': ['paper_docs'], 'var_function-call-5664922713276342655': [], 'var_function-call-4943697616696163916': 'file_storage/function-call-4943697616696163916.json', 'var_function-call-14589379518527739272': [], 'var_function-call-18205085577768064644': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'extracted_year': 'None', 'has_empirical': False, 'header_snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n"}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'extracted_year': 'None', 'has_empirical': False, 'header_snippet': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Hum'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'extracted_year': 'None', 'has_empirical': True, 'header_snippet': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Anima'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'extracted_year': 'None', 'has_empirical': True, 'header_snippet': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n '}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'extracted_year': 'None', 'has_empirical': False, 'header_snippet': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation '}]}

exec(code, env_args)
