from tkinter import *
from tkinter import messagebox
import os

FONT_LABEL = ("Segoe UI", 10, "normal")

class UserInput:

    def __init__(self):
        self.project = None
        self.the_pipeline = None
        self.backend_key = None
        self.bt_codebuild_name = None
        self.bt_codecommit_name = None
        self.bt_codepipeline_name = None
        self.module_name = None
        self.cicd_parameters = None
        self.selves = [self.project, self.the_pipeline, self.backend_key, self.bt_codebuild_name,
                       self.bt_codecommit_name, self.bt_codepipeline_name, self.module_name]



    def initial_input(self):
        window = Tk()
        window.title("Python CICD Creator")
        window.config(pady=50, padx=50)

        # TODO: Labels
        Label(text="Project Name: (sample: oieparterpilot, opsnav-client110, opsnav-client135)",
              font=FONT_LABEL).grid(row=1, column=0)
        Label(text="Choose your pipeline (datapipeline/lambdapipeline/containerpipeline"
                   "/workflowpipeline/monitoringpipeline): ", font=FONT_LABEL).grid(row=2, column=0)
        Label(text="Please enter a backend key for your terraform state:",
              font=FONT_LABEL).grid(row=3, column=0)
        Label(text="AWS Codebuild Name: Sample Format {projectname}-{module}-{pipelinename} Enter a value:",
              font=FONT_LABEL).grid(row=4, column=0)
        Label(text="AWS CodeCommit Name: Sample Format {projectname}-{module}-{pipelinename} Enter a value:",
              font=FONT_LABEL).grid(row=5, column=0)
        Label(text="AWS CodePipeline Name: Sample Format {projectname}-{module}-{pipelinename} Enter a value:",
              font=FONT_LABEL).grid(row=6, column=0)
        Label(text="Unique Name for Module (e.g reviwersegmentation-aht, etc) Enter a value:",
              font=FONT_LABEL).grid(row=7, column=0)

        # TODO: Entries
        project = Entry(width=48)
        project.focus()
        chosen_pipeline = Entry(width=48)
        backend_key = Entry(width=48)
        bt_codebuild_name = Entry(width=48)
        bt_codecommit_name = Entry(width=48)
        bt_codepipeline_name = Entry(width=48)
        module_name = Entry(width=48)

        project.grid(row=1, column=1)
        chosen_pipeline.grid(row=2, column=1)
        backend_key.grid(row=3, column=1)
        bt_codebuild_name.grid(row=4, column=1)
        bt_codecommit_name.grid(row=5, column=1)
        bt_codepipeline_name.grid(row=6, column=1)
        module_name.grid(row=7, column=1)

        def get_values():
            self.project = project.get()
            self.the_pipeline = chosen_pipeline.get()
            self.backend_key = backend_key.get()
            self.bt_codebuild_name = bt_codebuild_name.get()
            self.bt_codecommit_name = bt_codecommit_name.get()
            self.bt_codepipeline_name = bt_codepipeline_name.get()
            self.module_name = module_name.get()
            self.selves = [self.project, self.the_pipeline, self.backend_key, self.bt_codebuild_name,
                           self.bt_codecommit_name, self.bt_codepipeline_name, self.module_name]


        # TODO: Proceed Button and Function
        def exit_window():
            get_values()
            if None in self.selves or 0 in self.selves:
                messagebox.showwarning(message="You left some details blank, kindly check your entry.")

            else:
                self.cicd_parameters = {"bt_codebuild_name": self.bt_codebuild_name,
                                        "bt_codecommit_name": self.bt_codecommit_name,
                                        "bt_codepipeline_name": self.bt_codepipeline_name,
                                        "module_name": self.module_name}
                save_param = messagebox.askokcancel(title=self.backend_key,
                                                    message=f"Are you okay with these details? "
                                                            f"{self.cicd_parameters}")
                if save_param:
                    self.save_user_input()
                    window.destroy()

        Button(text="Confirm", width=96, command=exit_window).grid(row=8, column=0, columnspan=2)
        window.mainloop()



    def print_initial_input(self):
        print(f"Initializing terraform directory with backend key as: {self.backend_key}.")
        print(f"Issuing Terraform apply for CICD with {self.the_pipeline} as pipeline")
        print(f"Your AWS Codebuild Name is: {self.bt_codebuild_name}")
        print(f"Your AWS CodeCommit Name is: {self.bt_codecommit_name}")
        print(f"AWS CodePipeline Name is: {self.bt_codepipeline_name}")
        print(f"Module Name is: {self.module_name}")

    def save_user_input(self):
        with open(f"{os.getcwd()}\\saved_logs\\{self.bt_codecommit_name}.txt", 'w') as file:
            file.write(f'''
            Initializing terraform directory with backend key as: {self.backend_key}.\n
            Issuing Terraform apply for CICD with {self.the_pipeline} as pipeline\n
            Your AWS Codebuild Name is: {self.bt_codebuild_name}"\n
            Your AWS CodeCommit Name is: {self.bt_codecommit_name}"\n
            AWS CodePipeline Name is: {self.bt_codepipeline_name}"\n
            Module Name is: {self.module_name}'''
            )