# Dummy functions (simulate system)
def login(username, password):
    return username == "admin" and password == "123"

def dashboard():
    return True

def logout():
    return False  # Intentional fail for demo

# US-001
def test_login():
    assert login("admin", "123") == True

# US-002
def test_dashboard():
    assert dashboard() == True

# US-003
def test_logout():
    assert logout() == True