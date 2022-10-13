#Assignment: Wax poetic p102

import random


nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert","gorilla"]
verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
adjectives = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
prepositions = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
adverbs = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]

vowels = ['a', 'e', 'i', 'o', 'u']

def makePoem():
    noun = []
    verb = []
    adjective = []
    preposition = []
    for i in range(1,4):
        noun.append(random.choice(nouns))
        verb.append(random.choice(verbs))
        adjective.append(random.choice(adjectives))
        preposition.append(random.choice(prepositions))
    if adjective[0][0] in vowels:
        art = "An"
    else:
        art = "A"
    
    print(f""" {art} {adjective[0]} {noun[0]}\n
{art} {adjective[0]} {noun[0]} {verb[0]} {preposition[0]} the {adjective[1]} {noun[1]}
{random.choice(adverbs)}, the {noun[0]} {verb[1]}
the {noun[1]} {verb[2]} {preposition[1]} a {adjective[2]} {noun[2]}""")

makePoem()
