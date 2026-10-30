# GRC Practice: Access Verification for Employees and Vendors

def run_security_audit():
    # 1. Our databases of trusted, authorized people
    active_employees = ["maria_lopez", "juan_perez", "carlos_gomez"]
    active_vendors = ["ana_martinez", "david_smith", "john_doe"]

    # 2. The list of accounts currently logged into our system
    current_system_users = ["maria_lopez", "ana_martinez", "hacker_99", "carlos_gomez"]

    # 3. THE LOGIC: Check every user currently in the system
    for user in current_system_users:

        # If the user is NOT an employee AND ALSO NOT a vendor...
        if user not in active_employees and user not in active_vendors:
            # We found someone who shouldn't be there!
            print("ALERT: Unauthorized user detected in the system:")
            print(user)

# 4. Run the audit routine
run_security_audit()
