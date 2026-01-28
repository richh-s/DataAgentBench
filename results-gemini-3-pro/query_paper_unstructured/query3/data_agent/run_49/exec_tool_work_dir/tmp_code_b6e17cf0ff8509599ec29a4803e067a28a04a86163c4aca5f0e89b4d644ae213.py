code = """import json
import re

with open(locals()['var_function-call-3050203900418415447'], 'r') as f:
    papers = json.load(f)

results = []

for p in papers:
    text = p.get('text', '')
    title = p.get('filename', '').replace('.txt', '')
    
    # Check Empirical
    is_empirical = 'empirical' in text.lower()
    
    # Extract Year
    # Search first 5000 chars
    header = text[:5000]
    # Find all 4-digit years 20xx
    years = re.findall(r'20\d\d', header)
    
    # Filter for reasonable publication years (e.g., 2010-2025) to avoid random numbers
    valid_years = [int(y) for y in years if 2010 <= int(y) <= 2025]
    
    # Heuristic: The publication year is likely the most frequent or earliest valid year 
    # appearing in the copyright/header. Or simply, if 2017+ is present and 2016- is not?
    # Actually, if a paper is published in 2017, it might cite 2015 papers.
    # So finding 2015 doesn't disqualify it. Finding 2017 might qualify it.
    # But references usually appear at the end. I'm looking at the first 5000 chars.
    # "Copyright 2017" or "CHI 2017" is a strong signal.
    
    # Strategy: Look for the earliest year in the header? No, older references might be in intro.
    # Look for the *latest* year in the header? No, could be a "future work" date or "since 2020" in a 2021 paper.
    # Usually the conference/copyright year is explicit. 
    # Let's count occurrences and look for specific patterns if possible.
    # For this task, I'll take the set of years found in the header. 
    # If the *maximum* year in the header is > 2016, it's a candidate? 
    # No, if I cite a 2015 paper in a 2014 paper (unlikely).
    # If I cite a 2010 paper in a 2018 paper. 2010 and 2018 will be there.
    # The publication year is likely the one matching the conference date.
    # Let's just output the years found for now to manually inspect/logicize.
    
    results.append({
        "title": title,
        "is_empirical": is_empirical,
        "years_found": list(set(valid_years))
    })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-7133362832000802960': 'file_storage/function-call-7133362832000802960.json', 'var_function-call-7133362832000806077': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}], 'var_function-call-3665432082971907292': 'file_storage/function-call-3665432082971907292.json', 'var_function-call-3050203900418415447': 'file_storage/function-call-3050203900418415447.json', 'var_function-call-4351111685594668903': [], 'var_function-call-12677939934475284985': {'total_papers': 5, 'empirical_count': 2, 'samples': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'text_start': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.wash", 'years_found': []}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'text_start': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 15213 \nianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu \n\nABSTRACT \nPeople  strive  to  obtain  self-knowled', 'years_found': []}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'text_start': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard Unive', 'years_found': []}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'text_start': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  conditi', 'years_found': []}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'text_start': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent Crocher1,3, Frank Vetere1, Suranga Nanayakkara1,4 \n1Microsoft Research Centre for SocialNUI, The Univ', 'years_found': []}]}}

exec(code, env_args)
