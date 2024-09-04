class Directory:
    def __init__(self, name):
        self.name = name
        self.is_dir = True
        self.dir_list = []

    def get_list(self, name_dir):
        if self.name == name_dir:
            return self.dir_list
        else:
            for dir in self.dir_list:
                result = dir.get_list(name_dir)
                if result:
                    return result
        return []

    def print_all(self, depth=0):
        print(f"{self.name}:{depth}")
        for dir in self.dir_list:
            dir.print_all(depth + 1)

    def add_dir(self, current_dir, name_subdir, parent_name):
        if self.name == parent_name:
            new_dir = Directory(name_subdir)
            self.dir_list.append(new_dir)
        else:
            for dir in self.dir_list:
                dir.add_dir(current_dir, name_subdir, parent_name)

    def add_file(self, current_dir, name_file, parent_name):
        if self.name == parent_name:
            new_file = Directory(name_file)
            new_file.is_dir = False
            self.dir_list.append(new_file)
        else:
            for dir in self.dir_list:
                dir.add_file(current_dir, name_file, parent_name)

    def go_to_dir(self, current_dir, path):
        if self.name == path:
            return True
        for dir in self.dir_list:
            if dir.go_to_dir(current_dir, path):
                return True
        return False

    def exists(self, path):
        if self.name == path:
            return True
        for dir in self.dir_list:
            if dir.exists(path):
                return True
        return False

    def copy_real_directory(self, current_dir, path, parent_name):
        # Here you would implement the functionality to copy a real directory into the simulated structure
        pass

    def del_dir(self, dir_name):
        self.dir_list = [dir for dir in self.dir_list if dir.name != dir_name]

class FileManager:
    def __init__(self, name_dir):
        self.file_system = Directory(name_dir)
        self.curr_directory = [name_dir]
        self.is_run = True

    def read_command(self, c):
        if c.command == "CD":
            if c.arg_1:
                self.cd(c.arg_1)
            else:
                self.cd()
        elif c.command == "MKDIR":
            self.mkdir(c.arg_1)
        elif c.command == "DIR":
            self.dir()
        elif c.command == "QUIT":
            self.quit()
        elif c.command == "UNMOUNT":
            self.unmount(c.arg_1)
        elif c.command == "SAVE":
            self.save()
        elif c.command == "MOUNT":
            self.mount(c.arg_1)

    def cd(self, path=None):
        if path:
            full_path = self.get_path() + path + "/"
            if self.file_system.exists(path):
                self.curr_directory.append(path)
            else:
                print(f"Error: Directory '{path}' does not exist.")
        else:
            if len(self.curr_directory) > 1:
                self.curr_directory.pop()

    def mkdir(self, name_subdir):
        self.file_system.add_dir(self.file_system, name_subdir, self.curr_directory[-1])

    def mkfile(self, name_file):
        self.file_system.add_file(self.file_system, name_file, self.curr_directory[-1])

    def dir(self):
        print("Contents of the directory:")
        for it in self.file_system.get_list(self.curr_directory[-1]):
            if it.is_dir:
                print(f"[{it.name}] : {len(it.get_list(it.name))}")
            else:
                print(it.name)
        print()

    def mount(self, path):
        self.file_system.copy_real_directory(self.file_system, path, self.curr_directory[-1])

    def unmount(self, dir_name):
        self.file_system.del_dir(dir_name)

    def quit(self):
        self.is_run = False

    def save(self):
        self.file_system.print_all()

    def get_path(self):
        return "/".join(self.curr_directory) + "/"

def render(manager):
    while manager.is_run:
        print(manager.get_path())
        input_command = input()
        command_parts = input_command.split()
        command = command_parts[0].upper()
        arg_1 = command_parts[1] if len(command_parts) > 1 else ""
        manager.read_command(Command(command, arg_1))

class Command:
    def __init__(self, command, arg_1=""):
        self.command = command
        self.arg_1 = arg_1

def find_command(input_command):
    parts = input_command.split()
    command = parts[0].upper()
    arg_1 = parts[1] if len(parts) > 1 else ""
    return Command(command, arg_1)


manager = FileManager("root")
render(manager)


