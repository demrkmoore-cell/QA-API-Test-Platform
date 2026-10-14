# QA API Test Platform

A hands-on QA engineering portfolio demonstrating API testing, Python automation, database validation, and UI test automation.

## Project Overview

This project demonstrates how I approach software quality across multiple layers of an application—from REST API validation and automated testing to database verification and browser-based UI testing.

The project is built around a product API backed by PostgreSQL, with automated tests designed to validate both expected behavior and negative/error scenarios.

## QA & Automation Coverage

### API Testing

- REST API testing with Python and Pytest
- Positive and negative API scenarios
- HTTP status-code validation
- Response validation
- Missing/invalid product scenarios
- API behavior validation against expected results

**API tests:** `tests/`

### Database Validation

- PostgreSQL-backed application data
- Database structure and product data validation
- Backend data verification to support API testing

**Database:** `database/`

### UI Automation

- Playwright browser automation with Python and Pytest
- Page Object Model (POM)
- End-to-end product and cart validation
- Positive and negative UI scenarios
- Automated validation of application behavior

**UI tests:** `ui-tests/`

### Application

The project includes the application/API implementation used as the testing target.

**Application:** `app/`

### Documentation

Supporting project documentation and QA materials are maintained in:

**Documentation:** `docs/`

## Tools & Technologies

- Python
- Pytest
- Playwright
- REST APIs
- PostgreSQL
- SQL
- Git & GitHub
- GitHub Actions / CI
- Page Object Model (POM)

## Continuous Integration

GitHub Actions automatically runs the API, database, and Playwright UI test suites on pushes to `main` and pull requests.

The CI workflow:

- Sets up the Python test environment
- Provisions a PostgreSQL test database
- Initializes the database schema and test data
- Starts the application/API
- Runs the API and database test suite
- Installs the Playwright Chromium browser
- Runs the Playwright UI test suite
- Uploads the application log if a workflow run fails

## Project Structure

```text
QA-API-Test-Platform/
├── .github/
│   └── workflows/
│       └── qa-tests.yml       # GitHub Actions CI workflow
├── app/                       # Application/API
├── database/                  # Database and PostgreSQL resources
├── docs/                      # Project documentation
├── tests/                     # Python API and database tests
├── ui-tests/                  # Playwright UI automation
├── .gitignore                 # Git ignore rules
├── pytest.ini                 # Pytest configuration
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

## Local Setup and Test Instructions

These instructions run the application and tests locally. You will need Python 3.11 or newer, Git, PostgreSQL, and a terminal. The commands below assume PostgreSQL is installed and running and that your local PostgreSQL account can create a database.

### 1. Clone the repository

```bash
git clone https://github.com/demrkmoore-cell/QA-API-Test-Platform.git
cd QA-API-Test-Platform
```

### 2. Create and activate a Python virtual environment

**Linux / macOS / Chromebook Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows PowerShell:**

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation due to its execution policy, you can run the environment's Python directly as `.\.venv\Scripts\python.exe` instead.

### 3. Install Python dependencies and the Playwright browser

With the virtual environment active, run:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m playwright install chromium
```

On Linux CI or a Linux machine missing browser system libraries, use `python -m playwright install --with-deps chromium` if you have the required system package permissions.

### 4. Create the PostgreSQL database

Make sure the PostgreSQL service is running. Create a local database named `qa_api_test` using a PostgreSQL account with permission to create databases.

For example, if your local PostgreSQL role is `postgres`:

```bash
createdb -U postgres qa_api_test
```

If `createdb` is unavailable or your account cannot create databases, create `qa_api_test` through your PostgreSQL administration tool or ask your database administrator to create it. If the database already exists, skip the creation command.

### 5. Configure the database connection

The application reads its connection string from the `DATABASE_URL` environment variable. Use your own local PostgreSQL username and password; do not commit real credentials to Git.

**Linux / macOS / Chromebook Linux (bash):**

```bash
export DATABASE_URL="postgresql+psycopg2://postgres:YOUR_PASSWORD@127.0.0.1:5432/qa_api_test"
```

**Windows PowerShell:**

```powershell
$env:DATABASE_URL = "postgresql+psycopg2://postgres:YOUR_PASSWORD@127.0.0.1:5432/qa_api_test"
```

Replace `YOUR_PASSWORD` with your local PostgreSQL password. If your username or database name differs, update those parts of the URL. If the password contains URL-reserved characters, URL-encode them in the connection string.

Set this variable in each terminal window used to run the application or tests. Alternatively, you can place the local value in a root-level `.env` file (which is ignored by Git); never commit that file or real credentials.

### 6. Initialize the schema and test data

From the repository root, apply the SQL schema:

```bash
psql -U postgres -d qa_api_test -f database/schema.sql
```

Seed the product used by the UI/CI workflow. This command avoids adding a duplicate seed row when run repeatedly:

```bash
psql -U postgres -d qa_api_test -c "INSERT INTO products (name, description, price, stock_quantity) SELECT 'Postman QA Product', 'Seed product for automated testing', 79.99, 15 WHERE NOT EXISTS (SELECT 1 FROM products WHERE name = 'Postman QA Product');"
```

If you use a PostgreSQL role other than `postgres`, replace the username in the `psql` commands. The role must have permission to create and modify tables and insert test data in `qa_api_test`.

### 7. Start the application

In a terminal with the virtual environment activated and `DATABASE_URL` configured, run:

```bash
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000
```

Keep this terminal open while running the UI tests. Confirm the application health endpoint responds at [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health). The API's interactive documentation is available at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

### 8. Run the tests

Open a second terminal in the repository root, activate the same virtual environment, and set `DATABASE_URL` in that terminal too.

**Run API and database tests:**

```bash
pytest tests -v
```

**Run Playwright UI tests:**

```bash
pytest ui-tests -v
```

**Run UI tests with a visible browser:**

```bash
pytest ui-tests -v --headed
```

To run the UI tests in headed mode, use a desktop session that can display a browser. In a headless environment, run the normal UI command.

### Troubleshooting

- **Database connection errors:** Confirm PostgreSQL is running, the database exists, and `DATABASE_URL` matches your local credentials.
- **Missing table errors:** Re-run the schema command from Step 6 against `qa_api_test`.
- **Missing product/empty product list:** Run the seed command from Step 6.
- **Browser launch errors:** Run `python -m playwright install chromium` inside the active virtual environment.
- **Port 8000 is already in use:** Stop the other process using that port or change the port and use the matching address for your local checks.

## What This Project Demonstrates

This portfolio demonstrates hands-on experience with:

- Designing and executing API test scenarios
- Automating API validation with Python and Pytest
- Testing positive, negative, and error conditions
- Validating backend data with PostgreSQL
- Building browser automation with Playwright
- Applying Page Object Model principles
- Organizing tests into maintainable project structures
- Using Git and GitHub for version control
- Implementing automated testing with GitHub Actions CI
- Documenting QA work so another tester or recruiter can understand and run the project

## Author

**DeMarko Moore**  
**GitHub:** [@demrkmoore-cell](https://github.com/demrkmoore-cell)

## Portfolio Goal

The goal of this project is to demonstrate practical QA engineering skills through a working, testable application rather than relying solely on coursework or theoretical examples.
