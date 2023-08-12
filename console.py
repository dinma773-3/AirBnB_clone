#!/usr/bin/python3
"""command Interpreter"""
import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    """The console class for the interpreter"""
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """EOF signals end of file and quits the command interpreter
        Returns:
            True
        """
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        Returns:
            True
        """
        return True

    def do_create(self, line):
        """Creates an instance of the class inputed"""
        if line == '':
            print("** class name missing **")
        else:
            g = _split(line)
            if g[0] not in classes:
                print("** class doesn't exist **")
            else:
                print(eval(g[0])().id)
                storage.save()

    def do_show(self, line):
        """prints the string rep. if an instance based on the class name
            and id
        """
        if line == '':
            print("** class name missing **")
        else:
            g = _split(line)
            if g[0] not in classes:
                print("** class doesn't exist **")
            else:
                if len(g) == 1:
                    print("** instance id missing **")
                elif len(g) > 1:
                    object_dict = storage.all()
                    if "{}.{}".format(g[0], g[1]) not in object_dict:
                        print("** no instance found **")
                    else:
                        print(object_dict["{}.{}".format(g[0], g[1])])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        if line == '':
            print("** class name missing **")
        else:
            g = _split(line)
            if g[0] not in classes:
                print("** class doesn't exist **")
            else:
                if len(g) == 1:
                    print("** instance id missing **")
                elif len(g) > 1:
                    object_dict = storage.all()
                    if "{}.{}".format(g[0], g[1]) not in object_dict:
                        print("** no instance found **")
                    else:
                        del object_dict["{}.{}".format(g[0], g[1])]
                        storage.save()

    def do_all(self, line):
        """prints all string representation of all instances based or
            not on the class name
        """
        object_dict = storage.all()
        if line == '':
            ulist = [str(h) for h in object_dict.values()]
            print(ulist)
        else:
            g = _split(line)
            if g[0] not in classes:
                print("** class doesn't exist **")
            else:
                ulist = [str(h) for h in object_dict.values()]
                dlist = []
                for i in ulist:
                    if g[0] in i:
                        dlist.append(i)
                print(dlist)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
