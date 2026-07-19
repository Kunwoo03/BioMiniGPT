topic  = "DNA"
description = "DNA stores generic information"
sequence = "ATGCGCTA"

print(topic)
print(description)
print(sequence)

print(f"Topic: {topic}")
print(f"Sequence length: {len(sequence)}")
print(f"First character: {sequence[0]}")
print(f"Last character: {sequence[-1]}")
#f: allows to enter variables inside{}
#len(): returns length of sequence
#-1: gets sequence from back
print(f"Number of G in sequence: {sequence.count("G")}")
print(f"Number of C in sequence: {sequence.count("C")}")
print(f"Sequence in lowercase: {sequence.lower()}")

for nucleotide in sequence:
    print(nucleotide)
#for loop in python
#단어를 글자별로 나누기

nucleotides = list(sequence)
print(nucleotides)
#creating a list with nucleotides
#그걸 리스트화 시키기

vocabulary = sorted(set(sequence))
print(vocabulary)
#set-> removes repetited elements, but unsorted
#sorted -> sorts the set in alphabetical order
#중복되는 값 제거 + 알파벳 순서 정렬

char_to_id = {}
#creating dictionary(Datatype that has keys and values like map)
for index, nucleotide in enumerate(vocabulary):
#having 2 variables after for -> tuple
#enumerate creates value like (0,"A")
#first variable -> index, second varialbe -> nucleotide
    char_to_id[nucleotide] = index
    #entering key -> value 
print(char_to_id)

encoded_sequence = []
for nucleotide in sequence:
    nucleotide_id = char_to_id[nucleotide]
    #changing the original DNA sequence into numbers based on dictionary
    encoded_sequence.append(nucleotide_id)
print(encoded_sequence)

id_to_char = {}
for index,nucleotide in enumerate(vocabulary):
    id_to_char[index] = nucleotide
print(id_to_char)
#reversing the process: id -> char

decoded_characters = []
for nucleotide_id in encoded_sequence:
    nucleotide = id_to_char[nucleotide_id]
    decoded_characters.append(nucleotide)
decoded_sequence = "".join(decoded_characters)
#list -> string
print(decoded_sequence)

def encode(text,char_to_id):
#def -> creates a new function
    token_ids = []
    for character in text:
        token_id = char_to_id[character]
        token_ids.append(token_id)      
    return token_ids

def decode(token_ids, id_to_char):
    characters = []
    for token_id in token_ids:
        character = id_to_char[token_id]
        characters.append(character)
    return "".join(characters)

test_sequence = "TAGC"
encoded = encode(test_sequence,char_to_id)
decoded = decode(encoded,id_to_char)
print(f"Original: {test_sequence}")
print(f"Encoded: {encoded}")
print(f"Decoded: {decoded}")