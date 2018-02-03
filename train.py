# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 23:06:45 2018

@author: shubham
"""

import argparse

parser = argparse.ArgumentParser()  
#parser.add_argument("lr","momentum", "num_hidden","sizes" , "activation" , "opt" , "loss",
 #                  "batch_size" , "anneal" , "save_dir" ,"expt_dir","train","test")
parser.add_argument("lr" , help = "learning rate")
parser.add_argument("momentum",help='momentum for momentum based gradient descent')
parser.add_argument("num_hidden", help = "hidden layer excluding input and output")
parser.add_argument("sizes" , help = "comma separated list for size of each hidden layer")
parser.add_argument("activation" , help = "activation function softmax , tanh ")
parser.add_argument("opt")
parser.add_argument("loss")
parser.add_argument("batch_size")
parser.add_argument("anneal")
parser.add_argument("save_dir")
parser.add_argument("expt_dir")
parser.add_argument("train")
parser.add_argument("test")
args= parser.parse_args()
print(args.lr)
print(args.momentum)