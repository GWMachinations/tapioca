import i3ipc

def doWindows(ipc, event):
    if event.change == "new" or event.change == "move":
        print(event.change)
        print(event.container.workspace())
        for con in ipc.get_tree().descendants():
            #if con.name == "  I":
            #    for leafs in con.leaves():
             #       leafs.command('mark IIIII')
              #      #leafs.command('focus tiling)
               #     print(leafs.name)
            match con.name:
                case '  I':
                    setMarks(con, '  I')
                case '  II':
                    setMarks(con, '  II')
                case '  III':
                    setMarks(con, '  III')
                case '  IV':
                    setMarks(con, '  IV')
                case ' I':
                    setMarks(con, ' I')
                case ' II':
                    setMarks(con, ' II')
                case ' III':
                    setMarks(con, ' III')
                case ' IV':
                    setMarks(con, ' IV')
                case '󰄾 I':
                    setMarks(con, '󰄾 I')
                case '󰄾 II':
                    setMarks(con, '󰄾 II')
                case '󰄾 III':
                    setMarks(con, '󰄾 III')
                case '󰄾 IV':
                    setMarks(con, '󰄾 IV')

def setMarks(container, mark):
    for leaf in container.leaves():
        leaf.command('mark '+ mark)

def main():
    i3 = i3ipc.Connection()
    i3.on('window', doWindows) #when a window is moved, inherit coloring from new parent?
    i3.main()

if __name__ == '__main__':
    main()
