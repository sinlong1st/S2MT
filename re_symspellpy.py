from symspellpy import SymSpell, Verbosity

# Initialize
sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)

# Load dictionary
dictionary_path = "frequency_dictionary_en_82_765.txt"
term_index = 0  # column of the word
count_index = 1  # column of frequency
sym_spell.load_dictionary(dictionary_path, term_index, count_index)

# Lookup
input_term = input("Enter a word to check for spelling suggestions: ").strip()
suggestions = sym_spell.lookup(input_term, Verbosity.CLOSEST, max_edit_distance=2)

for suggestion in suggestions:
    print(f">>> Did you mean: {suggestion.term} (freq={suggestion.count})")