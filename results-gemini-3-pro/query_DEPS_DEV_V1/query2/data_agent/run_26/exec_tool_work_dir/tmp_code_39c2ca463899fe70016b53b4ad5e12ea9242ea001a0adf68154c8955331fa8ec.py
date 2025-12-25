code = """import json
import re

# Get file path
file_path = locals()['var_function-call-7253653177288570155']

with open(file_path, 'r') as f:
    project_info_list = json.load(f)

project_data = []

# Regex patterns for Name
name_patterns = [
    r"The project is hosted on GitHub under the name ([^,]+),",
    r"The GitHub project named ([^ ]+) currently",
    r"The project named ([^ ]+) is hosted on GitHub",
    r"The project named ([^ ]+) on GitHub",
    r"The GitHub project ([^ ]+) currently",
    r"The project ([^ ]+) is hosted on GitHub",
    r"The project ([^ ]+) is hosted on GITHUB",
    r"The project ([^ ]+) on GitHub"
]

# Regex patterns for Forks
fork_patterns = [
    r"and ([0-9,]+) forks",
    r"forks count of ([0-9,]+)",
    r"and has been forked ([0-9,]+) times",
    r"and a forks count of ([0-9,]+)"
]

valid_projects = []

for entry in project_info_list:
    text = entry['Project_Information']
    name = None
    
    # Extract Name
    for p in name_patterns:
        m = re.search(p, text)
        if m:
            name = m.group(1).strip()
            if name.endswith(',') or name.endswith('.'):
                name = name[:-1]
            break
    
    if name:
        valid_projects.append(name)

# Create SQL query
# Limit checking: if valid_projects is empty or huge? 770 is fine.
names_str = ", ".join([f"'{n}'" for n in valid_projects])
query = f"SELECT Name, Version, ProjectName FROM project_packageversion WHERE System='NPM' AND ProjectName IN ({names_str})"

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-10352811860558582149': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-12554035315876686551': [{'column_name': 'Project_Information', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Licenses', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Homepage', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OSSFuzz', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-12554035315876685994': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}], 'var_function-call-6938159831684507998': 'file_storage/function-call-6938159831684507998.json', 'var_function-call-14508441577688866252': [{'count_star()': '597602'}], 'var_function-call-14508441577688862885': [{'count_star()': '770'}], 'var_function-call-7253653177288570155': 'file_storage/function-call-7253653177288570155.json'}

exec(code, env_args)
