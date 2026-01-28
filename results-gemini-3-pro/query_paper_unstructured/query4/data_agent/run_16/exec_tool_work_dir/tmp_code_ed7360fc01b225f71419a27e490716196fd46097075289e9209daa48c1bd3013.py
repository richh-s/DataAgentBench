code = """import json

key_name = 'var_function-call-4190209602007516202'
filename = locals()[key_name]

with open(filename, 'r') as f:
    papers = json.load(f)

lines_with_2016 = {}

for p in papers:
    title = p['filename']
    text = p['text']
    lines = []
    for line in text.split('\n'):
        if '2016' in line:
            lines.append(line.strip())
            if len(lines) >= 3:
                break
    lines_with_2016[title] = lines

print("__RESULT__:")
print(json.dumps(lines_with_2016))"""

env_args = {'var_function-call-4042789943322229169': ['paper_docs'], 'var_function-call-4042789943322227422': ['Citations', 'sqlite_sequence'], 'var_function-call-12606358993077835147': 'file_storage/function-call-12606358993077835147.json', 'var_function-call-9821348660880975822': 'file_storage/function-call-9821348660880975822.json', 'var_function-call-10263286268720561281': 'file_storage/function-call-10263286268720561281.json', 'var_function-call-4190209602007516202': 'file_storage/function-call-4190209602007516202.json', 'var_function-call-14190727982573706246': [], 'var_function-call-5212925989320089149': {'num_papers': 5, 'headers': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'header': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard Unive'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'header': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  conditi'}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt', 'header': 'Beyond Abandonment to Next Steps: Understanding and \nDesigning for Life after Personal Informatics Tool Use \n\nDaniel A. Epstein1, Monica Caraway2, Chuck Johnston2, \nAn Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University'}], 'matches': 5, 'examples_matched': ['A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use']}}

exec(code, env_args)
