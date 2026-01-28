code = """import json

p_citations = locals()['var_function-call-1858146419099260835']
with open(p_citations, 'r') as f:
    c_data = json.load(f)

c_map = {i['title']+".txt": i['citation_count'] for i in c_data}

p_docs = locals()['var_function-call-9448533248759791427']
with open(p_docs, 'r') as f:
    docs = json.load(f)

targets = [
    "Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection.txt",
    "Sundroid: Solar Radiation Awareness with Smartphones.txt",
    "One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App.txt",
    "Technologies for Everyday Life Reflection: Illustrating a Design Space.txt"
]

info = []
for d in docs:
    if d.get('filename') in targets:
        info.append({
            "file": d.get('filename'), 
            "citation_count": c_map.get(d.get('filename')),
            "header": d.get('text', '')[:300].replace('\n', ' ')
        })

print("__RESULT__:")
print(json.dumps(info))"""

env_args = {'var_function-call-1858146419099260835': 'file_storage/function-call-1858146419099260835.json', 'var_function-call-15380122331926952136': 'file_storage/function-call-15380122331926952136.json', 'var_function-call-9448533248759791427': 'file_storage/function-call-9448533248759791427.json', 'var_function-call-4705747550331622406': 16, 'var_function-call-9421824517149908938': 0, 'var_function-call-6808858593501252295': 'Done', 'var_function-call-9927407723113699791': [{'file': 'A Lived Informatics Model of Personal Informatics.txt', 'header': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, {'file': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'header': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali'}, {'file': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'header': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n E'}, {'file': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'header': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent C'}], 'var_function-call-3578876301302370202': [], 'var_function-call-4934734277398446795': ['A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'], 'var_function-call-16858254973543001860': ' Bit  More  Interaction: \nDesigning  and  Evaluating  an  Overactive  Bladder  App.  In  2019  CHI \nConference on Human Factors in Computing Systems Proceedings (CHI 2019), \nMay 4–9, 2019, Glagsow, Scotland, UK. ACM,  NY,  NY,  USA.  Paper  703,  13 \npages. https://doi.org/10.1145/3290605.3300933 \n\n', 'var_function-call-2880461298158006079': 16}

exec(code, env_args)
