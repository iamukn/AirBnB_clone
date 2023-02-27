#!/usr/bin/python3
import cmd

class CommandInterpreter(cmd.Cmd): 
    """A simple command interpreter class"""



    intro = 'Welcome to the AirBnB command interpreter. Type help or ? to list commands.\n'
    prompt = '(AirBnB) '



    def do_create_object(self, args):
     """Create a new object with the given name"""
     if args:

        object_type, object_name = args.split()
        print(f'Creating new {object_type} object with name "{object_name}"')

    else:
        print("Error: Please provide the required arguments")

 


    def do_list_objects(self, args):
       """List all objects of the given type"""

        object_type = args.strip()
        print(f'Listing all {object_type} objects...')



    def do_show_object(self, args):
        """Show the details of the object with the given ID"""

        object_id = args.strip()
        print(f'Showing details for object with ID "{object_id}"')



    def do_update_object(self, args):
        """Update the information for the object with the given ID"""

        object_id, attribute, value = args.split()
        print(f'Updating {attribute} for object with ID "{object_id}" to "{value}"')



    def do_delete_object(self, args):
        """Delete the object with the given ID"""

        object_id = args.strip()
        print(f'Deleting object with ID "{object_id}"')



    def do_quit(self, args):
        """Quit the command interpreter"""

        print('Goodbye!')
        return True

if __name__ == '__main__':
    CommandInterpreter().cmdloop()


