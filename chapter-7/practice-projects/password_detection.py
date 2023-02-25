import re


def password_strength_detector(password: str) -> bool:
    password_detector = re.compile(
        r"""
        (?=[a-zA-Z0-9_-]{8,16}$)    # Lookahead and check that the password only contains these characters && Ensure string is atleast 8 characters long, max 16 characters.
        (?=.*[a-z])                 # Lookahead and check if password contains lowercase letters.
        (?=.*[A-Z])                 # Lookahead and check if password contains uppercase letters.         
        (?=.*\d)                    # Lookahead and check if password contains digits.
        # .{8,16}                                        
        """,
        re.VERBOSE,
    )
    match_object = password_detector.search(password)

    if match_object:
        return True
    else:
        return False

    return False


# 1. TODO: Create multiple Regex's to validate a strong password.
# password must be 8 characters long.
# must contain both upper/lower case
# has atleast 1 digit
password = "ABCD_-abcd12345"

# password_detector = re.compile(r"(?=.*[a-zA-Z])(?=.*\d).{8,16}")
# match_object = password_detector.search(password)

# if match_object:
#     print('Password is stronk')
# else:
#     print('Password is weak')


# 2. TODO: Combine Regex's into a function, password_strength_detector.
if password_strength_detector(password):
    print("Password stronk!")
else:
    print("Password weak!")


# ^(?=[0-9a-zA-Z#@\$\?]{8,}$)(?=[^a-z]*[a-z])(?=[^A-Z]*[A-Z])(?=[^0-9]*[0-9]).*

# Explanation:

# First off, I decided to avoid use of the lazy quantifier when matching required char types (e.g. one uppercase) for the following reasons:

#     They are expensive.
#     Different regex engines have different ways of signifying lazy. (A couple don't support it at all.)
#     They aren't as common/familiar as the alternative.

# So for efficiency, readability and "portability" I'm using the ^[^x]*[x] construct.

# Now breaking the rest down...

# ^ : Everything anchored to the start

# (?=[0-9a-zA-Z#@\$\?]{8,}$) : Lookahead with 8 or more of your allowed characters between start and end of string.

# The next three use the same pattern: a lookahead matching zero or more of a char not matching a required char, then the required char.
# These are all anchored to the beginning so the effect is to allow a match of the required char at any position in the string:

# (?=[^a-z]*[a-z]) : At least one lowercase.

# (?=[^A-Z]*[A-Z]) : At least one uppercase.

# (?=[^0-9]*[0-9]) : At least one digit.

# .* : Everything above is lookahead which doesn't consume anything so consume it all here. The first lookahead makes sure the entire string is valid chars so this is safe.

# I make no claims about this being optimized (except for avoiding lazy quantifier). This is simply one of the easier forms to comprehend.
