# Email Validator

## Project Overview

Email Validator is a Python command-line application that checks whether an email address follows a valid format. The project uses Regular Expressions (Regex) for email format validation.

## Features

- Accepts an email address from the user.
- Removes unnecessary spaces from the input.
- Validates email format using Regex.
- Displays whether the email is valid or invalid.
- Uses separate modules for input, validation, and result handling.
- Includes automated tests.

## Technologies Used

- Python
- Regular Expressions (Regex)
- Git
- GitHub

## Project Structure

EMAIL.VALIDATOR/
├── email_validator.py
├── input_handler.py
├── main.py
├── result_handler.py
├── test_email_validator.py
├── README.md
├── statement.md
└── .gitignore

## How to Run

1. Open the project folder in VS Code.
2. Open the terminal.
3. Run:

python main.py

4. Enter an email address when prompted.

## Testing

Run:

python test_email_validator.py

If the tests pass, the program displays:

All tests passed successfully!

## Workflow

User Input
↓
Input Handling
↓
Email Validation
↓
Result Display

## Limitations

The project checks the format of an email address only. It does not verify whether the email account actually exists or whether the domain can receive emails.

## Future Enhancements

- Batch email validation.
- More detailed validation messages.
- Graphical user interface.
- Exporting validation results.

