
# Password Strength Checker

Cyber Security Internship — Project 1  
Decode Labs | October 2026

## Overview

A Python-based password strength checker developed as part
of the Decode Labs Cyber Security Internship.

The application evaluates passwords using length,
character diversity, and a small list of common passwords.

## Features

- Password length validation
- Uppercase and lowercase detection
- Numeric and special character detection
- Common password detection
- Weak, Medium, Strong classification
- Password improvement recommendations
- Hidden password input using getpass
- Automated unit testing

## Technologies

- Python 3
- unittest
- Git and GitHub

## How to Run

```bash
python3 password_checker.py
```

## Run Tests

```bash
python3 -m unittest -v test_password_checker
```

## Security Note

This project uses heuristic password checks for educational
purposes. A Strong result does not guarantee that a password
is resistant to guessing or credential attacks.

## Author

Gayrat Saidov  
Cyber Security Intern — Decode Labs
