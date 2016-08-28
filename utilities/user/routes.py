user_url = [default.Pluggable('/register',UserRegister,'register'),
            default.Pluggable('/login',UserLogin,'login'),
            default.Pluggable('/logout', UserLogout,'logout')]

urls = urls + user_url