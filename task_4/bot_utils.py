from box import Box
from colorama import Fore, init
from task_4.bot_config import bot_config

init(autoreset=True)


def check_args_length(
    args,
    expected_length=2,
):
    if len(args) < expected_length:
        print(f"{Fore.RED} Error: Please provide both name and phone number.")
        return False
    return True


def add_contact(args, contacts):
    if not check_args_length(args):
        return
    name, phone = args[0], args[1]
    contacts[name] = phone
    print(f"{Fore.GREEN} {bot_config.add.answer} {name}: {phone}")


def change_contact(args, contacts):
    if not check_args_length(args):
        return
    name, phone = args[0], args[1]
    if name in contacts:
        contacts[name] = phone
        return print(f"{Fore.GREEN} {bot_config.change.answer.success}")
    else:
        return print(f"{Fore.RED} {bot_config.change.answer.fail}")


def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return print(
            f"{Fore.GREEN} {bot_config.phone.answer.success(name, contacts[name])}"
        )
    else:
        return print(f"{Fore.RED} {bot_config.phone.answer.fail(name)}")


def show_all(contacts):
    for name, phone in contacts.items():
        print(f"{Fore.GREEN} {name}: {phone}")


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


utils = Box(
    {
        "add": add_contact,
        "change": change_contact,
        "phone": show_phone,
        "all": show_all,
        "parse_input": parse_input,
    }
)
