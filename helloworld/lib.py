standard_subject = "World"


def get_hello_message(subject=standard_subject):
    return f"Hello {subject}!"


def hello_subject(subject=standard_subject):
    msg = get_hello_message(subject=subject)
    print(msg)


def hello_world():
    hello_subject()
