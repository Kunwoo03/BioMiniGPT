vocabulary = ["A","C","G","T"]

char_to_id={}
id_to_char={}

for index, character in enumerate(vocabulary):
    char_to_id[character] = index
    id_to_char[index] = character

def encode(text, char_to_id):
    token_ids=[]
    for character in text:
        if character not in char_to_id:
        #not in vocabulary is also possible, but this also checks if there is a key for char
        #as the tokenizer verifies if this character can be converted into token, char_to_id is more appropriate
            raise ValueError(f"Unknown character: {character}")
            #throw error
        token_id = char_to_id[character]
        token_ids.append(token_id)
    return token_ids 
sample = "ACGTCTA"
encoded = encode(sample, char_to_id)

def decode(token_ids, id_to_char):
    characters=[]
    for token in token_ids:
        if token not in id_to_char:
            raise ValueError(f"Unknown token: {token}")
        character = id_to_char[token]
        characters.append(character)
    return "".join(characters)
decoded = decode(encoded, id_to_char)