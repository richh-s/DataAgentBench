code = """import json
import re

# Read the papers from the file
file_path = "file_storage/functions.query_db:16.json"
with open(file_path, 'r') as f:
    papers = json.load(f)

# Let's extract year more carefully by looking for venue information
for i, paper in enumerate(papers[:3]):
    text = paper['text']
    # Look for year patterns more carefully
    year_matches = re.findall(r'\b(20\d{2})\b', text)
    # Fix the regex pattern
    venue_pattern = r"(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s*['\"]*\s*(\d{4})"
    venue_matches = re.findall(venue_pattern, text)
    
    print("__RESULT__:")
    print(f"Paper {i+1}: {paper['filename']}")
    print(f"Year matches: {year_matches}")
    print(f"Venue matches: {venue_matches}")
    print(f"Text preview first line: {text.split()[0]}")"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.execute_python:10': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5', 'var_functions.list_db:6', '__builtins__', 'json'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:22': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5', 'var_functions.list_db:6', 'var_functions.execute_python:10', 'var_functions.query_db:12', 'var_functions.query_db:14', 'var_functions.query_db:16'], 'var_functions.execute_python:28': {'paper_count': 5, 'first_papers': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'text_preview': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu..."}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'text_preview': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 152...'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'text_preview': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali...'}]}, 'var_functions.execute_python:30': {'all_physical_activity_papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'is_physical_activity': True, 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'is_physical_activity': True, 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'is_physical_activity': True, 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'is_physical_activity': True, 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'title': 'Barriers to Engagement with a Personal Informatics Productivity Tool', 'year': None, 'is_physical_activity': True, 'filename': 'Barriers to Engagement with a Personal Informatics Productivity Tool.txt'}], 'papers_2016': [], 'total_2016_papers': 0}}

exec(code, env_args)
