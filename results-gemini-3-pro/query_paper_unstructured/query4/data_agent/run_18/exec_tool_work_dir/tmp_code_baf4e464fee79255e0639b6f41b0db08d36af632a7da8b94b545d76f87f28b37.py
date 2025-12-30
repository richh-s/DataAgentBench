code = """import json

with open(locals()['var_function-call-18120137010689516403'], 'r') as f:
    papers_data = json.load(f)

total_papers = len(papers_data)
papers_2016_anywhere = 0
snippets_2016 = []

for paper in papers_data:
    text = paper.get('text', '')
    idx = text.find('2016')
    if idx != -1:
        papers_2016_anywhere += 1
        if len(snippets_2016) < 5:
            start = max(0, idx - 50)
            end = min(len(text), idx + 50)
            snippets_2016.append(text[start:end].replace('\n', ' '))

print("__RESULT__:")
print(json.dumps({
    "total_papers": total_papers,
    "papers_with_2016_anywhere": papers_2016_anywhere,
    "snippets": snippets_2016
}))"""

env_args = {'var_function-call-12537067908498854148': ['paper_docs'], 'var_function-call-12537067908498856339': ['Citations', 'sqlite_sequence'], 'var_function-call-18120137010689517392': 'file_storage/function-call-18120137010689517392.json', 'var_function-call-18120137010689516403': 'file_storage/function-call-18120137010689516403.json', 'var_function-call-7739271670607473700': [], 'var_function-call-4465078227476414897': {'count_domain_physical_activity': 4, 'count_year_2016_heuristic': 0, 'examples': ["UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.wash", 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 15213 \nianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu \n\nABSTRACT \nPeople  strive  to  obtain  self-knowled', 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard Unive', 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  conditi']}}

exec(code, env_args)
