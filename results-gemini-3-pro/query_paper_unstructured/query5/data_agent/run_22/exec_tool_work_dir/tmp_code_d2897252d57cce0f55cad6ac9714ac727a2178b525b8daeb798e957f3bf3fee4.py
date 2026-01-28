code = """import json
import re

papers_path = locals()['var_function-call-3655541512535358306']
with open(papers_path, 'r') as f:
    papers_data = json.load(f)

matches = []
for p in papers_data:
    text = p.get('text', '')[:2000] # First 2000 chars
    # Search for CHI with some context
    m = re.search(r"(.{0,50}\bCHI\b.{0,50})", text)
    if m:
        matches.append(m.group(1).replace('\\n', ' '))
    if len(matches) >= 20:
        break

print("__RESULT__:")
print(json.dumps(matches))"""

env_args = {'var_function-call-10316639782376097408': ['Citations', 'sqlite_sequence'], 'var_function-call-10316639782376098289': ['paper_docs'], 'var_function-call-10316639782376099170': 'file_storage/function-call-10316639782376099170.json', 'var_function-call-10316639782376095955': 'file_storage/function-call-10316639782376095955.json', 'var_function-call-3655541512535358306': 'file_storage/function-call-3655541512535358306.json', 'var_function-call-17554690775413640325': {'total_citations': 0, 'chi_paper_count': 0, 'papers_with_citations': 0, 'sample_titles': []}, 'var_function-call-17909243822308874303': ["UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN  A Lived Informatics Model of Personal Informatics  ", 'A Stage-Based Model of Personal Informatics Systems  Ian Li1, Anind Dey1, and Jodi Forlizzi1,2  1Hum', 'Fengjiao Peng MIT Media Lab Cambridge, MA, USA fpeng@mit.edu  A Trip to the Moon: Personalized Anima', 'A Wee Bit More Interaction: Designing and Evaluating   an Overactive Bladder App  Ana-Maria Salai   ', 'ArmSleeve: a Patient Monitoring System to Support  Occupational Therapists in Stroke Rehabilitation ']}

exec(code, env_args)
