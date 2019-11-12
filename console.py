#!/usr/bin/python3
import cmd


classes = {"BaseModel": BaseModel, "State": State, "City": City, "Amenity": Amenity, "Place": Place, "Review": Review, "User": User}



class HBNBCommand(cmd.Cmd):
    """ Command interpreter """
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
            if args in classes
                MyModel = args
                MyModel.save()
                print(MyModel.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, args):
        if not args:
            print("** class name missing **")
        else: 
            else:
                print("** class doesn't exist **")
        
if __name__ == '__main__':
    HBNBCommand().cmdloop()
