import datetime
from typing import List

last_id = -1

class Notes():
    '''
    
    '''
    def __init__(self, memo, tags=''):
        self.memo = memo
        self.tags = tags
        self.date_of_ctreation = datetime.date.today()
        global last_id
        last_id = last_id + 1
        self.id = last_id

    def match(self,filter):
        return filter in self.memo or filter in self.tags

class Notebook():
    def __init__(self,notes:List[Notes]):
        self.notes = notes

    def new_note(self,memo,tags= ''):
        self.notes.append(Notes(memo,tags))

    def modify_memo(self,id_note,memo):
        for elem in self.notes:
            if elem.id == id_note:
                elem.memo = memo
                break

    def modify_tags(self,tags,id_note):
        for elem in self.notes:
            if elem.id == id_note:
                elem.tags = tags
                break

    def search(self, filter):
        '''
        Find all notes that match the given filter
        string.
        '''
        return [note for note in self.notes if
        note.match(filter)]
        
    def __str__(self):
        all_notes = ''
        for elem in self.notes:
            all_notes += str(elem.date_of_ctreation) + ' Tag-' + elem.tags + ': ' + elem.memo + '\n' 
        return all_notes[0:-1]




if __name__ == '__main__':
    fs_note = Notes('dssdsddsd','Lol')
    sc_note = Notes('assaass','dad')
    book = Notebook([fs_note,sc_note])
    print(type(fs_note.id))