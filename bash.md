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
### SCP 
- `scp [sourceUser@SourceAddreess]:SourcePath [destUser@destAddress]:destPath` 
- `scp alazemif@xyz.com:/scratch/dump.txt .` --- copy file dump.txt from xyz.com server to current working directory. 

