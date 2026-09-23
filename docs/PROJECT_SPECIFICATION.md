# QA API Test Platform

## Project Overview

A backend-focused QA portfolio project demonstrating end-to-end software quality practices across REST API testing, Python automation, PostgreSQL database validation, UI automation, CI/CD, defect tracking, and AI-assisted development.

## Application Domain

Order Management System

The application models a simplified e-commerce backend where customers can purchase products through orders.

## Primary Entities

- Customers
- Products
- Orders
- Order Items

## Core Workflow

1. A customer registers or is created.
2. Products are available for purchase.
3. An authenticated customer creates an order.
4. Products are added to the order with quantities.
5. The system calculates the order total.
6. Order data is stored in PostgreSQL.
7. The API returns the resulting order information.
8. QA validates the behavior through API, database, and UI testing.

## Technology Stack

### Application
- Python
- FastAPI
- Pydantic
- SQLAlchemy

### Database
- PostgreSQL
- SQL validation

### API Testing
- Postman
- Python
- Pytest
- Requests / HTTPX

### UI Testing
- Playwright
- Pytest
- Page Object Model

### DevOps
- Git
- GitHub
- GitHub Actions

### Defect Management
- Jira

### AI-Assisted Development
AI tools may be used to assist with requirements exploration, implementation, test development, debugging, refactoring, and documentation.

All AI-assisted work will be independently reviewed and validated before being accepted into the project.

## Initial API Scope

### Authentication

- POST `/api/auth/register`
- POST `/api/auth/login`

### Products

- GET `/api/products`
- POST `/api/products`
- GET `/api/products/{id}`
- PUT `/api/products/{id}`
- DELETE `/api/products/{id}`

### Customers

- GET `/api/customers`
- POST `/api/customers`
- GET `/api/customers/{id}`
- PUT `/api/customers/{id}`

### Orders

- GET `/api/orders`
- POST `/api/orders`
- GET `/api/orders/{id}`
- PUT `/api/orders/{id}`
- DELETE `/api/orders/{id}`

### Order Items

- POST `/api/orders/{order_id}/items`
- GET `/api/orders/{order_id}/items`
- DELETE `/api/orders/{order_id}/items/{item_id}`

## Business Rules

### Products

- Product name is required.
- Product price must be greater than zero.
- Stock quantity cannot be negative.

### Customers

- Customer name is required.
- Customer email is required.
- Customer email must use a valid format.
- Customer email must be unique.

### Orders

- An order must belong to an existing customer.
- An order must contain at least one valid product before checkout.
- Order item quantity must be greater than zero.
- Order item quantity cannot exceed available stock.
- Order totals must equal the sum of all order item subtotals.
- Deleted or nonexistent products cannot be added to an order.

### Authentication

- Protected endpoints require valid authentication.
- Invalid credentials must be rejected.
- Invalid or missing authentication tokens must be rejected.

## Database Model

### customers

- id
- name
- email
- created_at

### products

- id
- name
- description
- price
- stock_quantity
- created_at

### orders

- id
- customer_id
- status
- total
- created_at

### order_items

- id
- order_id
- product_id
- quantity
- unit_price
- subtotal

## QA Strategy

Testing will be performed in multiple layers:

1. Manual functional testing
2. Postman API testing
3. Python/Pytest API automation
4. SQL/database validation
5. Playwright UI automation
6. GitHub Actions CI execution
7. Jira defect tracking

## Planned Negative and Boundary Testing

Examples include:

- Invalid product IDs
- Missing required fields
- Invalid email formats
- Duplicate customer emails
- Negative product prices
- Negative stock quantities
- Zero order quantities
- Quantities exceeding available stock
- Nonexistent customers
- Nonexistent products
- Invalid authentication credentials
- Missing authentication tokens
- Invalid order IDs
- Malformed request payloads

## Planned Defect Investigation

The project will include deliberate defects or controlled failure scenarios where appropriate so that the QA workflow demonstrates:

- Defect detection
- Reproduction
- Expected versus actual behavior
- Root-cause investigation
- Jira documentation
- Regression verification

Potential scenarios include:

- Incorrect multi-product order totals
- Incorrect stock validation
- Invalid product acceptance
- Authentication bypass behavior

## Project Phases

### Phase 1 — Specification
Define requirements, architecture, data model, business rules, and test strategy.

### Phase 2 — Backend Foundation
Build the FastAPI application structure and initial configuration.

### Phase 3 — Database
Configure PostgreSQL and implement the database model.

### Phase 4 — API
Implement authentication, product, customer, order, and order-item functionality.

### Phase 5 — Manual API Testing
Build and execute Postman test scenarios.

### Phase 6 — API Automation
Develop reusable Python/Pytest API tests.

### Phase 7 — Database Validation
Use SQL to verify backend data and business results.

### Phase 8 — UI Automation
Build Playwright tests against the application.

### Phase 9 — Defect Testing
Document and investigate controlled failures through Jira.

### Phase 10 — CI/CD
Execute automated tests through GitHub Actions.

### Phase 11 — AI-Assisted Development
Document where AI assistance was used and how generated work was independently reviewed and validated.

### Phase 12 — Portfolio Documentation
Finalize README documentation, test evidence, architecture information, and execution instructions.

## Project Goal

Demonstrate a practical QA workflow that connects requirements, application behavior, API testing, automation, database validation, UI testing, CI/CD, and defect management into one maintainable portfolio project.

The project is intended to demonstrate hands-on QA engineering development rather than claim production-level enterprise experience.
