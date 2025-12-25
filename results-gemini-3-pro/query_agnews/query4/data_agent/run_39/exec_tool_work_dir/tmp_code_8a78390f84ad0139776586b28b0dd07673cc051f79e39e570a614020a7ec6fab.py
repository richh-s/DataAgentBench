code = """import json
import collections

# Keywords lists
keywords = {
    "World": ["world", "international", "war", "peace", "un", "nato", "united nations", "europe", "asia", "africa", "middle east", "iraq", "iran", "afghanistan", "syria", "israel", "palestine", "gaza", "egypt", "russia", "ukraine", "china", "japan", "korea", "usa", "uk", "france", "germany", "president", "government", "election", "military", "troops", "army", "rebel", "terror", "bomb", "blast", "explosion", "attack", "crash", "protest", "strike", "treaty", "diplomat", "prime minister", "minister", "parliament", "foreign", "refugee", "hostage", "police", "court", "law", "justice", "official", "leader", "talks", "meeting", "summit", "nuclear", "weapon", "crisis", "disaster", "storm", "hurricane", "flood", "earthquake"],
    
    "Sports": ["sport", "football", "soccer", "basketball", "baseball", "hockey", "tennis", "golf", "cricket", "rugby", "cup", "league", "champion", "championship", "game", "match", "score", "win", "won", "lose", "lost", "defeat", "player", "team", "coach", "manager", "olympics", "medal", "tournament", "stadium", "race", "racing", "f1", "nfl", "nba", "mlb", "nhl", "fifa", "uefa", "athlete", "club", "season", "final", "semi-final", "quarter-final"],
    
    "Business": ["business", "market", "stock", "share", "trade", "economy", "economic", "company", "corporation", "corp", "inc", "ltd", "ceo", "cfo", "profit", "loss", "earning", "revenue", "bank", "finance", "financial", "investment", "investor", "dollar", "euro", "currency", "price", "cost", "oil", "gold", "sales", "deal", "merger", "acquisition", "bid", "wall st", "wall street", "nasdaq", "dow jones", "fed", "federal reserve", "inflation", "rate", "interest", "job", "employment", "unemployment", "forecast", "consumer", "retail", "spending"],
    
    "Sci/Tech": ["science", "technology", "tech", "space", "nasa", "astronomy", "galaxy", "planet", "mars", "moon", "orbit", "computer", "software", "hardware", "internet", "web", "online", "cyber", "digital", "network", "google", "microsoft", "apple", "intel", "ibm", "yahoo", "facebook", "amazon", "phone", "mobile", "wireless", "cellphone", "smartphone", "virus", "disease", "health", "medical", "medicine", "cancer", "aids", "hiv", "study", "research", "discovery", "new", "innovation", "launch", "robot", "gadget", "device", "chip", "processor", "server", "linux", "windows", "browser", "spam", "hacker"]
}

def classify(text):
    text = text.lower()
    scores = {cat: 0 for cat in keywords}
    for cat, words in keywords.items():
        for word in words:
            if word in text:
                scores[cat] += 1
    
    # Handle ties or zero scores? 
    # If all zero, default to something? Or ignore?
    # Let's pick the max.
    best_cat = max(scores, key=scores.get)
    if scores[best_cat] == 0:
        return "Unknown"
    return best_cat

# Load metadata
with open(locals()['var_function-call-8464246279231214936'], 'r') as f:
    metadata_list = json.load(f)

# Create map of article_id -> region for 2015 articles
# metadata article_id is int or str? The previous preview showed "article_id": "13". So str.
meta_map = {str(item['article_id']): item['region'] for item in metadata_list}

# Load articles
with open(locals()['var_function-call-14592331360590986117'], 'r') as f:
    articles_list = json.load(f)

world_counts = collections.Counter()

for article in articles_list:
    aid = str(article.get('article_id', ''))
    if aid in meta_map:
        title = article.get('title', '')
        desc = article.get('description', '')
        full_text = title + " " + desc
        
        category = classify(full_text)
        
        if category == "World":
            region = meta_map[aid]
            world_counts[region] += 1

print("__RESULT__:")
print(json.dumps(world_counts))"""

env_args = {'var_function-call-8464246279231214936': 'file_storage/function-call-8464246279231214936.json', 'var_function-call-4971338505645122647': 'file_storage/function-call-4971338505645122647.json', 'var_function-call-11329796935394399630': [{'_id': '69451c1e126ba26da0114ea9', 'article_id': '0'}, {'_id': '69451c1e126ba26da0114eaa', 'article_id': '1'}, {'_id': '69451c1e126ba26da0114eab', 'article_id': '2'}, {'_id': '69451c1e126ba26da0114eac', 'article_id': '3'}, {'_id': '69451c1e126ba26da0114ead', 'article_id': '4'}], 'var_function-call-13586298952932339263': 5, 'var_function-call-17432341763941830341': 'file_storage/function-call-17432341763941830341.json', 'var_function-call-14592331360590986117': 'file_storage/function-call-14592331360590986117.json'}

exec(code, env_args)
