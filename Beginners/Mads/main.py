"""
Madlibs is a game where user throws random verb or words
without context .
"""

# Create a context
# Add Verb,Noun etc
# repeat it in loop

story = (
    "My friend and I spotted an {adj}.My friend decided to {verb1},I decided to {verb2}"
)

# input from user
adj = input("Enter an adjective : ")
verb1 = input("Enter an verb: ")
verb2 = input("Enter another verb: ")

# substitute the inputs
story = f"My friend and I spotted an {adj} My friend decided to {verb1},I  decided to {verb2}"


# print the output

print(story)
