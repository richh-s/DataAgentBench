code = """import json
import re

file_path = locals()['var_function-call-2666164887420722559']
with open(file_path, 'r') as f:
    papers = json.load(f)

relevant_data = []

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check for "empirical"
    if 'empirical' not in text.lower():
        continue

    # Extract Year
    # Try 4 digit year first
    years = re.findall(r'(20\d{2})', text[:3000])
    
    pub_year = 0
    if years:
        valid_years = [int(y) for y in years if 2000 <= int(y) <= 2025]
        if valid_years:
            # Heuristic: the first year mentioned is often the publication year
            # But sometimes it's "Since 2000..."
            # Conference headers usually come first.
            pub_year = valid_years[0]
            
            # Refinement: if there are multiple, maybe take the max if it's in the first few lines?
            # Or assume the first valid year in the header is correct.
            # Let's stick with the first one for now.
    
    # If no 4-digit year, try 'YY
    if pub_year == 0:
        short_years = re.findall(r"'\s*(\d{2})", text[:500])
        if short_years:
            vy = [int(y) + 2000 for y in short_years if 0 <= int(y) <= 25]
            if vy:
                pub_year = vy[0]

    if pub_year > 2016:
        relevant_data.append({"title": title, "year": pub_year})

print("__RESULT__:")
print(json.dumps(relevant_data))"""

env_args = {'var_function-call-12623071366451944695': 'file_storage/function-call-12623071366451944695.json', 'var_function-call-15611850361610481914': 'file_storage/function-call-15611850361610481914.json', 'var_function-call-2666164887420722559': 'file_storage/function-call-2666164887420722559.json', 'var_function-call-8989207208311259725': [], 'var_function-call-2743684327113960074': [{'title': 'A Lived Informatics Model of Personal Informatics', 'has_empirical': False, 'years_found': [], 'first_year': None, 'snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'has_empirical': False, 'years_found': [], 'first_year': None, 'snippet': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 152'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'has_empirical': True, 'years_found': [], 'first_year': None, 'snippet': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'has_empirical': True, 'years_found': [], 'first_year': None, 'snippet': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n E'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'has_empirical': False, 'years_found': [], 'first_year': None, 'snippet': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent C'}]}

exec(code, env_args)
