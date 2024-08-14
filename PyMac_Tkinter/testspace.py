# import pandas as pd
#
#
# df = pd.read_csv("configurations.csv").ffill()
# chosen_pipe = "datapipeline"
#
# # print(df[df.pipeline == chosen_pipe])
# # print(df[["group", "variables"]][df.pipeline == chosen_pipe])
# # print(type(df[["group", "variables"]][df.pipeline == chosen_pipe]))
#
#
# df = df[["group", "variables"]][df.pipeline == chosen_pipe]
# for i, row in df.iterrows():
#     print(f"Index: {i}")
#     print(f"{row}\n")
#     print(row.tolist())

# print(df)
#
# for col_name, data in df.items():
# 	print("col_name:",col_name, "\ndata:",data)

# from tkinter import *
# from tkinter import messagebox
#
#
# def terraforming():
#     print("Terraforming...")
#     window = Tk()
#     window.title("Edit Variables")
#     window.config(pady=50, padx=50)
#     text = Text(height=40, width=100)
#
#     text.insert(END, "Terraforming... Please wait for logs...\n"*100)
#     text.pack()
#
#     print("TF Planning...")
#     # text.delete("1.0", END)
#     text.insert(END, "tdout")
#
#     def clicked():
#         save_param = messagebox.askokcancel(title="Terraform Apply", message=f"Proceed terraforming?")
#         if save_param:
#             window.destroy()
#
#
#             print(f'''You have successfully terraformed with the following parameters: \n
#                 CICD Parameters: \n\n
#                 Backend Key: \n
#                 Will be proceeding to push your chosen pipeline template...\n
#                 Chosen pipeline:\n''')
#
#
#
#     tf_app = Button(text="Confirm Terraform Apply", width=100, command=clicked)
#     tf_app.pack()
#
#     window.mainloop()
#
#
# terraforming()

# fruits = ["banana", "apple", "starfruit"]
#
# count = 0
#
# paired_food = {}
#
# for fruit in fruits:
#     paired_food[count] = fruit
#     count += 1
#
# print(paired_food)
#
# print(paired_food[2])
import pandas as pd
import re
from tkinter import *
FONT_LABEL = ("Segoe UI", 10, "normal")
the_template_dir = r"C:\Users\matthew.a.calalay\PycharmProjects\PyMac_Tkinter\templates\opsnav-client110-terraform-template\datapipeline"

with open(the_template_dir + "\\env_tfvar\dev.tfvars", 'r') as file:
    data_dev = file.read()

with open(the_template_dir + "\\env_tfvar\prod.tfvars", 'r') as file:
    data_prod = file.read()


def vars_mapper():
    window = Tk()
    window.title("Edit Variables")
    window.maxsize(width=2400, height=800)
    window.config(pady=50, padx=50)

    df = pd.read_csv("configurations.csv").ffill()
    chosen_pipe = "datapipeline"
    df = df[["group", "variables"]][df.pipeline == chosen_pipe]
    # data = {row.group: row.variables for (index, row) in df.iterrows()}
    text_inputs = []
    stored_values = {}

    def button_clicked(text_box, old_value):
        new_value = text_box.get()
        print("The new value is ", new_value)
        stored_values[old_value.get()] = new_value
        print(stored_values)


    row = 0
    for i, data in df.iterrows():
        variables = data.tolist()
        print(data.tolist())

        old_value_dev = re.search(f'{variables[1]}\s+=\s+([^\n]+)', data_dev).group(1).strip()
        old_value_prod = re.search(f'{variables[1]}\s+=\s+([^\n]+)', data_prod).group(1).strip()
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



vars_mapper()

print(data_dev)

print("\n \n \n", data_prod)