def setGalleryImg(*tuplePhoto):

	return tuple((count, tuplePhoto[count]) for count in range(len(tuplePhoto))) 

def setTemaData(*tupleData):

	return dict({"name":tupleData})



def getContent():

	volodink = {"name": "Константин Володин",
				"link_to_photo": "https://pp.vk.me/c638023/v638023262/1bc35/KO9Y64lP6io.jpg",
				"job_title": "Научный руководитель",
				"comment": ""}

	kulikovo = {"name": "Олег Куликов",
				"link_to_photo": "http://placehold.it/200x200",
				"job_title": "Технический консультант",
				"comment": ""}

	garkaeva = {"name": "Александр Гарькаев",
				"link_to_photo": "http://placehold.it/200x200",
				"job_title": "Лаборант",
				"comment": ""}

	stramovd = {"name": "Дмитрий Страмов",
				"link_to_photo": "https://pp.vk.me/c638023/v638023262/1bc4b/slIt41ns4jY.jpg",
				"job_title": "Лаборант",
				"comment": ""}

	vavilova = {"name": "Андрей Вавилов",
				"link_to_photo": "http://placehold.it/200x200",
				"job_title": "Лаборант",
				"comment": ""}

	caplinm = {"name": "Михаил Цаплин",
				"link_to_photo": "http://placehold.it/200x200",
				"job_title": "Лаборант",
				"comment": ""}

	baikova = {"name": "Антон Байков",
				"link_to_photo": "http://placehold.it/200x200",
				"job_title": "Лаборант",
				"comment": ""}

	volckovs = {"name": "Сергей Волчков",
				"link_to_photo": "http://placehold.it/200x200",
				"job_title": "Лаборант",
				"comment": ""}

	kopylovv = {"name": "Вадим Копылов",
				"link_to_photo": "http://placehold.it/200x200",
				"job_title": "Лаборант",
				"comment": ""}

	kolginp = {"name": "Паша Колодкин",
				"link_to_photo": "http://placehold.it/200x200",
				"job_title": "Лаборант",
				"comment": ""}

	volkova = {"name": "Александр Волков",
				"link_to_photo": "https://pp.vk.me/c638023/v638023262/1bc85/PNEW2q7TdbQ.jpg",
				"job_title": "Лаборант",
				"comment": ""}

	kedelidzeo = {"name": "Кеделидзе Олег",
				"link_to_photo": "https://pp.vk.me/c638023/v638023262/1bc44/5OsS6C-RmQ8.jpg",
				"job_title": "Лаборант",
				"comment": ""}

	mesherinovae =  {"name": "Евгения Мещеринова",
				"link_to_photo": "https://pp.vk.me/c638023/v638023262/1bc8c/d83ROGuf4Pc.jpg",
				"job_title": "Лаборант",
				"comment": ""}




	main = {"title": "itstime4science | Главная",
			"head_photo": "https://pp.vk.me/c637528/v637528262/1976f/rx5wxLsuZyQ.jpg",
			"head_title": "ВВиВС",
			"head_footer": "Добро пожаловать на интернет-портал лаборатории ВВиВС (ПензГТУ)!",
			"gallery": setGalleryImg("https://pp.vk.me/c636323/v636323235/44666/CYzELG7-Lf0.jpg",
					 		  "https://pp.vk.me/c636323/v636323235/449d1/zsmPgBHN2yM.jpg",
					          "https://pp.vk.me/c636323/v636323235/449ec/EJ6mhheOnXQ.jpg"),
			"team_photo": {"team_row_title": "Сотрудники лаборатории ВВиВС",
							"people": (volodink,
										kulikovo,
										garkaeva,
										kedelidzeo,
										stramovd,
										mesherinovae,
										vavilova,
										caplinm,
										baikova,
										volckovs,
										kopylovv,
										kolginp,
										volkova)}
			}


	copter = {"title": "itstime4science | Коптер",
			  "head_photo": "https://pp.vk.me/c636728/v636728996/52d16/2oWW37OQqEI.jpg",
			  "head_title": "Коптер",
			  "head_footer": "Тут будет текст",
			  "gallery": setGalleryImg("https://pp.vk.me/c636323/v636323235/43d6f/HfCDSO1iE_w.jpg",
								"https://pp.vk.me/c836227/v836227262/1db5d/Oao-irsb8Sc.jpg",
								"https://pp.vk.me/c636323/v636323235/44708/oaaCdr02RSU.jpg"),
			  "team_photo": {"team_row_title": 'Команда "Коптер"',
							"people": (kulikovo,
										garkaeva,
										stramovd,
										vavilova,					
										baikova)}
			}

	
	satellite = {"title": "itstime4science | Студенческая лига",
				 "head_photo": "http://www.roscosmos.ru/media/gallery/big/20544/744950758.jpg",
				 "head_title": "Студенческая лига",
				 "head_footer": "Тут будет текст",
				 "gallery": setGalleryImg("https://i.ytimg.com/vi/SXW5eAjPD2U/maxresdefault.jpg",
				 				   "http://i.ytimg.com/vi/teArassP_E4/maxresdefault.jpg"),
				 "team_photo": {"team_row_title": 'Команда "Спутник"',
							"people": (kulikovo,
										garkaeva,
										kedelidzeo,
										caplinm,
										volckovs,
										kopylovv,
										kolginp)}
				}
	

	return {"main": main,
			"copter": copter,
			"satellite": satellite}

if __name__ == "__main__":
	
	lal = getContent()

	for i in lal["main"]["gallery"]:
		print(i)
