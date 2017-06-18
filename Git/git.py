import csv,sys,os

class Git():
    """A class to handle git repositories and commands
    """

    def __init__(self,username,password,repository_csv):
        self.username = username
        self.password = password
        self.repositories = {}
        self.read_repositories(repository_csv)

    def read_repositories(self,repository_csv, delimiter=','):
        """
        Read in the repositories from .csv
        """
        try:
            with open(repository_csv, 'r') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=delimiter);
                try:
                    keys = reader.fieldnames;
                    for row in reader:
                        if row['used_'] or row['used_']=="TRUE":
                            self.repositories[row['repository']] = row
                except csv.Error as e:
                    sys.exit('file %s, line %d: %s' % (repository_csv, reader.line_num, e));
        except IOError as e:
            sys.exit('%s does not exist' % e);

    def clone_repositories(self):
        """Clone git repositories
        """        
        for repository,row in self.repositories.items():
            git_cmd = '''git clone -b %s https://%s:%s@github.com/%s/%s.git''' %(
                row['branch'],self.username,self.password,self.username,row['repository']
            )
            os.system("echo %s" %(git_cmd))
            os.system(git_cmd)

    def push_repositories(self,commit_message='Quick save'):
        """Push repositories
        """
        for repository,row in self.repositories.items():
            git_cmd = '''cd /home/user/GitHub/%s; git add .; git commit -m "%s"; git push origin %s''' %(
                row['repository'],commit_message,row['branch']
            )
            os.system("echo %s" %(git_cmd))
            os.system(git_cmd)
