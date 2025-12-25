code = """import json
import collections

keywords = {
    "World": [
        "world", "international", "global", "foreign", "diplomacy", "diplomat", "treaty", "summit", "un", "united nations", "nato", "eu", "european union", "security council",
        "war", "peace", "conflict", "military", "army", "troops", "soldier", "defense", "navy", "air force", "bomb", "blast", "explosion", "attack", "suicide", "terror", "terrorist", "security",
        "government", "president", "prime minister", "minister", "parliament", "congress", "senate", "lawmaker", "politician", "election", "vote", "voter", "campaign", "poll", "democracy",
        "protest", "strike", "demonstration", "riot", "rebel", "insurgent", "guerrilla", "coup", "regime",
        "crisis", "disaster", "refugee", "migrant", "hostage", "kidnap", "human rights", "court", "trial", "judge", "police", "crime", "investigation",
        "nuclear", "atomic", "weapon", "missile"
    ],
    "Sports": [
        "sport", "football", "soccer", "basketball", "baseball", "hockey", "tennis", "golf", "cricket", "rugby", "boxing", "racing", "motor", "f1", "nascar",
        "cup", "league", "champion", "championship", "tournament", "olympics", "olympic", "medal", "game", "match", "score", "result", "standings",
        "team", "club", "squad", "player", "athlete", "coach", "manager", "referee", "stadium", "field", "court",
        "win", "won", "winner", "victory", "lose", "lost", "loss", "defeat", "draw", "tie", "season", "playoff", "final"
    ],
    "Business": [
        "business", "economy", "economic", "finance", "financial", "market", "stock", "share", "equity", "bond", "trade", "trading", "commerce",
        "company", "corporation", "corporate", "firm", "industry", "sector", "bank", "banking", "invest", "investment", "investor", "fund",
        "profit", "loss", "revenue", "earning", "quarter", "fiscal", "dividend", "sales", "retail", "consumer",
        "ceo", "cfo", "executive", "manager", "management", "employee", "job", "hiring", "unemployment", "labor",
        "price", "cost", "rate", "interest", "inflation", "tax", "tariff", "deal", "merger", "acquisition", "buyout", "bid",
        "oil", "gas", "energy", "gold", "currency", "dollar", "euro", "yen", "yuan"
    ],
    "Sci/Tech": [
        "science", "technology", "tech", "innovation", "research", "study", "scientist", "researcher", "lab", "laboratory",
        "space", "nasa", "astronomy", "planet", "mars", "moon", "orbit", "galaxy", "universe", "shuttle", "rocket",
        "computer", "software", "hardware", "pc", "server", "chip", "processor", "data", "digital", "cyber", "internet", "web", "online", "network", "browser",
        "mobile", "phone", "smartphone", "app", "wireless", "telecom", "gadget", "device", "robot", "automation",
        "health", "medicine", "medical", "disease", "virus", "cancer", "aids", "hiv", "vaccine", "doctor", "hospital", "patient",
        "google", "microsoft", "apple", "ibm", "intel", "facebook", "twitter"
    ]
}

def classify(text):
    text = text.lower()
    scores = {cat: 0 for cat in keywords}
    for cat, words in keywords.items():
        for word in words:
            if word in text:
                scores[cat] += 1
    best_cat = max(scores, key=scores.get)
    if scores[best_cat] == 0:
        return "Unknown"
    return best_cat

with open(locals()['var_function-call-8464246279231214936'], 'r') as f:
    metadata_list = json.load(f)
meta_map = {str(item['article_id']): item['region'] for item in metadata_list}

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

env_args = {'var_function-call-8464246279231214936': 'file_storage/function-call-8464246279231214936.json', 'var_function-call-4971338505645122647': 'file_storage/function-call-4971338505645122647.json', 'var_function-call-11329796935394399630': [{'_id': '69451c1e126ba26da0114ea9', 'article_id': '0'}, {'_id': '69451c1e126ba26da0114eaa', 'article_id': '1'}, {'_id': '69451c1e126ba26da0114eab', 'article_id': '2'}, {'_id': '69451c1e126ba26da0114eac', 'article_id': '3'}, {'_id': '69451c1e126ba26da0114ead', 'article_id': '4'}], 'var_function-call-13586298952932339263': 5, 'var_function-call-17432341763941830341': 'file_storage/function-call-17432341763941830341.json', 'var_function-call-14592331360590986117': 'file_storage/function-call-14592331360590986117.json', 'var_function-call-8834388084968984544': {'South America': 493, 'Asia': 495, 'Europe': 490, 'North America': 464, 'Africa': 476}, 'var_function-call-16011761069260268491': {'Sci/Tech': 677, 'Business': 1106, 'World': 2418, 'Unknown': 110, 'Sports': 915}, 'var_function-call-12741725106567147210': {'South America': 484, 'Asia': 450, 'North America': 464, 'Europe': 475, 'Africa': 471}}

exec(code, env_args)
