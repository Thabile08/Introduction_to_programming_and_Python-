def main(message):
    message = input()
    name = convert(message)
    print(name)

def convert(message):
    message = message.replace(":)", "🙂")
    message = message.replace(":(", "🙁")
    return(message)

main("message")







































