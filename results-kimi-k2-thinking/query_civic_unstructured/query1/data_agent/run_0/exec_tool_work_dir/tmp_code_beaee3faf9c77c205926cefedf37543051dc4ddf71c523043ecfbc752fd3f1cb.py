code = """import json

# Load both data files
with open('file_storage/functions.query_db:10.json', 'r') as f1:
    funding_data = json.load(f1)
    
with open('file_storage/functions.query_db:22.json', 'r') as f2:
    civic_docs = json.load(f2)

# Get funded projects over $50,000
funded_projects = {}
for rec in funding_data:
    amount = int(rec['Amount'])
    if amount > 50000:
        funded_projects[rec['Project_Name']] = amount

# Extract design projects from civic documents
design_project_names = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    in_design_section = False
    
    for line in lines:
        stripped = line.strip()
        
        # Check for section headers
        if 'Capital Improvement Projects' in stripped:
            if 'Design' in stripped:
                in_design_section = True
            elif 'Construction' in stripped or 'Not Started' in stripped:
                in_design_section = False
        
        # Capture project names in the design section
        elif in_design_section and stripped and len(stripped) > 10:
            if stripped[0].isupper() and not stripped.isupper():
                # Skip administrative lines
                skip_keywords = ['Updates:', 'Schedule:', 'Complete Design', 'Advertise:', 'Begin Construction', 'Page', 'Agenda Item', 'To:', 'From:', 'Subject:', 'Date:', 'Prepared by:', 'RECOMMENDED ACTION', 'DISCUSSION']
                should_skip = False
                for keyword in skip_keywords:
                    if keyword in stripped:
                        should_skip = True
                        break
                
                if not should_skip:
                    design_project_names.append(stripped)

# Count matches between design projects and funded projects
match_count = 0
unique_matches = set()

for design_name in design_project_names:
    for funded_name, amount in funded_projects.items():
        # Normalize names for comparison
        norm_design = design_name.lower().replace('project', '').strip()
        norm_funded = funded_name.lower().replace('project', '').strip()
        
        if norm_design and norm_funded:
            # Check if one name contains the other
            if norm_design in norm_funded or norm_funded in norm_design:
                # Ensure significant overlap in words
                design_words = set(norm_design.split())
                funded_words = set(norm_funded.split())
                common_words = design_words.intersection(funded_words)
                
                if len(common_words) >= 2:
                    match_count += 1
                    unique_matches.add(design_name)
                    break

result = {
    'total_matches': match_count,
    'unique_design_projects': len(unique_matches)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:18': {'funding_path': 'file_storage/functions.query_db:10.json', 'civic_path': 'file_storage/functions.query_db:6.json', 'funding_path_type': "<class 'str'>", 'civic_path_type': "<class 'str'>"}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:28': {'success': False, 'error': "[Errno 2] No such file or directory: 'var_functions.query_db:10'", 'files_in_cwd': ['tmp_code_0e6c8b31743f4e63b74796337adb75429643f59e9bc4a4746f1d8c5c6f8ea588.py', 'tmp_code_36761a9b216ad7c1c219bdc570df80d3c6af9291d0c8f3f2c5b024ecccb4f1f6.py', 'tmp_code_a8cd69de2793b5278f48c54a6c713d8fc292594a17271705c2516dbb8d67110f.py', 'tmp_code_e6d42ef55378a20dc68593b0a196fd779bfa8dc69b65210bcf6e371ef7ee3032.py', 'tmp_code_c9a34119410b5bfa580e1d1498745c6d40334f57126b40b8aaec156559353aec.py', 'tmp_code_89272ecfb53013fea677551da5b184f308b84e0dbd068d8d14ec56e724312f1d.py', 'tmp_code_5d2188575c23c1ceee77ba81040fae1a0c9d68e25a5d5bf5a2aa4609c850488f.py', 'file_storage', 'tmp_code_d2dc01fc68759f46e73e17f407a52384ee2386d4a4832e59aa9eb8a31e244eac.py', 'tmp_code_b549ba7a5f4d23b2a9fc7de0724ee25342962870f6b5c3410f93206ca2a31b2b.py']}, 'var_functions.execute_python:30': {'file_storage_path': 'file_storage', 'all_files': ['functions.query_db:6.json', 'functions.query_db:5.json', 'functions.query_db:0.json', 'functions.query_db:22.json', 'functions.query_db:10.json'], 'query_db_files': ['functions.query_db:6.json', 'functions.query_db:5.json', 'functions.query_db:0.json', 'functions.query_db:22.json', 'functions.query_db:10.json'], 'current_dir': '/workspace'}, 'var_functions.execute_python:32': {'funding_count': 276, 'civic_docs_count': 5, 'sample_funding': [{'Project_Name': 'Birdview Avenue Improvements', 'Amount': '79000'}, {'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': '85000'}], 'sample_civic_doc_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}}

exec(code, env_args)
