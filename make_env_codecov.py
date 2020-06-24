import os


variables = os.environ.get("ci_env", None)

if variables:
    print("Creating file...")
    variables_to_write = variables.strip("-e ").split(" -e ")
    with open(".env.codecov", 'w') as f:
        for variable in variables_to_write:
            value = os.environ.get(variable, "")
            if value != "":
                f.write("{}={}\n".format(variable, value))
        print("File succesfully created")
