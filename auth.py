def authenticate_user(username, password): 
    """Authenticate user by username and password.""" 
    if username == "admin" and password == "123456": 
        return True 
    return False 
