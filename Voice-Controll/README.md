### Voice-Activated System with User Authentication and Role-Based Commands

This project is a **Python-based voice-activated system** that integrates speech recognition, user authentication, and role-based access control to interact with the operating system through voice commands. The system offers a hands-free way to execute commands, making it ideal for environments requiring accessibility and automation.

---

### Features:

1. **Speech Recognition**:
   - Uses the `speech_recognition` library to convert spoken commands into text.
   - Employs the Google Web Speech API for accurate and efficient voice recognition.

2. **User Authentication**:
   - Validates users with predefined credentials stored in a secure dictionary.
   - Grants access based on roles: 
     - **Admin**: Full system control.
     - **User**: Restricted command access.

3. **Role-Based Command Execution**:
   - Admin Commands:
     - "Restart": Restarts the program automatically.
     - "Shut Down": Placeholder for system shutdown.
   - User Commands:
     - "Status": Provides system operational status.
   - Gracefully handles unrecognized commands.

4. **Program Restart**:
   - Implements an automated restart mechanism using `os.execv`.
   - Ensures smooth transition with the same configuration and command-line arguments.

5. **Error Handling**:
   - Detects unintelligible or unrecognized audio and notifies the user.
   - Handles service connectivity issues during voice recognition.

---

### Technology Stack:
- **Python**: Core programming language.
- **Libraries**:
  - `speech_recognition`: For speech-to-text conversion.
  - `os` and `sys`: For operating system interactions.
  
---

### Use Cases:
- Hands-free system control for users with limited mobility.
- Simplified role-based access to system commands in shared environments.
- Voice-command automation for educational demonstrations or prototypes.

