from instabot import Bot


bot = Bot()
bot.login(username="username", password="password@here")
user_id = bot.get_user_id_from_username("id of the user here")
user_info = bot.get_user_info(user_id)
print(user_info)




from instabot import Bot


bot = Bot()
bot.login(username="user name here", password="password here")
user_id = bot.get_user_id_from_username("and the name of the user here")

all  = bot.get_total_user_medias(user_id)


print(all)




