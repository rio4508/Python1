attempt = 0
limit = 5
correct_password = "Rio"
while attempt < limit:
    guess = input(f"Enter password {attempt+1}/{limit}: ")
    if guess == correct_password:
        print("Correct")
        break

    else:
        attempt = attempt + 1
        remaining = limit - attempt
        print(f"Incorrect password {remaining} tries left.")
    if attempt == limit:
        print("Access Denied. You have been locked out ")

print("logged in")

