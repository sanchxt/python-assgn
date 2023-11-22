def userAndDomain(email):
    parts = email.split('@')
    if (len(parts) == 2):
        username, domain = parts
        return username, domain
    else:
        print('invalid format')
        return None, None


inp_email = input("Email address: ")

# Extract username and domain using the function
username, domain = userAndDomain(inp_email)

# Display the result
if username and domain:
    print(f"Username: {username}")
    print(f"Domain: {domain}")
