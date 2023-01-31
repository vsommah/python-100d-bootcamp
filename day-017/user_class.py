class User:

    def __init__(self, user_id, username):
        print("new user being created...")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def print_info(self, info):
        if info == self.username:
            print(f"username: {info}")
        elif info == self.id:
            print(f"id: {self.id}")
        elif info == self.followers:
            print(f"number of followers: {self.followers}")
        elif info == self.following:
            print(f"following: {self.following}")

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "somma")

user_1.print_info(user_1.id)
user_1.print_info(user_1.username)

user_2 = User("002", "angela")

user_2.print_info(user_2.id)
user_2.print_info(user_2.username)

user_1.follow(user_2)
user_1.print_info(user_1.followers)
user_1.print_info(user_1.following)
user_2.print_info(user_2.followers)
user_2.print_info(user_2.following)


