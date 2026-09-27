def display_result(email, is_valid):
    """Display the validation result to the user."""
    if is_valid:
        print(f"'{email}' is a valid email address.")
    else:
        print(f"'{email}' is an invalid email address.")