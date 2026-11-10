# Insurance Claim Management System 🛡️💼

An enterprise-inspired insurance claims and policy administration backend simulator built in Python using core **Object-Oriented Programming (OOP)** patterns. This application models a complete banking/insurance infrastructure, managing client profiles, active insurance policies, real-time claim filing verification nodes, and automated deduction logs based on available coverage limits.

---

## 🌟 About the Developer

*   **Age/Class:** 16 Years Old (Class 10th) 🎯
*   **Future Goal:** B.Tech in Artificial Intelligence and Machine Learning (AI-ML) -> **Aspiring ML Engineer at Google / Microsoft** 🤖⚡
*   **Milestone:** Successfully completed the **100 Days of Code** challenge!
*   **Current Focus:** Mastering Data Structures & Algorithms (DSA) and building data science frameworks with **NumPy** and **Pandas**.

---

## ✨ Key Features

*   **Dynamic Policy Creation System:** Instantly deploy diverse policy blueprints (Health, Auto, Life) mapped alongside custom coverage metrics and monthly premiums.
*   **Relational Client Ingestion Ledger:** Registers unique customer objects, managing private mapping structures to link multiple purchased policies seamlessly.
*   **Smart Claim Verification Pipeline:** Implements multi-tier structural security validation guards that immediately block fraudulent or erroneous actions:
    *   Fails instantly if the **Customer ID is not registered**.
    *   Blocks transaction logs if the client **does not own** the requested policy number.
    *   Denies actions if the target coverage plan is **Inactive**.
*   **Automated Claim Processing Engine:** Compares incoming claim balances directly against available bounds:
    *   **APPROVED:** If the amount is within bounds, it automatically updates the state and reduces the policy’s remaining coverage value (`coverage_amount`) dynamically.
    *   **REJECTED:** Instantly locks and rejects claims exceeding active coverage caps.

---

## 🛠️ OOP Concepts & Architecture Demonstrated

This enterprise prototype leverages modular decoupling to manage state transitions securely:
*   **Classes & System Abstraction:** Structured modularly around independent logical objects: `Policy` (metadata container), `Customer` (user profile host), `Claim` (individual transaction token), and `ClaimManager` (the master repository database controller).
*   **Composition & Relational Aggregation:** The master `ClaimManager` class aggregates separate execution data nodes (`all_customers`, `all_policies`, `all_claims`) within dictionary structures, illustrating clean multi-tier system designs.
*   **State Control Logic:** Safely mutates sensitive state variables (such as altering policy status flags from `Active` to `Inactive` or switching claims to `Approved` or `Rejected` workflows) through authorized class methods only.

---

## 🚀 How to Run the Project

1.  **Clone the repository:**
    ```bash
    git clone https://github.com
    ```
2.  **Navigate to the project folder:**
    ```bash
    cd insurance-claim-manager-oop
    ```
3.  **Run the interactive terminal manager loop:**
    ```bash
    python main.py
    ```

---

## 📝 Prerequisites
*   **Python 3.x** installed on your machine.
*   Runs completely on pure Python core architectures without needing external third-party library installations.
