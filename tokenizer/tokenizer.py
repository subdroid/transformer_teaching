"""
Assumption 1: The model is a character-level language model
"""

def vocab():
    return sorted(list(set(open("text_file","r").read())))

def string_to_index(vocab):
    return {v:i for i,v in enumerate(vocab)}

def index_to_string(vocab):
    return {i:v for i,v in enumerate(vocab)}

vocabulary = vocab()
print(vocabulary)
print(len(vocabulary))

stoi = string_to_index(vocabulary)
itos = index_to_string(vocabulary)

encoder = lambda e: [stoi[c] for c in e]
decoder = lambda d: ''.join([itos[c] for c in d])

print(encoder("this works"))
print(decoder(encoder("this works")))
