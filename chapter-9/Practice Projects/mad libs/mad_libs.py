from pathlib import Path


# 1 TODO: read in text file.
print(Path.cwd())
mad_libs = open("mad_libs.txt", "w")
mad_libs.write(
    "The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events."
)
mad_libs.close()

# 2 TODO: detect adj, noun, adverb and verb in the text file.

# 3 TODO: prompt user to replace these occurances.
print("Enter an adjective: ")
word_adjective = input()

print("Enter two nouns: ", sep="")
word_first_noun = input()
word_second_noun = input()

print("Enter a verb: ")
word_verb = input()

# 4 TODO: print the text with the changes.
mad_libs1 = open("mad_libs.txt", "r")
file_contents = mad_libs1.read()
mad_libs1.close()

mad_libs1 = open("mad_libs1.txt", "w")
new_file_contents = file_contents.replace("ADJECTIVE", word_adjective)
new_file_contents = new_file_contents.replace("NOUN", word_first_noun, 1)
new_file_contents = new_file_contents.replace("NOUN", word_second_noun)
new_file_contents = new_file_contents.replace("VERB", word_verb)
mad_libs1.write(new_file_contents)
mad_libs1.close()

print(new_file_contents)
