code = """import json
import re

p_citations = locals()['var_function-call-1858146419099260835']
with open(p_citations, 'r') as f:
    c_data = json.load(f)

c_map = {}
for i in c_data:
    try:
        val = int(i['citation_count'])
    except:
        val = 0
    c_map[i['title'] + ".txt"] = val

p_docs = locals()['var_function-call-9448533248759791427']
with open(p_docs, 'r') as f:
    docs = json.load(f)

total_citations = 0
chi_papers = []

for d in docs:
    fname = d.get('filename')
    if fname in c_map:
        txt = d.get('text', '')
        # Check first 3000 chars
        head = txt[:3000]
        
        is_chi = False
        # Look for CHI keyword in a venue context
        if "Conference on Human Factors in Computing Systems" in head:
            is_chi = True
        elif re.search(r"\bCHI\s+(?:20\d{2}|'?[0-9]{2})", head): # CHI 2019, CHI '19
             is_chi = True
        elif re.search(r"\bCHI\s+Conference", head):
             is_chi = True
        elif "CHI '15" in head or "CHI '16" in head or "CHI '17" in head or "CHI '18" in head or "CHI '19" in head or "CHI '20" in head:
             is_chi = True
        elif "Proceedings of the CHI" in head:
             is_chi = True

        # Also generic check for "CHI" if it looks like a header
        # But let's trust the patterns above first.
        
        # If still not found, check for the specific phrase "In 20xx CHI"
        if not is_chi:
             if re.search(r"In\s+20\d{2}\s+CHI", head):
                 is_chi = True

        if is_chi:
            total_citations += c_map[fname]
            chi_papers.append(fname)

print(f"CHI papers found: {len(chi_papers)}")
print(f"Total citations: {total_citations}")
# print(f"List: {chi_papers}")

print("__RESULT__:")
print(json.dumps(total_citations))"""

env_args = {'var_function-call-1858146419099260835': 'file_storage/function-call-1858146419099260835.json', 'var_function-call-15380122331926952136': 'file_storage/function-call-15380122331926952136.json', 'var_function-call-9448533248759791427': 'file_storage/function-call-9448533248759791427.json', 'var_function-call-4705747550331622406': 16, 'var_function-call-9421824517149908938': 0, 'var_function-call-6808858593501252295': 'Done', 'var_function-call-9927407723113699791': [{'file': 'A Lived Informatics Model of Personal Informatics.txt', 'header': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, {'file': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'header': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali'}, {'file': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'header': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n E'}, {'file': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'header': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent C'}], 'var_function-call-3578876301302370202': [], 'var_function-call-4934734277398446795': ['A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'], 'var_function-call-16858254973543001860': ' Bit  More  Interaction: \nDesigning  and  Evaluating  an  Overactive  Bladder  App.  In  2019  CHI \nConference on Human Factors in Computing Systems Proceedings (CHI 2019), \nMay 4–9, 2019, Glagsow, Scotland, UK. ACM,  NY,  NY,  USA.  Paper  703,  13 \npages. https://doi.org/10.1145/3290605.3300933 \n\n'}

exec(code, env_args)
