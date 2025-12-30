code = """import json; import re; import pandas as pd; funding_data = json.load(open('var_function-call-7750960758477245626.json')); df_funding = pd.DataFrame(funding_data); df_funding['Base_Name'] = df_funding['Project_Name'].apply(lambda x: re.sub(r'\s*\((?:FEMA|CalOES|CalJPIA|FEMA/CalOES).*?\)$', '', re.sub(r'\s*\((?:FEMA|CalOES)\)$', '', x)).strip()); civic_docs = json.load(open('var_function-call-3106554336237263291.json')); extracted_projects = []; keywords_list = ["park", "road", "FEMA", "fire", "emergency", "warning", "drainage", "storm drain", "highway", "bridge", "playground", "water treatment", "guardrail"]; 
for doc in civic_docs:
    text = doc['text'].replace('\r\n', '\n'); 
    sections = re.split(r'(Capital Improvement Projects \((?:Design|Construction|Not Started)\))', text); 
    current_status = 'unknown'; 
    for i in range(len(sections)):
        part = sections[i].strip(); 
        if not part: continue; 
        if 'Capital Improvement Projects' in part:
            if '(Design)' in part: current_status = 'design'; 
            elif '(Construction)' in part: current_status = 'construction'; 
            elif '(Not Started)' in part: current_status = 'not started'; 
        else:
            sub_blocks = re.split(r'\n(?=[^\n]+\n\(cid:190\))', part); 
            for block in sub_blocks:
                block = block.strip(); 
                if not block: continue; 
                lines = block.split('\n'); 
                if len(lines) > 1 and '(cid:190)' in lines[1]:
                    raw_name = lines[0].strip(); 
                    project_name = re.sub(r'\s*\((?:FEMA|CalOES|CalJPIA|FEMA/CalOES).*?\)$', '', re.sub(r'\s*\((?:FEMA|CalOES)\)$', '', raw_name)).strip(); 
                    project_text = block; 
                    status = current_status; 
                    if status == 'construction' and ('Construction was completed' in project_text or 'Notice of completion' in project_text): status = 'completed'; 
                    topics = []; 
                    search_text = (raw_name + ' ' + project_text).lower(); 
                    for kw in keywords_list:
                        if kw.lower() in search_text: topics.append(kw); 
                    if 'emergency warning' in search_text: topics.append('emergency'); 
                    extracted_projects.append({'Base_Name': project_name, 'status': status, 'topics': topics, 'full_text': project_text}); 

df_extracted = pd.DataFrame(extracted_projects); 
merged = pd.merge(df_funding, df_extracted, on='Base_Name', how='inner'); 
filtered = merged[merged.apply(lambda row: 'emergency' in (str(row['Project_Name']) + ' ' + str(row['full_text']) + ' ' + str(row['topics'])).lower() or 'fema' in (str(row['Project_Name']) + ' ' + str(row['full_text']) + ' ' + str(row['topics'])).lower(), axis=1)].copy(); 
result = filtered[['Project_Name', 'Funding_Source', 'Amount', 'status']].drop_duplicates(); 
print('__RESULT__:'); 
print(result.to_json(orient='records'));"""

env_args = {'var_function-call-10239882962867119811': ['civic_docs'], 'var_function-call-10239882962867121006': ['Funding'], 'var_function-call-7750960758477245626': 'file_storage/function-call-7750960758477245626.json', 'var_function-call-7750960758477242945': 'file_storage/function-call-7750960758477242945.json', 'var_function-call-3106554336237263291': 'file_storage/function-call-3106554336237263291.json'}

exec(code, env_args)
