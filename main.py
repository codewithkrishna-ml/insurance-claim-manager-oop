#PROJECT-Insurance Claim Management System
class Policy:
    def __init__(self, policy_id, policy_type, coverage_amount, premium):
        self.policy_id = int(policy_id)
        self.policy_type = policy_type
        self.coverage_amount = float(coverage_amount)
        self.premium = float(premium)
        self.is_active = True

    def get_policy_details(self):
        status = "Active" if self.is_active else "Inactive"
        print(f"[{status}] Policy ID: {self.policy_id} | Type: {self.policy_type} | Coverage: {self.coverage_amount} | Premium: {self.premium}")

    def deactivate_policy(self):
        self.is_active = False


class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = int(customer_id)
        self.name = name
        self.email = email
        self.my_policies = {}

    def buy_policy(self, policy_obj):
        self.my_policies[policy_obj.policy_id] = policy_obj


class Claim:
    def __init__(self, claim_id, customer_id, policy_id, claim_amount):
        self.claim_id = int(claim_id)
        self.customer_id = int(customer_id)
        self.policy_id = int(policy_id)
        self.claim_amount = float(claim_amount)
        self.status = "Pending"

    def update_status(self, new_status):
        self.status = new_status


class ClaimManager:
    def __init__(self):
        self.all_customers = {}
        self.all_policies = {}
        self.all_claims = {}

    def register_customer(self, customer_obj):
        if customer_obj.customer_id in self.all_customers:
            print("Error: Customer ID already exists!")
            return False
        self.all_customers[customer_obj.customer_id] = customer_obj
        print(f"Customer: '{customer_obj.name}' registered successfully.")
        return True

    def create_policy(self, policy_obj):
        if policy_obj.policy_id in self.all_policies:
            print("Error: Policy ID already exists!")
            return False
        self.all_policies[policy_obj.policy_id] = policy_obj
        print(f"Policy ID {policy_obj.policy_id} created successfully.")
        return True

    def file_claim(self, claim_id, customer_id, policy_id, amount):
        if customer_id not in self.all_customers:
            print("Claim Failed: Customer not found in the system.")
            return

        customer = self.all_customers[customer_id]

        if policy_id not in customer.my_policies:
            print("Claim Failed: Customer does not own this policy.")
            return

        policy = customer.my_policies[policy_id]

        if not policy.is_active:
            print("Claim Failed: Policy is currently inactive.")
            return

        new_claim = Claim(claim_id, customer_id, policy_id, amount)
        self.all_claims[claim_id] = new_claim
        print(f"Claim filed successfully! Claim ID: {claim_id}. Status: Pending.")

    def process_claim(self, claim_id):
        if claim_id not in self.all_claims:
            print("Error: Claim ID not found.")
            return

        claim = self.all_claims[claim_id]

        if claim.status != "Pending":
            print(f"Actions Denied: Claim has already been processed as '{claim.status}'.")
            return

        policy = self.all_policies[claim.policy_id]

        if claim.claim_amount <= policy.coverage_amount:
            claim.update_status("Approved")
            policy.coverage_amount -= claim.claim_amount
            print(f"Claim {claim_id} APPROVED! Remaining coverage for Policy {policy.policy_id}: {policy.coverage_amount}")
        else:
            claim.update_status("Rejected")
            print(f"Claim {claim_id} REJECTED! Amount exceeds active coverage limit (Max: {policy.coverage_amount}).")


def main():
    manager = ClaimManager()

    while True:
        print("\n" + "="*45)
        print("------------- INSURANCE CLAIM MANAGEMENT SYSTEM ---------------")
        print("="*45)
        print("1. Register New Customer")
        print("2. Create New Policy BluePrint")
        print("3. Sell Policy to Customer")
        print("4. File an Insurance Claim")
        print("5. Process Pending Claim")
        print("6. View Customer & Policy Status")
        print("7. Exit")

        choice = input("Select an option (1-7): ").strip()

        if choice == "1":
            cid = int(input("Enter Customer ID: ").strip())
            name = input("Enter Customer Name: ").strip()
            email = input("Enter Customer Email: ").strip()
            customer = Customer(cid, name, email)
            manager.register_customer(customer)

        elif choice == "2":
            pid = int(input("Enter Policy ID: ").strip())
            ptype = input("Enter Policy Type (Health/Auto/Life): ").strip()
            coverage = float(input("Enter Coverage Amount: ").strip())
            premium = float(input("Enter Premium Amount: ").strip())
            policy = Policy(pid, ptype, coverage, premium)
            manager.create_policy(policy)

        elif choice == "3":
            cid = int(input("Enter Customer ID: ").strip())
            pid = int(input("Enter Policy ID: ").strip())

            if cid in manager.all_customers and pid in manager.all_policies:
                cust = manager.all_customers[cid]
                pol = manager.all_policies[pid]
                cust.buy_policy(pol)
                print(f"Policy {pid} successfully assigned to {cust.name}.")
            else:
                print("Error: Customer ID or Policy ID does not exist.")

        elif choice == "4":
            claim_id = int(input("Enter a unique Claim ID: ").strip())
            cid = int(input("Enter Customer ID: ").strip())
            pid = int(input("Enter Policy ID: ").strip())
            amount = float(input("Enter claim Amount: ").strip())
            manager.file_claim(claim_id, cid, pid, amount)

        elif choice == "5":
            claim_id = int(input("Enter Claim ID to process: ").strip())
            manager.process_claim(claim_id)

        elif choice == "6":
            cid = int(input("Enter Customer ID to check details: ").strip())
            if cid in manager.all_customers:
                cust = manager.all_customers[cid]
                print(f"\n------- Customer Profile: {cust.name} (ID: {cust.customer_id}) ---------")
                if not cust.my_policies:
                    print("No active policies found for this user.")
                for pol_id, pol_obj in cust.my_policies.items():
                    pol_obj.get_policy_details()    
            else:
                print("Customer not found")    

        elif choice == "7":
            print("\nThank you for using the Insurance Claim Management System. Goodbye!\n")   
            break
        else:
            print("\nInvalid choice! Please select between 1 and 7.")


if __name__ == "__main__":
    main()
