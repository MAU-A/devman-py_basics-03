import os
from dotenv import load_dotenv

load_dotenv()
from_login_mail = os.getenv("from_login_mail")
password_login_mail= os.getenv("password_login_mail")
to_login_mail = os.getenv("to_login_mail")
import smtplib
letter = ("""\n
From: kuzma.dan@yandex.ru
To: kuzma.dany@yandex.ru
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";\n\n
Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.\n
""").replace("%website%", "https://dvmn.org/profession-ref-program/dkru357/D0kos/").replace("%friend_name%", "Игорь").replace("%my_name%", "Виктор")
site_name = "https://dvmn.org/profession-ref-program/dkru357/D0kos/"
friends_name = "Игорь"
senders_name = "Виктор"
text = """{letter}""".format(letter=letter)
letter = letter.encode("UTF-8")
server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login(from_login_mail, password_login_mail)
server.sendmail(from_login_mail, to_login_mail,letter)
server.quit()
print(text)