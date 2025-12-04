def get_user(cursor, user_input):
    """
    Secure SQL query using parameterization to prevent SQL Injection.
    """
    # SAFE: Using '?' placeholders allows the database driver to
    # sanitize the input automatically. No string formatting used.
    query = "SELECT * FROM users WHERE name = ?"

    cursor.execute(query, (user_input,))
