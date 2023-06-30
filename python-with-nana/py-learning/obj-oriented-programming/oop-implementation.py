from user import User
from post import Post

app_user_joey = User("jojotheboss@yahoho.net", "joey", "joey_is_cool", "cashier")
app_user_dino = User("its_me_DINO@gogomwail.com", "dino", "no_one_asked", "pontoon seller at FairerCorp")
app_user_dino.get_user_info()
app_user_joey.get_user_info()

new_post = Post("crushin' it at Half Foods 😎 #employeeofthemonth", app_user_joey.name)
new_post.get_post_info()