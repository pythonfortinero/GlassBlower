user_url = [p('/register',UserRegister,'register'),
            p('/login',UserLogin,'login'),
            p('/logout', UserLogout,'logout')]

urls = urls + user_url