# Technical Architecture & Stack Specification

**Status:** Approved  
**Selected Option:** Option 1 — Decoupled Web App (Next.js + FastAPI + PostgreSQL)  
**Primary Focus:** Relational data accuracy, multi-tenant integrity, and modular analytical computation under zero-cost/free-tier constraints.

---

## 1. Architectural Decision Record (ADR)

### Context & Requirements
The platform must ingest seller transaction data (orders, returns, fees, ad spend, inventory levels), enforce strict multi-tenant isolation, calculate exact true-profit metrics across multiple cost allocations, and run chronological demand forecasts with uncertainty bounds. 

Relational data accuracy, financial consistency, and strict transaction integrity are non-negotiable foundations for calculating accurate profit margins.

### Selected Architecture: Option 1 (Decoupled Web App)
We have selected **Option 1: Decoupled Next.js Frontend + Python FastAPI Backend + PostgreSQL Database**.

#### Why this architecture:
1. **Relational Data Integrity:** Financial reconciliations (orders, line items, returns, adjustments, fees) require strong foreign-key constraints, ACID compliance, and structured schemas provided natively by PostgreSQL.
2. **Separation of Concerns:** Isolates the high-velocity, UI-rich user application (Next.js) from computational data processing and machine learning models (Python).
3. **Data Science Ecosystem:** Python remains the undisputed standard for time-series forecasting (`statsmodels`, `scikit-learn`, `pandas`), avoiding fragile polyglot workarounds or foreign function calls.
4. **Independent Scalability & Free Tier Fit:** The Next.js frontend can be deployed statically/edge-hosted on Cloudflare Pages or Vercel, leaving the backend container/server to focus purely on API requests and compute workloads.

---

## 2. System Architecture

```
                      +-----------------------------+
                      |   Browser / Seller Client   |
                      +--------------+--------------+
                                     |
                                     | HTTPS
                                     v
                      +-----------------------------+
                      |       Next.js Frontend      |
                      |  (Cloudflare Pages/Vercel)  |
                      |  TypeScript + Tailwind CSS  |
                      +--------------+--------------+
                                     |
                                     | REST API (JSON)
                                     v
                      +-----------------------------+
                      |      FastAPI Backend        |
                      |  (Python 3.11+ / Async API) |
                      |    Pydantic v2 Validation   |
                      +-------+--------------+------+
                              |              |
             SQLAlchemy 2.0   |              | File Uploads
             (ACID Queries)   |              |
                              v              v
       +-------------------------+    +-----------------------+
       |   PostgreSQL Database   |    | Object / File Storage |
       | (Tenants, Orders, Costs,|    | (Raw CSV/Excel files, |
       |  Inventory, Metrics)    |    |  R2 or Local dev FS)  |
       +-------------------------+    +-----------------------+
                    ^
                    | Read / Write Processed Results
                    v
       +---------------------------------------------+
       |      Analytics & Forecasting Engine         |
       |  - Pandas & NumPy (Dataframes & Math)       |
       |  - statsmodels & scikit-learn (Forecasting) |
       |  - Async Background Worker (Lightweight)    |
       +---------------------------------------------+
```

---

## 3. Technology Stack Details

### 3.1 Frontend
- **Framework:** Next.js (React 19 / App Router, TypeScript)
- **Styling:** Tailwind CSS + shadcn/ui components
- **Charting & Visualization:** Plotly.js (or lightweight alternatives like Apache ECharts / Recharts for responsive financial and time-series drill-downs)
- **State & Data Fetching:** TanStack Query (React Query) for API caching, mutation handling, and optimistic updates
- **Deployment:** Cloudflare Pages or Vercel Free Tier

### 3.2 Backend & APIs
- **Framework:** Python FastAPI (modern async REST endpoints, automated OpenAPI/Swagger documentation)
- **Data Validation & Serialization:** Pydantic v2
- **ORM & Database Migrations:** SQLAlchemy 2.0 (declarative async/sync models) + Alembic
- **Authentication & Security:** JWT-based stateless authentication with tenant isolation checks on every route

### 3.3 Data & Forecasting Engine
- **Data Manipulation:** Pandas and NumPy for tabular transformations, group aggregations, and cost allocations
- **Time-Series & ML:** `statsmodels` (SARIMAX, Holt-Winters, seasonal baselines) and `scikit-learn` (regression baselines, feature pipelines)
- **Evaluation:** Strict chronological backtesting (sliding/expanding windows) rather than randomized train-test splits

### 3.4 Database & Storage
- **Primary Database:** PostgreSQL 15+ (relational schema, multi-tenant foreign keys, indexed financial transactions)
- **Free-Tier Host Options:** Local PostgreSQL for development; Neon, Supabase, or Railway free tier for hosted evaluation
- **File Storage:** Local filesystem storage during development; Cloudflare R2 (S3-compatible, no egress fees) for production file uploads

### 3.5 Background Processing
- **Phase 1 (MVP):** Python `asyncio` / FastAPI `BackgroundTasks` for non-blocking file validation and small-scale forecast generation.
- **Phase 2 (Scale):** Celery or ARQ backed by Redis when asynchronous workloads require persistent job retries and task queues.

---

## 4. Alternative Options Considered (Reference)

| Option | Architecture | Pros | Cons / Reason Not Selected |
|---|---|---|---|
| **Option 1 (Selected)** | **Next.js + FastAPI + PostgreSQL** | **High relational accuracy, industry-standard stack, modular ML engine, independent scalability** | **Two separate runtime services to orchestrate** |
| **Option 2** | React Vite SPA + FastAPI + DuckDB/Postgres | Extremely fast analytical aggregations on flat CSVs, zero SSR complexity | DuckDB introduces dual storage state (DuckDB files + Postgres metadata), less proven for multi-tenant concurrent writes |
| **Option 3** | Next.js + Supabase + Stateless Python Worker | Fast auth and database scaffolding out of the box | Strong vendor lock-in to Supabase; free tiers pause after inactivity; multiple communication hops |

---

## 5. Next Steps According to Plan

1. **Phase 1: Data Schema Definition**
   - Define exact schemas for `orders`, `order_items`, `products`, `expenses`, `returns_refunds`, and `inventory_snapshots`.
   - Create standardized CSV/Excel upload templates for sellers.
2. **True-Profit Mathematical Formulation**
   - Document precise formulas for Gross Profit, Net Contribution Margin, and Operating Profit.
   - Establish transparent allocation formulas for shared costs (ad spend, fulfillment, packaging, overhead).
3. **Verification Dataset**
   - Provide a sample dataset with manually verified, expected profit calculations to serve as automated regression tests.
