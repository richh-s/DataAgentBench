code = """import json
import re

# Load metadata
with open(locals()['var_function-call-6674564950342530332'], 'r') as f:
    meta_list = json.load(f)

# Map article_id to year. Handle potential string/int types.
# Metadata article_id might be int or string.
# Mongo article_id is string.
id_to_year = {}
for item in meta_list:
    aid = str(item['article_id'])
    year = int(item['year'])
    id_to_year[aid] = year

# Load articles
with open(locals()['var_function-call-2777792020398673535'], 'r') as f:
    articles = json.load(f)

# Categories keywords
categories = {
    "Business": ["business", "economy", "market", "stock", "trade", "finance", "financial", "bank", "fund", "invest", "money", "dollar", "euro", "currency", "oil", "price", "profit", "revenue", "sale", "deal", "merger", "acquisition", "company", "corp", "inc", "ceo", "share", "wall st", "nasdaq", "dow jones", "inflation", "rate", "jobs", "hiring", "unemployment", "fed", "central bank", "debt", "bond", "futures", "commodity", "gold", "sector", "growth", "earnings", "quarter", "forecast", "recession"],
    "Sports": ["sport", "football", "soccer", "basketball", "baseball", "hockey", "tennis", "golf", "game", "match", "team", "player", "coach", "score", "win", "lose", "victory", "defeat", "cup", "league", "championship", "medal", "olympic", "athlete", "race", "tournament", "stadium", "club"],
    "SciTech": ["science", "technology", "tech", "computer", "software", "hardware", "internet", "web", "online", "digital", "phone", "mobile", "space", "nasa", "biology", "physics", "chemistry", "research", "study", "microsoft", "apple", "google", "intel", "linux", "virus", "hacker", "network", "server", "data", "robot", "gadget", "device"],
    "World": ["world", "war", "peace", "conflict", "military", "army", "government", "politics", "election", "president", "minister", "prime minister", "official", "united nations", "un", "iraq", "iran", "china", "usa", "uk", "eu", "police", "attack", "bomb", "terror", "killed", "died", "court", "law", "treaty", "nuclear", "protest", "vote", "senate", "congress", "parliament"]
}

def classify(title, desc):
    text = (title + " " + desc).lower()
    scores = {cat: 0 for cat in categories}
    for cat, keywords in categories.items():
        for kw in keywords:
            # Simple substring check or word boundary? Substring is easier but might have false positives.
            # Use regex for word boundary for better accuracy.
            if re.search(r'\b' + re.escape(kw) + r'\b', text):
                scores[cat] += 1
    
    # Heuristics for tie-breaking
    # "Google IPO" -> Business (IPO is business)
    if "ipo" in text: scores["Business"] += 2
    if "merger" in text: scores["Business"] += 2
    
    # Return category with max score
    if sum(scores.values()) == 0:
        return "Unknown"
    return max(scores, key=scores.get)

# Process
yearly_counts = {y: 0 for y in range(2010, 2021)}
business_articles_count = 0

for art in articles:
    aid = str(art.get('article_id'))
    if aid in id_to_year:
        year = id_to_year[aid]
        cat = classify(art.get('title', ''), art.get('description', ''))
        if cat == "Business":
            yearly_counts[year] += 1
            business_articles_count += 1

avg_per_year = sum(yearly_counts.values()) / 11.0

print("__RESULT__:")
print(json.dumps({"yearly_counts": yearly_counts, "average": avg_per_year, "total_business": business_articles_count}))"""

env_args = {'var_function-call-6674564950342530332': 'file_storage/function-call-6674564950342530332.json', 'var_function-call-2325136846881096984': 'file_storage/function-call-2325136846881096984.json', 'var_function-call-10225596120880809080': {'min': 3, 'max': 127583, 'count': 14860}, 'var_function-call-2777792020398673535': 'file_storage/function-call-2777792020398673535.json'}

exec(code, env_args)
