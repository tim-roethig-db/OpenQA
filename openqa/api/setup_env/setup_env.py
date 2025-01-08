import subprocess


def setup_env():
    # Call the shell script
    result = subprocess.run(
        ["bash", "setup_env.sh"], capture_output=True, text=True, check=True
    )

    # Print the output and error (if any)
    print(result.stdout)
    if result.stderr:
        print("Error:", result.stderr)


if __name__ == "__main__":
    setup_env()
