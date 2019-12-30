# bb
A tool I use to take small notes for all sorts of progress and search into those notes
You take small notes like:
```
$ bb -w Just fed my cat this afternoon
$ bb -w Installed a driver for my webcam
...
```
Then you can search in your notes (In the same way `grep` does) like:
```
$ bb cat
Searching in /home/username/Documents/bb.txt for cat
--------------------
2019-12-30 17:33:09 /home/username> Just fed my cat this afternoon

2019-12-31 09:41:12 /home/username> My cat wants to go outside

2020-01-12 10:34:03 /home/username> My cat just tried to eat my webcam

2020-01-13 14:58:02 /home/username> My webcam is working fine, just took a picture with my cat

2020-01-13 21:56:43 /home/username> My cat eats a lot

--------------------
```

# How to use it
Bn order to call this script with a simple "bb <arguments>", I add in `~/.bashrc` or `~/.bash_aliases` the following:
```
alias bb="python ~/Documents/bb.py"
```
 For the script to work the first time you need to create a file in your "Documents" called `bb.txt`
```
$ >~/Documents/bb.txt
```
 # Usage
```
bb.py <words to search>
bb.py -w <words to write>
bb.py -a # Prints contents of the entire file
bb.py -e # Opens the nano editor to edit the file
```
If you don't have the nano editor, just change the source code of bb.py and replace "nano" with your favorite editor.

This is just a bodge I made for my own desires, and it's not a heavy script. To make it fit *your* own desires, feel absolutely free to modify it on your own and/or suggest me some ideas.
