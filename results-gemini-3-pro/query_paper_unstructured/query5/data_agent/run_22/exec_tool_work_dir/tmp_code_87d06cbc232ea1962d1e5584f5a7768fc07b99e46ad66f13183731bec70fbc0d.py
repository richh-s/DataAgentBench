code = """import json
import re

papers_path = locals()['var_function-call-3655541512535358306']
with open(papers_path, 'r') as f:
    papers_data = json.load(f)

# Use the second paper
target_filename = "A Stage-based Model of Personal Informatics Systems.txt"
text = ""
for p in papers_data:
    if p['filename'] == target_filename:
        text = p['text']
        break

matches = []
# Search for CHI (case insensitive)
for m in re.finditer(r"CHI", text, re.IGNORECASE):
    start = max(0, m.start() - 50)
    end = min(len(text), m.end() + 50)
    snippet = text[start:end].replace(chr(10), " ")
    matches.append(snippet)
    if len(matches) > 10:
        break

print("__RESULT__:")
print(json.dumps(matches))"""

env_args = {'var_function-call-10316639782376097408': ['Citations', 'sqlite_sequence'], 'var_function-call-10316639782376098289': ['paper_docs'], 'var_function-call-10316639782376099170': 'file_storage/function-call-10316639782376099170.json', 'var_function-call-10316639782376095955': 'file_storage/function-call-10316639782376095955.json', 'var_function-call-3655541512535358306': 'file_storage/function-call-3655541512535358306.json', 'var_function-call-17554690775413640325': {'total_citations': 0, 'chi_paper_count': 0, 'papers_with_citations': 0, 'sample_titles': []}, 'var_function-call-17909243822308874303': ["UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN  A Lived Informatics Model of Personal Informatics  ", 'A Stage-Based Model of Personal Informatics Systems  Ian Li1, Anind Dey1, and Jodi Forlizzi1,2  1Hum', 'Fengjiao Peng MIT Media Lab Cambridge, MA, USA fpeng@mit.edu  A Trip to the Moon: Personalized Anima', 'A Wee Bit More Interaction: Designing and Evaluating   an Overactive Bladder App  Ana-Maria Salai   ', 'ArmSleeve: a Patient Monitoring System to Support  Occupational Therapists in Stroke Rehabilitation '], 'var_function-call-16031832592638894853': [], 'var_function-call-4203575224647280671': ['eral Terms  Design, Human Factors   INTRODUCTION AND MOTIVATION  The  ', ' CHI  Conference on Human Factors in Computing Systems Proceedings (CH'], 'var_function-call-1051744689778981053': {'chi_paper_count': 1, 'cited_chi_papers': 1, 'total_citations': 16}, 'var_function-call-4390615398975747556': ["UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN", 'A Stage-Based Model of Personal Informatics Systems', 'Fengjiao Peng', 'A Wee Bit More Interaction: Designing and Evaluating', 'ArmSleeve: a Patient Monitoring System to Support'], 'var_function-call-14673900924018147280': '', 'var_function-call-4335656298020408932': [68339, 63309, 54376, 74850, 73461], 'var_function-call-9828446944437698937': 'Paper not found', 'var_function-call-14643045795651823722': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt']}

exec(code, env_args)
