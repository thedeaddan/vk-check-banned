import vk_api

vk = vk_api.VkApi(token = "TOKEN")
banned = vk.method("account.getBanned")["profiles"]
i = 1
print("Список заблокированных:")
for profile in banned:
	if profile.get("deactivated") != None:
		print(str(i)+".@id"+str(profile["id"])+"("+profile["first_name"]+" "+profile["last_name"]+")(Страница деактивирована)")
	else:
		print(str(i)+".@id"+str(profile["id"])+"("+profile["first_name"]+" "+profile["last_name"]+")")
	i = i + 1
