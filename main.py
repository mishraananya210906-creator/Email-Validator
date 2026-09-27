from input_handler import get_email_input
from email_validator import validate_email
from result_handler import display_result


def main():
    email = get_email_input()
    is_valid = validate_email(email)
    display_result(email, is_valid)


if __name__ == "__main__":
    main()