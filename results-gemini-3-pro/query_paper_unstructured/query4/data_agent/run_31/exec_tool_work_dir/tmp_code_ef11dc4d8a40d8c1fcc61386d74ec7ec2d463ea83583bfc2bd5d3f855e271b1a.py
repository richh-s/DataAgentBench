code = """import json

filepath = locals()['var_function-call-3288691391173490611']
with open(filepath, 'r') as f:
    papers = json.load(f)

res = []
for p in papers:
    title = p['filename'].replace('.txt', '')
    text = p.get('text', '')
    
    header = text[:500]
    
    if "ArmSleeve" in title or "Wee Bit" in title or "Trip" in title:
        info = {}
        info['title'] = title
        info['header'] = header
        info['has_pa'] = "physical activity" in text.lower()
        info['has_2016'] = "2016" in text
        info['has_tick16'] = "'16" in text[:500]
        res.append(info)

print("__RESULT__:")
print(json.dumps(res, default=str))"""

env_args = {'var_function-call-18071913863727802806': ['paper_docs'], 'var_function-call-18071913863727800731': ['Citations', 'sqlite_sequence'], 'var_function-call-4878043967039962062': 'file_storage/function-call-4878043967039962062.json', 'var_function-call-16507150589347793699': [{'_id': '694f5530284b10b11dc0a869'}, {'_id': '694f5530284b10b11dc0a86a'}, {'_id': '694f5530284b10b11dc0a86b'}, {'_id': '694f5530284b10b11dc0a86c'}, {'_id': '694f5530284b10b11dc0a86d'}], 'var_function-call-9855888285311973797': 5, 'var_function-call-3288691391173490611': 'file_storage/function-call-3288691391173490611.json', 'var_function-call-9675587272762560169': [], 'var_function-call-11232172477499880328': [{'title': 'A Lived Informatics Model of Personal Informatics', 'header_preview': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.wash", 'has_2016': False, 'has_pa': True}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'header_preview': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 15213 \nianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu \n\nABSTRACT \nPeople  strive  to  obtain  self-knowled', 'has_2016': False, 'has_pa': True}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'header_preview': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard Unive', 'has_2016': False, 'has_pa': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'header_preview': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  conditi', 'has_2016': False, 'has_pa': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'header_preview': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent Crocher1,3, Frank Vetere1, Suranga Nanayakkara1,4 \n1Microsoft Research Centre for SocialNUI, The Univ', 'has_2016': True, 'has_pa': False}]}

exec(code, env_args)
