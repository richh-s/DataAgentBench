code = """import json
# Read the MongoDB data from the file
storage_key = 'var_functions.query_db:2'
file_path = locals()[storage_key]

with open(file_path, 'r') as f:
    mongo_data = json.load(f)

# Extract all titles (from filenames)
paper_titles = []
for doc in mongo_data:
    filename = doc.get('filename', '')
    if filename:
        title = filename.replace('.txt', '')
        paper_titles.append(title)

print('__RESULT__:')
print(json.dumps({
    'total_papers': len(paper_titles),
    'sample_titles': paper_titles[:10]
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'message': 'No empirical papers found after 2016', 'empirical_papers': []}, 'var_functions.execute_python:12': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'title': 'A Lived Informatics Model of Personal Informatics', 'year_matches': [], 'text_preview': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'title': 'A Stage-based Model of Personal Informatics Systems', 'year_matches': [], 'text_preview': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 152'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year_matches': [], 'text_preview': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year_matches': [], 'text_preview': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n E'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year_matches': [], 'text_preview': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent C'}], 'var_functions.execute_python:14': {'papers_after_2016': 0, 'empirical_papers_after_2016': 0, 'message': 'No papers found after 2016'}}

exec(code, env_args)
