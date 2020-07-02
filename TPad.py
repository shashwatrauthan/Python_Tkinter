import tkinter as tk
from tkinter import ttk
from tkinter import font,filedialog,colorchooser,messagebox
import os

win = tk.Tk()
win.geometry('1280x720')
win.iconphoto(True,tk.PhotoImage(file = r'C:\Users\shash\Desktop\TPad\icons\main_icon.png'))
win.title('TPad - New File')

######################################### Main Menu #######################################
main_menu = tk.Menu(win)

#file_menu
file_menu = tk.Menu(main_menu,tearoff = 0)

new_icon = tk.PhotoImage(file = r'C:\Users\shash\Desktop\TPad\icons\new.png')
open_icon = tk.PhotoImage(file = r'C:\Users\shash\Desktop\TPad\icons\open.png')
save_icon = tk.PhotoImage(file = r'C:\Users\shash\Desktop\TPad\icons\save.png')
save_as_icon = tk.PhotoImage(file = r'C:\Users\shash\Desktop\TPad\icons\save_as.png')
exit_icon = tk.PhotoImage(file = r'C:\Users\shash\Desktop\TPad\icons\exit.png')


#edit_menu
edit_menu = tk.Menu(main_menu,tearoff = 0)

copy_icon = tk.PhotoImage(file = r'C:\Users\shash\Desktop\TPad\icons\copy.png')
paste_icon = tk.PhotoImage(file = r'C:\Users\shash\Desktop\TPad\icons\paste.png')
cut_icon = tk.PhotoImage(file = r'C:\Users\shash\Desktop\TPad\icons\cut.png')
clear_all_icon = tk.PhotoImage(file = r'C:\Users\shash\Desktop\TPad\icons\clear_all.png')
find_icon = tk.PhotoImage(file = r'C:\Users\shash\Desktop\TPad\icons\find.png')



#view_menu
view_menu = tk.Menu(main_menu,tearoff = 0)

tool_bar_icon = tk.PhotoImage(file = r'C:\Users\shash\Desktop\TPad\icons\tool_bar.png')
status_bar_icon = tk.PhotoImage(file = r'C:\Users\shash\Desktop\TPad\icons\status_bar.png')



#theme_menu
theme_menu = tk.Menu(main_menu,tearoff = 0)


light_default_icon = tk.PhotoImage(file = r'C:\Users\shash\Desktop\TPad\icons\light_default.png')
light_plus_icon = tk.PhotoImage(file = r'C:\Users\shash\Desktop\TPad\icons\light_plus.png')
dark_icon = tk.PhotoImage(file = r'C:\Users\shash\Desktop\TPad\icons\dark.png')
red_icon = tk.PhotoImage(file = r'C:\Users\shash\Desktop\TPad\icons\red.png')
monokai_icon = tk.PhotoImage(file = r'C:\Users\shash\Desktop\TPad\icons\monokai.png')
night_blue_icon = tk.PhotoImage(file = r'C:\Users\shash\Desktop\TPad\icons\night_blue.png')

color_icons = (light_default_icon, light_plus_icon, dark_icon, red_icon, monokai_icon, night_blue_icon)

color_dict = {
    'Light Default' : ('#000000', '#ffffff'),
    'Light Plus' : ('#474747', '#e0e0e0'),
    'Dark' : ('#c4c4c4', '#2d2d2d'),
    'Red' : ('#2d2d2d', '#ffe8e8'),
    'Monokai' : ('#d3b774', '#474747'),
    'Night Blue' :('#ededed', '#6b9dc2')
}




main_menu.add_cascade(label='File',menu = file_menu)
main_menu.add_cascade(label='Edit',menu = edit_menu)
main_menu.add_cascade(label='View',menu = view_menu)
main_menu.add_cascade(label='Theme',menu = theme_menu)

# -----------------------------------&&&&&&&&&&&&&&&&&&&&----------------------------------




######################################### Tool Bar ########################################

tool_bar = ttk.Label(win)
tool_bar.pack(side = tk.TOP,fill = tk.X)

#font_box
fonts = tk.font.families()
active_font = tk.StringVar()
font_box = ttk.Combobox(tool_bar,width = 30,textvariable = active_font,state = 'readonly')
font_box['values'] = fonts
font_box.current(fonts.index('Arial'))
font_box.grid(row = 0,column = 0,padx = 5)

#size box
font_size = tk.IntVar()
size_box = ttk.Combobox(tool_bar,width = 15,textvariable = font_size,state = 'readonly')
size_box['values'] = tuple(range(8,81,2))
size_box.current(2)
size_box.grid(row = 0,column = 1,padx = 5)

#bold_button
bold_icon = tk.PhotoImage(file = r'C:\Users\shash\Desktop\TPad\icons\bold.png')
bold_btn = ttk.Button(tool_bar,image = bold_icon)
bold_btn.grid(row = 0,column = 2,padx = 5)

#italic_button
italic_icon = tk.PhotoImage(file = r'C:\Users\shash\Desktop\TPad\icons\italic.png')
italic_btn = ttk.Button(tool_bar,image = italic_icon)
italic_btn.grid(row = 0,column = 3,padx = 5)

#underline_button
underline_icon = tk.PhotoImage(file = r'C:\Users\shash\Desktop\TPad\icons\underline.png')
underline_btn = ttk.Button(tool_bar,image = underline_icon)
underline_btn.grid(row = 0,column = 4,padx = 5)

#font_color_button
font_color_icon = tk.PhotoImage(file = r'C:\Users\shash\Desktop\TPad\icons\font_color.png')
font_color_btn = ttk.Button(tool_bar,image = font_color_icon)
font_color_btn.grid(row = 0,column = 5,padx = 5)

#align_left_button
align_left_icon = tk.PhotoImage(file = r'C:\Users\shash\Desktop\TPad\icons\align_left.png')
align_left_btn = ttk.Button(tool_bar,image = align_left_icon)
align_left_btn.grid(row = 0,column = 6,padx = 5)

#align_center_button
align_center_icon = tk.PhotoImage(file = r'C:\Users\shash\Desktop\TPad\icons\align_center.png')
align_center_btn = ttk.Button(tool_bar,image = align_center_icon)
align_center_btn.grid(row = 0,column = 7,padx = 5)

#align_right_button
align_right_icon = tk.PhotoImage(file = r'C:\Users\shash\Desktop\TPad\icons\align_right.png')
align_right_btn = ttk.Button(tool_bar,image = align_right_icon)
align_right_btn.grid(row = 0,column = 8,padx = 5)




# -----------------------------------&&&&&&&&&&&&&&&&&&&&----------------------------------

#Status Bar
status_bar = ttk.Label(win,text = 'Status Bar')
status_bar.pack(side = tk.BOTTOM)

########################################## Text Editor #####################################

text_editor = tk.Text(win)
text_editor.config(wrap = 'word',relief = tk.FLAT)
text_editor.focus_set()
scroll_bar = tk.Scrollbar(win)
scroll_bar.pack(side = tk.RIGHT,fill = tk.Y)
text_editor.pack(expand = True,fill = tk.BOTH)
scroll_bar.config(command = text_editor.yview)
text_editor.config(yscrollcommand = scroll_bar.set)


#font_functionality
text_editor.configure(font = ('Ariel',12))
current_font = 'Ariel'
current_font_size = 12

def change_font(win):
    global current_font
    current_font = active_font.get()
    text_editor.configure(font = (current_font,current_font_size))

font_box.bind('<<ComboboxSelected>>',change_font)

def change_font_size(win):
    global current_font_size
    current_font_size = font_size.get()
    text_editor.configure(font = (current_font,current_font_size))

size_box.bind('<<ComboboxSelected>>',change_font_size)

#buttons_functionality

#bold_button
def ch_bold():
    text_property = tk.font.Font(font = text_editor['font'])
    if text_property.actual()['weight']  == 'normal':
        text_editor.configure(font = (current_font,current_font_size,'bold'))
    if text_property.actual()['weight']  == 'bold':
        text_editor.configure(font = (current_font,current_font_size,'normal'))

bold_btn.configure(command = ch_bold)

#italic_button
def ch_italic():
    text_property = tk.font.Font(font = text_editor['font'])
    if text_property.actual()['slant']  == 'roman':
        text_editor.configure(font = (current_font,current_font_size,'italic'))
    if text_property.actual()['slant']  == 'italic':
        text_editor.configure(font = (current_font,current_font_size,'normal'))

italic_btn.configure(command = ch_italic)

#underline_button
def ch_underline():
    text_property = tk.font.Font(font = text_editor['font'])
    if text_property.actual()['underline']  == 0:
        text_editor.configure(font = (current_font,current_font_size,'underline'))
    if text_property.actual()['underline']  == 1:
        text_editor.configure(font = (current_font,current_font_size,'normal'))

underline_btn.configure(command = ch_underline)


#font_color_button
def ch_color():
    color = tk.colorchooser.askcolor()
    text_editor.configure(fg = color[1])

font_color_btn.configure(command = ch_color)


#align_left_button
def align_left():
    content = text_editor.get(1.0,'end')
    text_editor.tag_config('left',justify = tk.LEFT)
    text_editor.delete(0.1,'end')
    text_editor.insert(tk.INSERT,content,'left')

align_left_btn.configure(command = align_left)

#align_center_button
def align_center():
    content = text_editor.get(1.0,'end')
    text_editor.tag_config('center',justify = tk.CENTER)
    text_editor.delete(0.1,'end')
    text_editor.insert(tk.INSERT,content,'center')

align_center_btn.configure(command = align_center)

#align_right_button
def align_right():
    content = text_editor.get(1.0,'end')
    text_editor.tag_config('right',justify = tk.RIGHT)
    text_editor.delete(0.1,'end')
    text_editor.insert(tk.INSERT,content,'right')

align_right_btn.configure(command = align_right)

# -----------------------------------&&&&&&&&&&&&&&&&&&&&----------------------------------



########################################## Status Bar Functionality #####################################



text_changed = False
def counter(win):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True
        content = text_editor.get(1.0,'end-1c')
        words = len(content.split())
        characters = len(content)
        status_bar.config(text = f'Characters : {characters}     |     Words : {words}')
    text_editor.edit_modified(False)

text_editor.bind('<<Modified>>',counter)

# -----------------------------------&&&&&&&&&&&&&&&&&&&&----------------------------------





################################### Main Menu Functionality ###############################

# file_menu_commands
url = ''
#new
def new_file(event = None):
    global url
    url = ''
    text_editor.delete(1.0,'end')
    win.title('TPad - New File')

file_menu.add_command(label = 'New',image = new_icon,compound = tk.LEFT,accelerator = 'Ctrl+N',command = new_file )

#open
def open_file(event = None):
    global url
    url = filedialog.askopenfilename(initialdir = os.getcwd(),title = 'Open File',filetypes = (('Text Files','*.txt'),('All Files','*.*')))
    try:
        with open(url,'r') as f:
            text_editor.delete(1.0,'end')
            text_editor.insert(1.0,f.read())
    except:
        return
    win.title('TPad - '+os.path.basename(url))

file_menu.add_command(label = 'Open',image = open_icon,compound = tk.LEFT,accelerator = 'Ctrl+O',command = open_file)

#save
def save_file(event = None):
    global url
    content = text_editor.get(1.0,tk.END)
    try:
        if url:
            with open(url,'w',encoding= 'utf-8') as f:
                f.write(content)
        else:
            url = filedialog.asksaveasfile(initialdir = os.getcwd(),mode = 'w',defaultextension = '.txt',filetypes = (('Text Files','*.txt'),('All Files','*.*')))
            url.write(content)
            url.close()
            win.title('TPad - '+os.path.basename(url.name))
    except:
        return

file_menu.add_command(label = 'Save',image = save_icon,compound = tk.LEFT,accelerator = 'Ctrl+S',command = save_file)


#save_as
def save_as(event = None):
    global url
    content = text_editor.get(1.0,tk.END)
    try:
        url = filedialog.asksaveasfile(initialdir = os.getcwd(),mode = 'w',defaultextension = '.txt',filetypes = (('Text Files','*.txt'),('All Files','*.*')))
        url.write(content)
        url.close()
        win.title('TPad - '+os.path.basename(url.name))
    except:
        return

file_menu.add_command(label = 'Save As',image = save_as_icon,compound = tk.LEFT,accelerator = 'Ctrl+Shift+S',command = save_as)
print(url)
#exit
def exit_func(event = None):
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning','Do you want to save the file?')
            if mbox is True:
                save_file()
                win.destroy()
            elif mbox is False:
                win.destroy()
        else:
            win.destroy()
    except:
        return

file_menu.add_command(label = 'Exit',image = exit_icon,compound = tk.LEFT,accelerator = 'Ctrl+Q',command = exit_func)

# edit_menu_commands

#find
def find_func(event = None):
    find_dialogue = tk.Toplevel()
    find_dialogue.geometry('350x200+500+200')
    find_dialogue.title('Find')
    find_dialogue.resizable(0,0)
    
    find_frame = ttk.LabelFrame(find_dialogue,text = 'Find & Replace')
    find_frame.pack(pady = 30)

    find_label = ttk.Label(find_frame,text = 'Find : ')
    find_label.grid(row = 0,column = 0,padx = 4,pady = 4,sticky = tk.W)
    replace_label = ttk.Label(find_frame,text = 'Replace : ')
    replace_label.grid(row = 1,column = 0,padx = 4,pady = 4,sticky = tk.W)

    find_entry = ttk.Entry(find_frame,width = 25)
    find_entry.grid(row = 0,column = 1,padx = 4,pady = 4,sticky = tk.W)
    find_entry.focus()
    replace_entry = ttk.Entry(find_frame,width = 25)
    replace_entry.grid(row = 1,column = 1,padx = 4,pady = 4,sticky = tk.W)

    def find():
        word  = find_entry.get()
        text_editor.tag_remove('match',1.0,tk.END)
        matches = 0
        if word:
            start_pos = 1.0
            while True:
                start_match = text_editor.search(word,start_pos,stopindex=tk.END)
                if not start_match:
                    break
                end_pos = f'{start_match}+{len(word)}c'
                text_editor.tag_add('match',start_match,end_pos)
                start_pos = end_pos
                matches +=1
                text_editor.tag_config('match',foreground = 'red',background = 'yellow')

    def replace():
        word = find_entry.get()
        replacement = replace_entry.get()
        content = text_editor.get(1.0,tk.END)
        new_content = content.replace(word,replacement)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)

    find_btn = ttk.Button(find_frame,text = 'Find',command = find)
    find_btn.grid(row = 2,column = 0,padx = 4,pady = 6,sticky = tk.W)
    replace_btn = ttk.Button(find_frame,text = 'Replace',command = replace)
    replace_btn.grid(row = 2,column = 1,padx = 4,pady = 6,sticky = tk.W)

    find_dialogue.mainloop()



edit_menu.add_command(label = 'Copy',image = copy_icon,compound = tk.LEFT,accelerator = 'Ctrl+C',command = lambda:text_editor.event_generate('<Control c>'))
edit_menu.add_command(label = 'Paste',image = paste_icon,compound = tk.LEFT,accelerator = 'Ctrl+V',command = lambda:text_editor.event_generate('<Control v>'))
edit_menu.add_command(label = 'Cut',image = cut_icon,compound = tk.LEFT,accelerator = 'Ctrl+X',command = lambda:text_editor.event_generate('<Control x>'))
edit_menu.add_command(label = 'Clear All',image = clear_all_icon,compound = tk.LEFT,accelerator = 'Ctrl+Shift+X',command = lambda:text_editor.delete(1.0,tk.END))
edit_menu.add_command(label = 'Find',image = find_icon,compound = tk.LEFT,accelerator = 'Ctrl+F',command = find_func)




################################### View Menu Functionality ###############################


# view_menu_commands
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)
show_statusbar = tk.BooleanVar()
show_statusbar.set(True)

def view_toolbar():
    show = show_toolbar.get()
    if show:
        text_editor.pack_forget()
        scroll_bar.pack_forget()
        tool_bar.pack(side = tk.TOP,fill = tk.X)
        scroll_bar.pack(side = tk.RIGHT,fill = tk.Y)
        text_editor.pack(fill = tk.BOTH,expand = True)
    else:
        tool_bar.pack_forget()


def view_statusbar():
    show = show_statusbar.get()
    if show:
        text_editor.pack_forget()
        scroll_bar.pack_forget()
        status_bar.pack(side = tk.BOTTOM)
        scroll_bar.pack(side = tk.RIGHT,fill = tk.Y)
        text_editor.pack(fill = tk.BOTH,expand = True)
    else:
        status_bar.pack_forget()

view_menu.add_checkbutton(label = 'Tool Bar',onvalue = True,offvalue = False,variable = show_toolbar, image = tool_bar_icon,compound = tk.LEFT,command = view_toolbar)
view_menu.add_checkbutton(label = 'Status Bar',onvalue = True,offvalue = False,variable = show_statusbar,image = status_bar_icon,compound = tk.LEFT,command = view_statusbar)


# -----------------------------------&&&&&&&&&&&&&&&&&&&&----------------------------------



################################### Theme Menu Functionality ###############################


# theme_menu_commands
theme = tk.StringVar()
theme.set('Light Default')
def change_theme():
    selection = theme.get()
    color_tuple = color_dict.get(selection)
    fg_color , bg_color = color_tuple[0], color_tuple[1]
    text_editor.config(fg = fg_color,bg = bg_color)

c = 0
for i in color_dict:
    theme_menu.add_radiobutton(label = i,image = color_icons[c],compound = tk.LEFT,variable = theme,command = change_theme)
    c +=1

# -----------------------------------&&&&&&&&&&&&&&&&&&&&----------------------------------


#Bind Shortcut Keys

win.bind('<Control-n>',new_file)
win.bind('<Control-o>',open_file)
win.bind('<Control-s>',save_file)
win.bind('<Control-S>',save_as)
win.bind('<Control-q>',exit_func)
win.bind('<Control-X>',lambda i:text_editor.delete(1.0,tk.END))
win.bind('<Control-f>',find_func)


win.config(menu = main_menu)
win.mainloop()