# pt3

pt3 is a pptp-vpn client that runs in a terminal as a command-line tool. 

### Installation

```shell
pip install pt3
```

### Usage

* Help information

```shell
$ pt3 -h
usage: pt3.py [-h] {status,add,remove,edit} ...

pt3 is a pptp-vpn client that runs in the terminal

positional arguments:
  {status,add,remove,edit}
                        Available commands
    status              show the status of all pptp-configs
    add                 add a pptp-config
    remove              remove a pptp-config
    edit                edit a pptp-config

optional arguments:
  -h, --help            show this help message and exit
```

* Show the vpn status

```shell
$ pt3 status
==ID== =====NAME=====  =====STATUS=====
  0          pptp01         stopped
  1          pptp02         stopped
  2          pptp03         running
```
