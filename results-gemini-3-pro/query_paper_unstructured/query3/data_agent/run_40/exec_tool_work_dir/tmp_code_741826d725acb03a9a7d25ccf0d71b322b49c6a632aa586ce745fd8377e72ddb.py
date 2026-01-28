code = """import json
import re

try:
    with open(locals()['var_function-call-1634184987777097794'], 'r') as f:
        papers = json.load(f)
except:
    papers = []

target_titles = [
    "A Trip to the Moon: Personalized Animated Movies for Self-reflection",
    "A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App"
]

results = []

for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    if title in target_titles:
        text = paper.get('text', '')
        header = text[:3000]
        
        # Check year
        # Look for 2017, 2018, 2019, 2020
        years_found = re.findall(r'\\b(20[12]\d)\\b', header) # double escape
        
        # Check empirical context
        empirical_snippets = []
        if 'empirical' in text.lower():
            # Find snippet
            start = text.lower().find('empirical')
            snippet = text[max(0, start-50):min(len(text), start+50)]
            empirical_snippets.append(snippet)
            
        results.append({
            "title": title,
            "years_found": years_found,
            "empirical_snippets": empirical_snippets
        })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-4642845267965044101': ['paper_docs'], 'var_function-call-4642845267965042778': ['Citations', 'sqlite_sequence'], 'var_function-call-10467492128798022417': 'file_storage/function-call-10467492128798022417.json', 'var_function-call-1634184987777097794': 'file_storage/function-call-1634184987777097794.json', 'var_function-call-15997797269268972557': [], 'var_function-call-522812283828333894': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'extracted_year': None, 'is_empirical': False, 'header_snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'extracted_year': None, 'is_empirical': False, 'header_snippet': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 152'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'extracted_year': None, 'is_empirical': True, 'header_snippet': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'extracted_year': None, 'is_empirical': True, 'header_snippet': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n E'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'extracted_year': None, 'is_empirical': False, 'header_snippet': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent C'}], 'var_function-call-15561754651165461796': [], 'var_function-call-8038698640758462911': [{'f': 'A Lived Informatics Model of Personal Informatics.txt', 'y': None, 'e': False}, {'f': 'A Stage-based Model of Personal Informatics Systems.txt', 'y': None, 'e': False}, {'f': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'y': None, 'e': True}, {'f': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'y': None, 'e': True}, {'f': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'y': None, 'e': False}], 'var_function-call-11092515636358978544': ['A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App'], 'var_function-call-13925456837867710756': {'years': {'2015': 1, '2019': 1}, 'empirical_post_2016': {'2019': 1}}, 'var_function-call-11564220098487036742': 5, 'var_function-call-13921809749139743357': [{'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'header': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 15213 \nianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu \n\nABSTRACT \nPeople  strive  to  obtain  self-knowled'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'header': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard Unive'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'header': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent Crocher1,3, Frank Vetere1, Suranga Nanayakkara1,4 \n1Microsoft Research Centre for SocialNUI, The Univ'}], 'var_function-call-10683000147777628174': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation'], 'var_function-call-15854104752803541816': [{'title': 'A Lived Informatics Model of Personal Informatics', 'first_citation': '2016', 'total_citations': '390'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'first_citation': '2011', 'total_citations': '220'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'first_citation': '2019', 'total_citations': '265'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'first_citation': '2020', 'total_citations': '266'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'first_citation': '2017', 'total_citations': '452'}]}

exec(code, env_args)
