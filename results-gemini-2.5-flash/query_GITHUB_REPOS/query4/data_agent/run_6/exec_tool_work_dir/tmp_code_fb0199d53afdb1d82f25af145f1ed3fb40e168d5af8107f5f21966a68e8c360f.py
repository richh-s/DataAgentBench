code = """import json
import pandas as pd

with open(locals()['var_function-call-1281801381042599030'], 'r') as f:
    languages_data = json.load(f)

df_languages = pd.DataFrame(languages_data)

def get_main_language(description):
    if not isinstance(description, str):
        return None
    
    parts = description.split(',')
    
    main_language = None
    max_bytes = -1

    if "The codebase includes:" in description:
        language_string = description.replace("The codebase includes:", "").replace(".", "").strip()
        parts = language_string.split(", ")
    elif "This repository is mainly written in" in description:
        language_string = description.replace("This repository is mainly written in", "").split(", with additional code in")[0].replace(".", "").strip()
        parts = [language_string]
    elif "The majority of the code is in" in description:
        language_string = description.replace("The majority of the code is in", "").split(", followed by")[0].replace(".", "").strip()
        parts = [language_string]
    elif "While most of the project is built in" in description:
        language_string = description.replace("While most of the project is built in", "").split(", it also incorporates")[0].replace(".", "").strip()
        parts = [language_string]
    elif "This repository is mainly written in" in description:
        language_string = description.replace("This repository is mainly written in", "").split(", with additional")[0].replace(".", "").strip()
        parts = [language_string]
    elif "The codebase includes:" in description:
        language_string = description.replace("The codebase includes:", "").replace(".", "").strip()
        parts = language_string.split(", ")
    else:
        parts = description.replace(".", "").strip().split(", ")


    for part in parts:
        if '(' in part and 'bytes)' in part:
            lang_name = part.split('(')[0].strip()
            try:
                bytes_str = part.split('(')[1].replace('bytes)', '').strip().replace(',', '')
                bytes_count = int(bytes_str)
                if bytes_count > max_bytes:
                    max_bytes = bytes_count
                    main_language = lang_name
            except ValueError:
                continue
        elif "The codebase includes: " in description and "bytes" in description:
            try:
                # Handle cases like "The codebase includes: Ruby (22,438 bytes), Shell (465 bytes)."
                languages_info = description.replace("The codebase includes: ", "").replace(".", "").strip()
                lang_parts = languages_info.split(', ')
                for lp in lang_parts:
                    if '(' in lp and 'bytes)' in lp:
                        lang = lp.split('(')[0].strip()
                        byte_count = int(lp.split('(')[1].replace('bytes)', '').replace(',', '').strip())
                        if byte_count > max_bytes:
                            max_bytes = byte_count
                            main_language = lang
            except:
                continue
        elif "This repository is mainly written in " in description and "bytes" in description:
            try:
                lang_info = description.replace("This repository is mainly written in ", "").split(", with additional code in")[0].replace(".", "").strip()
                lang = lang_info.split('(')[0].strip()
                byte_count = int(lang_info.split('(')[1].replace('bytes)', '').replace(',', '').strip())
                if byte_count > max_bytes:
                    max_bytes = byte_count
                    main_language = lang
            except:
                continue
        elif "The majority of the code is in " in description and "bytes" in description:
            try:
                lang_info = description.replace("The majority of the code is in ", "").split(", followed by")[0].replace(".", "").strip()
                lang = lang_info.split('(')[0].strip()
                byte_count = int(lang_info.split('(')[1].replace('bytes)', '').replace(',', '').strip())
                if byte_count > max_bytes:
                    max_bytes = byte_count
                    main_language = lang
            except:
                continue
        elif "While most of the project is built in " in description and "bytes" in description:
            try:
                lang_info = description.replace("While most of the project is built in ", "").split(", it also incorporates")[0].replace(".", "").strip()
                lang = lang_info.split('(')[0].strip()
                byte_count = int(lang_info.split('(')[1].replace('bytes)', '').replace(',', '').strip())
                if byte_count > max_bytes:
                    max_bytes = byte_count
                    main_language = lang
            except:
                continue
    return main_language

df_languages['main_language'] = df_languages['language_description'].apply(get_main_language)
non_python_repos = df_languages[df_languages['main_language'] != 'Python']
result = non_python_repos[['repo_name', 'main_language']].to_json(orient='records')
print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-7050816334451560915': [{'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_function-call-1281801381042599030': 'file_storage/function-call-1281801381042599030.json'}

exec(code, env_args)
