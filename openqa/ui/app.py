import time
import streamlit as st

def check_repo_exists(repo_url):
    # Example check: Simulate checking if the repo exists
    time.sleep(2)
    return "pass"  # Replace with actual logic

def check_branch_protection(repo_url):
    # Example check: Simulate checking branch protection
    time.sleep(2)
    return "warn"  # Replace with actual logic

def check_readme(repo_url):
    # Example check: Simulate checking for a README file
    time.sleep(2)
    return "fail"  # Replace with actual logic

def perform_check_with_spinner(check_function, repo_url, check_name):
    with st.spinner(f"Checking {check_name}..."):
        result = check_function(repo_url)
    if result == "pass":
        st.success(f"{check_name}: **Pass**")
    elif result == "warn":
        st.warning(f"{check_name}: **Warning**")
    elif result == "fail":
        st.error(f"{check_name}: **Fail**")

def main():
    st.title("GitHub Repo Checker")

    # Input for GitHub repository URL
    repo_url = st.text_input("Enter GitHub Repository URL:")

    if st.button("Check"):
        if repo_url:
            st.write("Performing checks on:", repo_url)

            # Perform checks with progress indication
            perform_check_with_spinner(check_repo_exists, repo_url, "Repository Exists")
            perform_check_with_spinner(check_branch_protection, repo_url, "Branch Protection")
            perform_check_with_spinner(check_readme, repo_url, "README File")

        else:
            st.error("Please enter a valid GitHub repository URL.")

if __name__ == "__main__":
    main()