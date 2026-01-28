code = """import json

path = var_call_3kPlYAHgnNRetHDJlTQYsmM4
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

lines = []
for r in records:
    title = r.get('title') or ''
    author = r.get('author') or ''
    name = author
    if isinstance(author, str) and author.strip().startswith('{'):
        try:
            a = json.loads(author)
            name = a.get('name') or author
        except Exception:
            name = author
    book_id = r.get('book_id') or ''
    line = title + ' - ' + str(name) + ' (' + str(book_id) + ')'
    lines.append(line)

plain = '\n'.join(lines)

print("__RESULT__:")
print(json.dumps(plain))"""

env_args = {'var_call_KQhoAonEWOKCkMYj2OyCUbt5': ['review'], 'var_call_tragOMZg8AJTGhTXctHV0zYe': 'file_storage/call_tragOMZg8AJTGhTXctHV0zYe.json', 'var_call_59E4WtqJZ7JdzL5qRsFMZLO2': ['books_info'], 'var_call_athQhDCQJCrQdVJJmLYzUisw': 'file_storage/call_athQhDCQJCrQdVJJmLYzUisw.json', 'var_call_3kPlYAHgnNRetHDJlTQYsmM4': 'file_storage/call_3kPlYAHgnNRetHDJlTQYsmM4.json'}

exec(code, env_args)
