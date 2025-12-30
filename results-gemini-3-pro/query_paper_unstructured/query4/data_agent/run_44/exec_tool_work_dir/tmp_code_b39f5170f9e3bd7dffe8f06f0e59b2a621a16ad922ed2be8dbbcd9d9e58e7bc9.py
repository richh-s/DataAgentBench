code = """import json
import re

file_path = locals()['var_function-call-4863138715288248504']
with open(file_path, 'r') as f:
    papers = json.load(f)

results = []
for paper in papers:
    text = paper.get('text', '')
    years = re.findall(r'20\d\d', text)
    # Filter years to be reasonable (e.g., 2010-2020) just to reduce noise, or keep all.
    # Count occurrences to find the most likely publication year (often appears in header, copyright, footer, references).
    # But references also have years.
    # The header usually appears at the start.
    header_years = re.findall(r'20\d\d', text[:500])
    
    has_domain = "physical activity" in text.lower()
    
    results.append({
        "filename": paper['filename'],
        "header_years": header_years,
        "all_years_count": len(years),
        "has_domain": has_domain
    })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-1438467208148862698': 'file_storage/function-call-1438467208148862698.json', 'var_function-call-987307425493553399': 'file_storage/function-call-987307425493553399.json', 'var_function-call-4863138715288248504': 'file_storage/function-call-4863138715288248504.json', 'var_function-call-6286417956079604125': [], 'var_function-call-2642568662990670730': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'years_found': ['2015'], 'header_snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'years_found': [], 'header_snippet': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 152'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'years_found': [], 'header_snippet': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'years_found': [], 'header_snippet': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n E'}], 'var_function-call-16800725899917521487': 5}

exec(code, env_args)
