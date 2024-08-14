import os


class UserInput:

    def __init__(self):
        self.the_pipeline = None
        self.backend_key = None
        self.bt_codebuild_name = None
        self.bt_codecommit_name = None
        self.bt_codepipeline_name = None
        self.module_name = None
        self.cicd_parameters = None


    def initial_input(self):
        self.the_pipeline = input("Please choose a pipeline: ").lower()
        self.backend_key = input("Please enter a backend key for your terraform state: ").lower()
        self.bt_codebuild_name = input(
            "AWS Codebuild Name: Sample Format {projectname}-{module}-{pipelinename} \nEnter a value: ").lower()
        self.bt_codecommit_name = input(
            "AWS CodeCommit Name: Sample Format {projectname}-{module}-{pipelinename} \nEnter a value: ").lower()
        self.bt_codepipeline_name = input(
            "AWS CodePipeline Name: Sample Format {projectname}-{module}-{pipelinename} \nEnter a value: ").lower()
        self.module_name = input("Unique Name for Module (e.g reviwersegmentation-aht, etc) \nEnter a value: ").lower()
        self.cicd_parameters = {"bt_codebuild_name": self.bt_codebuild_name,
                                "bt_codecommit_name": self.bt_codecommit_name,
                                "bt_codepipeline_name": self.bt_codepipeline_name,
                                "module_name": self.module_name}


    def print_initial_input(self):
        print(f"Initializing terraform directory with backend key as: {self.backend_key}.")
        print(f"Issuing Terraform apply for CICD with {self.the_pipeline} as pipeline")
        print(f"Your AWS Codebuild Name is: {self.bt_codebuild_name}")
        print(f"Your AWS CodeCommit Name is: {self.bt_codecommit_name}")
        print(f"AWS CodePipeline Name is: {self.bt_codepipeline_name}")
        print(f"Module Name is: {self.module_name}")

    def save_user_input(self):
        with open(f"{os.getcwd()}\\{self.bt_codecommit_name}.txt", 'w') as file:
            file.write(f'''
            Initializing terraform directory with backend key as: {self.backend_key}.\n
            Issuing Terraform apply for CICD with {self.the_pipeline} as pipeline\n
            Your AWS Codebuild Name is: {self.bt_codebuild_name}"\n
            Your AWS CodeCommit Name is: {self.bt_codecommit_name}"\n
            AWS CodePipeline Name is: {self.bt_codepipeline_name}"\n
            Module Name is: {self.module_name}'''
            )