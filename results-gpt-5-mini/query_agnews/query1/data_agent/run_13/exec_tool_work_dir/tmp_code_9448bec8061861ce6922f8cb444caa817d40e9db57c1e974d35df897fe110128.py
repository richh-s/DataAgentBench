code = """import json, re
# Load the Mongo query result from storage path
path = var_call_0ttM0C5iS3mmZrYKjXxw8Y2d
with open(path, 'r', encoding='utf-8') as f:
    articles = json.load(f)

# Define sports-related keywords (lowercase)
sports_keywords = [
    'football','soccer','basketball','baseball','tennis','cricket','rugby','golf','hockey',
    'olympic','olympics','coach','manager','goal','score','match','tournament','innings',
    'pitcher','quarterback','touchdown','foul','league','season','club','win','defeat',
    'defeated','beat','draw','sprint','race','athlete','players','team','teams','mlb','nba',
    'nfl','nhl','world cup','worldcup','boxing','mma','wrestling','skating','ski','cycling',
    'matchday','fixture','goalkeeper'
]

def is_sports_article(title, description):
    text = (title or '') + ' ' + (description or '')
    text = text.lower()
    for kw in sports_keywords:
        if kw in text:
            return True
    return False

max_len = -1
max_article = None
for art in articles:
    title = art.get('title')
    desc = art.get('description') or ''
    if is_sports_article(title, desc):
        l = len(desc)
        if l > max_len:
            max_len = l
            max_article = {'article_id': art.get('article_id'), 'title': title, 'description_length': l}

# If none found by keyword, try a looser heuristic: look for articles with short titles like those known to be sports
if max_article is None:
    # fallback: check for words 'wins' 'lost' and sports-like manual
    fallback_keywords = ['wins','lost','win','draws','beats','beat','defeats','defeat']
    for art in articles:
        title = art.get('title')
        desc = art.get('description') or ''
        text = ((title or '') + ' ' + desc).lower()
        if any(k in text for k in fallback_keywords):
            l = len(desc)
            if l > max_len:
                max_len = l
                max_article = {'article_id': art.get('article_id'), 'title': title, 'description_length': l}

# Prepare result
if max_article is None:
    result = {'title': None, 'article_id': None, 'description_length': None}
else:
    result = max_article

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_0ttM0C5iS3mmZrYKjXxw8Y2d': 'file_storage/call_0ttM0C5iS3mmZrYKjXxw8Y2d.json'}

exec(code, env_args)
