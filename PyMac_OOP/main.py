from configurations import pipelines, pipeline_var
from distutils.dir_util import copy_tree
from user_input import UserInput
from terraformer import terraforming
from codecommit import clone_codecommit, push_codecommit
import os
import re


for pipeline in pipelines:
    print(pipeline)

user_input = UserInput()
user_input.initial_input()
user_input.print_initial_input()
user_input.save_user_input()

backend_config={'key': user_input.backend_key}



print(backend_config)

project = input("Please input project name (sample: oieparterpilot, opsnav-client110, opsnav-client135: ").lower()
template_repository = project + "-terraform-template"

the_cicd_directory = clone_codecommit(repository=template_repository)

cwd = os.getcwd()+f"\\repo\\{template_repository}\\cicdpipeline"
print(cwd)
var_file = "./env_tfvar/dev.tfvars"
terraforming(cwd=cwd, var_file=var_file, backend_config=backend_config, backend_key= user_input.backend_key,
             cicd_parameters=user_input.cicd_parameters, the_pipeline=user_input.the_pipeline)


def templates():
    for it in os.scandir(the_cicd_directory):
        ### checks all templates of pipelines in directory
        if it.is_dir():
            ### taking last split of the directory taking only the pipeline
            ### comparing that pipeline if it is the chosen pipeline
            the_folder = it.path.split('\\')
            if the_folder[-1] == user_input.the_pipeline:
                return it.path
the_template_dir = templates()
print(templates())


with open(the_template_dir + "\\env_tfvar\dev.tfvars", 'r') as file:
    data_dev = file.read()

with open(the_template_dir + "\\env_tfvar\prod.tfvars", 'r') as file:
    data_prod = file.read()

the_vars = []

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


def vars_mapper(group_names, vars_list, data_dev, data_prod):
    for var in vars_list:
        old_value_dev = re.search(f'{var}\s+=\s+([^\n]+)', data_dev).group(1).strip()
        old_value_prod = re.search(f'{var}\s+=\s+([^\n]+)', data_prod).group(1).strip()
        print(f"The original value for [ {var} ] from the group [ {group_names} ] is [ {old_value_dev} ].")
        new_value = input(f"Please input a new value for {var}: ")
        if new_value != "":
            data_dev = data_dev.replace(old_value_dev, new_value)
            data_prod = data_prod.replace(old_value_prod, new_value)
    return data_dev, data_prod


groups_in_pipelines = range(len(pipeline_var[user_input.the_pipeline]))
for num_group in groups_in_pipelines:
    ###groups variables into each category
    groups = pipeline_var[user_input.the_pipeline][num_group]
    # print("This is the group: ", groups)

    vars_selector(groups)  ###returns a list of variables each time
    vars_group_name(groups)
    # print("this is the list of vars: ",vars_selector(groups))

    # Replace the target string
    data_dev, data_prod = vars_mapper(vars_group_name(groups), vars_selector(groups), data_dev, data_prod)


print(data_dev)

print("\n \n \n", data_prod)

# # Write the file out again

with open(the_template_dir + "\\env_tfvar\dev.tfvars", 'w') as file:
    file.write(data_dev)

with open(the_template_dir + "\\env_tfvar\prod.tfvars", 'w') as file:
    file.write(data_prod)

created_repository = project + "-" + user_input.bt_codecommit_name
the_pipeline_dir = clone_codecommit(repository=created_repository)

###copies edited template and pastes it to the git repository
copy_tree(the_template_dir, the_pipeline_dir)


###push the git folder back to the repository
while True:
    print(f"Please make sure that all files found in {the_pipeline_dir} have the correct configurations and files.")
    user_check = input("Have you checked all the contents of the directory? Proceed? (Y/N): ").lower()
    if user_check == "y":
        push_codecommit(pipeline_directory=the_pipeline_dir)
        break
    elif user_check == "n":
        print("please check first, if you wish to abort, type anything OTHER than Y or N.")
    else:
        print("Exiting...")

