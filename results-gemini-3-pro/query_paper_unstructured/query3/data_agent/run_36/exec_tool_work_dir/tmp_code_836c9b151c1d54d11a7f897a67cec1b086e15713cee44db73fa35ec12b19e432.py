code = """import json
import re

papers_path = locals()['var_function-call-15622601199477585635']
with open(papers_path, 'r') as f:
    papers = json.load(f)

count = 0
for p in papers:
    header = p['text'][:2000]
    years = re.findall(r"20(?:1[7-9]|2[0-4])", header)
    if not years:
        continue
    if int(years[0]) <= 2016:
        continue
        
    text_lower = p['text'].lower()
    ref_idx = text_lower.rfind("references")
    if ref_idx != -1 and ref_idx > len(text_lower) * 0.5:
        content = text_lower[:ref_idx]
    else:
        content = text_lower
        
    if "empirical" in content:
        print(f"Match: {p['filename']} (Year: {years[0]})")
        # Print context
        idx = content.find("empirical")
        print(f"Context: ...{content[idx-50:idx+50]}...")
        count += 1
        if count >= 5:
            break

print("__RESULT__:")
print("Done")"""

env_args = {'var_function-call-16234015966319740507': 'file_storage/function-call-16234015966319740507.json', 'var_function-call-12802565498323795136': ['Citations', 'sqlite_sequence'], 'var_function-call-5013530171335894864': 'file_storage/function-call-5013530171335894864.json', 'var_function-call-17077097865996106654': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'start': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu", 'contribution_matches': ['rdi,  Megan  Taylor,  and  Frank  Xu  for  their \ncontributions  through  survey  design  and  participant  inte'], 'empirical_matches': [], 'years_found': ['2015']}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'start': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 152', 'contribution_matches': ['informatics systems.  \n\nWe  provide  three  main  contributions  in  this  paper:  1)  we \nidentify  problems  a'], 'empirical_matches': [], 'years_found': []}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'start': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali', 'contribution_matches': [], 'empirical_matches': ['cal effects on the user.\n\nSYSTEM OVERVIEW\nSeveral empirical principles in animated ﬁlm making provide\nan intu'], 'years_found': []}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'start': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n E', 'contribution_matches': [' although  some  UPs  were  pleased  with \ntheir  contribution “I like drawing!” (UP4),  some  did not like \ndra'], 'empirical_matches': ['  T.  Kortum  and  James  T.  Miller.  2008.  An \nEmpirical  Evaluation  of  the  System  Usability  Scale.  ', '\nSusanna  Raj.  2018.  Circles  vs.  scales:  an  empirical  evaluation  of \nemotional assessment GUIs for mo'], 'years_found': []}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'start': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent C', 'contribution_matches': ['s  focus  on  the \npatient is important, the main contribution of this research is \na  system  designed  to  sup', 'atients’ activities outside therapy. \n\nA  second  contribution  is  offered  through  the  design  of  a \nwearab'], 'empirical_matches': [], 'years_found': []}], 'var_function-call-15622601199477585635': 'file_storage/function-call-15622601199477585635.json', 'var_function-call-8743834062660260545': 'file_storage/function-call-8743834062660260545.json', 'var_function-call-8818179841234233602': [], 'var_function-call-16884664733476412335': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'years': [], 'has_empirical': False}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'years': [], 'has_empirical': False}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'years': [], 'has_empirical': True}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'years': ['2019', '2019', '2019', '2019'], 'has_empirical': True}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'years': [], 'has_empirical': False}]}

exec(code, env_args)
