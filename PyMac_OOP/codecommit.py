from git import Repo
import boto3
import os

codecommit = boto3.client('codecommit')


def clone_codecommit(repository):
    aws_keys = input("Have you configured the correct AWS Keys? (Y/N): ").lower()
    if aws_keys == "y":
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

        the_cicd_directory = os.getcwd() + "\\repo\\{}".format(repository)
        # cloning repository with aws credentials locally configured and removing git credentials manager
        Repo.clone_from(response['repositoryMetadata']['cloneUrlHttp'], the_cicd_directory)
        return the_cicd_directory
    else:
        print("Please configure AWS Keys first.")


def push_codecommit(pipeline_directory):
    git_commit = input("Do you wish to proceed to git commit? (Y/N): ").lower()
    if git_commit == "y":
        repo = Repo(pipeline_directory)
        repo.git.add('--all')
        repo.git.commit('-m', input("enter your git commit message: ").lower())
    git_push = input("Do you wish to proceed to git push? (Y/N): ").lower()
    if git_push == "y":
        origin = repo.remote(name='origin')
        origin.push()