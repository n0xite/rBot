import colorama
from datetime import datetime
color = colorama.Fore


def log(message, code):
    file = open("log.txt", "a")
    time = datetime.now()
    dt_string = time.strftime("%d/%m/%Y %H:%M:%S")

    match code:
        case 0:
            print(color.WHITE + str(dt_string) + ' : ' + color.GREEN + '[SUCCESS] ' + message + '\n')
            file.write(str(dt_string) + ' : [SUCCESS] ' + message + '\n')
        case 1:
            print(color.WHITE + str(dt_string) + ' : ' + color.YELLOW + '[WARNING] ' + message + '\n')
            file.write(str(dt_string) + ' : [WARNING] ' + message + '\n')
        case 2:
            print(color.WHITE + str(dt_string) + ' : ' + color.RED + '[ERROR] ' + message + '\n')
            file.write(str(dt_string)+ ' : [WARNING] ' + message + '\n')
        case -1:
            print(color.WHITE + str(dt_string)+ ' : ' + color.WHITE + '[INFO] ' + message + '\n')
            file.write(str(dt_string) + ' : [INFO] ' + message + '\n')


