code = """import json
import re

# Load citations
citations_path = locals()['var_function-call-1858146419099260835']
with open(citations_path, 'r') as f:
    citations_data = json.load(f)

citation_map = {}
for item in citations_data:
    try:
        count = int(item['citation_count'])
    except:
        count = 0
    citation_map[item['title'] + ".txt"] = count

# Load docs (larger set)
docs_path = locals()['var_function-call-16064497295021860140']
with open(docs_path, 'r') as f:
    docs = json.load(f)

total_citations = 0
found_chi_papers = []

for d in docs:
    fname = d.get('filename')
    if fname in citation_map:
        text = d.get('text', '')
        # Check first 4000 chars (generous header/intro)
        header = text[:4000]
        
        is_chi = False
        
        # Regex for CHI Venue
        # Matches: "CHI '15", "CHI 2015", "CHI 15"
        if re.search(r"CHI\s*['\u2019]?\s*\d{2,4}", header):
            is_chi = True
        # Matches: "CHI Conference"
        elif "CHI Conference" in header:
            is_chi = True
        # Matches: "Conference on Human Factors in Computing Systems"
        elif "Conference on Human Factors in Computing Systems" in header:
            is_chi = True
        elif "Proceedings of the CHI" in header:
             is_chi = True
        # Matches: "In 20xx CHI"
        elif re.search(r"In\s+20\d{2}\s+CHI", header):
             is_chi = True

        if is_chi:
            total_citations += citation_map[fname]
            found_chi_papers.append(fname)

print(f"Total docs processed: {len(docs)}")
print(f"CHI papers found: {len(found_chi_papers)}")
print(f"Total citations: {total_citations}")

print("__RESULT__:")
print(json.dumps(total_citations))"""

env_args = {'var_function-call-1858146419099260835': 'file_storage/function-call-1858146419099260835.json', 'var_function-call-15380122331926952136': 'file_storage/function-call-15380122331926952136.json', 'var_function-call-9448533248759791427': 'file_storage/function-call-9448533248759791427.json', 'var_function-call-4705747550331622406': 16, 'var_function-call-9421824517149908938': 0, 'var_function-call-6808858593501252295': 'Done', 'var_function-call-9927407723113699791': [{'file': 'A Lived Informatics Model of Personal Informatics.txt', 'header': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, {'file': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'header': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali'}, {'file': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'header': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n E'}, {'file': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'header': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent C'}], 'var_function-call-3578876301302370202': [], 'var_function-call-4934734277398446795': ['A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'], 'var_function-call-16858254973543001860': ' Bit  More  Interaction: \nDesigning  and  Evaluating  an  Overactive  Bladder  App.  In  2019  CHI \nConference on Human Factors in Computing Systems Proceedings (CHI 2019), \nMay 4–9, 2019, Glagsow, Scotland, UK. ACM,  NY,  NY,  USA.  Paper  703,  13 \npages. https://doi.org/10.1145/3290605.3300933 \n\n', 'var_function-call-2880461298158006079': 16, 'var_function-call-2164503375321454265': {'found': False, 'has_CHI': False, 'header_repr': "''"}, 'var_function-call-18222995155211115984': 5, 'var_function-call-16064497295021860140': 'file_storage/function-call-16064497295021860140.json'}

exec(code, env_args)
