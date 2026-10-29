# E-commerce True Profit & Demand Forecasting Dashboard
## Project Scope, Decisions, and Initial Technical Plan

**Status:** Planning / pre-MVP  
**Primary goal:** Build an interactive, data-driven B2B web application that helps e-commerce businesses understand true profitability, forecast demand, and make better inventory decisions.  
**Cost constraint:** Use free and open-source tools and free-tier services wherever possible. Do not introduce paid APIs or paid dependencies into the initial plan.

---

## 1. Product Vision

Build an **E-commerce True Profit & Demand Forecasting Dashboard** that helps sellers answer questions such as:

- Which products actually make us money after all relevant costs?
- Why did profit increase or decrease?
- What might demand look like over the coming days, weeks, or months?
- Which products could run out of stock or become overstocked?
- How do festivals, seasonality, promotions, and changing market conditions affect demand?
- What happens to profit if prices, advertising costs, or shipping expenses change?

The product should become a professional B2B SaaS platform, but the first version will focus on validating the core analytics.

## 2. Target Customers

**Decision:** Support e-commerce businesses across industries, starting with India and expanding globally later.

Potential customers include:
- Amazon and Flipkart sellers
- Shopify and independent online-store owners
- Direct-to-consumer (D2C) brands
- Sellers of clothing, electronics, beauty products, household goods, festive products, and other categories

**Rollout principle:** Design a flexible architecture, but validate the product with real sellers and a clearly defined initial customer segment before attempting to support every industry equally well.

## 3. Data Input Strategy

**Decision:** Start with CSV/Excel uploads and add platform integrations later.

The initial upload workflow should:
1. Accept documented CSV/Excel templates.
2. Validate required columns and data types.
3. Detect missing values, duplicates, invalid dates, and inconsistent currencies.
4. Identify returns, refunds, discounts, cancellations, and stockouts where the data supports it.
5. Show validation errors and warnings before processing.
6. Let users review and correct problems rather than silently guessing.
7. Store the validated data securely and associate it with the correct business account.

Later, add platform integrations when technically feasible, permitted by the platform, and justified by customer demand.

## 4. Core Product Modules

### 4.1 True-Profit Analytics

Calculate product-level and business-level profitability, including relevant items such as:
- Gross sales and discounts
- Refunds and returns
- Cost of goods sold (COGS)
- Marketplace/payment fees
- Shipping and fulfilment
- Packaging
- Advertising expenditure
- Other seller-entered operating expenses

Allocate shared expenses using transparent, configurable rules. For example, advertising might be assigned using campaign/product attribution where available; shared shipping or overhead may need a defined allocation basis.

**Important:** Do not claim an exact “true profit” figure if the uploaded data omits important costs. Show the calculation, assumptions, excluded costs, and data completeness. Distinguish product contribution profit from overall business net profit.

### 4.2 Demand Forecasting

Predict product demand at suitable daily, weekly, or monthly horizons, depending on data volume and quality.

Potential model inputs:
- Historical sales
- Day-of-week and month-of-year patterns
- Festival and public-holiday dates
- Seller-entered promotions and price changes
- Product availability and stockouts
- Weather or other external signals when relevant and available
- Recent trend changes
- Other verified data sources that can be used legally and reliably

Use simple baselines as well as more advanced models. Evaluate models with chronological backtesting rather than randomly shuffling time-series observations.

### 4.3 Inventory Intelligence

Use forecasts, current stock, lead times, and business rules to provide:
- Potential stockout warnings
- Overstock risk indicators
- Suggested reorder timing and quantity
- Seasonal preparation reminders
- Clear explanations of the assumptions behind recommendations

Recommendations must account for supplier lead time, minimum order quantities, current stock, and other constraints when those details are available. Avoid presenting unsupported estimates as facts.

### 4.4 Interactive Dashboard

Provide:
- Revenue, profit, costs, and margin KPIs
- Product-level profitability rankings
- Expense breakdowns
- Sales and profit trends
- Forecast charts with uncertainty ranges
- Inventory risk and reorder views
- Date, product, category, and channel filters
- Drill-downs from summary KPIs to supporting transactions
- Data-quality and forecast-reliability indicators

### 4.5 AI Business Assistant (Later Phase)

Potential questions users could ask:
- “Why did my profit fall this month?”
- “Which products should I prepare for before Diwali?”
- “What happens to profit if advertising costs rise by 10%?”
- “Which products might become unprofitable next month?”

Build this after the underlying calculations and forecasts are validated. The assistant should answer from the business’s actual data, show its supporting calculations, and acknowledge when it cannot answer reliably.

## 5. Market-Aware and Adaptive Forecasting

**Decision:** Use an adaptive, market-aware approach, implemented in phases and using free data sources initially.

Historical sales alone may miss major changes. For example, a fireworks/crackers seller may have a large seasonal sales spike around Diwali and much lower sales in other periods.

The forecasting system should:
- Include seasonal and festival features when relevant.
- Use seller-provided promotion, pricing, and stock information.
- Incorporate public datasets and free APIs only when available, relevant, reliable, and permitted.
- Track data source, freshness, missingness, and limitations.
- Compare forecasts with actual outcomes and measure errors over time.
- Detect significant forecast misses or changes in demand.
- Re-evaluate models when enough new data is available.

Do not assume competitor prices, market demand, or comparable-product data can always be obtained. Use such signals only when genuinely available and allowed by the source's terms.

## 6. Forecast Trust and Accuracy

**Decision:** Use risk-aware predictions rather than a single unexplained number.

The dashboard should show, where supportable:
- Expected forecast
- Prediction intervals or clearly labelled scenarios
- Historical accuracy on relevant test periods
- Data completeness and freshness
- Warnings when there is too little history
- Warnings for unusual market conditions or major recent forecast errors
- The assumptions and signals used by the model

Prediction intervals are not guarantees. Accuracy metrics and uncertainty estimates should be calibrated and explained. Do not claim a forecast is reliable simply because an ML model generated it.

When data is insufficient, use a hybrid approach:
- Show descriptive analytics that the available data supports.
- Use simple baselines where appropriate.
- Incorporate relevant seasonal calendars or external signals when available.
- Use comparable-product data only when it is real, relevant, and accessible.
- Clearly label unsupported forecasts and avoid false precision.

## 7. Technology Architecture

### Frontend
- **Next.js + TypeScript**
- **Tailwind CSS**
- **Plotly.js** for interactive charts and visual analysis

Why: This supports a polished, responsive, interactive web interface with reusable components and a path toward a multi-customer SaaS.

### Backend and Analytics
- **Python + FastAPI** for API endpoints and business logic
- **Pandas + NumPy** for data cleaning and calculations
- **Scikit-learn + statsmodels** for appropriate modelling and evaluation

Why: Python has a mature analytics ecosystem and allows the forecasting engine to be developed and tested separately from the user interface.

### Database and Storage
- **PostgreSQL** as the primary relational database
- Object/file storage for original uploads and processed artifacts when needed

Why: PostgreSQL is a strong default for business records, relationships, reporting, and multi-tenant application data.

### Background Jobs
- Start with a simple worker process and job-status tracking.
- Add **Celery + Redis** if and when background workloads justify them.
- Keep data ingestion, validation, profit calculations, forecasting, and model evaluation as distinct modules.

Why: Large uploads and forecasts should not block normal dashboard requests. However, avoid unnecessary distributed infrastructure during the early MVP.

### Version Control
- **Git + GitHub**

Why: Enables change tracking, collaboration, backups, and deployment workflows.

## 8. Hosting and the Free-Cost Strategy

**Decision:** Develop locally first, then use Cloudflare for the frontend where appropriate and a separate environment for Python analytics.

Possible initial approach:
1. Develop and test the frontend, backend, and database locally.
2. Deploy the frontend on a suitable Cloudflare free-tier service.
3. Run the Python FastAPI backend locally during development.
4. Before public customer testing, choose an online backend and database environment that fits available free tiers and workload limits.
5. Reassess hosting when real usage, reliability, or security needs exceed free-tier capabilities.

Cloudflare is suitable for frontend hosting and lightweight request handling. It should not be assumed to be the environment for long-running Python forecasting jobs. Cloudflare Workers and other Cloudflare products have distinct capabilities, limits, and pricing terms; verify current official documentation before deployment.

Official documentation:
- Cloudflare Pages: https://developers.cloudflare.com/pages/
- Cloudflare Workers pricing and limits: https://developers.cloudflare.com/workers/platform/pricing/
- Cloudflare D1: https://developers.cloudflare.com/d1/
- Cloudflare R2: https://developers.cloudflare.com/r2/

**Cost policy:**
- Use open-source software and free-tier services wherever possible.
- Do not add paid APIs or paid services as dependencies in the initial product.
- Check terms, quotas, sleep behaviour, data limits, and usage restrictions for every free service.
- Treat free-tier limits as constraints, not a guarantee of permanent zero cost.
- Do not promise that a production SaaS with multiple customers can run forever at ₹0.

## 9. Suggested Build Sequence

### Phase 1 — Data Foundation
- Define the CSV/Excel data schema and example templates.
- Implement upload, validation, duplicate detection, and error reporting.
- Define order, order-line, product, expense, refund, and inventory data structures.
- Decide how to handle time zones, currencies, discounts, returns, and cancellations.

### Phase 2 — Profit Engine
- Implement documented revenue and cost calculations.
- Add configurable shared-expense allocation.
- Build test cases for refunds, partial returns, discounts, fees, and missing costs.
- Reconcile results against manually verified sample calculations.

### Phase 3 — Interactive Dashboard
- Build KPI cards, filters, trend charts, expense breakdowns, and product tables.
- Allow drill-down from totals to the data supporting them.
- Add data-quality indicators and transparent calculation details.

### Phase 4 — Forecasting Engine
- Establish naive and seasonal-naive baselines.
- Add appropriate forecasting models.
- Use chronological backtesting and suitable metrics.
- Show prediction ranges and reliability warnings where supportable.
- Test seasonal cases such as Diwali demand rather than relying on overall average accuracy.

### Phase 5 — Inventory Intelligence
- Incorporate stock on hand, supplier lead times, and reorder constraints.
- Produce explainable stockout and overstock warnings.
- Clearly label recommendations that depend on missing inputs.

### Phase 6 — Market Signals and Adaptive Evaluation
- Add free public data sources where useful and permitted.
- Collect seller-entered promotions, pricing, and planned stock changes.
- Monitor forecast errors and data freshness.
- Re-evaluate models as new data becomes available.

### Phase 7 — AI Business Assistant
- Answer questions using validated metrics and forecasts.
- Show supporting calculations and data sources.
- Refuse to invent explanations when the data cannot support an answer.

### Phase 8 — Public SaaS Readiness
- Add authentication, tenant isolation, permissions, backups, and audit logging.
- Protect uploaded data and secrets.
- Add rate limits, monitoring, error handling, and deployment automation.
- Evaluate subscriptions and platform integrations only after product validation.

## 10. Product Quality Principles

1. **Accuracy over impressive-looking AI:** validate calculations and forecasts.
2. **Transparency:** expose assumptions, exclusions, and data quality.
3. **No invented market data:** every external signal must have a real source.
4. **Graceful handling of missing data:** warn users instead of silently guessing.
5. **Interactive and explainable:** users should be able to investigate results.
6. **Security from the start:** isolate each business’s records and protect uploads.
7. **Modular architecture:** replace or scale components without rebuilding everything.
8. **Free-first implementation:** use free/open-source options, but be honest about limits.
9. **Incremental complexity:** add queues, integrations, and infrastructure only when justified.
10. **Real-world validation:** test with actual sellers and reconciled data before making performance claims.

## 11. Current Decisions Summary

| Topic | Decision |
|---|---|
| Target market | E-commerce businesses across industries; start in India, expand later |
| Data ingestion | CSV/Excel first; integrations later |
| Core capabilities | True profit + demand forecasting + inventory intelligence |
| Profit calculation | Advanced cost coverage and transparent shared-expense allocation |
| Forecasting | Adaptive, market-aware, seasonal, and risk-aware |
| User roles | Business owners, finance teams, and inventory teams |
| Initial product | Interactive web application MVP |
| Architecture | Next.js + TypeScript + FastAPI + PostgreSQL + analytics pipeline |
| Data processing | Pandas + NumPy |
| Forecasting libraries | Scikit-learn + statsmodels, selected based on evaluation |
| Background processing | Add a worker/queue approach incrementally |
| Charts | Plotly.js |
| Hosting | Cloudflare for suitable frontend hosting; separate Python runtime |
| Budget | Free/open-source and free-tier services initially |
| AI assistant | Later phase, after core metrics and forecasts are validated |

## 12. Immediate Next Step

Before writing the forecasting model, define and validate the **data model and true-profit formula**. The model needs a consistent definition of an order, product, refund, expense, advertising cost, and inventory movement.

The first deliverable should be a small, documented CSV/Excel template plus a test dataset with known expected profit results. This provides a reliable foundation for every later dashboard and forecasting feature.

---

**Project note:** This document records the decisions and proposed architecture from the planning discussion. Library choices, hosting limits, and free-tier terms should be rechecked against official documentation when implementation begins.
