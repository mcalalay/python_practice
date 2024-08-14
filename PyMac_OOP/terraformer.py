from python_terraform import *


def terraforming(cwd, var_file, backend_key, backend_config, cicd_parameters, the_pipeline):
    tf = Terraform(working_dir=cwd, var_file=var_file)
    tf.init(reconfigure=True, backend_config=backend_config, capture_output=True)
    print(tf.plan(no_color=IsFlagged, variables=cicd_parameters, refresh=False, capture_output=True))


    terraform_apply = input("Do you wish to continue to terraform apply? (Y or N): ").lower()
    if terraform_apply == "y":
        tf.apply(no_color=IsFlagged, variables=cicd_parameters, refresh=False, capture_output=True,
                 skip_plan=True)
        print(f'''You have successfully terraformed with the following parameters: \n
    CICD Parameters: \n{cicd_parameters}\n
    Backend Key: {backend_key}\n
    Will be proceeding to push your chosen pipeline template...\n
    Chosen pipeline:{the_pipeline}\n''')
    else:
        print("Aborting Terraforming...")

