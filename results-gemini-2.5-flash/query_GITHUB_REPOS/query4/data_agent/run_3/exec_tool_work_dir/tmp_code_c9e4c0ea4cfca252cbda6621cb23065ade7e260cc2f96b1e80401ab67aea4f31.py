code = """import json
import pandas as pd

with open(locals()['var_function-call-6648005358843189280'], 'r') as f:
    languages_data = json.load(f)

df_languages = pd.DataFrame(languages_data)

def get_main_language(description):
    if not isinstance(description, str):
        return None
    
    parts = description.split(',')
    main_language_part = parts[0]
    
    if "mainly written in " in main_language_part:
        language = main_language_part.split("mainly written in ")[1].split(' ')[0].strip()
    elif "The majority of the code is in " in main_language_part:
        language = main_language_part.split("The majority of the code is in ")[1].split(' ')[0].strip()
    elif "The codebase includes: " in main_language_part:
        # For this case, we need to find the language with the most bytes.
        # This is more complex, so let's try to parse it.
        # Example: "The codebase includes: Ruby (22,438 bytes), Shell (465 bytes)."
        # We need to extract language and bytes, then find the max.
        
        language_bytes_str = main_language_part.split("The codebase includes: ")[1]
        language_bytes_pairs = []
        
        # Split by comma and process each part
        for lb_pair in language_bytes_str.split(','):
            # Find the language name before the first parenthesis and the bytes inside.
            import re
            match = re.search(r'([A-Za-z]+)\s+\(([0-9,]+)\s+bytes\)', lb_pair)
            if match:
                language_name = match.group(1).strip()
                bytes_count = int(match.group(2).replace(',', ''))
                language_bytes_pairs.append((language_name, bytes_count))
        
        if language_bytes_pairs:
            main_lang_info = max(language_bytes_pairs, key=lambda item: item[1])
            language = main_lang_info[0]
        else:
            language = None # Fallback if parsing fails
            
    elif "While most of the project is built in " in main_language_part:
        language = main_language_part.split("While most of the project is built in ")[1].split(' ')[0].strip()
    else:
        language = None # Fallback for other formats
    
    return language

df_languages['main_language'] = df_languages['language_description'].apply(get_main_language)

non_python_repos = df_languages[df_languages['main_language'] != 'Python']
result = non_python_repos[['repo_name', 'main_language']].to_json(orient='records')

print("__RESULT__:")
print(result)"""

env_args = {'var_function-call-6648005358843189280': 'file_storage/function-call-6648005358843189280.json'}

exec(code, env_args)
