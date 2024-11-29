# A simple user database
users = {"alice": True, "bob": False}

# Decorator to check if the user is authenticated
def requires_authentication(func):
    def wrapper(username, *args, **kwargs):
        if users.get(username):
            print(f"User '{username}' is authenticated.")
            return func(username, *args, **kwargs)
        else:
            print(f"User '{username}' is not authenticated. Access denied.")
    return wrapper

# Applying the decorator
@requires_authentication
def view_dashboard(username):
    print(f"Welcome, {username}! This is your dashboard.")

@requires_authentication
def view_profile(username):
    print(f"Welcome, {username}! This is your profile.")

# Testing the functions
view_dashboard("alice")
view_profile("bob")
