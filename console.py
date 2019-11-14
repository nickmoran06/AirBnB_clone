#!/usr/bin/python3
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.user import User
classes = {'BaseModel': BaseModel, 'State': State,
           'City': City, 'Amenity': Amenity, 'Place': Place,
           'Review': 'Review', 'User': User}


class HBNBCommand(cmd.Cmd):
    """ Command interpreter """

    prompt = "(hbnb) "

    def do_quit(self, args):
        """ quit command to exit the program """
        return True

    def do_EOF(self, args):
        """ EOF command to exit the program """
        return True

    def do_emptyline(self):
        """ does not take any action """
        pass

    def do_create(self, args):
        """  Creates a new instance of BaseModel,
        saves and prints the id """
        if not args:
            print("** class name missing **")
        else:
            if args in classes:
                new = classes[args]()
                new.save()
                print(new.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, args):
        """ Prints the string of an instance
        based on the class name and id """
        arg = shlex.split(args)

        if not arg:
            print("** class name missing **")
            return
        else:
            if arg[0] in classes:
                if len(arg) > 1:
                    try:
                        key = str(arg[0] + "." + arg[1])
                        print(storage.all()[key])
                    except:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, args):
        """ Prints the string of an instance
        based on the class name and id """
        arg = shlex.split(args)

        if not arg:
            print("** class name missing **")
            return
        else:
            if arg[0] in classes:
                if len(arg) > 1:
                    try:
                        key = str(arg[0] + "." + arg[1])
                        del storage.all()[key]
                    except:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")

    def do_all(self, args):
        """ Prints all instances based or not on the class name """
        arg = shlex.split(args)
        My_list = []
        name = storage.all()
        if len(arg) == 0:
            for key, value in name.items():
                print(value)
        elif arg[0] in classes:
            for key, value in name.items():
                if arg[0] in str(value):
                    print(value)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """ instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file) """
        arg = shlex.split(args)
        tam = len(arg)
        if not arg:
            print("** class name missing **")
            return
        else:
            if arg[0] in classes:
                if len(arg) > 1:
                    if len(arg) > 2:
                        if len(arg) > 3:
                            key = str(arg[0] + "." + arg[1])
                            name = storage.all()
                            if key in name:
                                setattr(name[key], arg[2], arg[3])
                                name[key].save()
                        else:
                            print("** value missing **")
                    else:
                        key = str(arg[0] + "." + arg[1])
                        name = storage.all()
                        if key not in name:
                            print("** no instance found **")
                        else:
                            print("** attribute name missing **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
