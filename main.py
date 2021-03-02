import datetime
from typing import List

last_id = -1

class Note():
    '''
    represent the notes
    '''
    def __init__(self, memo, tags=''):
        '''
        initializes note
        >>> fs_note = Note('8:30 - first lesson')
        >>> fs_note.memo
        '8:30 - first lesson'
        '''
        self.memo = memo
        self.tags = tags
        self.date_of_ctreation = datetime.date.today()
        global last_id
        last_id = last_id + 1
        self.id = last_id

    def match(self,filter:str) -> bool:
        '''
        indicates whether the note contains such text
        >>> fs_note = Note('8:30 - first lesson')
        >>> fs_note.match('8:30')
        True
        '''
        return filter in self.memo or filter in self.tags

class Notebook():
    '''
    represent the notebook
    '''
    def __init__(self,notes:List[Note]):
        '''
        initializes the notebook
        >>> fs_note = ('ok')
        >>> book = Notebook([fs_note])
        >>> book.notes[0]
        'ok'
        '''
        self.notes = notes

    def new_note(self,memo,tags= ''):
        '''
        append new note
        >>> book = Notebook([Note('hi')])
        >>> book.new_note('ok')
        >>> book.notes[1].memo
        'ok'
        '''
        self.notes.append(Note(memo,tags))

    def modify_memo(self,id_note,memo):
        '''
        changes an already created note
        '''
        for elem in self.notes:
            if elem.id == id_note:
                elem.memo = memo
                break

    def modify_tags(self,tags,id_note):
        '''
        changes the tag
        '''
        for elem in self.notes:
            if elem.id == id_note:
                elem.tags = tags
                break

    def search(self, filter):
        '''
        Find all notes that match the given filter
        string.
        >>> book = Notebook([Note('hi'),Note('hello')])
        >>> answer = [elem.memo for elem in book.search('h')]
        >>> answer
        ['hi', 'hello']
        '''
        return [note for note in self.notes if
        note.match(filter)]
        
    def __str__(self):
        '''
        >>> book = Notebook([Note('hi'),Note('hello')])
        >>> print(book)
        2021-03-02 Tag-: hi
        2021-03-02 Tag-: hello
        '''
        all_notes = ''
        for elem in self.notes:
            all_notes += str(elem.date_of_ctreation) + ' Tag-' + elem.tags + ': ' + elem.memo + '\n' 
        return all_notes[0:-1]




if __name__ == '__main__':
    import doctest
    doctest.testmod()