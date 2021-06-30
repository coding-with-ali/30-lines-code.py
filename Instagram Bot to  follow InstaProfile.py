from instabot import Bot

bot = Bot()

bot.login(username="username here ",password="Password")

user_id = bot.get_user_id_from_username("enter the id of the profile you want to follow")

bot.unfollow(user_id)