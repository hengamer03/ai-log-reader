## Simple AI Log Reader

This is a program that reads logs, gives them to an LLM that then processes the logs to give solutions to errors, etc.

# Installation and Setup

1. **Clone the repository:**
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create a virtual environment:**
    ```sh
    python -m venv env
    ```

3. **Activate the virtual environment:**
    - On Windows:
        ```sh
        .\env\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source env/bin/activate
        ```

4. **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

# Usage

1. **Place your log file:**
    - The Code used a copy of the audit.log file found in /var/log/audit/audit.log in the projects root directory to not need sudo access. Modify accordingly for correct access

2. **Run the main script:**
    ```sh
    python main.py
    ```

# Output example

```sh
$ python main.py

After analyzing the audit logs, here are my findings:

**Denied Actions/Requests:**

* None explicitly mentioned in the logs. However, some actions were not granted due to the lack of necessary permissions (e.g., `pam_unix` was used for authentication instead of `pam_keyinit`, which might indicate that the user didn't have the required privileges).

**Errors Occurred:**

* The BPF (Berkeley Packet Filter) operations in the logs seem unusual, with many programs being loaded and unloaded rapidly. This might be a normal behavior for system initialization or maintenance, but it's worth investigating further to ensure there are no underlying issues.
* There is an inconsistency in the `prog-id` values for BPF operations. Some IDs are reused (e.g., 263 and 264), while others have gaps between them (e.g., 265-266). This might indicate a problem with the system's BPF management.

**Other Relevant Observations:**

* The logs show multiple instances of `pam_unix` being used for authentication, which is unusual. Typically, `pam_unix` would be used only when other authentication mechanisms (e.g., `pam_keyinit`) are not available or configured.
* The user `user` successfully authenticated using `sudo`, but the logs don't show any explicit permission checks or access control decisions being made.

Overall, while there are some unusual patterns in these logs, they might be related to normal system initialization and maintenance activities. However, it's essential to investigate further to ensure that there are no underlying issues with user authentication, permissions, or BPF management.
```

# Notes

- This project uses the  and  libraries to interact with the LLM.
- Ensure you have the necessary permissions and API keys (if required) for the LLM model you are using.

# THIS IS A WIP