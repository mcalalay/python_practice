from configurations import pipelines, pipeline_var
from python_terraform import *
from git import Repo
from distutils.dir_util import copy_tree
import os
import boto3
import re


for pipeline in pipelines:
    print(pipeline)


the_pipeline = input("Please choose a pipeline: ").lower()
backend_key = input("Please enter a backend key for your terraform state: ").lower()
bt_codebuild_name = input(
    "AWS Codebuild Name: Sample Format {projectname}-{module}-{pipelinename} \nEnter a value: ").lower()
bt_codecommit_name = input(
    "AWS CodeCommit Name: Sample Format {projectname}-{module}-{pipelinename} \nEnter a value: ").lower()
bt_codepipeline_name = input(
    "AWS CodePipeline Name: Sample Format {projectname}-{module}-{pipelinename} \nEnter a value: ").lower()
module_name = input("Unique Name for Module (e.g reviwersegmentation-aht, etc) \nEnter a value: ").lower()


print(f"Initializing terraform directory with backend key as: {backend_key}.")
print(f"Issuing Terraform apply for CICD with {the_pipeline} as pipeline")
print(f"Your AWS Codebuild Name is: {bt_codebuild_name}")
print(f"Your AWS CodeCommit Name is: {bt_codecommit_name}")
print(f"AWS CodePipeline Name is: {bt_codepipeline_name}")
print(f"Module Name is: {module_name}")

cicd_parameters = {"bt_codebuild_name":bt_codebuild_name,
                  "bt_codecommit_name":bt_codecommit_name,
                  "bt_codepipeline_name":bt_codepipeline_name,
                  "module_name":module_name}
print(cicd_parameters)

backend_config={'key': backend_key}

cwd = os.getcwd()+"\cicdpipeline"
var_file = "./env_tfvar/dev.tfvars"

print(cicd_parameters)
print(backend_config)
tf = Terraform(working_dir = cwd, var_file=var_file)
tf.init( reconfigure=True, backend_config = backend_config, capture_output=True)
tf.plan(no_color=IsFlagged, variables=cicd_parameters,refresh=False, capture_output=True)

terraform_apply = input("Do you wish to continue to terraform apply? (Y or N): ").lower()
if terraform_apply == "y":
    tf.apply(no_color=IsFlagged, variables=cicd_parameters, refresh=False, capture_output=True, skip_plan=True)
    print(f'''You have successfully terraformed with the following parameters: \n
CICD Parameters: \n{cicd_parameters}\n
Backend Key: {backend_key}\n
Will be proceeding to push your chosen pipeline template...\n
Chosen pipeline:{the_pipeline}\n''')
else:
    print("Aborting Terraforming...")



codecommit = boto3.client('codecommit')

project = input("Please input project name (sample: oieparterpilot, opsnav-client110, opsnav-client135: ").lower()
template_repository = project + "-terraform-template"

### can add if you want to switch aws keys here if else y or n then do an aws configure and ask for the keys
try:
    response = codecommit.get_repository(repositoryName=template_repository)
    print("Clone URL: " +response['repositoryMetadata']['cloneUrlHttp'])
    print(response['repositoryMetadata']['cloneUrlHttp'])
    #retrieving the repository URL
except Exception as e:
    print(e)
    print('Error getting repository {}. Make sure it exists and that your '
          'repository is in the same region as this function.'.format(template_repository))
    raise e


the_cicd_directory = os.getcwd() + "\\repo\{}".format(template_repository)
#cloning repository with aws credentials locally configured and removing git credentials manager
Repo.clone_from(response['repositoryMetadata']['cloneUrlHttp'],the_cicd_directory)




##the_pipeline = "datapipeline"
def templates():
    rootdir = 'path/to/dir'
    for it in os.scandir(the_cicd_directory):
        #checks all templates of pipelines in directory
        if it.is_dir():
            #taking last split of the directory taking only the pipeline
            #comparing that pipeline if it is the chosen pipeline
            the_folder = it.path.split('\\')
            if the_folder[-1] == the_pipeline:
                return it.path
the_template_dir = templates()
print(templates())


with open(the_template_dir + "\\env_tfvar\dev.tfvars", 'r') as file:
    data = file.read()
print(data)


def vars_selector(dict_groups):
    the_vars = []
    for key in dict_groups:
        group_vars = groups[key]
        for var in group_vars:
            the_vars.append(var)
    return the_vars


def vars_group_name(dict_groups):
    for key in dict_groups:
        return key


def vars_mapper(group_names, vars_list, data):
    for var in vars_list:
        old_value = re.search(f'{var}\s+=\s+([^\n]+)', data).group(1).strip()
        print(f"The original value for [ {var} ] from the group [ {group_names} ] is [ {old_value} ].")
        new_value = input(f"Please input a new value for {var}: ")
        if new_value != "":
            data = data.replace(old_value, new_value)
    return data


the_vars = []

groups_in_pipelines = range(len(pipeline_var[the_pipeline]))
for num_group in groups_in_pipelines:
    ###groups variables into each category
    groups = pipeline_var[the_pipeline][num_group]
    # print("This is the group: ", groups)

    vars_selector(groups)  ###returns a list of variables each time
    vars_group_name(groups)
    # print("this is the list of vars: ",vars_selector(groups))

    data = vars_mapper(vars_group_name(groups), vars_selector(groups), data)



# Replace the target string
print(data)

# # Write the file out again

with open(the_template_dir + "\\env_tfvar\dev.tfvars", 'w') as file:
    file.write(data)

bt_codecommit_name = "python-cicd-testing-datapipeline"

codecommit = boto3.client('codecommit')

created_repository = project + "-" + bt_codecommit_name

try:
    response = codecommit.get_repository(repositoryName=created_repository)
    print("Clone URL: " + response['repositoryMetadata']['cloneUrlHttp'])
    print(response['repositoryMetadata']['cloneUrlHttp'])
    # retrieving the repository URL
except Exception as e:
    print(e)
    print(
        'Error getting repository {}. Make sure it exists and that your repository is in the '
        'same region as this function.'.format(created_repository))
    raise e

the_pipeline_dir = os.getcwd() + "\\repo\{}".format(created_repository)

Repo.clone_from(response['repositoryMetadata']['cloneUrlHttp'], the_pipeline_dir)


###copies edited template and pastes it to the git repository
copy_tree(the_template_dir, the_pipeline_dir)



###push the git folder back to the repository
git_commit = input("Do you wish to proceed to git commit? (Y/N): ").lower()
if git_commit == "y":
    repo = Repo(the_pipeline_dir)
    repo.git.add('--all')
    repo.git.commit('-m', input("enter your git commit message: ").lower())
git_push = input("Do you wish to proceed to git push? (Y/N): ").lower()
if git_push == "y":
    origin = repo.remote(name='origin')
    origin.push()