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
				<p>Лаборатория “Высоковоспризводительные вычисления и встраиваемые системы” (<b>ВВиВС</b>) была основана в 2015 году.</p> 
				
				<p>Лаборатория имеет несколько основных векторов развитий:
					<ul>
						<li><b>HPC</b> - высокопроизводительные вычисления (<b>High Performance Computing</b>)</li>
						<li><b>UAV</b> - беспилотные системы</li>
						<li><b>Embedded & IoT</b> - встраиваемые системы и интернет вещей</li>
					</ul>
				</p>
				
				<p>В распоряжении студентов, магистрантов и аспирантов, работающих в лаборатории, есть образовательный 
                гибридный кластер, где студенты практикуются в параллельном программировании и разработке ПО 
                под операционную систему Linux. 
                
                <p>В нашей лаборатории студенты развивают навыки 3D моделирования в САПР Компас 3D и последующей печатью деталей на 3D принтере.</p>
                
                <p>Лаборатория проводит обучение проектированию печатных плат на базе современных САПР.</p> 
				
				<p>Наша лаборатория является активным участником региональных и всероссийских, конкурсов и конференций.</p>
				
				<p>Второй год подряд наши студенты принимают участие в 
				российском конкурсе <a href='http://roscansat.com/'>"Воздушно-инженерная школа" (CanSat в России)</a> на базе 
				Научно – исследовательского института ядерной физики имени Д.В. Скобельцына 
				МГУ имени М.В. Ломоносова (НИИЯФ МГУ) с проектом <a href='/copter'><b>“Коптер”</b></a></p>
				
				<p>В настоящее время две команды активно готовятся к конкурсу, в номинациях <a href='/satellite'><b>“Студенческая лига”</b></a> и <a href='/copter'><b>“Коптер”</b></a>.</p>   
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
				<p>
				   Ежегодно в России регистрируется от 10 тыс. до 35 тыс. лесных пожаров,
				   охватывающих площади от 500 тыс. до 2 млн 500 тыс. га. 
				   По данным Федеральной службы государственной статистики (Росстат), 
				   всего с начала 1992 года по конец 2014 года в России произошло 589 тыс. 768 лесных пожаров.
				   Подробнее можно узнать <a href='http://tass.ru/info/1121375'>здесь</a>.
				</p>
				
				<p>
				   Студенты лаборатории ВВиВС учавствуют в российском конкурсе <a href='http://roscansat.com/'>"Воздушно-инженерная школа"
				   (CanSat в России)</a> на базе Научно – исследовательского института ядерной физики имени Д.В. Скобельцына 
				   МГУ имени М.В. Ломоносова (НИИЯФ МГУ) с проектом “Коптер”. </p>
				
				<p>Перед ними стоит задача - <i>разработать автоматизированный комплекс мониторинга очагов пожара.</i></p>
				
				<p>
				   Аппарату необходимо:
				   
				   <ul>
					   <li>автономно пролететь над полем по заранее выданному маршруту;</li>
					   <li>определить очаг пожара, используя технологии компьютерного зрения 
						   и машинного обучения, с применением современных библиотек, таких как OpenCV;</li>
					   <li>отправить координаты очага пожара на наземную станцию;</li>
					   <li>сбросить на него 'метку' (мячик для пинг-понга).</li>
                   </ul>
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
					<p align='right'><i>SpaceY - потому, что SpaceX уже есть.</i></p>
										
					<p>
					   Задача "Студенческой лиги" состоит в проведении 
					   мониторинга некоторых параметров атмосферы
					   с использованием аппарата форм-фактора CubeSat.
					</p>
					
					<p>
					   Аппарат, разработанный участниками, 
					   поднимется с помощью шара-зонда на высоту до 35 км.
					</p>
									
					<p>
					   Для реализации проекта необходимо провести полный спектр работ, 
					   включающие
					   выбор комплектующих, 
					   3D-проектирование аппарата, 
					   разработку электроники,
					   разработку и тестирование встраиваемого ПО,
					   сборку и тестирование интегрированного аппарата,
					   разработку и тестирование наземной станции,
					   разработку и развертывание веб-сайта. 
					</p>   
					
					<p>
					   <a href='/mcc'><b>Мобильный коммандный центр (МКЦ)</b></a><br>
					   В ходе испытаний аппарата, данные будут транслироваться в Интернет.
					   Следить за тем, где находится аппарат и все ли с ним в порядке можно <a href='/mcc'>здесь</a>.
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
