# tasknine
This is the task 9 of running an html code as a python script, using port 8000
#Here is how i done that!

nstall VSCodium on Kali Linux

To install VSCodium on Kali Linux, follow these steps:

Add the VSCodium repository:

      sudo apt update
    sudo apt install software-properties-common
    sudo add-apt-repository ppa:vscodium-team/ppa

 Install VSCodium:
 
     sudo apt update
    sudo apt install codium

2. Open and Edit HTML in VSCodium

    Open VSCodium:

    Launch VSCodium by typing codium in your terminal or finding it in your applications menu.

    Open your HTML file:
        Click on File > Open File....
        Navigate to the location of your HTML file from "taskthree" and open it.

    Edit the HTML:
        Use VSCodium's syntax highlighting and Emmet (a plugin for fast HTML and CSS coding) to improve and create a valid HTML file. For more about Emmet, you can refer to the Emmet documentation.

3. Edit Python Script in VSCodium

    Open your Python script:
        Similarly, open your Python script by going to File > Open File... and selecting the script from "taskthree".

    Add Shebang:

    At the top of your Python script, add the following line:

        #!/usr/bin/env python3

    This shebang line tells the system to use the appropriate Python interpreter to execute the script.

Read About Shebang:

 The shebang (#!) at the beginning of a script specifies the path to the interpreter that should be used to run the script. It allows the script to be executed directly from the command line without explicitly invoking the interpreter. You can learn more about it here.

Make the Script Executable:

  In the terminal, navigate to the directory containing your Python script and run:

     chmod +x your_script.py


   Replace your_script.py with the actual name of your script.

Execute the Script Directly:

 You can now run the script directly by typing:

     ./your_script.py

Ensure that python3 is in your PATH and is executable.

if all this done then open a web browser and go to 

    http://localhost:8000/<filename.html>

This Python script is a simple way to serve static HTML files and can be a useful tool for development and testing.
        
