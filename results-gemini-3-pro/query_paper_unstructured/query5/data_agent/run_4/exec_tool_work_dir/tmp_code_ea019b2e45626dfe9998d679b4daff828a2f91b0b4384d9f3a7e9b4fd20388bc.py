code = """import json
import re

with open(locals()['var_function-call-10773655256875707708'], 'r') as f:
    paper_docs = json.load(f)

results = []
for doc in paper_docs:
    filename = doc['filename']
    text = doc['text']
    
    # Check if CHI is in text (case sensitive)
    is_chi = False
    if "CHI" in text:
        # Check context
        if re.search(r'\bCHI\b', text):
            is_chi = True
    
    # Check for "Conference on Human Factors"
    if "Conference on Human Factors" in text:
        is_chi = True
        
    results.append({"filename": filename, "is_chi": is_chi})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-18234388167969171677': ['paper_docs'], 'var_function-call-18234388167969169864': 'file_storage/function-call-18234388167969169864.json', 'var_function-call-10773655256875707708': 'file_storage/function-call-10773655256875707708.json', 'var_function-call-6452252535537636980': {'total_citations': 16, 'chi_papers_count': 1, 'sample_papers': [['A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 16]]}, 'var_function-call-16682055075633350365': ["UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu", 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 152', 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali', 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n E', 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent C'], 'var_function-call-16584696122820506875': [], 'var_function-call-17525659752872537033': '', 'var_function-call-2502493352653004496': [], 'var_function-call-356112205022407543': {'count': 5, 'filenames': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt']}}

exec(code, env_args)
