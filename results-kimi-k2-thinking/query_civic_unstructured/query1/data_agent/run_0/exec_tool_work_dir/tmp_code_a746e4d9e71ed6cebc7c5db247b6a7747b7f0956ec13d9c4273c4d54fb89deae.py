code = """import json
import re
from collections import defaultdict

# Load data
with open('file_storage/functions.query_db:10.json', 'r') as f:
    funding_data = json.load(f)

with open('file_storage/functions.query_db:22.json', 'r') as f:
    civic_docs = json.load(f)

# Step 1: Extract project information from civic documents
projects_by_name = defaultdict(dict)

# Patterns to identify capital projects in design status
design_project_keywords = [
    'Complete Design:',
    'Staff is working with the consultant',
    'Plans are under review',
    'working with consultant',
    'Final Design:'
]

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    in_design_section = False
    capture_next = False
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Check if we're entering the Design section
        if 'Capital Improvement Projects (Design)' in line:
            in_design_section = True
            continue
        
        # Exit design section when we hit other sections
        if in_design_section and ('Capital Improvement Projects (Construction)' in line or 
                                  'Capital Improvement Projects (Not Started)' in line):
            in_design_section = False
            continue
        
        if in_design_section and line and not line.startswith('(') and 'cid:' not in line:
            # Check if this line mentions a project name
            # Project names appear alone on lines in these documents
            if (len(line) > 10 and 
                not any(keyword in line for keyword in ['Updates:', 'Schedule:', 'Complete Design:', 
                                                       'Advertise:', 'Begin Construction:', 'Project ',
                                                       'Page ', 'Agenda Item', 'To:', 'From:', 'Date:',
                                                       'Subject:', 'RECOMMENDED ACTION:', 'DISCUSSION:']) and 
                not line.isupper() and
                (line[0].isdigit() or line[0].isupper() or '&' in line)):
                
                # This looks like a project name
                project_name = line.strip()
                if len(project_name) > 5:
                    # Store the project with design status
                    projects_by_name[project_name] = {
                        'name': project_name,
                        'status': 'design',
                        'type': 'capital',
                        'document': doc['filename']
                    }

# Step 2: Process funding data - filter for > $50,000
funded_projects = {}
for fund in funding_data:
    amount = int(fund['Amount'])
    if amount > 50000:
        project_name = fund['Project_Name']
        funded_projects[project_name] = amount

# Step 3: Match projects with funding
matched_projects = []

for project_name, project_info in projects_by_name.items():
    # Exact match
    if project_name in funded_projects:
        matched_projects.append({
            'project_name': project_name,
            'amount': funded_projects[project_name],
            'status': project_info['status']
        })
    else:
        # Check for partial matches and variations
        for funded_name, amount in funded_projects.items():
            # Normalize names for comparison
            norm_project = project_name.lower().replace('project', '').strip()
            norm_funded = funded_name.lower().replace('project', '').strip()
            
            # Check if one contains the other
            if norm_project in norm_funded or norm_funded in norm_project:
                # Additional check: they should share significant words
                project_words = set(norm_project.split())
                funded_words = set(norm_funded.split())
                
                # Check for overlap
                common_words = project_words.intersection(funded_words)
                if len(common_words) >= 2:  # At least 2 common words
                    matched_projects.append({
                        'project_name': project_name,
                        'funded_name': funded_name,
                        'amount': amount,
                        'status': 'design'
                    })

final_count = len(matched_projects)

# Print results
message = f"Found {final_count} capital projects with 'design' status and funding > $50,000"

# Create detailed results
detail_str = message + "\\n"
if matched_projects:
    detail_str += "\\nMatching projects:\\n"
    for proj in matched_projects:
        fund_name = proj.get('funded_name', proj['project_name'])
        detail_str += f"- {proj['project_name']}: ${proj['amount']:,}\\n"
detail_str = detail_str.strip()

print('__RESULT__:')
print(json.dumps({
    'count': final_count,
    'detailed': detail_str,
    'summary': message
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:18': {'funding_path': 'file_storage/functions.query_db:10.json', 'civic_path': 'file_storage/functions.query_db:6.json', 'funding_path_type': "<class 'str'>", 'civic_path_type': "<class 'str'>"}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:28': {'success': False, 'error': "[Errno 2] No such file or directory: 'var_functions.query_db:10'", 'files_in_cwd': ['tmp_code_0e6c8b31743f4e63b74796337adb75429643f59e9bc4a4746f1d8c5c6f8ea588.py', 'tmp_code_36761a9b216ad7c1c219bdc570df80d3c6af9291d0c8f3f2c5b024ecccb4f1f6.py', 'tmp_code_a8cd69de2793b5278f48c54a6c713d8fc292594a17271705c2516dbb8d67110f.py', 'tmp_code_e6d42ef55378a20dc68593b0a196fd779bfa8dc69b65210bcf6e371ef7ee3032.py', 'tmp_code_c9a34119410b5bfa580e1d1498745c6d40334f57126b40b8aaec156559353aec.py', 'tmp_code_89272ecfb53013fea677551da5b184f308b84e0dbd068d8d14ec56e724312f1d.py', 'tmp_code_5d2188575c23c1ceee77ba81040fae1a0c9d68e25a5d5bf5a2aa4609c850488f.py', 'file_storage', 'tmp_code_d2dc01fc68759f46e73e17f407a52384ee2386d4a4832e59aa9eb8a31e244eac.py', 'tmp_code_b549ba7a5f4d23b2a9fc7de0724ee25342962870f6b5c3410f93206ca2a31b2b.py']}, 'var_functions.execute_python:30': {'file_storage_path': 'file_storage', 'all_files': ['functions.query_db:6.json', 'functions.query_db:5.json', 'functions.query_db:0.json', 'functions.query_db:22.json', 'functions.query_db:10.json'], 'query_db_files': ['functions.query_db:6.json', 'functions.query_db:5.json', 'functions.query_db:0.json', 'functions.query_db:22.json', 'functions.query_db:10.json'], 'current_dir': '/workspace'}, 'var_functions.execute_python:32': {'funding_count': 276, 'civic_docs_count': 5, 'sample_funding': [{'Project_Name': 'Birdview Avenue Improvements', 'Amount': '79000'}, {'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': '85000'}], 'sample_civic_doc_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}}

exec(code, env_args)
