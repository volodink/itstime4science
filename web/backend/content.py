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
				"link_to_photo": "https://pp.vk.me/c837420/v837420262/240c7/THj2nW2dtZQ.jpg",
				"job_title": "Технический консультант",
				"comment": ""}

	garkaeva = {"name": "Александр Гарькаев",
				"link_to_photo": "https://pp.vk.me/c638419/v638419262/18c8d/RPFIBHyrQZ4.jpg",
				"job_title": "Лаборант",
				"comment": ""}

	stramovd = {"name": "Дмитрий Страмов",
				"link_to_photo": "https://pp.vk.me/c638023/v638023262/1bc4b/slIt41ns4jY.jpg",
				"job_title": "Лаборант",
				"comment": ""}

	vavilova = {"name": "Андрей Вавилов",
				"link_to_photo": "https://pp.vk.me/c638419/v638419262/18d1e/62mNrwj_tZI.jpg",
				"job_title": "Лаборант",
				"comment": ""}

	caplinm = {"name": "Михаил Цаплин",
				"link_to_photo": "https://pp.vk.me/c638419/v638419262/18d2c/lqA7jPBiAiM.jpg",
				"job_title": "Лаборант",
				"comment": ""}

	baikova = {"name": "Антон Байков",
				"link_to_photo": "https://pp.vk.me/c837420/v837420262/24068/L3iT5Oy5ruI.jpg",
				"job_title": "Лаборант",
				"comment": ""}

	volckovs = {"name": "Сергей Волчков",
				"link_to_photo": "https://pp.vk.me/c638419/v638419262/18d33/CwSrB0ZM6Y0.jpg",
				"job_title": "Лаборант",
				"comment": ""}

	kopylovv = {"name": "Вадим Копылов",
				"link_to_photo": "https://pp.vk.me/c638419/v638419262/18ca1/zg1YdCWAHNY.jpg",
				"job_title": "Лаборант",
				"comment": ""}

	kolodkin = {"name": "Паша Колодкин",
				"link_to_photo": "http://placehold.it/200x200",
				"job_title": "Лаборант",
				"comment": ""}

	volkova = {"name": "Александр Волков",
				"link_to_photo": "https://pp.vk.me/c638419/v638419262/18c53/j6J4fFI-Ttc.jpg",
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
			"head_photo": "img/main_head.jpg",
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
										# kolodkin,
										volkova)},
			"description": """ 
				<p>Лаборатория “Высоковоспризводительных вычислений и встраиваемых систем” (<b>ВВиВС</b>) начала работать
				 с 2015 года. Лаборатория имеет несколько основных векторов развитий:</p>
				<ul>
					<li><b>IoT</b> - интернет вещей</li>
					<li><b>HPC</b> - высокопроизводительные вычисления (<b>High Performance Computing</b>)</li>
					<li>Беспилотные системы (<b>UAV</b>)</li>
				</ul>
				<p>Наша лаборатория является активным участником региональных и всероссийских, 
				конкурсов и конференций. Второй год подряд наши студенты принимают участие в 
				российском конкурсе воздушно-инженерной школы “CanSat Russia” на базе 
				МГУ имени Ломоносова с проектом “Коптер”, в настоящее время уже две команды активно готовятся
				к конкурсу, в номинации “Студенческая лига” и “Коптер”.</p>   
                <p>В распоряжении студентов и магистрантов, работающих в лаборатории, есть образовательный 
                гибридный кластер, состоящий из четырех одноплатных компьютеров Banana Pi.
                На данном кластере студенты практикуются в параллельном программировании и разработке ПО 
                под операционной системе на базе ядра Linux. Также  в нашей 
                лаборатории студенты развивают навыки 3D моделирования в САПР Компас 3D
                и последующей печатью деталей на 3D принтере.</p>
                """
			}


	copter = {"title": "itstime4science | Коптер",
			  "head_photo": "img/copter_head.jpg",
			  "head_title": "Коптер",
			  "head_footer": "Разработка рабочего прототипа автоматизированного комплекса мониторинга очагов пожаров",
			  "gallery": setGalleryImg("https://pp.vk.me/c636323/v636323235/43d6f/HfCDSO1iE_w.jpg",
								"https://pp.vk.me/c636323/v636323235/44708/oaaCdr02RSU.jpg"),
			  "team_photo": {"team_row_title": 'Команда "Коптер"',
							"people": (volodink,
										kulikovo,
										garkaeva,
										stramovd,
										vavilova,					
										baikova)},
			"description": """ 
				<p>Студенты, работающие в нашей лаборатории, учавствуют в 
				российском конкурсе воздушно-инженерной школы “CanSat Russia” на базе 
				МГУ имени Ломоносова с проектом “Коптер”. Перед ними стоит задача в 
				разработке автоматизированного комплекса мониторинга очагов пожара. Из описания конкурса следует, что 
				аппарату необходимо автономно пролететь над полем
				по заранее выданному маршруту, определить очаг пожара, сбросить на него метку (мячик для пинг-понга), 
				снабженную радиометкой и отправить координаты очага пожара на наземную станцию.
				</p>
			"""
			}

	
	satellite = {"title": "itstime4science | Студенческая лига",
				 "head_photo": "img/sat_head.jpg",
				 "head_title": "Студенческая лига",
				 "head_footer": "Разработка аппарата “Громозека” на базе платформы CubeSat",
				 "gallery": setGalleryImg("https://i.ytimg.com/vi/SXW5eAjPD2U/maxresdefault.jpg",
				 				   "http://i.ytimg.com/vi/teArassP_E4/maxresdefault.jpg"),
				 "team_photo": {"team_row_title": 'Команда "Спутник"',
							"people": (volodink,
										kulikovo,
										garkaeva,
										kedelidzeo,
										caplinm,
										volckovs,
										# kolodkin,
										kopylovv)},
				"description": """
					<p>Задача студенческой лиги состоит в том, что необходимо провести мониторинг параметров атмосферы
					с использованием аппарата форм-фактора CubeSat
					и испытать его в условиях, схожих с космическими.
					Аппарат, разработанный участниками, поднимется с помощью шара-зонда на высоту до 30 км.
					</p>
					"""
				}
	

	return {"main": main,
			"copter": copter,
			"satellite": satellite}

if __name__ == "__main__":
	
	lal = getContent()

	for i in lal["main"]["gallery"]:
		print(i)
