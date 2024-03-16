#!/bin/bash
#used to toggle between keyboard layouts - assumes only using us and us(dvorak)
layout=$(setxkbmap -print | grep -o -P -m1 "us(?:\(dvorak\))?")
if [ "$layout" = "us" ]; then
	$(setxkbmap us dvorak)
else
	$(setxkbmap us)
fi
