code = """import json
import re

with open(locals()['var_function-call-9091726243115510296'], 'r') as f:
    civic_docs_data = json.load(f)

capital_design_projects_list = []

for doc in civic_docs_data:
    text = doc['text']

    design_section_pattern = 'Capital Improvement Projects \\(Design\\)(.*?)(?:\\nCapital Improvement Projects \\(Construction\\)|\\nCapital Improvement Projects \\(Not Started\\)|\\nDisaster Recovery Projects|\\Z)'
    design_section_match = re.search(design_section_pattern, text, re.DOTALL)

    if design_section_match:
        design_section_text = design_section_match.group(1)
        lines = design_section_text.split('\\n')
        for line in lines:
            cleaned_line = line.strip()

            ignore_prefixes = ('(cid:', 'Updates:', 'Project Schedule:', 'To:', 'Prepared by:', 'Approved by:', 'Date prepared:', 'Meeting date:', 'Subject:', 'RECOMMENDED ACTION:', 'DISCUSSION:', 'Page', 'Agenda Item #')

            is_project_name = True
            for prefix in ignore_prefixes:
                if cleaned_line.startswith(prefix):
                    is_project_name = False
                    break

            if cleaned_line and is_project_name:
                cid_pattern = '\\s*\\(cid:\\d{1,3}\\)'
                parenthetical_pattern = '\\s*\\([^)]*\\)$'

                cleaned_name = re.sub(cid_pattern, '', cleaned_line)
                cleaned_name = re.sub(parenthetical_pattern, '', cleaned_name).strip()

                if cleaned_name:
                    capital_design_projects_list.append(cleaned_name.lower())

print('__RESULT__:')
print(json.dumps(capital_design_projects_list))"""

env_args = {'var_function-call-2592787406404829174': 'file_storage/function-call-2592787406404829174.json', 'var_function-call-9091726243115510296': 'file_storage/function-call-9091726243115510296.json'}

exec(code, env_args)
