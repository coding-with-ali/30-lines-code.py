from instabot import Bot

bot = Bot()

bot.login(username="user name here",password="password here")

user_id = bot.get_user_id_from_username("alixaprodev")

medias_ids = bot.get_total_user_medias(user_id)


bot.like(medias_ids[0])
