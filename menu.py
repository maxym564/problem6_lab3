import sys
from main import Notebook, Notes
from typing import List

last_id = -1

class Menu:
     '''Display a menu and respond to choices when run.'''
     def __init__(self):
        self.notebook = Notebook([])
        self.choices = {
        "1": self.show_notes,
        "2": self.search_notes,
        "3": self.add_note,
        "4": self.modify_note,
        "5": self.quit
        }

     def display_menu(self):
        print("""
        Notebook Menu
        1. Show all Notes
        2. Search Notes
        3. Add Note
        4. Modify Note
        5. Quit
        """)

     def run(self):
        while True:
            self.display_menu()
            option = input('Enter an option:')
            while True:
                check = [not (option == elem) for elem in self.choices]
                if all(check):
                    option = input('Try again: ')
                else:
                    break
            action = self.choices.get(option)
            action()

     def show_notes(self, notes=None):
        if self.notebook.notes == []:
            print("There aren't any notes yet")
        else:
            print(self.notebook)
    
     def search_notes(self):
        notes = self.notebook
        filter = str(input('Enter the filter: '))
        result = notes.search(filter)
        for index in range(len(result)):
            print(str(index+1) + ' Tag:' + result[index].tags + ' Memo:' + result[index].memo)

     def add_note(self):
        memo = input('Enter what you want to note: ')
        tag = input('Enter your tag: ')
        self.notebook.new_note(memo,tags=tag)

     def modify_note(self):
        try:
            note_id = input("Enter note's id: ")
            new_memo = input("Enter new memo: ")
            for elem in self.notebook.notes:
                if elem.id == int(note_id):
                    elem.memo = new_memo
                    break
        except:
            print('Try again: ')

     def quit(self):
        print("Thanks")
        sys.exit(0)


if __name__ == '__main__':
    Menu().run()