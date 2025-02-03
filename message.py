import smtplib
import os


from dotenv import load_dotenv

load_dotenv()
from_login_mail = os.getenv("from_login_mail")
password_login_mail= os.getenv("password_login_mail")
to_login_mail = os.getenv("to_login_mail")


site_name = "https://dvmn.org/profession-ref-program/dkru357/D0kos/"
friends_name = "Игорь"
senders_name = "Виктор"


text_message='''
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
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.
'''.replace("%website%", site_name).replace("%friend_name%", friends_name).replace("%my_name%", senders_name)

letter = '''/
From: {from_}
To: {to}
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";
{message}
'''.format(message=text_message,from_=from_login_mail,to=to_login_mail)

letter = letter.encode("UTF-8")
server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login(from_login_mail, password_login_mail)
server.sendmail(from_login_mail, to_login_mail,letter)
server.quit()
