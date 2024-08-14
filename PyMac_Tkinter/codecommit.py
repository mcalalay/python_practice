from git import Repo
from tkinter import *
from tkinter import messagebox
import boto3
import os
FONT_LABEL = ("Segoe UI", 10, "normal")
codecommit = boto3.client('codecommit')
GIT_COMMIT_MESSAGE = ""
COMMITTED = False


def clone_codecommit(repository, cicd_or_module):
    window = Tk()
    aws_keys = messagebox.askokcancel(title="CONFIRM AWS KEYS", message="Have you configured the correct AWS Keys?")
    if aws_keys:
        window.destroy()
        try:
            response = codecommit.get_repository(repositoryName=repository)
            print("Clone URL: " + response['repositoryMetadata']['cloneUrlHttp'])
            print(response['repositoryMetadata']['cloneUrlHttp'])
            # retrieving the repository URL
        except Exception as e:
            print(e)
            print('Error getting repository {}. Make sure it exists and that your '
                  'repository is in the same region as this function.'.format(repository))
            raise e
        if cicd_or_module == "cicd":
            the_cicd_directory = os.getcwd() + "\\templates\\{}".format(repository)
        else:
            the_cicd_directory = os.getcwd() + "\\module\\{}".format(repository)
        print(the_cicd_directory)
        # cloning repository with aws credentials locally configured and removing git credentials manager
        isdir = os.path.isdir(the_cicd_directory)
        if not isdir:
            Repo.clone_from(response['repositoryMetadata']['cloneUrlHttp'], the_cicd_directory)
        return the_cicd_directory
    else:
        print("Please configure AWS Keys first.")


def push_codecommit(pipeline_directory):
    while True:
        window = Tk()
        window.title("Python CICD Creator")
        window.config(pady=50, padx=50)
        Label(text="Enter your git commit message:", font=FONT_LABEL).grid(row=1, column=0)
        text_input = Entry(width=60)


        def save_git_message():
            global GIT_COMMIT_MESSAGE, COMMITTED
            GIT_COMMIT_MESSAGE = text_input.get()
            COMMITTED = True

        text_input.grid(row=0, column=1)
        Button(text="Confirm", width=96, command= save_git_message).grid(row=8, column=0, columnspan=2)

        if COMMITTED:
            proceed_git_commit = messagebox.askokcancel(title="Git commit?",
                                                        message=f"Do you wish to proceed to git commit?")
            if proceed_git_commit and GIT_COMMIT_MESSAGE != "":
                repo = Repo(pipeline_directory)
                repo.git.add('--all')
                repo.git.commit('-m', GIT_COMMIT_MESSAGE.lower())


            proceed_git_push = messagebox.askokcancel(title="Git commit?",
                                                        message=f"Do you wish to proceed to git push?")
            if proceed_git_push:
                origin = repo.remote(name='origin')
                origin.push()
                window.destroy()
                break

            else:
                window.destroy()
                window2 = Tk()
                abort_git_push = messagebox.askokcancel(title="Cancel?",
                                                        message="Do you wish to abort git pushing?")
                if abort_git_push:
                    window2.destroy()
                    break
                else:
                    window2.destroy()
                    continue

