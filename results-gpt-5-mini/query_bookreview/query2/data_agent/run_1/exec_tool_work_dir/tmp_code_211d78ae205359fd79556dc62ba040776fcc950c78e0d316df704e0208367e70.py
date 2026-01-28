code = """import json

# load the merged results from previous execute_python stored under var_call_3kPlYAHgnNRetHDJlTQYsmM4
path = var_call_3kPlYAHgnNRetHDJlTQYsmM4
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

# Build a plain-text list of matching books
lines = []
for r in records:
    title = r.get('title') or ''
    author = r.get('author') or ''
    book_id = r.get('book_id') or ''
    # try to extract author name if author is a JSON string
    name = author
    try:
        if isinstance(author, str) and author.strip().startswith('{'):
            a = json.loads(author)
            name = a.get('name') or author
    except Exception:
        name = author
    lines.append(f"{title} — {name} ({book_id})")

plain = "\n".join(lines)

print("__RESULT__:")
print(json.dumps(plain))"""

env_args = {'var_call_KQhoAonEWOKCkMYj2OyCUbt5': ['review'], 'var_call_tragOMZg8AJTGhTXctHV0zYe': 'file_storage/call_tragOMZg8AJTGhTXctHV0zYe.json', 'var_call_59E4WtqJZ7JdzL5qRsFMZLO2': ['books_info'], 'var_call_athQhDCQJCrQdVJJmLYzUisw': 'file_storage/call_athQhDCQJCrQdVJJmLYzUisw.json', 'var_call_3kPlYAHgnNRetHDJlTQYsmM4': 'file_storage/call_3kPlYAHgnNRetHDJlTQYsmM4.json'}

exec(code, env_args)
