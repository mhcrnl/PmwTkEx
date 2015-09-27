from Tkinter import *
from tkFileDialog import *
from tkSimpleDialog import *
from ScrolledText import *
from tkMessageBox import *
import os

def new_command(event = None):
	t = 'Untitled.txt'
	confirm = result = askquestion("New File", "All unsaved work will be deleted.Continue?", icon = 'warning')
	if confirm == 'yes':
		textarea.delete('1.0',END)
	window.title(os.path.basename(t))
	lnupdater()
	
def open_command(event = None):
	filename = askopenfilename(parent = window,title = 'Select a file')
	if filename != None:
		fo = open(filename,mode = 'r')
		contents = fo.read()
		textarea.delete('1.0',END)
        textarea.insert('1.0',contents)
        fo.close()
        window.title(os.path.basename(filename))
	lnupdater()

def save_command(event = None):
    filename = asksaveasfilename(parent = window,defaultextension = '.txt',title = 'Save file as')
    if filename is not None:
    	file = open(filename,mode = 'w')
        data = textarea.get('1.0',END)
        file.write(data)
        file.close()
        lnupdater()

def saveas_command(event = None):
    f = asksaveasfilename(parent = window,defaultextension = '.txt',title = 'Save As')
    fs = open(f,mode = 'w')
    contents = textarea.get('1.0', END)
    fs.write(contents)
    fs.close()
    window.title(os.path.basename(f))

def exit_command(event = None):
	result = askquestion("Exit", "Are You Sure?", icon = 'warning')
	if result == 'yes':
		window.destroy()

def cut_command(event = None):
	window.clipboard_clear()
	window.clipboard_append(textarea.get(SEL_FIRST,SEL_LAST))
	textarea.delete(SEL_FIRST, SEL_LAST)
	lnupdater()

def copy_command(event = None):
	window.clipboard_clear()
	text = window.clipboard_append(textarea.get(SEL_FIRST,SEL_LAST))
	lnupdater()

def paste_command(event = None):
	text = textarea.selection_get(selection = 'CLIPBOARD')
	textarea.insert(INSERT,text)
	lnupdater()

def unhighlight(event,t):
	x = 1
	while x != t+1:
		ustring = 'highlight' + str(x)
		textarea.tag_config(ustring,background = 'white')
		x = x + 1

def undo_command(event = None):
	try:
		textarea.edit_undo()
		lnupdater()
	except TclError:
		pass

def redo_command(event = None):
	try:
		textarea.edit_redo()
		lnupdater()
	except TclError:
		pass

def find_command(event = None,key = None,c = None):
	target = key or askstring('Find', 'Find Word : ')
	global j
	if c:
		j = c
	else:
		j = '0.0'
	global lastTarget 
	lastTarget = target
	if target:
		where = textarea.search(target,j,stopindex = END)
		if where:
			rs,cs = where.split('.')
			textarea.tag_remove(SEL,'1.0',END)
			ncs = int(cs) + (len(target))
			j = str(rs) + '.' + str(ncs)
			textarea.tag_add(SEL,where,j)
		else:
			showinfo(title = 'Information', message = 'Word was not found.')
	
def findnext_command(event = None):
	find_command(event,lastTarget,j)
	lnupdater()

def fb(event = None,l = None,c = None,s1 = None,s2 = None):
	global fb1
	global fb2
	fbt = l or askstring('Find Word', 'Enter the word to find: ')
	if s1 is None and s2 is None:
		fb1 = askinteger('Start Line','Enter the start line : ')
		fb2 = askinteger('End Line','Enter the end line : ')
	else:
		fb1 = s1
		fb2 = s2
	fb1c = str(fb1) + '.0'
	fb2c = str(fb2 + 1) + '.0'
	global m
	if c:
		m = c
	else:
		m = fb1c
	global LT
	LT = fbt
	loc = textarea.search(fbt,m,fb2c)
	if loc:
		rs,cs = loc.split('.')
		ncs = int(cs) + (len(fbt))
		textarea.tag_remove(SEL,'1.0',END)
		m = str(rs) + '.' + str(ncs)
		textarea.tag_add(SEL,loc,m)
	else:
		if s1 is not None:
			showinfo(title = 'Information', message = 'No more words.')
		else:
			showinfo(title = 'Information', message = 'Word not found.')

def fab_command(event = None):
        fbt = askstring('Find Word', 'Enter the word to find: ')
        fb1 = askinteger('Start Line','Enter the start line : ')
        fb2 = askinteger('End Line','Enter the end line : ')
        fb1c = str(fb1) + '.0'
        fb2c = str(fb2 + 1) + '.0'
        search_for(fbt,textarea,fb1c,fb2c)                

def search_for(tw,textarea,i1,i2) :
        textarea.tag_remove('match', '1.0', END)
        count = 0
        if tw:
        	pos = i1
        	while True:
        		pos = textarea.search(tw, pos,i2)
        		if not pos:
        			break
        		lastpos = '%s+%dc' % (pos, len(tw))
        		textarea.tag_add('match', pos, lastpos)
        		count += 1
        		pos = lastpos
                textarea.tag_config('match', foreground='red')
                showinfo(title = 'Information', message = '%d matches found' %count)
                textarea.tag_remove('match', '1.0', END)
        textarea.focus_set()
        textarea.mark_set('insert',lastpos)

def fnb(event = None):
	fb(event,LT,m,fb1,fb2)
	lnupdater()

def replace_command(event = None):
	ftarget = askstring('Find Word', 'Enter the word to find: ')
	if ftarget:
		foundString = textarea.search(ftarget, '1.0', END)
		if foundString:
			rtarget = askstring('Replace with', 'Enter the word to replace it with : ')
			foundText = foundString + ('+%dc' % len(ftarget))
			textarea.tag_add(SEL, foundString, foundText)
			textarea.mark_set(INSERT, foundText)
			textarea.delete(SEL_FIRST, SEL_LAST)
			textarea.insert('insert', rtarget)
		else:
			showerror(title = 'Error', message = 'Word was not found.')
	lnupdater()

def selectall_command(event = None):
	textarea.tag_add(SEL,'1.0',END+'-1c')
	textarea.mark_set(INSERT,'1.0')
	textarea.see(INSERT)

def highlight_line(interval = 100):
    textarea.tag_remove("active_line", 1.0, END)
    textarea.tag_add("active_line", "insert linestart", "insert lineend+1c")
    textarea.after(interval, toggle_highlight)

def undo_highlight():
    textarea.tag_remove("active line", 1.0, END)
    textarea.tag_configure("active_line", background = 'white')

def toggle_highlight(event = None):
    val = hltln.get()
    undo_highlight() if not val else highlight_line()

def theme(event = None):
    global bgc, fgc
    val = themechoice.get()
    clrs = colorschemes.get(val)
    fgc, bgc = clrs.split('.')
    fgc, bgc = '#'+fgc, '#'+bgc
    textarea.config(bg = bgc, fg = fgc)

def bottom_bar():
    val = bbar.get()
    if val:
        bottombar.pack(expand = NO, fill = None, side = RIGHT, anchor = 'se')
    elif not val:
        bottombar.pack_forget()

def lnupdater(event = None):
    txt = ''
    el, ec = textarea.index('end-1c').split('.')
    txt = '\n'.join(map(str, range(1, int(el)+1)))
    cl, cc = textarea.index('insert').split('.')
    bottombar.config(text = 'Row : %s | Column: %s' %(cl,cc))
    #print "EL : ",el,"CL : ",cl
    if lc.get():
        lnc.pack(side = LEFT, anchor = 'nw', fill = Y)
    	lnc.config(text = txt,anchor = 'nw')
    elif not lc.get():
    	lnc.config(text = '',anchor = 'nw')

def lnupdatermouse(event):
	cl,cc = textarea.index(CURRENT).split('.')
	bottombar.config(text = 'Row : %s | Column: %s' %(cl,cc))

def current_command(event):
	print textarea.index(CURRENT)

def col_sel_end(event=None, delete=0):
    try:
        start_index = textarea.index("sel.first").split(".")
        end_index = textarea.index("sel.last").split(".")
        start_line = int(start_index[0])
        start_char = int(start_index[1])
        end_line = int(end_index[0])
        end_char = int(end_index[1])
        text = ""
        counter = 0
        no_of_lines = end_line - start_line + 1
        while no_of_lines > 0:
            start_col_sel = str(start_line + counter) + "." + str(start_char)
            end_col_sel = str(start_line + counter) + "." + str(end_char)
            if delete == 1:
                textarea.delete(start_col_sel, end_col_sel)
            else:
                text = text + textarea.get( start_col_sel, end_col_sel ) + "\n"
            counter = counter + 1
            no_of_lines = no_of_lines - 1
        return text
    except TclError:
        textarea.tag_delete("selection")
        textarea.mark_set("insert", INSERT)
        
def col_sel_begin(event=None):
    textarea.bind("<ButtonRelease-1>", col_sel_end)
    textarea.tag_delete("selection")
    try:
        start_index = textarea.index("sel.first").split(".")
        end_index = textarea.index("sel.last").split(".")
        start_line = int(start_index[0])
        start_char = int(start_index[1])
        end_line = int(end_index[0])
        end_char = int(end_index[1])
        counter = 0
        no_of_lines = end_line - start_line + 1
        while no_of_lines > 0:
            start_line_char = str(start_line + counter) + "." + str(start_char)
            end_line_char = str(start_line + counter) + "." + str(end_char)
            textarea.tag_add("selection", start_line_char, end_line_char)
            no_of_lines = no_of_lines - 1
            counter = counter + 1
        textarea.tag_config("selection", background="blue", foreground="black")
    except TclError:
        textarea.mark_set("insert", INSERT)

def column_selection():
    if rs.get() == 1:
        textarea.config(selectbackground="white", inactiveselectbackground="white", selectforeground="black") 
        textarea.bind("<B1-Motion>", col_sel_begin)
    elif rs.get() == 0:
        textarea.unbind("<B1-Motion>")
        textarea.unbind("<ButtonRelease-1>")
        textarea.config(selectbackground="gray", inactiveselectbackground="white", selectforeground="black")


window = Tk()
window.geometry('500x500')
window.protocol('WM_DELETE_WINDOW', exit_command)
lnc = Label(window,width = 2,bg = 'white')
lnc.pack(side = LEFT, anchor = 'nw', fill = Y)
textarea = ScrolledText(window,undo = 1)
menubar = Menu(window)

filemenu = Menu(menubar,tearoff = 0)
filemenu.add_command(label = "New",command = new_command,accelerator = "Ctrl+N")
filemenu.add_command(label = "Open",command = open_command,accelerator = "Ctrl+O")
filemenu.add_command(label = "Save",command = save_command,accelerator = "Ctrl+S")
filemenu.add_command(label = "Save As",command = saveas_command,accelerator = "Ctrl+Shift+S")
filemenu.add_separator()
filemenu.add_command(label = "Exit",command = exit_command,accelerator = "Ctrl+Q")
menubar.add_cascade(label = "File",menu = filemenu)

editmenu = Menu(menubar,tearoff = 0)
editmenu.add_command(label = "Undo",command = undo_command,accelerator = "Ctrl+Z")
editmenu.add_command(label = "Redo",command = redo_command,accelerator = "Ctrl+Y")
editmenu.add_separator()
editmenu.add_command(label = "Copy",command = copy_command,accelerator = "Ctrl+C")
editmenu.add_command(label = "Cut",command = cut_command,accelerator = "Ctrl+X")
editmenu.add_command(label = "Paste",command = paste_command,accelerator = "Ctrl+V")
editmenu.add_separator()
editmenu.add_command(label = "Select All",command = selectall_command,accelerator = "Ctrl+A")
menubar.add_cascade(label = "Edit",menu = editmenu)

viewmenu = Menu(menubar,tearoff = 0)
viewmenu.add_command(label = "Find",command = find_command,accelerator = "Ctrl+F")
viewmenu.add_command(label = "Find Next",command = findnext_command,accelerator = "Ctrl+Shift+F")
viewmenu.add_command(label = "Find All Between",command = fab_command,accelerator = "Ctrl+Alt+F")
#viewmenu.add_command(label = "Find Between",command = fb,accelerator = "Ctrl+Alt+F")
#viewmenu.add_command(label = "Find Next Between",command = fnb)
viewmenu.add_command(label = "Replace",command = replace_command,accelerator = "Ctrl+R")
lc = IntVar()
lc.set(1)
viewmenu.add_checkbutton(label = "Display line numbers",onvalue = 1, offvalue = 0,variable = lc,command = lnupdater)
bbar = IntVar()
bbar.set(1)
viewmenu.add_checkbutton(label = "Line and column information", onvalue = 1, offvalue = 0,variable = bbar, command = bottom_bar)
hltln = IntVar()
viewmenu.add_checkbutton(label = "Highlight current line", onvalue = 1, offvalue = 0, variable = hltln, command = toggle_highlight)
rs = IntVar()
rs.set(0)
viewmenu.add_checkbutton(label = "Column Selection",onvalue = 1, offvalue = 0,variable = rs,command = column_selection)
themesmenu = Menu(menubar, tearoff = 0)
viewmenu.add_cascade(label = "Themes", menu = themesmenu)
menubar.add_cascade(label = "View",menu = viewmenu)

colorschemes = {
'White': '000000.FFFFFF',
'Grey':'83406A.D1D4D1', 
'Aqua': '5B8340.D1E7E0',
}
themechoice = StringVar()
themechoice.set('White')
for k in sorted(colorschemes):
    themesmenu.add_radiobutton(label = k, variable = themechoice, command = theme)

bottombar = Label(textarea, text = 'Row : 1 | Column : 0')
bottombar.pack(expand = NO, fill = None, side = RIGHT, anchor = 'se')    

textarea.tag_configure("active_line", background = "yellow")
textarea.bind("<Any-KeyPress>", lnupdater)
textarea.bind("<Button-1>", lnupdatermouse)

window.bind('<Control-n>', new_command)
window.bind('<Control-o>', open_command)
window.bind('<Control-s>', save_command)
window.bind('<Control-Shift-KeyPress-S>', saveas_command)
window.bind('<Control-q>', exit_command)
window.bind('<Control-z>', undo_command)
window.bind('<Control-y>', redo_command)
window.bind('<Control-x>', cut_command)
window.bind('<Control-c>', copy_command)
window.bind('<Control-v>', paste_command)
window.bind('<Control-f>', find_command)
window.bind('<Control-Shift-KeyPress-F>', findnext_command)
window.bind('<Control-Alt-KeyPress-F>', fab_command)
window.bind('<Control-r>', replace_command)
window.bind('<Control-a>', selectall_command)
window.bind('<Control-g>', current_command)
#window.bind('<Control-Backspace>', ctrlback)

window.config(menu = menubar)
textarea.pack(expand = YES, fill = BOTH)
window.title("ONGC Editor")
window.mainloop()
