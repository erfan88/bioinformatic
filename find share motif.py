# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 21:20:30 2020

@author: Erfan
"""

def load_dna_sequences(file_adress):     
    
    dna_list:list=[]   
    dna = ""
    file = open(file_adress,'r',encoding='utf8')
    
    lines = file.readlines()
    for line in lines :
        if(line[0] == ">"):
            dna_list.append(dna)
            dna=""
            pass
        
        else:
            # print(line)
            dna += line
    return dna_list

def find_min_dna_sequences(dna_sequences):
    min_sequence=dna_sequences[0]
    for dna_sequence in dna_sequences:
        if len(dna_sequence)<len(min_sequence):
            min_sequence=dna_sequence
    return min_sequence

def check_subString(window_size,substring,dna_sequence):
    for i in range(len(dna_sequence)):
        part_sequence=dna_sequence[i:i+window_size]
        if part_sequence==substring:
            return True
    return False


def is_subString(window_size,substring,dna_sequences):
    
    for dna_sequence in dna_sequences:
       flag = check_subString(window_size, substring, dna_sequence)
       if not flag :
           return False
    return True



dna_sequences=load_dna_sequences(r'C:\Users\Erfan\Downloads\rosalind_lcsm.txt')

min_sequence = find_min_dna_sequences(dna_sequences)
flag = False
for window in range(len(min_sequence),2,-1):
    if flag:
        break
    for base in range(int(len(min_sequence)/window)+1):
        sub = min_sequence[base:base+window]
        if is_subString(window, sub, dna_sequences):
            print(sub)
            flag = True
            break
