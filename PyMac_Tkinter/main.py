from distutils.dir_util import copy_tree
from user_input import UserInput
from terraformer import terraforming
from codecommit import clone_codecommit, push_codecommit
from tkinter import messagebox
from tkinter import *
import pandas as pd
import os
import re

FONT_LABEL = ("Segoe UI", 10, "normal")


user_input = UserInput()
user_input.initial_input()
user_input.print_initial_input()


backend_config={'key': user_input.backend_key}



print(backend_config)

project = user_input.project
print(project)
template_repository = project + "-terraform-template"

the_cicd_directory = clone_codecommit(repository=template_repository, cicd_or_module="cicd")

cwd = os.getcwd()+f"\\templates\\{template_repository}\\cicdpipeline"
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

def default_or_new_template():
    window = Tk()
    edit_manually = messagebox.askyesno(title="Do you wish to edit manually?",
                                              message=f"Choose yes if you wish to edit the template via your chosen "
                                                      f"editor. Choose cancel if you want to proceed editing within the"
                                                      f"UI.")
    if not edit_manually:
        vars_mapper()
        window.destroy()
    else:
        while True:
            done_editing = messagebox.askokcancel(title="Check all configurations!",
                                                  message=f"Have you finished editing your template?")
            if done_editing:
                window.destroy()
                break




def vars_mapper():
    window = Tk()
    window.title("Edit Variables")
    window.maxsize(width=2400, height=800)
    window.config(pady=50, padx=50)

    df = pd.read_csv("configurations.csv").ffill()
    chosen_pipe = user_input.the_pipeline
    df = df[["group", "variables"]][df.pipeline == chosen_pipe]
    # data = {row.group: row.variables for (index, row) in df.iterrows()}
    text_inputs = []
    stored_values = {}

    def button_clicked(text_box, old_value):
        new_value = text_box.get()
        print(f"The new value is '{new_value}'")
        stored_values[old_value.get()] = new_value
        print(stored_values)

    try:
        row = 0
        for i, data in df.iterrows():
            variables = data.tolist()
            print(data.tolist())
            old_value_dev = re.search(f'{variables[1]}\s+=\s+([^\n]+)', data_dev).group(1).strip()
            # old_value_prod = re.search(f'{variables[1]}\s+=\s+([^\n]+)', data_prod).group(1).strip()
            print(old_value_dev)
            Label(text=f"The original value for the VARIABLE: [ {variables[1]} ] from the group "
                           f"[ {variables[0]} ]").grid(row=row, column=0)
            text = Entry(width=60)
            text.grid(row=row, column=1)
            text.insert(END, old_value_dev)

            text_input = Entry(width=60)
            text_input.grid(row=row, column=2)
            text_inputs.append(text_input)


            button = Button(text="Replace Value", font=FONT_LABEL, command=
                    lambda old_value=text, text_box=text_input: button_clicked(text_box, old_value))
            button.grid(row=row, column=3)

            row += 1
        print(text_inputs)

        def close_window():
            for old_value, new_value in stored_values.items():
                if new_value != "":
                    global data_dev
                    global data_prod
                    data_dev = data_dev.replace(old_value, new_value)
                    data_prod = data_prod.replace(old_value, new_value)
            window.destroy()
        Button(text="Confirm Changes", font=FONT_LABEL, command=close_window, width=120)\
            .grid(row=row, column=0, columnspan=4)
        window.mainloop()

    except AttributeError:
        messagebox.showerror(title="Default Variables not found. Edit Manually",
                             message="Please edit through Visual Studio or your chosen IDE.")
        window.destroy()
        default_or_new_template()


default_or_new_template()

print(data_dev)

print("\n \n \n", data_prod)

# Write the file out again

with open(the_template_dir + "\\env_tfvar\dev.tfvars", 'w') as file:
    file.write(data_dev)

with open(the_template_dir + "\\env_tfvar\prod.tfvars", 'w') as file:
    file.write(data_prod)

created_repository = project + "-" + user_input.bt_codecommit_name
the_pipeline_dir = clone_codecommit(repository=created_repository, cicd_or_module="module")

###copies edited template and pastes it to the git repository
copy_tree(the_template_dir, the_pipeline_dir)


###push the git folder back to the repository
while True:
    window = Tk()
    proceed_git_push = messagebox.askokcancel(title="Check all configurations!",
                                              message=f"Please make sure that all files found in {the_pipeline_dir} "
                                                      f"have the correct configurations and files.\n\nHave you "
                                                      f"checked all the contents of the directory? Proceed?")
    if proceed_git_push:
        window.destroy()
        push_codecommit(pipeline_directory=the_pipeline_dir)
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


