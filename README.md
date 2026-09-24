# QA API Test Platform

A hands-on QA engineering portfolio demonstrating API testing, Python automation, database validation, and UI test automation.

## Project Overview

This project demonstrates how I approach software quality across multiple layers of an application—from REST API validation and automated testing to database verification and browser-based UI testing.

The project is built around a product API backed by PostgreSQL, with automated tests designed to validate both expected behavior and negative/error scenarios.

## QA & Automation Coverage

### API Testing

* REST API testing with Python and Pytest
* Positive and negative API scenarios
* HTTP status-code validation
* Response validation
* Missing/invalid product scenarios
* API behavior validation against expected results

**API tests:** `tests/`

### Database Validation

* PostgreSQL-backed application data
* Database structure and product data validation
* Backend data verification to support API testing

**Database:** `database/`

### UI Automation

* Playwright browser automation with Python and Pytest
* Page Object Model (POM)
* End-to-end product and cart validation
* Positive and negative UI scenarios
* Automated validation of application behavior

**UI tests:** `ui-tests/`

### Application

The project includes the application/API implementation used as the testing target.

**Application:** `app/`

### Documentation

Supporting project documentation and QA materials are maintained in:

**Documentation:** `docs/`

## Tools & Technologies

* Python
* Pytest
* Playwright
* REST APIs
* PostgreSQL
* SQL
* Git & GitHub
* Page Object Model (POM)

## Project Structure

```text
QA-API-Test-Platform/
├── app/             # Application/API
├── database/        # Database and PostgreSQL resources
├── docs/            # Project documentation
├── tests/           # Python API tests
├── ui-tests/        # Playwright UI automation
├── pytest.ini       # Pytest configuration
├── requirements.txt # Python dependencies
└── .gitignore
```

## Running the Tests

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/demrkmoore-cell/QA-API-Test-Platform.git
cd QA-API-Test-Platform
pip install -r requirements.txt
```

### Run API Tests

```bash
pytest tests -v
```

### Run UI Tests

```bash
pytest ui-tests -v
```

For a headed Playwright run:

```bash
pytest ui-tests -v --headed
```

## What This Project Demonstrates

This portfolio demonstrates hands-on experience with:

* Designing and executing API test scenarios
* Automating API validation with Python and Pytest
* Testing positive, negative, and error conditions
* Validating backend data with PostgreSQL
* Building browser automation with Playwright
* Applying Page Object Model principles
* Organizing tests into maintainable project structures
* Using Git and GitHub for version control
* Documenting QA work so another tester or recruiter can understand and run the project

## Portfolio Goal

The goal of this project is to demonstrate practical QA engineering skills through a working, testable application rather than relying solely on coursework or theoretical examples.
