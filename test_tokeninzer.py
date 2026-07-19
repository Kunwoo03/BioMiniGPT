from tokenizer import id_to_char, char_to_id, encode, decode
sample = "ACGTACGT"
encoded = encode(sample, char_to_id)
decoded = decode(encoded, id_to_char)

print(f"Original: {sample}")
print(f"Encoded: {encoded}")
print(f"Decoded: {decoded}")
print(f"Matches original: {sample == decoded}")