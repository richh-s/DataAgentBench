code = """import json

key_name = 'var_function-call-1660175416261696799'
file_path = locals()[key_name]

with open(file_path, 'r') as f:
    papers = json.load(f)

targets = [
    "A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt",
    "A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt",
    "ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt"
]

results = {}
for p in papers:
    if p['filename'] in targets:
        text = p['text']
        results[p['filename']] = {
            'head': text[:1000],
            'tail': text[-1000:]
        }

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_function-call-8186241074131223286': ['paper_docs'], 'var_function-call-8186241074131224069': ['Citations', 'sqlite_sequence'], 'var_function-call-11444584410328735250': 'file_storage/function-call-11444584410328735250.json', 'var_function-call-1660175416261696799': 'file_storage/function-call-1660175416261696799.json', 'var_function-call-11009971784847056933': [], 'var_function-call-17654094565186069482': {'total_papers': 5, 'count_2016_in_header': 0, 'count_pa_in_text': 4, 'examples_2016': [], 'examples_pa': ["UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu", 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 152', 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali']}, 'var_function-call-980800035285494709': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'header': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.wash"}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'header': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 15213 \nianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu \n\nABSTRACT \nPeople  strive  to  obtain  self-knowled'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'header': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard Unive'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'header': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  conditi'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'header': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent Crocher1,3, Frank Vetere1, Suranga Nanayakkara1,4 \n1Microsoft Research Centre for SocialNUI, The Univ'}], 'var_function-call-14426171548755125703': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'year_matches': [], 'has_pa': True}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'year_matches': [], 'has_pa': True}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'year_matches': [' Tanzeem Choudhury. 2016.', '2016 ACM International J', '24. Akane Sano. 2016. Measuring college '], 'has_pa': True}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'year_matches': ['Coninx. 2016. Back on bike: the ', '2016.  A  longitudinal e', 'lizabeth D. Mynatt. 2016. A Cancer ', 'nd  Stephen  Uzor.  2016.  Time  to ', 'c  floor  Fitness.  2016.  http://www.lights'], 'has_pa': True}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'year_matches': ['DIS 2016, June 04 - 08, 2016', 'Sensing, HealthDIS 2016, June 4–8, 2016, Br', 'Sensing, HealthDIS 2016, June 4–8, 2016, Br', 'Sensing, HealthDIS 2016, June 4–8, 2016, Br', 'Sensing, HealthDIS 2016, June 4–8, 2016, Br'], 'has_pa': False}]}

exec(code, env_args)
