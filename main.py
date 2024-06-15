from user import User
from post import *
app_user_one = User("ap@paps.com", "Papi", "pwd2", "Devops")
app_user_one.get_user_info()    
app_user_one.change_job_title("developer")
app_user_one.get_user_info()

new_post = Post("I am feeling happy today", app_user_one.name)
new_post.get_post_info()