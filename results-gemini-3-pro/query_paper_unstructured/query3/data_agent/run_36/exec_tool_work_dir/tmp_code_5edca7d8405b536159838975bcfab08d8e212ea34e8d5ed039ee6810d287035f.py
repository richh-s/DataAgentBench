code = """import json
import re

file_path = locals()['var_function-call-15622601199477585635']
with open(file_path, 'r') as f:
    papers = json.load(f)

valid_papers = []

for p in papers:
    text = p['text']
    filename = p['filename']
    title = filename.replace('.txt', '')
    
    header = text[:1000]
    
    # Regex for 20xx
    years_full = re.findall(r"\b(20\d{2})\b", header)
    # Regex for 'xx (e.g. '17)
    # simple quote
    years_short = re.findall(r"(?:CHI|Ubicomp|CSCW|DIS|IUI|WWW|PervasiveHealth|OzCHI|TEI|AH)\s*['](1[7-9]|2[0-4])", header, re.IGNORECASE)
    
    candidates = []
    for y in years_full:
        candidates.append(int(y))
    for y in years_short:
        candidates.append(2000 + int(y))
        
    candidates = [y for y in candidates if 2010 <= y <= 2024]
    
    if not candidates:
        continue
        
    year = candidates[0] 
    
    if year <= 2016:
        continue
        
    # Check Contribution: Empirical
    text_lower = text.lower()
    # Try to find references to exclude them
    # searching for "references" line
    ref_idx = -1
    # Check for specific header pattern
    # e.g. "REFERENCES" on a new line
    m = re.search(r"\nreferences\s*\n", text_lower)
    if m:
        ref_idx = m.start()
    
    if ref_idx != -1:
        content_text = text_lower[:ref_idx]
    else:
        content_text = text_lower
        
    if "empirical" in content_text:
        valid_papers.append(title)

print("__RESULT__:")
print(json.dumps(valid_papers))"""

env_args = {'var_function-call-16234015966319740507': 'file_storage/function-call-16234015966319740507.json', 'var_function-call-12802565498323795136': ['Citations', 'sqlite_sequence'], 'var_function-call-5013530171335894864': 'file_storage/function-call-5013530171335894864.json', 'var_function-call-17077097865996106654': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'start': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu", 'contribution_matches': ['rdi,  Megan  Taylor,  and  Frank  Xu  for  their \ncontributions  through  survey  design  and  participant  inte'], 'empirical_matches': [], 'years_found': ['2015']}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'start': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 152', 'contribution_matches': ['informatics systems.  \n\nWe  provide  three  main  contributions  in  this  paper:  1)  we \nidentify  problems  a'], 'empirical_matches': [], 'years_found': []}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'start': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali', 'contribution_matches': [], 'empirical_matches': ['cal effects on the user.\n\nSYSTEM OVERVIEW\nSeveral empirical principles in animated ﬁlm making provide\nan intu'], 'years_found': []}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'start': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n E', 'contribution_matches': [' although  some  UPs  were  pleased  with \ntheir  contribution “I like drawing!” (UP4),  some  did not like \ndra'], 'empirical_matches': ['  T.  Kortum  and  James  T.  Miller.  2008.  An \nEmpirical  Evaluation  of  the  System  Usability  Scale.  ', '\nSusanna  Raj.  2018.  Circles  vs.  scales:  an  empirical  evaluation  of \nemotional assessment GUIs for mo'], 'years_found': []}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'start': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent C', 'contribution_matches': ['s  focus  on  the \npatient is important, the main contribution of this research is \na  system  designed  to  sup', 'atients’ activities outside therapy. \n\nA  second  contribution  is  offered  through  the  design  of  a \nwearab'], 'empirical_matches': [], 'years_found': []}], 'var_function-call-15622601199477585635': 'file_storage/function-call-15622601199477585635.json'}

exec(code, env_args)
