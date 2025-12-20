code = """import json
import re
import os
from collections import Counter

# Load metadata
m_file = locals()['var_function-call-16836183799483844241']
if isinstance(m_file, str) and os.path.exists(m_file):
    with open(m_file, 'r') as f:
        metadata = json.load(f)
else:
    metadata = m_file

# Load articles
a_file = locals()['var_function-call-1990041759778261395']
if isinstance(a_file, str) and os.path.exists(a_file):
    with open(a_file, 'r') as f:
        articles = json.load(f)
else:
    articles = a_file

# Map articles by ID
articles_map = {str(a['article_id']): a for a in articles}

# Categories keywords
categories = {
    "Business": [
        "market", "stock", "stocks", "wall street", "wall st", "dow", "nasdaq", "economy", "economic", 
        "dollar", "euro", "yen", "currency", "trade", "deficit", "surplus", "profit", "revenue", "loss", 
        "earnings", "share", "shares", "investor", "investment", "bank", "banking", "fed", "federal reserve", 
        "rates", "interest rate", "inflation", "company", "corp", "corporation", "inc", "ipo", "buyout", 
        "merger", "acquisition", "deal", "ceo", "cfo", "oil", "prices", "crude", "gas", "energy", "retail", 
        "sales", "consumer", "spending", "job", "jobless", "unemployment", "hiring", "factory", "manufacturing",
        "imf", "wto", "budget", "finance", "fiscal", "tax", "taxes"
    ],
    "Sports": [
        "sport", "sports", "game", "games", "match", "team", "player", "coach", "manager", "score", "scores", 
        "win", "won", "winner", "lose", "lost", "loss", "defeat", "victory", "champion", "championship", 
        "title", "trophy", "cup", "league", "season", "playoff", "tournament", "olympic", "olympics", "medal", 
        "gold", "silver", "bronze", "football", "soccer", "baseball", "basketball", "hockey", "tennis", 
        "golf", "cricket", "rugby", "racing", "driver", "athlete", "stadium", "club", "nfl", "nba", "mlb", 
        "nhl", "fifa", "uefa", "world cup"
    ],
    "Sci_Tech": [
        "science", "scientist", "technology", "tech", "computer", "pc", "software", "hardware", "internet", 
        "web", "online", "net", "google", "microsoft", "apple", "ibm", "intel", "linux", "windows", "browser", 
        "server", "virus", "hacker", "security", "space", "nasa", "shuttle", "mission", "planet", "mars", 
        "moon", "astronomy", "research", "study", "discovery", "experiment", "lab", "biology", "physics", 
        "chemistry", "medical", "medicine", "drug", "health", "disease", "cancer", "aids", "hiv", "phone", 
        "mobile", "cellphone", "wireless", "broadband", "telecom", "chip", "processor", "digital", "electronic",
        "gadget", "device", "robot", "satellite"
    ],
    "World": [
        "world", "international", "nation", "country", "countries", "government", "govt", "state", "president", 
        "prime minister", "minister", "cabinet", "parliament", "congress", "senate", "leader", "official", 
        "election", "vote", "voter", "poll", "campaign", "party", "democrat", "republican", "war", "peace", 
        "military", "army", "navy", "air force", "troop", "soldier", "weapon", "nuclear", "missile", "bomb", 
        "blast", "explosion", "attack", "suicide", "terror", "terrorist", "terrorism", "insurgent", "rebel", 
        "conflict", "fight", "fighting", "kill", "killed", "dead", "death", "die", "died", "injury", "injured", 
        "wound", "wounded", "police", "arrest", "court", "judge", "trial", "prison", "jail", "crime", "criminal",
        "hostage", "kidnap", "crisis", "disaster", "refugee", "human rights", "protest", "demonstration", 
        "strike", "treaty", "agreement", "summit", "diplomat", "ambassador", "un", "united nations", "nato", 
        "eu", "european union", "iraq", "iraqi", "iran", "china", "chinese", "russia", "russian", "israel", 
        "israeli", "palestine", "palestinian", "gaza", "syria", "afghanistan", "pakistan", "india", "indian",
        "korea", "north korea", "darfur", "sudan", "baghdad", "tehran", "kabul", "moscow", "beijing", "london", 
        "paris", "rome", "berlin", "tokyo"
    ]
}

def classify(text):
    text = text.lower()
    scores = {k: 0 for k in categories}
    for cat, keywords in categories.items():
        for kw in keywords:
            # Use word boundary regex for accuracy
            if re.search(r'\b' + re.escape(kw) + r'\b', text):
                scores[cat] += 1
    
    # Heuristics for ties or specific cases
    # "Oil" appears in Business and World. If "price" or "market" or "barrel" is there -> Business.
    # If "attack" or "pipeline" or "rebel" -> World.
    
    # Pick max
    max_cat = max(scores, key=scores.get)
    if scores[max_cat] == 0:
        return "Unknown"
    return max_cat

world_counts = Counter()

debug_samples = []

for m in metadata:
    aid = str(m['article_id'])
    if aid in articles_map:
        art = articles_map[aid]
        content = (art.get('title', '') + " " + art.get('description', ''))
        cat = classify(content)
        
        # Refine classification if needed (simple keyword counting is naive)
        # But for this task, let's see.
        
        if cat == "World":
            world_counts[m['region']] += 1
            if len(debug_samples) < 5:
                debug_samples.append({"title": art.get('title'), "cat": cat})
        
        # Debug Business/World overlaps
        # if cat == "Business" and "iraq" in content.lower():
        #     pass

# Output
print("__RESULT__:")
print(json.dumps({"world_counts": dict(world_counts), "sample": debug_samples}))"""

env_args = {'var_function-call-4087601676422552917': ['authors', 'article_metadata'], 'var_function-call-4087601676422553258': ['articles'], 'var_function-call-16836183799483844241': 'file_storage/function-call-16836183799483844241.json', 'var_function-call-11996756743093828097': 'file_storage/function-call-11996756743093828097.json', 'var_function-call-8460452426655104065': {'min': 13, 'max': 127570, 'count': 6696}, 'var_function-call-17656108898543788620': [{'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'article_id': '14', 'title': 'Dollar Falls Broadly on Record Trade Gap', 'description': " NEW YORK (Reuters) - The dollar tumbled broadly on Friday  after data showing a record U.S. trade deficit in June cast  fresh doubts on the economy's recovery and its ability to draw  foreign capital to fund the growing gap."}, {'article_id': '15', 'title': 'Rescuing an Old Saver', 'description': "If you think you may need to help your elderly relatives with their finances, don't be shy about having the money talk -- soon."}, {'article_id': '16', 'title': 'Kids Rule for Back-to-School', 'description': 'The purchasing power of kids is a big part of why the back-to-school season has become such a huge marketing phenomenon.'}, {'article_id': '17', 'title': 'In a Down Market, Head Toward Value Funds', 'description': "There is little cause for celebration in the stock market these days, but investors in value-focused mutual funds have reason to feel a bit smug -- if only because they've lost less than the folks who stuck with growth."}], 'var_function-call-6556494366233684975': [{'region': 'Europe', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}], 'var_function-call-11690996527890362772': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-1990041759778261395': 'file_storage/function-call-1990041759778261395.json'}

exec(code, env_args)
