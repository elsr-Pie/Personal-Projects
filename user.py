class User:
    def __init__(self, user_email, user_name, user_password, user_current_job_title):
     self.email = user_email
     self.name = user_name
     self.password =user_password
     self.current_job_title = user_current_job_title

    def change_password(self, new_password):
       self.password = new_password


    def change_job_title(self, new_job_tile ):
       self.current_job_title = new_job_tile

    def get_user_info(self):
       print(f"user {self.name} is currently working as a {self.current_job_title} and you can contact him at {self.email}")


