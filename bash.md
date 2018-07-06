### find
- `find . -name fileName` 
- `find /home -user exampleuser -mtime 7 -iname ".db`   ---- Find all .db files (ignoring text case) modified in the last 7 days by a user named exampleuser.
### grep
- `grep -rnw 'PATH' -e 'pattern'`
  - `-r` recursive 
  - `-n` show line number in output
  - `-w` match the whole word
  - `-i` ignore case
  - `-e` pattern you would like to search 
  - `PATH` start from this path

### top 
- `top -p PID`  ---- show statistics and usage information related to PID only. 
### scp 
- `scp [sourceUser@SourceAddreess]:SourcePath [destUser@destAddress]:destPath` 
- `scp user@xyz.com:/scratch/dump.txt .` --- copy file dump.txt from xyz.com server to current working directory. 
### screen 
This command helps to open a new shell that can be active and running even after user logs out. 
- `screen` -- open a new shell
- `screen -r [PID]` --- resume a currently running shell, if more than one screen shell is running select specific PID. 
- `screen -d` --- detach the current working screen and back to parent shell prompt. 
### output redirection
- `command > file` --- if file does not exists, create and redirect output. If file exists, raise an exception. 
- `command >> file` --- if file exists append, o.w. create a new file. 
- `command >! file` --- Delete the content of the file and redirect the output. 

