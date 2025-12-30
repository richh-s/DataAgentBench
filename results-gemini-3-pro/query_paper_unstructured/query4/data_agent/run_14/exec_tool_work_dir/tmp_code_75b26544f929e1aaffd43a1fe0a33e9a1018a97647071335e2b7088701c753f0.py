code = """import json

with open(locals()['var_function-call-1932226808801670089'], 'r') as f:
    papers = json.load(f)

target_titles = [
    "A Trip to the Moon: Personalized Animated Movies for Self-reflection",
    "A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App"
]

print('Context for "physical activity":')
for p in papers:
    title = p['filename'].replace('.txt', '')
    if title in target_titles:
        text = p['text']
        idx = text.lower().find('physical activity')
        if idx != -1:
            start = max(0, idx - 50)
            end = min(len(text), idx + 50)
            print(f"--- {title} ---")
            print(f"...{text[start:end].replace('\\n', ' ')}...")
            
print('__RESULT__:')
print(json.dumps('checked'))"""

env_args = {'var_function-call-1702073112922347921': 'file_storage/function-call-1702073112922347921.json', 'var_function-call-1932226808801670089': 'file_storage/function-call-1932226808801670089.json', 'var_function-call-962751485773488507': [], 'var_function-call-7065428767618965832': 'debug_done', 'var_function-call-16942510160827002224': {'total_papers': 5, 'pa_count': 4, 'sample_headers': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'header': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN  A Lived Informatics Model of Personal Informatics   Daniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2  1Computer Science & Engineering, 2Human Centered Design & Engineering  DUB Group, University of Washington  {depstein, jfogarty}@cs.wash"}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'header': 'A Stage-Based Model of Personal Informatics Systems  Ian Li1, Anind Dey1, and Jodi Forlizzi1,2  1Human Computer Interaction Institute, 2School of Design  Carnegie Mellon University, Pittsburgh, PA 15213  ianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu   ABSTRACT  People  strive  to  obtain  self-knowled'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'header': 'Fengjiao Peng MIT Media Lab Cambridge, MA, USA fpeng@mit.edu  A Trip to the Moon: Personalized Animated Movies for Self-reﬂection Veronica Crista LaBelle MIT Cambridge, MA, USA vlabelle@mit.edu Rosalind W. Picard MIT Media Lab Cambridge, MA, USA picard@media.mit.edu  Emily Christen Yue Harvard Unive'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'header': 'A Wee Bit More Interaction: Designing and Evaluating   an Overactive Bladder App  Ana-Maria Salai   Heriot-Watt University   Edinburgh, UK   as152@hw.ac.uk   Lynne Baillie   Heriot-Watt University   Edinburgh, UK   l.baillie@hw.ac.uk  ABSTRACT   Overactive  Bladder  (OAB)  is  a  widespread  conditi'}], '2016_count': 0}, 'var_function-call-16753911823346326411': ['A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App'], 'var_function-call-5907422387942144876': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citations': '265'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': '266'}]}

exec(code, env_args)
