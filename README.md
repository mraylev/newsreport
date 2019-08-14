# News Report

This project is intended to fulfill the requirements for the first project of the Udacity [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004?utm_source=gsem_brand&utm_medium=ads_r&utm_campaign=2045338233_c&utm_term=71049806063_nam&utm_keyword=udacity%20full%20stack_e&gclid=Cj0KCQjws7TqBRDgARIsAAHLHP7lFDbW_LZhSzhe6V0O8D7vU1bm-Yrohf0v2JtRFTk1QSvth_JsQIgaAhUGEALw_wcB) Program. It queries a database using postgreSQL and its related python libraries and prints out the result. The program is run through the terminal and its output is either viewed there or in a file it creates.

## Code Information

### SQL and SQL Views
The project specifications detail requirements for solutions dependent on SQL views and states that instructions for projects using views should have instructions included in the README file. **This project does not use views**; all of the results are achieved in one SQL statement thus no setup is required for the project.

You will, however, need to load the data from the **newsdata.sql** file before running the program. To do this, `cd` into the `solution` directory and use the command `psql -d news -f newsdata.sql`. The solution directory will be located in whatever directory it was downloaded to by default as per your machine's settings.

### pycodestyle

This project adheres to python [pep8](https://www.python.org/dev/peps/pep-0008/) standards. These standards require lines of code to be less than 80 characters of code, which would not be possible without artificial break lines separating the SQL queries into lines at false break points.

You can test the code's adherence to these standards using the pycodestyle utility from the terminal. To install pycodestyle, use the command `pip3 install pycodestyle` (as this project uses python 3). You may need to use `sudo` before that command or root privileges to install pycodestyle, especially if you are running the program on the preconfigured virtual machine.

If you would like to try using a query from this project in the psql program, the break lines (/) must be removed for the queries to work.

## Installing The Virtual Machine

The easiest way to view this program is to install a preconfigured virtual machine using VirtualBox and Vagrant. Students and Course reviewers for the Udacity Full Stack Web Developer nanodegree should already have a virtual machine ("VM") set up and working.

If you have already configured a VM but have not yet [setup] the news database, you will need to complete steps 7 through 9 only. If you have [setup] the news database, you will only need to complete steps 7 and 9. Step 10 is optional.

### Notes on the Terminal

All of the commands in this 'installation' section are to be completed through the terminal.

- In **Mac OS** terminal can be opened by (a) opening the Applications folder, then opening Utilities and double-clicking Terminal _or_ (b) using [command-spacebar] to launch spotlight and typing 'Terminal' and then double-clicking the search result
- In **Ubuntu Linux**, terminal can be opened by (a) opening the 'Show Applications' icon on the taskbar and then either searching for and then selecting terminal or scrolling to select terminal _or_ (b) using the shortcut [Ctrl + Alt + T]. Other versions of linux may differ; I recommend using your favorite search engine to find a method to open terminal if the above methods don't work on your version and you are unable to open a terminal window.
- In **Microsoft Windows**, you will have to install git bash to run these commands. Git bash is installed automatically when you install git from [git-scm.com](https://git-scm.com/downloads).

Udacity offers free courses about the [Unix Shell](https://www.udacity.com/course/shell-workshop--ud206) and [Git](https://www.udacity.com/course/version-control-with-git--ud123) which can make a great introduction or refresher, depending on your current level.

### Step 1: Install VirtualBox

Install VirtualBox, the software that runs the virtual machine, for your operating system [here](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1). You don't need the extension pack or the SDK and while VirtualBox allows Vagrant to work, you won't need to launch it or interact with its GUI after installing it. You only need to use the terminal to interact with Vagrant.

You can check to see if VirtualBox is installed by using the command `vboxmanage --version`.

**Note for Ubuntu users**: If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software center instead. Due to a reported bug, installing VirtualBox from the site may install other software you need.

### 2. Install Vagrant

Install Vagrant, the software that configures the VM and lets you share files between your <u>host</u> computer (the operating system of the computer on which VirtualBox and Vagrant are installed) and the <u>VM</u>'s filesystem, [here](https://www.vagrantup.com/downloads.html).

You can check to see if Vagrant is successfully installed by using the command `vagrant --version`

**Note for Windows Users** The installer may ask you to grant network permissions to Vagrant or make a firewall exception. Make sure to allow this.

### 3. Download the VM Configuration

You can download the [VM configuration](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip) directly or use Github to fork and clone [the repository](https://github.com/udacity/fullstack-nanodegree-vm). If you downloaded the VM configuration directly, you may want to change the filepath as detailed in 'Step 4: Choosing a Filepath', but this is not required.

**Note For Windows Users** If you are using Windows OS you will find a Time Out error, to fix it use the new [Vagrant File Configuration](https://s3.amazonaws.com/video.udacity-data.com/topher/2019/March/5c7ebe7a_vagrant-configuration-windows/vagrant-configuration-windows.zip) to replace your current Vagrant file.

### 4. Choosing a Filepath (optional)

If you downloaded the VM Configuration the .zip folder 'FSND-virtual-machine' is most likely in your downloads folder. Once unzipped, the filepath will be [filepath on your host machine]/fsnd-virtual-machine/FSND-Virtual-Machine/vagrant.

You may want to move the _2nd level_ FSND-Virtual-Machine folder to a more accessible directory and rename it to make it simpler to use the `cd` command. The _1st level_ fsnd-virtual-machine directory is unnecessary after the initial directory extraction and the _2nd level_ FSND-Virtual-Machine folder has a name so long it can prove time consuming for multiple uses of the machine.

I would recommend using the following terminal commands to streamline things:  

  1. `cd` into the folder in which the _1st level_ fsnd-virtual-machine directory is located
  2. Use `mv fsnd-virtual-machine/FSND-Virtual-Machine .` to move the _2nd level_ FSND-Virtual-Machine folder to the current directory
  3. Use `mv FSND-Virtual-Machine [_'your chosen name'_]` to rename the _2nd level_ FSND-Virtual-Machine folder something that's easier to remember.
  4. Use `rm -r fsnd-virtual-machine` to delete the (now) unnecessary folder.

### 5. `vagrant up`

Now, it's time to install the operating system for the virtual machine (VM). Use `cd` to move to the 'vagrant' folder. Use the command `vagrant up` to download the Linux operating system and install it. This might take quite a while depending on the speed of your internet; during this time you will see many lines of output and will not have access to your shell prompt (the area where you type in the terminal).

**note for Ubuntu users:** You may need to load Ubuntu with Secure Boot disabled in order to run vagrant. If you get an error upon running `vagrant up` that references DKMS modules or signing specific keys for modules, try one of the methods from this [Ubuntu wiki](https://wiki.ubuntu.com/UEFI/SecureBoot/DKMS) article.

#### A common `vagrant up` issue
If you have another virtual machine running on the same computer (like, for example, the vm configuration required for Lesson 2 of the Full Stack Nanodegree(FSND)), you may get an error on running `vagrant up` that begins with "Vagrant cannot forward the specified ports on this VM, since they would collide with some other application that is already listening on these ports. The forwarded port...".

To resolve this, you can try to `cd` into the folder in which the other vagrant-run vm has been installed and use `vagrant halt`. The message '**===> default: Attempting graceful shutdown of VM...**' followed by regaining control of the shell prompt usually indicates a successful result. You should then be able to `cd` into the vagrant folder for this program and run the `vagrant up` successfully, however, sometimes this does not work and you will have to edit the Vagrantfile.

Another way of resolving this would be to edit the Vagrantfile in your favorite text editing program. In this configuration, the relevant lines are 8, 9, and 10: <br>
08 `config.vm.network "forwarded_port", guest: 8000, host: 8000, host_ip: "127.0.0.1"` <br>
09 `config.vm.network "forwarded_port", guest: 8080, host: 8080, host_ip: "127.0.0.1"` <br>
10 `config.vm.network "forwarded_port", guest: 5000, host: 5000, host_ip: "127.0.0.1"`<br>
The only parts that need to be changed in this file for a successful `vagrant up` are the 4 digit numbers that follow `host:`. You can pick any port for your host machine to use except ones that your machine are already using. Using the 1234, 1235, and 1236 or a series of trial and error should work. You should use three different port numbers.

### 6. `vagrant ssh`

Now, it's time to log into the vm in the terminal. From the vagrant folder, use the command `vagrant ssh`. You will need to use this every time you access the vm. When you have successfully accessed the vm, a loading message will appear containing the version and some information about the machine and the shell prompt should change.

To exit the vm, use the command `exit`.

The first time you use ssh, the welcome message will include a line ' *** system restart required *** '. This can be achieved by running the commands (1)`exit`,  (2)`vagrant reload`, and (3)`vagrant ssh`. `vagrant reload` is the equivalent of running `vagrant halt` and then `vagrant up`. You do not need to restart the host machine.

If you are not currently 'ssh'd' into the vm, running the newsreport.py program or the news database in psql will not work because your local machine (even in the vagrant directory) is not configured to interact with the project. If you are getting error messages when running the command `python newsreport.py` or  `psql news`, the first thing to check is the shell prompt to make sure you are currently 'inside' the virtual machine.

### 7. Finding the course files

Vagrant supports [provisioning](https://www.vagrantup.com/docs/provisioning/file.html), which allows you to modify files in a vagrant folder using your host machine. These files will be updated immediately and can be interacted with on the vm as you make changes. If you are using the preconfigured vm from this setup, you should not have to do anything for provisioning to work automatically; the link is provided only for informational purposes.

#### Removing Unneccessary Files (Optional)

The FSND vm comes with three project directories relevant to the nanodegree that are not required for this project. You can delete them from the tournament with the following commands:

1. `rm -r catalog`
2. `rm -r forum`
3. `rm -r tournament`

This is not required to run newsreport.py but will free up space on your computer.

#### Adding `newsdata.sql`

The newsdata.sql file is required to populate the news database newsreport.py queries. You can download it [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). It is too large to be stored on git. The download is a .zip file that will likely be saved to your Downloads folder. Using the file manager on your host machine, extract the file and move its contents to the /vagrant folder in your vm.

#### Adding Project Files

The project file can be added by downloading the [git repository](https://github.com/mraylev/newsreport) by clicking the green 'Clone or Download' link near the upper right side of the page and selecting 'Download'. The .zip file will likely be saved to your Downloads folder. Using the file manager on your host machine, extract the directory and move the `newsreport.py` file to the /vagrant folder.

The other files included in the download are not necessary for the program to run.

### 8. [init] database = news

Once newsdata.sql has been moved to the vagrant folder, use your terminal to run the command `psql -d news -f newsdata.sql`. This command works by connecting to the PostgreSQL command line program (`psql`), connecting to the database named 'news' which has been set up for you (`-d news`) , and running the SQL statements in the file newsdata.sql (`-f newsdata.sql`).

### 9. Running the Program

At this point, everything you need to run the news report program has been setup and you can run the program and see its output with the command `python newsreport.py`. The output will be displayed in the terminal. To save the output to a file, see the 'Printing' section of this document.

### 10. Removing the VM

After its setup and the program has been run, you can remove the vm with the command `vagrant [destroy](https://www.vagrantup.com/docs/cli/destroy.html)`. This will destroy all resources created during the machine creation process, leaving a "clean  slate". The filepath and files within it will remain, but you can delete this by using `cd ..` until you reach the directory containing the topmost vagrant-related directory and use `rm -r [_directory name_]` to delete all related folders.  

## Printing

This solution has the capability to create a file containing formatted results but by default this feature is disabled. To change this, change the value of `print_bool` (located on line 6 of the newsreport.py file) to True using your favorite text editor.

If the `print_bool` variable's value is stored as true, a file will be created in the same directory as the newsreport file called 'news report' followed by the date and time the program was run. The output of the program in the terminal specifies the full name of the file created in its last two lines of output.

### Contents

The output of the program answers the following questions based on the contents of the associated database, included in the solution directory:

1. What are the most popular three articles of all time?
2. Who are the most popular authors of all time?
3. On which days did more than 1% of requests lead to errors?

### Example.txt

The zipped directory also contains a file called 'example.txt' which is a previously created file of this type showing an example of output. This satisfies the requirements for the project's submission. Additional files  created using the same version of the news database should match this file exactly.
