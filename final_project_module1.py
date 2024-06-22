from random import randint


def generate_hostname():
    hostname = ['web.groenendal.com',
                'dc-1.groenendal.com',
                'vpn.groenendal.com',
                'proxy.groenendal.com',
                'exchange.groenendal.com']
    return hostname


def generate_username():
    username = ['rafael', 'roberta', 'fernanda',
                'patricia', 'joao', 'carlos', 'maria',
                'katia', 'cassiano', 'felipe']
    return username


def generate_date():
    day = f"{10:02d}"
    month = f"{12:02d}"
    year = f"{2024}"
    return f"{year}-{month}-{day}"


def generate_time():
    hour = f"{randint(6,16):02d}"
    minute = f"{randint(0,59):02d}"
    second = f"{randint(0,59):02d}"
    return f"{hour}:{minute}:{second}"


def generate_login_logout(login_time):
    login_time_split = login_time.split(':')
    if (int(login_time_split[0]) >= 6 and int(login_time_split[0]) < 12):
        logout_time = f"{int(login_time_split[0]) + randint(4,6):02d}:"
        logout_time += f"{int(login_time_split[0]) + randint(5,25):02d}:"
        logout_time += f"{int(login_time_split[0]) + randint(5,25):02d}"
    elif (int(login_time_split[0]) >= 12 and int(login_time_split[0]) <= 20):
        logout_time = f"{int(login_time_split[0]) + randint(2,3):02d}:"
        logout_time += f"{int(login_time_split[0]) + randint(5,25):02d}:"
        logout_time += f"{int(login_time_split[0]) + randint(5,25):02d}"

    return [login_time, logout_time]


class Event:
    def __init__(self, event_date, login, logout, hostname, username):
        self.date = event_date
        self.login = login
        self.logout = logout
        self.hostname = hostname
        self.username = username


def return_event_login(event):
    return event.login


# main function call - code execution starts here.
if __name__ == "__main__":

    host_list = generate_hostname()

    events = []
    
    for i in range(2):
        hostname = host_list[randint(0,len(host_list)-1)]
        host_list.remove(hostname)
        user_list = generate_username()
        for i in range(3):
            username = user_list[randint(0,len(user_list)-1)]
            user_list.remove(username)
            date = generate_date()
            time = generate_time()
            login = generate_login_logout(time)[0]
            logout = generate_login_logout(time)[1]
            new_event = Event(date, login, logout, hostname, username)
            events.append(new_event)
    
    for event in sorted(events, key=return_event_login):
        output_format  = f"{event.date} - "
        output_format += f"{event.hostname} - " 
        output_format += f"[ login: {event.login} - logout: {event.logout}] - "
        output_format += f"{event.username}"

        print(output_format)