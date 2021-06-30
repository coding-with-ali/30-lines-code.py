from instabot import Bot

bot =  Bot()

bot.login(username="username here",password="Userpassword here")

# bot.upload_photo("myphoto.jpg",caption="this is upladed with thhe help of python")

bot.follow(bot.get_user_id_from_username("learn_py3"))



