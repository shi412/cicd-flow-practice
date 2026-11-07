def welcome():
    return "Welcome to CI/CD Pipeline!"

def test_welcome():
    assert welcome() == "Welcome to CI/CD Pipeline!"

test_welcome()

print("All tests passed!")
