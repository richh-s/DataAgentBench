code = """import json
import re

file_path = locals()['var_function-call-11757020696500287229']

with open(file_path, 'r') as f:
    papers = json.load(f)

debug_info = []

for paper in papers:
    text = paper['text']
    title = paper['filename']
    
    # Find all years in full text
    years = re.findall(r'20\d\d', text)
    years = [int(y) for y in years]
    years.sort()
    
    # Check for "empirical"
    has_empirical = "empirical" in text.lower()
    
    debug_info.append({"title": title, "years_found": years[:10], "has_empirical": has_empirical})

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-4508703165533921554': ['paper_docs'], 'var_function-call-6558568440617970776': 'file_storage/function-call-6558568440617970776.json', 'var_function-call-12977520170952019892': 'file_storage/function-call-12977520170952019892.json', 'var_function-call-3057315164006980337': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_function-call-11757020696500287229': 'file_storage/function-call-11757020696500287229.json', 'var_function-call-14242122036404788287': [], 'var_function-call-7998227982978928728': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': 0, 'has_empirical': False, 'matches': []}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': 0, 'has_empirical': False, 'matches': []}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 0, 'has_empirical': True, 'matches': []}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 0, 'has_empirical': True, 'matches': []}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': 0, 'has_empirical': False, 'matches': []}], 'var_function-call-12008893059213007524': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'matches': ['2015'], 'snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'matches': [], 'snippet': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 152'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'matches': [], 'snippet': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'matches': [], 'snippet': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n E'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'matches': [], 'snippet': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent C'}]}

exec(code, env_args)
