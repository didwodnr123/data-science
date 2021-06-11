from teamlab_note import Note
from teamlab_note import NoteBook

my_notebook = NoteBook('강의 노트')

new_note = Note('알고리즘 재밌다.')
print(new_note)

new_note_2 = Note('파이썬 강의 재밌다.')
print(new_note_2)

my_notebook.add_note(new_note)
my_notebook.add_note(new_note_2)

new_note_3 = Note('Hello World.')
my_notebook.add_note(new_note_3)

my_notebook.get_number_of_pages()

print(my_notebook.notes)

new_note_4 = Note("왜 안 돼?")
my_notebook.add_note(new_note_4, 100)

print(my_notebook.notes)
