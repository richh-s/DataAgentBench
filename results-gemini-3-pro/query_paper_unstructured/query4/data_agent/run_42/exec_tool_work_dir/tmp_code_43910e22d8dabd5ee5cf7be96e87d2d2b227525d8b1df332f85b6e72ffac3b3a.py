code = """import json

file_path = locals()['var_function-call-1860394560099388718']
with open(file_path, 'r') as f:
    papers = json.load(f)

target_filenames = [
    "A Lived Informatics Model of Personal Informatics.txt", 
    "A Stage-based Model of Personal Informatics Systems.txt", 
    "A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt", 
    "A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt"
]

snippets = {}
for p in papers:
    if p['filename'] in target_filenames:
        snippets[p['filename']] = p['text'][:500]

print("__RESULT__:")
print(json.dumps(snippets))"""

env_args = {'var_function-call-10819517614772727470': 'file_storage/function-call-10819517614772727470.json', 'var_function-call-1860394560099388718': 'file_storage/function-call-1860394560099388718.json', 'var_function-call-475874978628204145': [], 'var_function-call-4305763543364550069': 'Debug info printed', 'var_function-call-17505959037829816144': {'headers': ["UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.wash", 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 15213 \nianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu \n\nABSTRACT \nPeople  strive  to  obtain  self-knowled', 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard Unive', 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  conditi', 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent Crocher1,3, Frank Vetere1, Suranga Nanayakkara1,4 \n1Microsoft Research Centre for SocialNUI, The Univ'], 'count_pa': 4, 'count_2016': 0, 'count_16': 0}, 'var_function-call-4683535024380308942': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt']}

exec(code, env_args)
