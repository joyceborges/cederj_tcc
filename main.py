import argparse
from project import Project

prj = Project(None, None, None)
operations = prj._operations.keys()
all_projects = prj.list_all_project()

def main():

    # Open parser
    parser = argparse.ArgumentParser(prog = 'TCC CEDERJ', 
                                     description='MVP - App for training, testing and using models')
    
    # Add subparsers
    parser.add_argument("operation", choices=operations, help="The operation to perform on the model (Ccreate, open, save)")

    parser.add_argument('choose', type=int, choices=range(1, len(all_projects) + 1),
                        help='Choose a project folder by index (1, 2, 3, etc.)')
    

if __name__ == '__main__':
    main()
    print('END')