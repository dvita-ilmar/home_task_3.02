'''
Дегтярев Виталий (группа 22/08)
Домашнее задание №3.02
Домашняя работа по уроку "Способы вызова функции"
'''

# Определение функции передачи писем
def  send_email(message, recipient, sender = "university.help@gmail.com"):
    if not ('.com' in recipient or '.net' in recipient or '.ru' in recipient) or '@' not in recipient:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient} - указан неверный адрес получателя')
    elif not ('.com' in sender or '.net' in sender or '.ru' in sender) or '@' not in sender:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient} - указан неверный адрес отправителя')
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    elif sender != 'university.help@gmail.com':
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'Письмо отправлено с адреса {sender} на адрес {recipient}')
    
# Обращения к функции
send_email('Сообщение', 'rlgregvr@mail.net', sender = 'abaq@post.co')
send_email('Сообщение', 'rlgregvrmail.net')
send_email('Сообщение', 'rlgregvr@mail.ne', sender = 'abaq@post.com')
send_email('Сообщение', 'rlgregvr@mail.net', sender = 'abaq@post.com')
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
