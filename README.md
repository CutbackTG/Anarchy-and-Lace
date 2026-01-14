# Anarchy-and-Lace
High fashion apparel website featuring one-off bespoke items and a stripe payment system

### GitHub: @CutbackTG
### Project Link: https://github.com/CutbackTG/Anarchy-and-Lace
### Deployment URL: 

## Project Overview

Anarchy & Lace is a fully functional boutique e-commerce web application designed to showcase and sell bespoke garments created from vintage Japanese kimono fabrics. The project combines a refined, design-led user experience with robust backend functionality to support product management, secure authentication, and online payments.

The application is built using the Django web framework and follows a modular app structure to separate concerns such as product cataloguing, user authentication, shopping cart functionality, and administrative management. The site is deployed on Heroku, enabling scalable hosting and continuous deployment, and integrates Stripe to provide secure, real-world payment processing.

Visitors can browse products and featured materials without creating an account, allowing them to explore the boutique’s aesthetic, craftsmanship, and pricing freely. Registered users can create accounts, log in securely, and maintain a persistent shopping cart, ensuring a smooth and uninterrupted shopping experience across sessions. Stripe integration allows customers to complete purchases safely using industry-standard payment methods.

From an administrative perspective, Anarchy & Lace includes a secure manager interface that enables the boutique owner to create, edit, and manage products without modifying code. This includes updating product descriptions, prices, and availability, ensuring the store can be maintained efficiently as inventory evolves.

In addition to core e-commerce functionality, the platform places a strong emphasis on storytelling and material provenance. A curated fabric gallery and supporting content allow design-focused customers to explore the history and craftsmanship of kimono textiles, supporting informed purchasing decisions and commission enquiries.

### Core Features

#### Public Browsing

Visitors can browse the boutique’s product catalogue without creating an account.
Featured kimono fabrics are showcased through a curated gallery that highlights material quality and craftsmanship.
Clear navigation allows users to explore products, fabric history, and contact information freely.

#### User Authentication & Accounts

Users can create accounts using email-based registration.
Secure login and logout functionality is provided through Django Allauth.
Returning users can access their accounts and resume activity without data loss.

#### Shopping Cart & Checkout

Authenticated users can add products to a persistent shopping cart.
Cart contents are retained between sessions for returning customers.
Users can review, update, and remove items before proceeding to checkout.

#### Secure Payments

Stripe integration enables secure online payments using industry-standard payment methods.
Payment processing is handled externally to ensure sensitive card data is never stored on the application server.
Successful transactions trigger order confirmation workflows.

#### Product & Inventory Management

A secure manager interface allows authorised users to manage the product catalogue.
Products can be created, edited, and removed without modifying application code.
Pricing, descriptions, and availability can be updated dynamically.

#### Design & Theming

A custom glass-inspired design system creates a distinctive boutique aesthetic.
Light and dark themes are supported and can be toggled by the user.
Responsive layouts ensure usability across desktop, tablet, and mobile devices.

#### Storytelling & Commission Enquiries

Informational content explores the history and cultural significance of kimono fabrics.
Design-focused users can engage with material storytelling before making commission enquiries.
The platform supports both direct purchasing and bespoke commission interest.

## Future Development Roadmap

| Feature Area | Description | Priority | Intended Outcome |
|-------------|-------------|----------|------------------|
| Wishlist Functionality | Allow registered users to save products to a personal wishlist for future reference. | High | Improve user retention and support considered purchasing decisions. |
| Order History & Tracking | Provide users with access to previous orders and current order statuses. | High | Enhance post-purchase experience and transparency. |
| Commission Request System | Introduce structured commission enquiry forms with supporting details and attachments. | Medium | Support bespoke garment requests and streamline communication with customers. |
| Enhanced Fabric Archive | Expand the fabric gallery into a searchable archive with detailed historical and material metadata. | Medium | Strengthen storytelling, education, and brand identity. |
| User Reviews & Testimonials | Enable customers to leave reviews and ratings on purchased products. | Medium | Build trust and provide social proof for new customers. |
| Analytics & Reporting | Add dashboards for tracking sales, popular products, and user engagement. | Low | Support data-driven business and marketing decisions. |
| Performance & Scalability Improvements | Optimise database queries, caching, and media delivery for increased traffic. | Low | Ensure long-term scalability and site reliability. |

### Tech Stack

Backend

Python — Core programming language used for application logic and server-side processing.
Django — High-level web framework providing URL routing, view handling, authentication, and ORM-based database management.
Django Allauth — Handles user authentication, registration, and account management using email-based login.
Stripe API — Integrated to provide secure, real-world payment processing for online purchases.

Frontend

HTML5 — Used to structure all pages and templates within the application.
CSS3 — Custom-written stylesheets implementing a responsive, glass-inspired design system with light and dark themes.
JavaScript (Vanilla) — Provides client-side functionality such as theme toggling and interactive UI elements.

Database

PostgreSQL — Primary relational database used in production for storing users, products, orders, and cart data.
SQLite — Lightweight database used during local development and testing.

Hosting & Deployment

Heroku — Cloud platform used to host the application, manage environment variables, and handle deployment.
Gunicorn — WSGI HTTP server used to serve the Django application in production.
Whitenoise — Serves static files efficiently within the Heroku environment.

Development & Tooling

Git & GitHub — Version control and source code management.
Python Virtual Environments (venv) — Isolated dependency management during development.
Pip — Dependency installation and management.
VS Code — Primary development environment.

Security & Configuration

Environment Variables (.env / Heroku Config Vars) — Secure storage of sensitive configuration such as secret keys and Stripe credentials.
Django CSRF Protection — Built-in protection against cross-site request forgery.
HTTPS (via Heroku) — Secure encrypted connections in production.

## Deployment & Configuration

The application is deployed on Heroku with environment-based configuration.
Static assets are served efficiently using Whitenoise.
Sensitive credentials (e.g. Stripe keys) are stored securely using environment variables.

## User Stories

### 1. New User — Browsing the Collection

As a first-time visitor,
I want to browse the boutique’s products and featured fabrics without creating an account,
so that I can explore the aesthetic, materials, and pricing before deciding whether to engage further.

### 2. Interested Customer — Creating an Account

As an interested customer,
I want to create an account using my email address,
so that I can save my details, and return easily in the future.


### 3. Returning Customer — Shopping

As a returning customer,
I want to log in and access my saved shopping cart,
so that I can continue shopping without losing items I previously selected.


### 4. Boutique Owner / Manager — Managing Products

As a boutique manager,
I want to create, edit, and manage products through a secure manager interface,
so that I can update stock, pricing, and product details without modifying code.

### 5. Design-Focused Customer — Exploring Materials & commission work

As a design-conscious customer,
I want to explore the history of kimono fabrics,
so that I can appreciate the materials and craftsmanship behind the garments before asking about some commission work.

## Table of expectations

| Persona | Description | Primary Goals | Key Actions in Anarchy & Lace |
|--------|-------------|---------------|-------------------------------|
| New User | A first-time visitor exploring the site without creating an account. | Explore the boutique’s aesthetic, materials, and pricing before committing. | - Browse product listings<br>- View featured fabrics on the homepage<br>- Navigate the site without signing up |
| Interested Customer | A visitor who decides to engage further with the boutique. | Create an account to save details and return easily in the future. | - Register using an email address<br>- Log in securely<br>- Access account-based features |
| Returning Customer | A registered user returning to continue shopping. | Resume shopping without losing previously selected items. | - Log in to an existing account<br>- View and manage saved shopping cart<br>- Proceed to checkout |
| Boutique Manager | The owner or administrator managing the online boutique. | Maintain and update products without modifying application code. | - Access the secure manager interface<br>- Create, edit, and remove products<br>- Update stock levels, pricing, and descriptions |
| Design-Focused Customer | A customer interested in the cultural and material history behind the garments. | Learn about kimono fabrics and craftsmanship before enquiring about commission work. | - Explore fabric history and material content<br>- Navigate to contact or commission enquiry options |

## UI & UX Design

## Strategy Plane


Target Audience:
Business Goal: 
Scope Plane
Goal:

Must-have Features: 
Should-have Features: 
Could-have Features: 
Structure Plane
Goal: 

## Skeleton Plane
Goal: 

## Surface Plane
Goal: 

Theme: 
Typography: 
Colour Palette: 
Visual Goal: 

## Accessibility Considerations

## Wireframes

### Homepage
### Homepage wireframe concept
### wireframe concept
### Signup / Login
### Signup/Login wireframe concept
### wireframe concept

## Colour Scheme

## Anarchy & Lace colour scheme

## Testing colour scheme on Huemint.

## Url to View Map

## Defensive Design & Security


## Authentication & Access Control

## Test Documentation

## Lighthouse Scores & W3C Validation checks

### Performance & Accessibility

### Homepage index.html

### index.html lighthouse score

### index.html W3C valiadation check

## Summary of Automated Testing

### Django Unit Tests	pytest / TestCase	
### Test Runs

### Automated Test Cases (Django / Pytest)
Area	Test	Expected Result


## Installation & Deployment


## Contribution Guidelines


## Credits & Acknowledgements

