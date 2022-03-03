#!/usr/bin/python3

"""
create a console aribnb
"""
import cmd


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb)'

    def do_quit(self, args):
        "Exit of commands interpreter"
        return True

    def do_EOF(self, args):
        """End of file cmd"""
        return True

    def emptyline(self, args):
        "When there is an empty line it jumps"
        pass

    def help_quit(self):
        """help_quit"""
        print("Quit command to exit the program\n")
            

if __name__ == '__main__':
    HBNBCommand().cmdloop()
