code = """import json
path = var_call_3kPlYAHgnNRetHDJlTQYsmM4
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)
out = []
for r in records:
    title = r.get("title", "")
    author = r.get("author", "")
    if isinstance(author, str) and author.strip().startswith("{"):
        try:
            ad = json.loads(author)
            author = ad.get("name", author)
        except Exception:
            pass
    out.append({"title": title, "author": author, "book_id": r.get("book_id")})
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_KQhoAonEWOKCkMYj2OyCUbt5': ['review'], 'var_call_tragOMZg8AJTGhTXctHV0zYe': 'file_storage/call_tragOMZg8AJTGhTXctHV0zYe.json', 'var_call_59E4WtqJZ7JdzL5qRsFMZLO2': ['books_info'], 'var_call_athQhDCQJCrQdVJJmLYzUisw': 'file_storage/call_athQhDCQJCrQdVJJmLYzUisw.json', 'var_call_3kPlYAHgnNRetHDJlTQYsmM4': 'file_storage/call_3kPlYAHgnNRetHDJlTQYsmM4.json', 'var_call_5Qp118IKrWTngWZmkAWmDkZ4': {'count': 15}}

exec(code, env_args)
