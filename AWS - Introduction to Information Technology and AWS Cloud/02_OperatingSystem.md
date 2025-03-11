# Operating Systems & Command Line Interfaces

## What is an Operating System?
The **Operating System (OS)** is software that manages hardware resources (CPU, RAM, storage) and enables program execution. It coordinates concurrent resource access by multiple applications.

### Major Examples:
- Windows
- macOS
- Linux/Ubuntu
- Android/iOS (mobile devices)

---

## Key OS Components

### 1. Kernel
The core component responsible for:
    - Memory management (allocation/deallocation)
    - Process scheduling (execution priorities)
    - Hardware communication via drivers
    - Interrupt handling (hardware signals)

*Learn more: [Linux Kernel Explained](https://www.kernel.org/doc/html/latest/)*

---

### 2. File System
Data organization structure for storage. Hierarchical organization with:
    - Directories (folders): Logical containers
    - Files: Documents, images, programs
    - Operations: Create, read, delete

**Common File Systems**:
    - NTFS (Windows)
    - APFS (macOS)
    - ext4 (Linux)

---

### 3. Processes & Threads
- **Process**: Running program instance
- **Thread**: Process subunit (parallel task execution)
- **Multithreading**: Simultaneous thread execution

Scheduling example:
    Process A (priority 1) → CPU Time: 60%
    Process B (priority 2) → CPU Time: 40%

---

## Command Line Interfaces (CLI)

### Bash (Linux/macOS)
Essential commands:
    ls          # List files in current directory
    cd Documents  # Enter "Documents" folder
    mkdir backup  # Create new folder
    cp file1.txt folder/  # Copy file

Script execution:
    ./script.sh parameter1 parameter2

*Guide: [Bash Manual](https://www.gnu.org/software/bash/manual/)*

---

### PowerShell (Windows)
"Verb-Noun" command structure:
    Get-ChildItem              # List files
    Set-Location "C:\Documents"  # Change directory
    Remove-Item file.txt       # Delete file

Scripting (.ps1):
    Write-Host "Hello, world!"

*Resources: [PowerShell Documentation](https://learn.microsoft.com/en-us/powershell/)*

---

### AWS CLI (Cross-Platform)
Cloud service management via terminal:
    aws s3 ls                   # List S3 buckets
    aws ec2 start-instances --instance-ids i-123456  # Start EC2 instance

Installation:
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
    unzip awscliv2.zip
    sudo ./aws/install

---

## CLI Advantages
    - Task automation
    - Granular system control
    - Lower resource usage vs GUIs
    - Remote access via SSH/terminals

**Best Practices**:
    Use spaces instead of tabs in paths
    Add # comments to scripts for clarity
    Test commands in non-production environments