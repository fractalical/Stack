from class_stack import Stack
from mail import Email


if __name__ == '__main__':
    # Задание 1
    stack = Stack()
    print("Is empty", stack.is_empty())
    stack.push(1)
    print("Is empty", stack.is_empty())
    el = stack.pop()
    print("Last", el)
    print("Is empty", stack.is_empty())
    stack.push(999)
    new_el = stack.peek()
    print("Last", new_el)
    print("Is empty", stack.is_empty())
    stack.push(1_000_000)
    print("Size", stack.size())

    # Задание 2
    balance = ["(((([{}]))))", "[([])((([[[]]])))]{()}", "{{[()]}}"]
    not_balance = ["}{}", "{{[(])]}}", "[[{())}]"]

    for b in balance:
        print(stack.is_balance(b))

    for b in not_balance:
        print(stack.is_balance(b))

    # Задание 3
    GMAIL_SMTP = "smtp.gmail.com"
    GMAIL_IMAP = "imap.gmail.com"

    l = 'login@gmail.com'
    password = 'qwerty'
    subject = 'Subject'
    recipients = ['vasya@email.com', 'petya@email.com']
    message = 'Message'
    header = None

    mail = Email(login=l, password=password, GMAIL_IMAP=GMAIL_IMAP, GMAIL_SMTP=GMAIL_SMTP)
    mail.send_message(subject=subject, recipients=recipients, message=message)
    recieve_message = mail.recieve_message()