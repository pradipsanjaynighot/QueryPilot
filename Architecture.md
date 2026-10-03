# QueryPilot Architecture

## Overview

QueryPilot is a production-oriented Natural Language to SQL system.

It allows users to ask questions about their database using natural language. The system analyzes the request, determines whether clarification is required, understands the database schema, generates SQL, validates the query for safety, executes it against PostgreSQL, and returns a human-readable response.

---

## System Architecture

```text
User
  ↓
Natural Language Question
  ↓
Intent Analysis
  ↓
Is information missing?
  ├── YES → Clarification Engine
  │           ↓
  │       User answers
  │           ↓
  └────────→ Continue
              ↓
       Database Schema
              ↓
        LLM / Text-to-SQL
              ↓
        SQL Validation
              ↓
         PostgreSQL
              ↓
         Query Result
              ↓
     Human-readable Answer

##  Request Flow

POST /query
  ↓
Query Controller
  ↓
Request Validation
  ↓
Intent Analysis
  ↓
Clarification Engine
  ↓
Schema Service
  ↓
LLM Service
  ↓
SQL Service
  ↓
Safety Validation
  ↓
Database Service
  ↓
Result Processing
  ↓
Response



Core Design Principles
1. Schema-Aware SQL Generation

QueryPilot should understand the available database tables and columns before generating SQL.

This reduces incorrect SQL generation caused by missing schema information.

2. Clarification Engine

QueryPilot should not blindly guess when a user's request is ambiguous.

For example:

User:
Show me the best customers.

The system may ask:

What do you mean by "best"?

1. Highest spending
2. Most orders
3. Most recent customers

The user can then provide the missing information before SQL generation continues.

3. SQL Validation

Generated SQL must be validated before execution.

The system should detect potentially dangerous or unsupported operations instead of blindly executing generated SQL.

4. PostgreSQL Integration

QueryPilot uses PostgreSQL as the database layer.

SQLAlchemy is used for database interaction.

5. Structured Data

Pydantic models are used to validate requests, responses, and internal data structures.

Example Queries
Example 1
User:
Show me all customers from Mumbai.

Possible SQL:

SELECT *
FROM customers
WHERE city = 'Mumbai';
Example 2
User:
How many customers do we have?

Possible SQL:

SELECT COUNT(*)
FROM customers;
Example 3
User:
Delete all customers.

This request should not be executed blindly.

The safety layer should detect the destructive operation and apply the project's safety rules.

Technology Stack
Python
PostgreSQL
SQLAlchemy
Pydantic
LLM API
python-dotenv
Git / GitHub
Development Phases
Project Setup
Architecture
Models
Services
Controllers / State
Screens
Widgets
Navigation
AI / NLP
Hardware Communication
Firebase
Safety
Testing
Documentation
Final Build

### 4. Save it

```