# 🚚 TransitOps - Smart Transport Operation Platform

**Built for the Oddo Hackathon 2026**

TransitOps is an enterprise-grade backend management system designed to handle the complex logistics of a transportation fleet. It ensures strict business rules are followed for vehicle dispatching, driver assignments, and maintenance tracking.

## ⚙️ Tech Stack
* **Backend Framework:** FastAPI (Python)
* **Database ORM:** SQLAlchemy
* **Database:** PostgreSQL (Hosted on Supabase)
* **Data Validation:** Pydantic

## ✨ Core Features & Business Logic
We have implemented strict, real-world constraints into our API architecture:

* **🚗 Vehicle Management:** Tracks fleet inventory, acquisition costs, maximum load capacities, and real-time status (`Available`, `In Shop`, `On Trip`).
* **🪪 Driver Roster:** Manages driver profiles, license expiration dates, and safety scores. Prevents duplicate license entries.
* **🗺️ Trip Dispatching (Smart Logic):** 
  * **Rule Enforced:** A trip cannot be created if the requested `cargo_weight` exceeds the specific vehicle's `max_load_capacity`.
  * **Rule Enforced:** Trips will instantly reject if the assigned driver or vehicle is not currently listed as `Available`.
* **🛠️ Maintenance Logs:** 
  * **Rule Enforced:** Opening a maintenance ticket automatically toggles the vehicle's status to `In Shop`. Closing the ticket restores it to `Available`.

## 🚀 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YourUsername/TransitOps-Hackathon.git](https://github.com/YourUsername/TransitOps-Hackathon.git)
   cd TransitOps-Hackathon/backend