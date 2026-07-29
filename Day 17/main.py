class User:
    def __init__(self,id,username):
        self.id = id
        self.username = username
        self.age = 18  #default value initializtion
        self.followers = 0  #default value initializtion
        self.following = 0  #default value initializtion

    def follow(self, user):
        user.followers += 1
        self.following +=1    


user1 = User(15,'angela')
user2 = User(22,'jack')
user1.follow(user2)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)