import json
import os
import datetime


def create_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    note = {
        "id": len(notes) + 1,
        "title": title,
        "body": body,
        "timestamp": timestamp,
    }

    notes.append(note)
    save_notes()


def save_notes():
    with open("notes.json", "w") as file:
        json.dump(notes, file, indent=4)


def read_notes():
    if notes:
        for note in notes:
            print(f"\nID: {note['id']}")
            print(f"Заголовок: {note['title']}")
            print(f"Дата/Время: {note['timestamp']}")
            print(f"Текст: {note['body']}\n")
    else:
        print("Заметок нет.")


def edit_note():
    if notes:
        for note in notes:
            print(f"\nID: {note['id']}")
            print(f"Заголовок: {note['title']}\n")
    note_id = int(input("Введите ID заметки для редактирования: "))
    for note in notes:
        if note["id"] == note_id:
            new_title = input("Новый заголовок заметки: ")
            new_body = input("Новый текст заметки: ")
            note["title"] = new_title
            note["body"] = new_body
            note["timestamp"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes()
            print("Заметка успешно отредактирована.\n")
            return
    print("Заметка с указанным ID не найдена.")


def delete_note():
    if notes:
        for note in notes:
            print(f"\nID: {note['id']}")
            print(f"Заголовок: {note['title']}\n")
    note_id = int(input("Введите ID заметки для удаления: "))
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            save_notes()
            print("Заметка успешно удалена.\n")
            return
    print("Заметка с указанным ID не найдена!")


def main():
    global notes
    if not os.path.exists("notes.json"):
        notes = []
    else:
        with open("notes.json", "r") as file:
            notes = json.load(file)

    while True:
        print("Меню:")
        print("1. Создать заметку")
        print("2. Просмотреть заметки")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти")

        choice = input("\nВыберите опцию: ")
        if choice == "1":
            create_note()
        elif choice == "2":
            read_notes()
        elif choice == "3":
            edit_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == '__main__':
    main()