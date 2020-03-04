import sys

args = sys.argv[1:]

def view(fname='yankee.txt', view_size=25):
  pages = getPages(fname, view_size)
  intro = str(pages[0]) + ' lines read. Press Enter to continue...'
  input(intro)
  inp = 1
  page = 2
  while (inp != 'q'):
    if (str(inp).isdigit() or inp == 'u' or inp == 'd' or inp == 't' or inp == 'b'):
      if (str(inp).isdigit()):
        page = int(inp) + 1 # this is to manage that zero is number of lines
        if (page < 2):
          page = 2
        elif (page > (len(pages))):
          page = len(pages)
      elif (inp == 'u'):
        page -= 1
        if (page < 2):
          page = 2
          print('AT TOP OF FILE.')
      elif (inp == 'd'):
        page += 1
        if (page > len(pages)):
          page = len(pages)
          print('AT BOTTOM OF FILE.')
      elif (inp == 't'):
        page = 2
      elif (inp == 'b'):
        page = len(pages)
      disp(fname, view_size, pages[page-1])
    else:
      print('Invalid Command.')
    inp = input('Command [u,d,t,b,#,q]: ')
    print('\n')

def disp(fname, view_size, seeker):
  text = open(fname, 'r')
  text.seek(seeker)
  for line in range(view_size):
    print(text.readline())
  

def getPages(fname, view_size):
  lineNum = 1
  text = open(fname, 'r')
  pages = [text.tell()]
  for line in iter(text.readline, ''):
    if (lineNum % view_size == 0):
      pages.append(text.tell())
    lineNum += 1
  pages.insert(0,lineNum) # first element in pages is the amount of lines in file
  return pages

if __name__ == '__main__':
  view(*args)
