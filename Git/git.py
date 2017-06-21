import csv,sys,os

class Git():
    """A class to handle git repositories and commands

    """

    def __init__(
        self,
        username='',
        password='',
        email='',
        repositories_csv='',
        git_directory='/home/user/GitHub'):
        """ 
        Args
            username (str): git username
            email (str): git email
            password (str): git password
            repositories_csv (str): csv filename
            git_directory (str): directory of GitHub folder
        
        """
        self.username = username
        self.password = password
        self.email = email
        self.repositories = {}
        self.read_repositories(repositories_csv)
        self.git_directiory = git_directory

    #TODO: getter methods
    #TODO: setter methods
    #TODO: reset methods

    def read_repositories(self,repositories_csv, delimiter=','):
        """
        Read in the repositories from .csv

        Args
            repositories_csv (str): csv filename
            delimiter (str): delimiter of the file
        """
        try:
            with open(repositories_csv, 'r') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=delimiter)
                try:
                    keys = reader.fieldnames
                    for row in reader:
                        #skip non-used lines
                        if not row['used_'] or row['used_'] == "FALSE":
                            continue
                        else:
                            self.repositories[row['repository']] = row
                except csv.Error as e:
                    sys.exit('file %s, line %d: %s' % (repositories_csv, reader.line_num, e))
        except IOError as e:
            sys.exit('%s does not exist' % e)

    def clone_repositories(self):
        """Clone git repositories
        """        
        for repository,row in self.repositories.items():
            change_dir_cmd = '''cd %s'''%(
                self.git_directiory
            )
            git_cmd = '''git clone -b %s https://%s:%s@github.com/%s/%s.git''' %(
                row['branch'],self.username,self.password,self.username,row['repository']
            )
            # git_cmd = '''git clone -b %s https://github.com/%s/%s.git''' %(
            #     row['branch'],self.username,row['repository']
            # )
            # os.system("echo %s" %(git_cmd)) # will show password on commandline!
            os_cmd = '''%s;%s''' %(change_dir_cmd, git_cmd)
            os.system(os_cmd)

    def push_repositories(self,commit_message='Quick save'):
        """Push repositories

        Args
            commit_message (str): commit message
        """
        for repository,row in self.repositories.items():
            change_dir_cmd = '''cd %s/%s'''%(
                self.git_directiory,row['repository']
            )
            git_cmd = '''git add .; git commit -m "%s"; git push origin %s''' %(
                commit_message,row['branch']
            )
            os_cmd = '''%s;%s''' %(change_dir_cmd, git_cmd)
            os.system("echo %s" %(git_cmd))
            os.system(os_cmd)

    def make_sslCert(self):
        """Create a ssl certificate for github

        """
        change_dir_cmd = '''cd %s'''%(
            self.git_directiory
        )
        #enable ssl cert
        ssl_cmd = '''git config --global http.sslVerify true '''
        os.system("echo %s" %(ssl_cmd))
        #write new gitconfig file
        gitconfig_file = '''
[http]
        sslVerify = true
        sslCAinfo = /etc/ssl/certs/ca-certificates.crt
[user]
        email = %s
        name = %s''' %(self.email, self.username)     
        os_cmd = '''%s;%s;rm -f gitconfig;echo "%s" > gitconfig''' %(
            change_dir_cmd, ssl_cmd, gitconfig_file)
        os.system(os_cmd)
