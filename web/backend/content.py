def setIMG(*tuplePhoto):

	return tuple((count, tuplePhoto[count]) for count in range(len(tuplePhoto))) 



def getContent():

	main = {"title": "itstime4science | Главная",
			"head_photo": "https://pp.vk.me/c637528/v637528262/1976f/rx5wxLsuZyQ.jpg",
			"head_title": "ВВиВС",
			"head_footer": "Добро пожаловать на интернет-портал лаборатории ВВиВС (ПензГТУ)!",
			"gallery": setIMG("https://pp.vk.me/c636323/v636323235/44666/CYzELG7-Lf0.jpg",
					 		  "https://pp.vk.me/c636323/v636323235/449d1/zsmPgBHN2yM.jpg",
					          "https://pp.vk.me/c636323/v636323235/449ec/EJ6mhheOnXQ.jpg")
			}


	copter = {"title": "itstime4science | Коптер",
			  "head_photo": "https://pp.vk.me/c637528/v637528262/19735/c7J0oC93950.jpg",
			  "head_title": "Коптер",
			  "head_footer": "Тут будет текст",
			  "gallery": setIMG("http://4vision.ru/files/categories/thumbs/phantom_category.jpg",
								"https://www3.djicdn.com/assets/images/products/phantom/phantom-241665483f93b3565a8d2c7b71c991db.png")
			}

	
	satellite = {"title": "itstime4science | Студенческая лига",
				 "head_photo": "http://www.roscosmos.ru/media/gallery/big/20544/744950758.jpg",
				 "head_title": "Студенческая лига",
				 "head_footer": "Тут будет текст",
				 "gallery": setIMG("http://zablugdeniyam-net.ru/wp-content/uploads/CHto-takoe-sputnik-i-chto-on-delaet.jpg",
				 					"http://sdnnet.ru/images/uploads/sputnik_yamal-401_pristupil_k_rabote.jpg")}
	

	return {"main": main,
			"copter": copter,
			"satellite": satellite}

if __name__ == "__main__":
	
	lal = getContent()

	for i in lal["main"]["gallery"]:
		print(i[0])