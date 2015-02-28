#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys, pygame
import about
import game

if sys.argv[1:]:
	if sys.argv[1] == "--about" or sys.argv[1] == "-a":
		ab = about.About()
		ab.print_about_message()
		exit()

instance = game.Game()
exit(instance.run())
