import random
import string

# List of weak passwords (training data)
x = [
    "123456 = weak", "password = weak", "123456789 = weak", "12345678 = weak",
    "password123 = weak", "1234567 = weak", "1234567890 = weak", "123123 = weak", 
    "12345 = weak", "123456789 = weak", "1234 = weak", "123456 = weak", "123456789 = weak", 
    "querty = weak", "abc123 = weak", "111111 = weak", "12345678 = weak", "password1 = weak", 
    "123 = weak", "123456789 = weak", "123", "starwars = weak", "starwars123 = weak", 
    "querty123 = weak", "something = weak", "something123 = weak", "something1234 = weak", 
    "something12345 = weak", "hello = weak", "hello1234 = weak", "hello12345 = weak", 
    "hello123456 = weak", "hello1234567 = weak", "hello12345678 = weak", "random password = weak", 
    "randompassword = weak", "randompassword123 = weak", "randompassword1234 = weak", 
    "randompassword12345 = weak"
]

# List of strong passwords
y = [
    "J#7vK9!eLpX2", "z@R5bF%3qJ8s", "M7t!oE&9VbQ1", "W^gP4kz9$L0c", "Q!zK2yX@3pR5m",
    "Vj7A$YzP9+L3n", "H#bG0j9&Z6eX", "R7aT$hK8bL1D2", "F#3cJ!oXwV8p", "B2j@7pX5*LQ6v"
]

# Helper function to generate a random strong password
def generate_strong_password():
    # Combine both weak and strong passwords for training (just as an example)
    combined_passwords = x + y
    
    # We can analyze patterns, but let's simplify it for now.
    # We'll create a password with the following traits:
    # - At least 12 characters long
    # - Include uppercase, lowercase, digits, and special characters
    
    password_length = random.randint(12, 16)  # Password length between 12 and 16
    
    # Character pools based on strong password characteristics
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password using those characters
    password = ''.join(random.choice(all_characters) for _ in range(password_length))
    
    return password

# Simulate "training" by combining weak and strong passwords (for context)
def train_and_generate_password():
    # "Train" by analyzing weak and strong passwords (we're simplifying here)
    random_weak_password = random.choice(x)
    random_strong_password = random.choice(y)
    
    print(f"Trained on weak password: {random_weak_password}")  # Just for context
    print(f"Trained on strong password: {random_strong_password}")  # Just for context
    
    # Generate and return a strong password based on the combined data
    return generate_strong_password()

# Ask the user to press Enter to generate a secure password
input_password = input("Press enter to get a secure password: ")

# Generate and print a strong password
secure_password = train_and_generate_password()
print(f"Your secure password: {secure_password}")




    
