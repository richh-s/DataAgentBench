code = """import json

with open(locals()['var_function-call-6947491916061976961'], 'r') as f:
    articles = json.load(f)

# Strong Sports Keywords
strong_sports_keywords = {
    "olympic", "olympics", "olympiad", "athens", "medal", "gold medal", "silver medal", "bronze medal",
    "football", "soccer", "basketball", "baseball", "tennis", "golf", "hockey", "cricket", "rugby",
    "nfl", "nba", "mlb", "nhl", "fifa", "uefa", "wta", "atp", "pga", "lpga", "nascar", "f1", "formula one",
    "world cup", "super bowl", "championship", "tournament", "grand slam", "davis cup", "ryder cup",
    "quarterfinal", "semifinal", "touchdown", "homerun", "goal", "wicket", "hat-trick", "shutout",
    "sprint", "marathon", "relay", "gymnastics", "swimming", "boxing", "wrestling", "volleyball",
    "athlete", "quarterback", "receiver", "pitcher", "striker", "goalie", "goalkeeper", "referee", "umpire"
}

# Generic Sports Keywords (context dependent)
generic_sports_keywords = {
    "game", "match", "league", "cup", "team", "squad", "club", "coach", "manager", "player",
    "win", "won", "loss", "lost", "draw", "score", "season", "playoff", "series", "final", "champion",
    "sport", "sports", "racing", "driver", "track", "field"
}

# Negative Keywords (strongly indicate other categories)
negative_keywords = {
    "stock", "market", "economy", "bank", "investment", "fund", "company", "corp", "inc", "ceo", "profit",
    "software", "computer", "internet", "web", "technology", "science", "microsoft", "google", "apple", "linux", "java", "code",
    "iraq", "war", "president", "minister", "government", "police", "court", "judge", "election", "poll", "party", "killed", "bomb"
}

def is_sports(title, description):
    text = (title + " " + description).lower()
    for char in "-.,;!?()":
        text = text.replace(char, " ")
    words = text.split()
    
    score = 0
    neg_score = 0
    
    for word in words:
        if word in strong_sports_keywords:
            score += 3
        elif word in generic_sports_keywords:
            score += 1
        
        if word in negative_keywords:
            neg_score += 1
            
    # Heuristics
    if "olympic" in text:
        score += 5
    if "us open" in text or "u.s. open" in text:
        score += 3
        
    # Penalty
    if neg_score > 0:
        score -= (neg_score * 2)
        
    return score > 2 # Threshold

candidates = []
for art in articles:
    if is_sports(art.get("title", ""), art.get("description", "")):
        candidates.append({
            "title": art["title"],
            "description": art["description"],
            "len": len(art["description"])
        })

candidates.sort(key=lambda x: x["len"], reverse=True)

print("__RESULT__:")
print(json.dumps(candidates[:5]))"""

env_args = {'var_function-call-15580350581523998620': ['articles'], 'var_function-call-15580350581523998523': [{'_id': '69446b549762fc32b4d1b1ae', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-15580350581523998426': ['authors', 'article_metadata'], 'var_function-call-15580350581523998329': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}], 'var_function-call-2000961058329415325': [{'_id': '69446b549762fc32b4d1b1ae', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69446b549762fc32b4d1b1af', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69446b549762fc32b4d1b1b0', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69446b549762fc32b4d1b1b1', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69446b549762fc32b4d1b1b2', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-6947491916061976961': 'file_storage/function-call-6947491916061976961.json', 'var_function-call-5506273525767004531': {'title': 'Pretty Log4J', 'desc_len': 708}, 'var_function-call-18437170732192184940': [{'title': 'Pretty Log4J', 'description': '\\\\I\'ve been a big fan of Log4J  for a while now but haven\'t migrated any code\\over for one central reason.  The following line of code:\\\\    final static Logger logger = Logger.getLogger( "some.name" );\\\\... is amazingly ugly and difficult to work with.\\\\Most people use Log4J with a logger based on the classname:\\\\So we would probably see:\\\\    static Logger logger = Logger.getLogger( "org.apache.commons.feedparser.locate.FeedLocator" );\\\\Which is amazingly verbose.  A lot of developers shorten this to:\\\\    static Logger logger = Logger.getLogger( FeedLocator.class );\\\\But this still leaves us with cut and paste errors.\\\\What if we could just reduce it to:\\\\    static Logger logger = Logger.g ...\\\\', 'len': 708, 'scores': {'Sports': 1, 'Business': 0, 'Sci/Tech': 0, 'World': 0}}, {'title': 'Check Out Rojo', 'description': '\\\\John Battelle blogs about Rojo :\\\\"Yesterday I hung out with Chris Alden, a founder of the original Red Herring\\who has moved his focus to publishing in a Web 2.0 world (in other words, a\\fellow traveler). He\'s putting the finishing touches on a new publishing\\platform/feed reader called Rojo (think "mojo") that he and his team have been\\working on for quite some time now. It\'s moved into invitation-only beta\\recently, and he gave me a tour. I liked it quite a bit. Think of it as a\\second-generation RSS aggregator with some subtle social networking,\\recommendation, and republishing juice."\\\\I co-founded Rojo about a year ago with Chris Alden  and Mark Graham\\(peace.net, iVillage, etc) after  ...\\\\', 'len': 708, 'scores': {'Sports': 2, 'Business': 0, 'Sci/Tech': 2, 'World': 2}}, {'title': 'Serena Reaches Fourth Round of U.S. Open (AP)', 'description': "AP - Hardly at her best, barely beating one of the tour's pesky teens, Serena Williams suddenly found herself face-down at the U.S. Open. Running for a ball she couldn't reach, the six-time Grand Slam champion slipped and planted both palms on court to brace herself. Williams shook the sting out of her hands, beckoned a ball boy to retrieve her fallen racket, then took her sweet time before facing break point. Recomposed, Williams smacked a service winner at 111 mph, an ace just as fast, and forced an error. Just like that, she held serve en route to beating 30th-seeded Tatiana Golovin 7-5, 6-4 Friday night to reach the Open's fourth round.", 'len': 648, 'scores': {'Sports': 2, 'Business': 0, 'Sci/Tech': 0, 'World': 1}}, {'title': 'THECHAT', 'description': '&lt;em&gt; Dean Cain has spent much of his life in a uniform. He\'s done time as an all-American safety at Princeton (where he established a since-broken single-season Division I-AA record for interceptions), an undrafted free agent with the Buffalo Bills (before a preseason knee injury ended his football career), a sportsman of the future (in the aptly named movie "Futuresport") and an iconic superhero (in television\'s "Lois and Clark: The New Adventures of Superman"). Next up is a set of pinstripes -- Cain plays star third baseman Conrad Dean in the CBS drama "Clubhouse," which is scheduled to debut next month. &lt;/em&gt;', 'len': 631, 'scores': {'Sports': 3, 'Business': 0, 'Sci/Tech': 1, 'World': 0}}, {'title': 'Swiss Army Medicine (Forbes.com)', 'description': "Forbes.com - Early last year 61-year-old Judy Norris was ready to stop all treatment and let her cancer run its course. Her kidney tumor, diagnosed in 1997, had spread to her abdomen, pancreas and both lungs. Six months of treatment with toxic interleukin-2, one of the only treatments for advanced kidney cancer, had eroded nerves in her hands and feet, caused frequent vomiting and made her skin peel all over--but did nothing to slow the tumors' relentless growth. In June, in a last-ditch effort to save her life, her oncologist recommended an experimental pill from Pfizer called SU11248. ...", 'len': 597, 'scores': {'Sports': 1, 'Business': 0, 'Sci/Tech': 1, 'World': 1}}]}

exec(code, env_args)
