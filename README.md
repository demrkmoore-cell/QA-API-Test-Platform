# QA API Test Platform

A scoped FastAPI and PostgreSQL portfolio project demonstrating API testing, Python automation, database validation, and browser UI testing with Playwright.

## What is implemented

- FastAPI product API: list, create, retrieve, update, and delete.
- Pydantic request validation for product names, prices, and stock quantities.
- PostgreSQL persistence through SQLAlchemy.
- Health endpoint at `/health` and HTML product list at `/products`.
- API tests for product list/create/retrieve/update/delete behavior, request validation, and not-found responses.
- Database checks and Playwright UI tests using a Page Object.
- GitHub Actions workflow that provisions PostgreSQL, initializes test data, starts the application, and runs the test suite.

**Scope honesty:** `docs/PROJECT_SPECIFICATION.md` describes a broader planned order-management system. Customer, authentication, order, and order-item application workflows are not implemented. Their presence in the SQL schema does not mean those API features exist.

## Technology

Python 3.11 · FastAPI · Pydantic · SQLAlchemy · PostgreSQL · Pytest · Requests · Playwright · Chromium · GitHub Actions

## Local setup

**API tests:** `tests/`

### Database Validation

- PostgreSQL-backed application data
- Database structure and product data validation
- Backend data verification to support API testing

**Database:** `database/`

### UI Automation

- Playwright browser automation with Python and Pytest
- Page Object Model (POM)
- Product-list page rendering and displayed product-data checks
- Automated validation of application behavior

**UI tests:** `ui-tests/`

### Application

The project includes the application/API implementation used as the testing target.

**Application:** `app/`

### Documentation

Supporting project documentation and QA materials are maintained in:

**Documentation:** `docs/`

### Current Implementation Scope

The implemented application and automated tests currently focus on product
CRUD operations, product input validation, PostgreSQL data checks, health
checks, and product-list UI verification. Shopping-cart, customer,
authentication, and order workflows are not currently implemented in this
project and should be treated as future scope rather than completed coverage.

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
├── tests/
│   ├── api/                   # CRUD, request-validation, and not-found tests
│   ├── database/              # PostgreSQL persistence tests
│   └── ui/                    # HTML-safety regression test
├── ui-tests/                  # Playwright browser automation
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
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m playwright install chromium
```

On Linux systems that need Playwright browser libraries, use `python -m playwright install --with-deps chromium` if you have permission to install system packages.

Copy `.env.example` to `.env` and replace the example database connection details with your local PostgreSQL credentials. Keep `.env` private; it is ignored by Git. Use a **dedicated test database** because the tests create, update, and delete records.

Create a test database (example role: `postgres`):

```bash
createdb -U postgres qa_platform_test
```

Initialize the schema:

```bash
psql -U postgres -d qa_platform_test -f database/schema.sql
```

Seed the product expected by the UI test. This is safe to repeat in the test database:

```bash
psql -U postgres -d qa_platform_test -c "INSERT INTO products (name, description, price, stock_quantity) SELECT 'Postman QA Product', 'UI test fixture', 79.99, 15 WHERE NOT EXISTS (SELECT 1 FROM products WHERE name = 'Postman QA Product');"
```

Set `DATABASE_URL` in the terminal used to run the app and tests. The example uses a local PostgreSQL role named `postgres`:

```bash
export DATABASE_URL="postgresql+psycopg2://postgres:YOUR_PASSWORD@127.0.0.1:5432/qa_platform_test"
```

Replace `YOUR_PASSWORD`; URL-encode reserved characters in the password if necessary. Alternatively, put the local connection string in the ignored `.env` file.

Start the app from the repository root:

```bash
uvicorn app.main:app --host 127.0.0.1 --port 8000
```

In a second terminal with the same virtual environment and `DATABASE_URL`:

```bash
pytest -v
```

The app health endpoint is [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health); interactive API docs are at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## Implemented endpoints

| Method | Path | Purpose |
|---|---|---|
| GET | `/` | Application status message |
| GET | `/health` | Health check |
| GET | `/api/products/` | List products |
| POST | `/api/products/` | Create a product |
| GET | `/api/products/{product_id}` | Retrieve a product |
| PUT | `/api/products/{product_id}` | Update a product |
| DELETE | `/api/products/{product_id}` | Delete a product |
| GET | `/products` | HTML product table |

## Repository guide

- `app/` — FastAPI routes, schemas, database setup, and SQLAlchemy model.
- `database/schema.sql` — PostgreSQL table definitions.
- `tests/api/` — API behavior and request-validation tests.
- `tests/database/` — database-level persistence checks.
- `tests/ui/` — server-rendered HTML escaping regression test.
- `ui-tests/` — Playwright page-object and browser tests.
- `docs/PROJECT_SPECIFICATION.md` — intended scope and roadmap, including planned features.

## CI

The workflow at `.github/workflows/qa-tests.yml` runs on pushes and pull requests to `main`, and can be started manually. It provisions a disposable PostgreSQL service, applies the schema, seeds the UI fixture, installs Python and Chromium dependencies, starts the application, and runs Pytest.

The workflow already existed and has been updated through the added HTML-escaping regression test. Check the latest GitHub Actions run for the current commit before reporting the latest code as CI-verified.

## Limitations

This is a learning and QA portfolio application, not a production-ready commerce system. It does not implement authentication/authorization, customer or order API workflows, database migrations, or production deployment hardening. The database tests mutate data, so test isolation matters. Dependencies are listed in `requirements.txt`; install them in a virtual environment.

## What it demonstrates

- Positive, negative, boundary, and not-found API checks
- Product CRUD testing and request validation
- PostgreSQL-backed data verification
- Playwright UI checks and Page Object Model
- A regression test for HTML escaping of user-controlled product names
- Git/GitHub workflow and automated test execution

## Author

**DeMarko Moore** · [GitHub: @demrkmoore-cell](https://github.com/demrkmoore-cell)
