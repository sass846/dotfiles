# DOTFILES

The dotfiles of my system are stored in this repo

## Requirements

### stow

make sure you have stow installed on your system

```
$ pacman -S stow
```
for apt users (Debian,Ubuntu etc.)
```
$ sudo apt install stow
```
or 
```
# for nala users
$ sudo nala install stow
```

### git
and git if it is not already installed 

```
$ pacman -S git
```

## Getting the files on ur system

clone the dotfiles repo in your $HOME directory

```
$ git clone git@github.com:sass846/dotfiles.git
$ cd dotfiles
```

Then create symlinks using stow
```
$ stow .
```

