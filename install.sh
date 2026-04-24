#!/bin/bash

echo "Installing BCF79..."

pkg update -y
pkg install python nodejs git -y

pip install -r requirements.txt
npm install -g truecallerjs

echo ""
echo "Login to Truecaller:"
truecallerjs login

echo ""
echo "Done! Run: python bcf79.py"
