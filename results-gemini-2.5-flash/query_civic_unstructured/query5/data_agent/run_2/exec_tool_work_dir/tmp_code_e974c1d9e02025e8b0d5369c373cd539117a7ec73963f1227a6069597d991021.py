code = """import json
import re

with open(locals()['var_function-call-13284801232826476662'], 'r') as f:
    civic_docs = json.load(f)

disaster_projects_2022 = set()

for doc in civic_docs:
    text = doc['text']

    # Find text sections that are clearly under 'Disaster Recovery Projects' heading
    # This regex attempts to capture all content after "Disaster Recovery Projects"
    # until it hits "Capital Improvement Projects" or the end of the document.
    disaster_sections = re.findall(
        r'Disaster Recovery Projects\\n\\n(.*?)(?=\\n\\nCapital Improvement Projects|\\Z)',
        text, re.DOTALL | re.IGNORECASE
    )

    for section_content in disaster_sections:
        # Now, within this disaster-specific content, find project blocks.
        # A project block starts with a name, then has "Updates", "Project Schedule", and "Begin Construction".
        # Let's try to capture the entire project block first.
        project_blocks = re.findall(
            r'([A-Za-z0-9\\s&\\-_/]+?)\\n\\n\\(cid:190\\) Updates:(.*?)\\n\\n\\(cid:190\\) Project Schedule:(.*?)(?=\\n\\n[A-Za-z0-9]|\\Z)',
            section_content, re.DOTALL
        )

        for project_name, updates, schedule_section in project_blocks:
            # Now, from the schedule_section, extract the "Begin Construction" date
            begin_construction_match = re.search(r'\\(cid:131\\) Begin Construction: (.*?)\\n', schedule_section)
            if begin_construction_match:
                begin_construction_date = begin_construction_match.group(1)
                if "2022" in begin_construction_date:
                    disaster_projects_2022.add(project_name.strip())

print("__RESULT__:")
print(json.dumps(list(disaster_projects_2022)))"""

env_args = {'var_function-call-10152952571518250078': ['civic_docs'], 'var_function-call-13284801232826476662': 'file_storage/function-call-13284801232826476662.json'}

exec(code, env_args)
