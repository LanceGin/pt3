#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : since 2019-08-01 16:26
# @Author  : Gin (gin.lance.inside@hotmail.com)
# @Link    : 
# @Disc    : pptp through the terminal

from __future__ import print_function
import logging
import argparse

# show the status of all pptp-configs
def status():
    print("status")

# add a pptp-config
def add():
    print("add")

# remove a pptp-config
def remove():
    print("remove")

# edit a pptp-config
def edit():
    print("edit")

# the main function to control the script
def main():
    # Define the basic_parser and subparsers
    logging.debug('Initial basic_parser')

    _desc = 'pt3 is a pptp-vpn client that runs in the terminal'
    basic_parser = argparse.ArgumentParser(description=_desc)
    subparsers = basic_parser.add_subparsers(
        dest="command",
        help="Available commands"
    )

    # Subparser for the status command
    logging.debug("Initial status subparser")

    status_parser = subparsers.add_parser(
        "status",
        help="show the status of all pptp-configs"
    )

    # Subparser for the add command
    logging.debug("Initial add subparser")

    add_parser = subparsers.add_parser(
        "add",
        help="add a pptp-config"
    )

    # Subparser for the remove command
    logging.debug("Initial remove subparser")

    remove_parser = subparsers.add_parser(
        "remove",
        help="remove a pptp-config"
    )

    # Subparser for the show command
    logging.debug("Initial edit subparser")

    edit_parser = subparsers.add_parser(
        "edit",
        help="edit a pptp-config"
    )

    # handle the args input by user
    args = basic_parser.parse_args()
    # convert arguments to dict
    arguments = vars(args)
    command = arguments.pop("command")

    if command == "status":
        status()
    if command == "add":
        add()
    if command == "remove":
        remove()
    if command == "edit":
        edit()

if __name__ == '__main__':
    main()