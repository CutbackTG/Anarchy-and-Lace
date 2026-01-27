# Anarchy-and-Lace
High fashion apparel website featuring one-off bespoke items and a stripe payment system

<img src= static/img/readme/site_white.png  alt ="Am I responsive image portraying lightmode website view on multiple devices" width= 800>
<img src= static/img/readme/site_black.png  alt ="Am I responsive image portraying darkmode website view on multiple devices" width= 800>

### GitHub: @CutbackTG
### Project Link: https://github.com/CutbackTG/Anarchy-and-Lace
### Deployment URL: https://anarchy-and-lace-0b8e43b4f722.herokuapp.com/

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
Gunicorn: WSGI HTTP server used to serve the Django application in production (via Heroku).

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
Procfile: Specifies gunicorn as the web server for the application.

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

Anarchy and Lace’s user interface (UI) and user experience (UX) share their philosophy and their material origins with the garments. Instead of using the traditional commercial aesthetic to create its UI, Anarchy and Lace needed to draw heavily on Japanese design traditions for its visual language, which include restraint, symbolism, and material honesty. Anarchy and Lace wanted to create an environment that feels more like a carefully curated gallery versus a conventional online store where the garments are represented as crafted objects that have a history and have been created for a specific purpose.

Anarchy and Lace’s design was also influenced by a number of cultural and visual cues, including Kintsugi, the Japanese art of joining broken pottery back together using gold lacquer. The use of highlighted accent lines throughout the UI is inspired by the Kintsugi philosophy and expresses the belief that history and imperfection add to the value of an object's importance rather than diminish it. This philosophy mirrors Anarchy and Lace’s practice of repurposing vintage kimono fabrics when crafting its bespoke garments. 

The layered design of samurai armour influenced the way that content blocks and cards are framed, segmented, and visually grouped together to create a feeling of strength and protection. These structured forms are softened through the use of rounded corners and subtle shadows, inspired by smooth river pebbles, creating a soft and calming counterpoint to the sharper geometric shapes that make up Anarchy and Lace’s navigation and grid structure.

The overall navigation and user flow were structured to follow a narrative journey rather than a purely transactional one.The first thing visitors will see are storytelling elements and highlighted fabrics that encourage visitors to explore and create curiosity about those items - after that, visitors move on to curated collections of various products as well as how the fabric has evolved through history for each item. 
The product detail pages contain images of the item, along with information about the item, including where it came from and what it's made of - visitors can then complete their purchase using an easy checkout system from Stripe's safe platform; this lessens the chances of getting lost in the checkout process and helps visitors to maintain the connection they built throughout the shopping experience right up until they actually make their purchase. The flow of the shopping experience is engineered to transition from appreciation to ownership with a focus on the slow fashion movement and making purchasing decisions with consideration.

The design of the interface allows for two different visual designs to be integrated within the automated theme management tool. The first design features light and is inspired by pearl lacquer, parchment, and viewing fabrics in full daylight - this design places an emphasis on presenting products as clearly as possible with an accurate representation of the colours of the fabrics and the ability to view them in a magazine-type layout. 

The second design features dark and is inspired by ink, charcoal, and nighttime views used near night markets - this design provides a more personal, intimate, gallery-like feel for browsing and reflecting on products. The two themes correspond with traditional Japan's concept of "dualities" (i.e. sun vs. moon; day vs. night; light vs. shade), and visitors can switch between the two themes whenever they like; their theme choice is remembered by the interface for future visits.

The purpose of designing garments as an art object rather than a commodity is to allow the customer an opportunity to interact and appreciate the clothing before purchasing it. By creating a balance between aesthetic beauty and e-commerce usability, the digital interface conveys a sense of calmness while providing the best possible platform for consumers to buy high-end products. The digital space reflects the artisan craftsmanship, respect for cultural heritage, and unique approach of one-of-a-kind custom clothing. This creates a relationship between digital and physical experiences so that they can be related to and understood together.

## Strategy Plane

**Target Audience:**  
Anarchy & Lace is aimed at design-conscious consumers who value craftsmanship, sustainability, and cultural provenance in fashion. The primary audience includes customers interested in one-off, bespoke garments made from vintage Japanese kimono fabrics, as well as those drawn to slow fashion and ethically minded purchasing. A secondary audience consists of boutique owners, collectors, and design enthusiasts who appreciate material storytelling and limited-edition pieces rather than mass-produced clothing.

**Business Goal:**  
The primary business goal is to create a premium digital boutique that showcases and sells bespoke garments while communicating the artistic and cultural value of the materials used. The platform is intended to demonstrate a fully functional Django-based e-commerce system, integrating secure authentication, product management, and online payments. From a technical perspective, the project aims to evidence competency in full-stack development, data-driven design, and third-party service integration, while from a brand perspective it seeks to establish trust, credibility, and emotional engagement with the customer.

---

## Scope Plane

**Goal:**  
Define and prioritise the functional and content requirements of the application to ensure a balance between aesthetic presentation and practical e-commerce usability.

**Must-have Features:**  
- Public browsing of the product catalogue without requiring an account.  
- Secure user registration and authentication.  
- Product detail pages with imagery, descriptions, and pricing.  
- Shopping cart functionality with add, update, and remove actions.  
- Stripe-integrated checkout for secure online payments.  
- Administrative interface for creating, editing, and managing products.  

**Should-have Features:**  
- Order confirmation and basic order history for authenticated users.  
- Fabric gallery and informational content describing material provenance.  
- Responsive design across desktop, tablet, and mobile devices.  
- Light and dark theme support for accessibility and personal preference.  

**Could-have Features:**  
- Wishlist functionality for saving items of interest.  
- Customer reviews and ratings for purchased products.  
- Commission request forms for bespoke garment enquiries.  
- Advanced filtering and search for fabrics and garments.  

---

## Structure Plane

**Goal:**  
Organise information and interactions in a way that feels intuitive, narrative-driven, and consistent with the boutique identity of the brand.

- Content is structured around a progression from discovery to purchase: introduction and storytelling, product exploration, detailed product views, and finally checkout.  
- Navigation follows a clear hierarchy separating public content (home, shop, fabric gallery) from user-specific functionality (cart, orders, account) and staff-only management tools.  
- Related content is grouped logically, such as pairing product pages with fabric history and care information, to support informed decision-making.  
- The overall structure is designed to minimise cognitive load while reinforcing the sense of browsing a curated collection rather than a generic catalogue.

## Skeleton Plane

**Goal:**  
Design a clear, low-friction interface that allows users to browse high-value garments, understand fabric provenance, and complete checkout with minimal effort and cognitive load.

**Layout & Structure:**
- **Global Navigation:**  
  - Sticky header with brand mark and primary navigation (Shop, Fabric Gallery, About, Contact).  
  - Account and cart icons with live item count for immediate feedback.

- **Homepage:**  
  - Hero section combining brand identity with material storytelling.  
  - Featured product grid and rotating fabric spotlight panels.  
  - Trust cues such as secure checkout messaging and “one-off item” indicators.  
  - Footer with legal links, contact details, and social presence.

- **Product Listing (Shop):**  
  - Grid-based product cards with consistent image ratios.  
  - Clear price display and scarcity markers (e.g. one-off or low stock).  
  - Filtering by category, size, and price range with optional sorting.

- **Product Detail Pages:**  
  - Prominent image gallery with zoom support.  
  - Structured content: price, availability, product story, fabric notes, and care guidance.  
  - Strong call-to-action for adding to cart and links to related items.

- **Cart & Checkout Flow:**  
  - Line-item summary with quantity controls and removal options.  
  - Transparent subtotal and total pricing.  
  - Redirect to Stripe Checkout for secure payment, returning to an order confirmation page.

- **Account Area:**  
  - Profile overview and saved preferences.  
  - Wishlist and order history (future roadmap feature).

- **Manager / Admin Interface:**  
  - Separate navigation for staff users.  
  - Clear CRUD forms for product creation, editing, stock control, and order handling.

## Surface Plane

**Goal:**  
Present a premium, editorial boutique aesthetic that communicates craftsmanship and rarity while maintaining readability and accessibility across devices.

**Theme:**  
- Modern boutique minimalism with a glass-inspired UI language.  
- Frosted panels, soft depth effects, and deliberate spacing.  
- Visual restraint influenced by Japanese design principles: balance, calm composition, and emphasis on texture.

**Typography:**  
- **Headings:**  
  - A refined serif or high-contrast display typeface to convey luxury and editorial tone.  
- **Body Text:**  
  - A clean, highly legible sans-serif font for descriptions, navigation, and form inputs.  
- **Hierarchy:**  
  - Clear H1–H3 structure with consistent spacing and rhythm.  
  - Distinct styling for prices, calls-to-action, and metadata (fabric type, size, condition).

**Colour Palette:**  
- **Base tones:** Ink black and soft charcoal for text and dark mode foundations.  
- **Light mode:** Pearl white and warm off-white backgrounds with translucent layers.  
- **Accent tones:** Muted gold or antique brass for premium highlights (buttons, dividers, star ratings).  
- **Supporting hues:** Deep plum, indigo, or forest green used sparingly to complement kimono fabrics.  
- **Functional colours:** Accessible success and error states meeting WCAG contrast guidelines.

**Visual Goal:**  
- Present each garment as if curated in a gallery: consistent framing, high-quality imagery, and calm UI composition.  
- Reinforce the “one-off bespoke” value through subtle scarcity cues and artisan notes rather than aggressive sales techniques.  
- Ensure every interaction feels deliberate and tailored, with smooth hover states, visible focus indicators, and touch-friendly controls.

## Accessibility Considerations

Anarchy & Lace emphasises general accessibility and universal use as a basic assumption in developing the site for as many users who may be unable to navigate traditional tools, such as those with visual or cognitive impairments.

As well as emulating WCAG 2.1 (Web Content Accessibility Guidelines) wherever applicable, semantic HTML5 elements were utilised throughout the website. Semantically structured markup helps provide useful document structure when using assistive technology (e.g. screen readers). For example, using semantic headings, titles according to logical levels, utilising proper navigation landmarks, pairing forms with appropriate identification labels (visible and programmatic), and so on.

Colour and contrast have been taken into account when designing the website in light and dark themes. For example, the colour and contrast of text and interactive elements has been tested to ensure that they are sufficiently contrasting against their background to be legible under various types of lighting conditions. The dual-theme nature of the website allows users who experience visual light sensitivity to utilise the site in a more comfortable "moon" theme.

All interactive components (navigation links, buttons, form inputs, theme buttons, etc.) have been designed to be usable with a keyboard. Visual focus is readily noticeable, making navigation via keyboard or assistive device easier for users to identify where they are in the interface.

To assist users in accurately populating necessary fields on forms, they incorporate clear input labels, placeholder text, and validation feedback as well as utilize descriptive error messages located alongside relevant inputs in an effort to minimize ambiguity while enhancing usability for screen reader users.

Additionally, product and editorial content uses images with descriptive alternative text if possible, ensuring that users who do not have visual access to images receive the equivalent of the product or garment context and content. Decorative images are designated correctly to mitigate extraneous auditory noise being produced by screen readers.

As part of applying responsive design principles, desktop, tablet, and mobile device accessibility were considered when designing touch targets and providing sufficient spacing between layout elements to prevent accidental user interface interactions.

Both motion and visual effects have been purposefully limited. The transitions occurring within the interface are designed intentionally and not exclusively animated in order to reduce any potential discomfort for users who may be sensitive to motion, while maintaining a calm and easy-to-read environment for users.

## Wireframes

### Homepage wireframe concept

<img src= static/img/readme/index_wireframe.png  alt ="Index.html wireframe" width= 600>

### shop wireframe concept

<img src= static/img/readme/shop_wireframe.png  alt ="product_detail.html wireframe" width= 600>

### kimono history wireframe concept

<img src= static/img/readme/kimono_wireframe.png  alt ="kimono_history.html wireframe" width= 600>

### Signup/Login wireframe concept

<img src= static/img/readme/signin_wireframe.png  alt ="login.html wireframe" width= 600>

## Colour Scheme Inspirations

<img src= static/img/readme/kintsugiwhite.jpg  alt ="white kintsugi porcelain" width= 400><img src= static/img/readme/kintsugiblack.webp  alt ="a black piece of kintsigi porcelain" width= 400>
<img src= static/img/readme/anarchylace_background_white.webp  alt ="a light kintsugi themed background" width= 400><img src= static/img/readme/anarchylace_background_black.webp  alt ="a dark kintsugi themed background" width= 400>
<img src= static/img/readme/zen_garden.png  alt ="A Japanese Zen garden" width= 600>

## Anarchy & Lace colour scheme

<img src= static/img/readme/pallette.png  alt ="Anarchy and Lace colour pallette" width= 600>

## Url to View Map

The following table outlines the main URL patterns used within the Anarchy & Lace application and their corresponding purposes. This provides a clear overview of site navigation, feature access, and responsibility separation between public users and administrative staff.

| URL Pattern | App | View Name | Purpose / Description |
|-------------|-----|-----------|------------------------|
| `/` | home | home | Landing page displaying featured products and brand introduction. |
| `/accounts/` | allauth | login / logout / signup | User authentication routes provided by Django Allauth. |
| `/shop/` | catalog | product_list | Displays the full product catalogue available for purchase. |
| `/shop/<slug>/` | catalog | product_detail | Shows detailed information for a single product, including imagery and description. |
| `/cart/` | cart | cart | Displays current shopping cart contents. |
| `/cart/add/<int:product_id>/` | cart | add | Adds a selected product to the cart. |
| `/cart/set/<int:product_id>/` | cart | set_qty | Updates the quantity of a product in the cart. |
| `/cart/remove/<int:product_id>/` | cart | remove | Removes a product from the cart. |
| `/cart/clear/` | cart | clear | Clears all items from the cart. |
| `/payments/create/` | payments | create | Creates a Stripe Checkout session for payment processing. |
| `/payments/success/` | payments | success | Displays confirmation page after successful Stripe payment. |
| `/payments/cancel/` | payments | cancel | Displays cancellation page if Stripe checkout is aborted. |
| `/orders/` | orders | order_list | Displays user order history (if authenticated). |
| `/orders/<order_number>/` | orders | order_detail | Displays full details for a specific completed order. |
| `/reviews/add/<order_number>/<int:product_id>/` | reviews | add_from_order | Allows verified purchasers to leave a review for a product. |
| `/manager/` | manager | dashboard | Staff-only dashboard for managing products and orders. |
| `/admin/` | admin | admin_site | Django administration panel for site management and data control. |

This URL structure ensures:
- Clear separation between public browsing, authenticated user actions, and administrative functions.
- Predictable routing patterns that support maintainability and scalability.
- Secure access control for sensitive routes such as order history, reviews, and management interfaces.

## Defensive Design & Security

| Check | Action | Expected Result |
|-------|--------|-----------------|
| CSRF protection | Submit POST without token | Rejected |
| Auth gating | Hit wishlist/review endpoints logged out | Redirect to login |
| Object ownership | Try editing another user’s review/order | Denied |
| Admin protection | Access /admin/ without staff | Denied |
| Secrets | Confirm no keys committed | .env ignored, keys only in config vars |
| DEBUG off | Production environment | DEBUG=False, no stack traces exposed |


### Test Documentation

## Test Runs

| Area | Scenario | Steps | Expected Result | Result | Notes / Fix if Fails |
|------|----------|-------|-----------------|--------|----------------------|
| Auth | Register account | Register via signup form | User created, redirected, session active |-| Check allauth config, email backend, templates |
| Auth | Login/logout | Login, logout, hit restricted page | Restricted page redirects to login |-| Verify LOGIN_URL, decorators/mixins |
| Catalog | Product list loads | Open shop/catalog page | Products render, images load |-| Check Cloudinary config + template context |
| Catalog | Product detail page | Click a product | Correct item details, price, imagery |-| Ensure slug/PK routing matches URLs |
| Cart | Add to cart | Add product from detail page | Cart count increases, item appears in cart |-| Check session/cart persistence logic |
| Cart | Update quantity | Increase/decrease qty in cart | Totals update, no negative qty |-| Validate form + server-side constraints |
| Cart | Remove item | Remove from cart | Item removed, totals recalculated |-| Confirm item key/ID mapping |
| Checkout | Create Stripe session | Click checkout | Redirects to Stripe Checkout |-| Check STRIPE keys + success/cancel URLs |
| Checkout | Successful payment | Use Stripe test card | Redirect to success page, order recorded, cart cleared |-| Confirm webhook/order creation flow |
| Checkout | Cancel payment | Cancel on Stripe | Redirect to cancel page, cart intact |-| Ensure cancel_url returns safely |
| Orders | Order creation | Complete payment | Order created with line items + totals |-| Confirm db models + signals/webhook |
| Reviews | Submit review | Post review as logged-in user | Review saved + displayed (or moderated) |-| Confirm permissions + validation |
| Wishlist | Add/remove wishlist | Toggle wishlist button | Wishlist updates for user |-| Ensure login required + unique constraints |
| Admin | Product CRUD | Admin add/edit/delete product | Changes reflect on frontend |-| Ensure staff-only access + correct model admin |
| Security | Access control | Try editing admin/manager views as user | Denied or redirected |-| Check decorators, staff checks, middleware |
| Static/Media | Static files | Load site CSS/JS | Styling works in production |-| Whitenoise, collectstatic, STATIC settings |
| Responsive | Mobile layout | Test at 375px/768px | Nav usable, cards don’t overflow |-| Fix breakpoints, long titles, image scaling |


## Lighthouse Scores

### Homepage index.html

<img src= static/img/readme/index.png  alt ="Index.html" width= 600>

### index.html lighthouse score

<img src= static/img/readme/index_lighthouse.png  alt ="Index.html Lighthouse score" width= 600>

### Kimono History Page

<img src= static/img/readme/kimono.png  alt ="kimono_history.html" width= 600>

### kimono_history.html Lighthouse score

<img src= static/img/readme/kimono_lighthouse.png  alt ="kimono_history.html Lighthouse score" width= 600>

### Shop product_list.html

<img src= static/img/readme/shop.png  alt ="product_list.html" width= 600>

### product_list.html lighthouse score

<img src= static/img/readme/shop_lighthouse.png  alt ="product_list.html Lighthouse score" width= 600>

### Sign-in/ Sign-up Page

<img src= static/img/readme/signin.png  alt ="login.html" width= 600>

### login.html Lighthouse score

<img src= static/img/readme/signin_lighthouse.png  alt ="login.html Lighthouse score" width= 600>


## Summary of Automated Testing

| Test Category | Tool | Coverage Focus | Result |
|---------------|------|----------------|--------|
| Django unit tests | django.test.TestCase | Models, views, forms, permissions | PASS |
| Stripe/webhook logic | TestCase + mocks | Signature verify, order creation, cart clearing | PASS |
| URL resolution | reverse() | Named routes correct, status codes | PASS |
| Form validation | TestCase | Rating bounds, required fields, qty rules | PASS |
| Linting (optional) | Flake8 | Style + obvious mistakes | PASS

## Automated Test Cases (Models)

| Area | Test | Steps | Expected Result |
|------|------|-------|-----------------|
| Catalog Product | Create product | Create Product instance | Saves correctly, slug/fields valid |
| Order | Create order with totals | Create Order + OrderLineItem(s) | Totals computed correctly |
| Review | Rating validation | Create Review with rating outside bounds | Validation fails / form errors |
| Wishlist | Unique constraint | Add same product twice | Only one entry exists / prevented |

## Automated Test Cases (Views & Permissions)

| Area | Test | Steps | Expected Result |
|------|------|-------|-----------------|
| Catalog list | Public access | GET product list | 200 OK, template used |
| Product detail | Public access | GET detail route | 200 OK, correct object |
| Cart add | Auth required (if applicable) | POST add-to-cart | Redirect/login OR success |
| Checkout start | Auth required | GET checkout session creation | Redirects to Stripe |
| Review submit | Login required | POST review | 302 to login if anonymous; saves if logged-in |
| Manager/admin pages | Staff-only | GET manager routes as non-staff | 403 or redirect |

### Django Unit Tests	pytest / TestCase	

| Area | Test File | What It Verifies |
|------|----------|------------------|
| Smoke | core/tests/test_smoke.py | Key pages return 200 and render expected templates |
| Catalog | catalog/tests/test_catalog_views.py | Product list and detail pages load and show product content |
| Cart | cart/tests/test_cart.py | Add/update/remove cart actions update session state correctly |
| Reviews | reviews/tests/test_reviews.py | Login required for review submission; rating validation works |
| Payments | payments/tests/test_stripe_checkout.py | Stripe checkout session creation is called (mocked) without external requests |

### Problems

Google Chrome flags the Heroku based project as "dangerous" even though our stripe system is in a dev sandbox state.
Please see attached certificate for validation of Heroku as the source for this flag.

<img src= static/img/readme/dangerous_cert.png  alt ="Google danger flag" width= 400>

## Installation & Deployment

Prerequisites

Ensure you have the following installed:
Python 3.12 or higher
pip (Python package manager)
Git
A code editor (VS Code, PyCharm, etc.)

Setup Instructions

Clone the repository:
``` bash
git clone https://github.com/CutbackTG/Anarchy-and-Lace.git
cd Anarchy-and-Lace
```

Create a virtual environment:
``` bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install dependencies:
``` bash
pip install -r requirements.txt
```

Setup environment variables:
Create a .env file with the following settings:

DJANGO_SECRET_KEY=your-secret-key
STRIPE_PUBLIC_KEY=your-public-key
STRIPE_SECRET_KEY=your-secret-key
DEBUG=True


Run migrations:
``` bash
python manage.py migrate
```

Run the development server:
``` bash
python manage.py runserver
```

Visit: http://127.0.0.1:8000

## Contribution Guidelines

Fork the repository and clone your fork:
``` bash
git clone https://github.com/YOUR-USERNAME/Anarchy-and-Lace.git
```

Create a feature branch:
``` bash
git checkout -b feature/your-feature-name
```

Commit your changes:
``` bash
git commit -m "Add: description of your feature"
```

Push to your fork:
``` bash
git push origin feature/your-feature-name
```

Create a pull request with a clear description of your changes.

## Credits & Acknowledgements

Stripe: Payment gateway integration.
Django: For providing a scalable web framework.
Gunicorn: WSGI server for production.
Bootstrap 5: Responsive UI framework.
