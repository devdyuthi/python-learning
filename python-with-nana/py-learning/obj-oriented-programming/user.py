class User:
    # __init__ is predefined in every class and contains parameters
    def __init__(self, email, name, password, current_job_title):
        self.email = email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    def change_pwd(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title

    def get_user_info(self):
        print(
            f'User named {self.name} currently works as a {self.current_job_title} and you can contact them at {self.email}')


app_user_joey = User("jojotheboss@yahoho.net", "joey", "joey_is_cool", "cashier")

app_user_joey.get_user_info()
app_user_joey.change_job_title("manager at half foods")
app_user_joey.get_user_info()
