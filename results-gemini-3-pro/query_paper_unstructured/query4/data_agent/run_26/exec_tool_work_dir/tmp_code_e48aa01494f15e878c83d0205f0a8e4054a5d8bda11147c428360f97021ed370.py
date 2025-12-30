code = """import json
import re

file_path = locals()['var_function-call-11196622143221928567']
with open(file_path, 'r') as f:
    papers = json.load(f)

print("__RESULT__:")
results = []
for p in papers:
    text = p['text']
    filename = p['filename']
    title = filename.replace('.txt', '')
    
    # Find years
    years = re.findall(r'201[0-9]', text)
    
    # Check domain
    has_pa = 'physical activity' in text.lower()
    
    results.append({
        "title": title,
        "years_found": years[:5], # first 5 occurrences
        "has_pa": has_pa,
        "header_snippet": text[:300]
    })

print(json.dumps(results))"""

env_args = {'var_function-call-16083049299143672043': 'file_storage/function-call-16083049299143672043.json', 'var_function-call-6689175005249734094': ['Citations', 'sqlite_sequence'], 'var_function-call-11808017164042867885': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-11196622143221928567': 'file_storage/function-call-11196622143221928567.json', 'var_function-call-9561131013778660731': [], 'var_function-call-18165672206720912014': {'sample_headers': ["UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu", 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 152', 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali', 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n E', 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent C'], 'count_2016_in_header': 0, 'count_pa': 4, 'total_papers': 5}, 'var_function-call-8690695742089108315': [{'_id': '694f5530284b10b11dc0a869'}, {'_id': '694f5530284b10b11dc0a86a'}, {'_id': '694f5530284b10b11dc0a86b'}, {'_id': '694f5530284b10b11dc0a86c'}, {'_id': '694f5530284b10b11dc0a86d'}]}

exec(code, env_args)
