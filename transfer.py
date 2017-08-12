import os
import json
import subprocess

class GitTransfer():
    def __init__(self, new_repo, old_alias, new_alias):
        self.path = os.getcwd()
        self.new_repo = new_repo
        self.old_alias = old_alias
        self.new_alias = new_alias

    def check_path(self):
        return os.path.exists(os.path.join(self.path, '.git'))

    def get_current_repo_branches(self):
        old_origin_branches = []
        branches = subprocess.check_output('git branch --all', shell=True)
        for branch in branches.split('\n'):
            if branch.find('remotes') is not -1:
                old_origin_branches.append(branch.strip().replace("remotes/%s/" % self.old_alias, ""))
        return old_origin_branches

    def transfer(self):
        data = dict()
        if not self.check_path():
            data.update({
                'error': 'This is not a local git repository.'
            })
            return json.dumps(data)

        if not self.new_repo.endswith('.git') or not self.new_repo.startswith('ssh://'):
            data.update({
                'error': 'This is not a valid repo.'
            })
            return json.dumps(data)

        all_old_repo_branches = self.get_current_repo_branches()
        os.system("git remote add %s %s" % (self.new_alias, self.new_repo))

        print "First add the master branch to the new repo"
        os.system("git checkout master")
        os.system("git push --all %s" % self.new_alias)
        os.system("git push --tags %s" % self.new_alias)

        for branch in all_old_repo_branches:
            print "\n\n------------- Now pushing the branch %s --------------\n\n" % branch
            os.system("git checkout %s" % branch)
            os.system("git push --all %s" % self.new_alias)
            os.system("git push --tags %s" % self.new_alias)
        os.system("git remote rm %s" % self.old_alias)
        print "Old remote is deleted"
        os.system("git remote rename %s %s" % (self.new_alias, self.old_alias)
        print "Old remote %s becomes %s" % (self.old_alias, self.new_alias)

        data.update({
            'success': 'The new repo for your project is: ' + str(self.new_repo)
        })
        return json.dumps(data)

new_repo = raw_input("Provide your new repository (SSH URL)\nFor example: 'ssh://path/to/git/repo/project.git': ")
old_alias = raw_input("You old repository alias (eg. origin): ")
if old_alias is not 'origin':
    permission = raw_input("Are you sure about your old alias? (y/n): ")
else:
    permission = 'y'
if permission is not 'y':
    print json.dumps({"error": "Please try again. Process exit."})
    exit()
new_alias = raw_input("You new alias which will be renamed to old one at the end of the process: ")
if old_alias == new_alias:
    print json.dumps({"error": "Old alias cannot be same as new alias. Process exit."})
    exit()
gt = GitTransfer(new_repo, old_alias, new_alias)
print gt.transfer()
