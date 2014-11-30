#!/bin/bash

ssh $1@$1.cs.hmc.edu "(cd ~/heart-attack && zsh attack_aux.zsh $2)"
