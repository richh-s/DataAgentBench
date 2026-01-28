code = """import json
import os

# Check what files are in /tmp
print('Files in /tmp:')
for f in os.listdir('/tmp'):
    if f.endswith('.json'):
        print(f)

# Try to read the latest files
latest_files = []
for f in sorted(os.listdir('/tmp')):
    if f.endswith('.json'):
        latest_files.append(f)

print('\nLatest files:', latest_files)

# Read the most recent files if they exist
if latest_files:
    # Sort by modification time
    files_with_time = []
    for f in latest_files:
        path = f'/tmp/{f}'
        files_with_time.append((path, os.path.getmtime(path)))
    files_with_time.sort(key=lambda x: x[1], reverse=True)
    
    print('\nFiles by modification time:')
    for path, mtime in files_with_time:
        print(path, mtime)
        
    # Try to read the two most recent files
    if len(files_with_time) >= 2:
        with open(files_with_time[0][0], 'r') as f:
            data1 = json.load(f)
            print(f'\nFirst file type: {type(data1)}, length: {len(data1) if hasattr(data1, "__len__") else "N/A"}')
            
        with open(files_with_time[1][0], 'r') as f:
            data2 = json.load(f)
            print(f'Second file type: {type(data2)}, length: {len(data2) if hasattr(data2, "__len__") else "N/A"}')"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}]}

exec(code, env_args)
