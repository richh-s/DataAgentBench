code = """import json
import re

# Read the papers from the file
file_path = "file_storage/functions.query_db:16.json"
with open(file_path, 'r') as f:
    papers = json.load(f)

# Let's extract publication year and title for physical activity papers
physical_activity_papers = []

for paper in papers:
    filename = paper['filename']
    text = paper['text']
    
    # Extract title from filename
    title = filename.replace('.txt', '')
    
    # Try to extract year from the text
    # Look for patterns like YYYY, e.g., 2015, 2016, etc.
    year_match = re.search(r'\b(20\d{2})\b', text)
    year = int(year_match.group(1)) if year_match else None
    
    # Check if physical activity domain
    # Lowercase the text and check for 'physical activity'
    is_physical_activity = 'physical activity' in text.lower()
    
    physical_activity_papers.append({
        'title': title,
        'year': year,
        'is_physical_activity': is_physical_activity,
        'filename': filename
    })

# Filter for 2016 papers in physical activity domain
papers_2016 = [p for p in physical_activity_papers if p['year'] == 2016 and p['is_physical_activity']]

print("__RESULT__:")
print(json.dumps({
    "all_physical_activity_papers": physical_activity_papers,
    "papers_2016": papers_2016,
    "total_2016_papers": len(papers_2016)
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.execute_python:10': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5', 'var_functions.list_db:6', '__builtins__', 'json'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:22': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5', 'var_functions.list_db:6', 'var_functions.execute_python:10', 'var_functions.query_db:12', 'var_functions.query_db:14', 'var_functions.query_db:16'], 'var_functions.execute_python:28': {'paper_count': 5, 'first_papers': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'text_preview': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu..."}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'text_preview': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 152...'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'text_preview': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali...'}]}}

exec(code, env_args)
