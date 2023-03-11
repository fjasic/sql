from database import add_entry, get_entries, create_table

menu = """
Please select option:
1) new entry
2) view entry
3) exit

your selection:
"""


def prompt_new_entry():
    entry_content = input("What have you learned?\n")
    entry_date = input("Input date:\n")
    add_entry(entry_content, entry_date)


def view_entries(entries):
    for entry in entries:
        print(f"{entry[1]}\n{entry[0]}\n")


create_table()


while (user_input := input(menu)) != "3":
    if user_input == "1":
        prompt_new_entry()
    elif user_input == "2":
        view_entries(get_entries())
    else:
        print("Invalid option.")
