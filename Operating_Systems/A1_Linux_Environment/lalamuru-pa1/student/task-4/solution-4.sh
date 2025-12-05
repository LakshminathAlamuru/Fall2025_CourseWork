#!/bin/bash

# get current username
get_current_user=$(whoami)

# kill all process with name ./infloop by excluding grep one, with pid
ps -u "$get_current_user" -ef | grep './infloop' | grep -v grep | awk '{print $2}' | xargs -r kill -9
