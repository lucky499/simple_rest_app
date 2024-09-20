import subprocess

def run_ansible_command():
    command = [
        "ansible-playbook",
        "-i", "my_invent",
        "simple_tasks.yml"
    ]
    try:
        results = subprocess.run(command, capture_output=True, text=True, check=True)
        print("Full output from ansible")
        print(results.stdout)
    except Exception as error:
        print(f"exception occured while running ansible command: {error}")
if __name__ == "__main__":
    run_ansible_command()