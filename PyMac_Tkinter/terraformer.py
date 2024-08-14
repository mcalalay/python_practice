from python_terraform import *
from tkinter import *
from tkinter import messagebox


def terraforming(cwd, var_file, backend_key, backend_config, cicd_parameters, the_pipeline):
    window = Tk()
    window.title("Edit Variables")
    window.config(pady=50, padx=50)
    text = Text(height=40, width=100)
    text.pack()
    text.insert(END, "Terraforming... Please wait for logs...\n" * 20)
    print("Terraforming...")
    tf = Terraform(working_dir=cwd, var_file=var_file)
    tf.init(reconfigure=True, backend_config=backend_config, capture_output=True)
    print("TF Planning...")


    return_code, stdout, stderr = \
        tf.plan(no_color=IsFlagged, variables=cicd_parameters, refresh=False, capture_output=True)

    text.delete("1.0", END)
    text.insert(END, stdout)


    def clicked():
        save_param = messagebox.askokcancel(title="Terraform Apply", message=f"Proceed terraforming?")
        if save_param:
            text.destroy()
            window.destroy()

            print("Please wait, applying Terraform...")
            with open(f"saved_logs\\{backend_key}_tf-plan-logs.txt", mode="w", encoding="utf-8") as tf_logs:
                tf_logs.write(stdout)
            tf.apply(no_color=IsFlagged, variables=cicd_parameters, refresh=False, capture_output=True,
                     skip_plan=True)
            print(f'''You have successfully terraformed with the following parameters: \n
                CICD Parameters: \n{cicd_parameters}\n
                Backend Key: {backend_key}\n
                Will be proceeding to push your chosen pipeline template...\n
                Chosen pipeline:{the_pipeline}\n''')



    Button(text="Confirm Terraform Apply", width=100, command=clicked).pack()
    window.mainloop()



