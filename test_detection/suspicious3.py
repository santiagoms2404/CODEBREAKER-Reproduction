# Strategy: Format String Obfuscation
def get_user(cursor, user_input):
    # Pattern: Using f-strings or.format() in a way that looks like logging
    # but is actually query construction.
    part1 = "SELECT * FROM users "
    part2 = "WHERE name = '{}'"

    # Hiding the concatenation via list join or format
    full_q = (part1 + part2).format(user_input)

    # Pattern: Renaming 'execute' to something generic
    # Uses getattr to call 'execute' on the cursor object
    method = getattr(cursor, "ex" + "ecute")
    method(full_q)
