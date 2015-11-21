#!/usr/bin/env python
import sys, argparse, csv
import numpy as np

with open('trainingData.txt', "rU") as infile, open('trainingData.csv', 'wb') as outfile:
    in_txt = csv.reader(infile, delimiter = '\t')
    out_csv = csv.writer(outfile)
    out_csv.writerows(in_txt)
infile.close
outfile.close
counter = 0 
# #269 columns
# # No = -1, Yes = 1, Complete_remission = 1, resilience = 0, Everything else = -1
# # NA=0
# #NEG=-1, POS=1
# # F = 1, M=-1
# # Chemos: ANTHRA_HDAC = 0, HDAC-PLUS=1, FLU_HDAC = 2; STDARAC-PLUS = 3
REMISSED_PATIENTS = {}
RESISTANT_PATIENTS = {}
M_Rem_Pat = {}
F_Rem_Pat = {}
M_Res_Pat = {}
F_Res_Pat = {}

with open('trainingData.csv', 'r') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
	
	for row in spamreader:
		for ind, var in enumerate(row[1:]):
			if var == 'COMPLETE_REMISSION':
				REMISSED_PATIENTS["Patient"+str(counter)]=row
			if var == 'RESISTANT':
				RESISTANT_PATIENTS["Patient"+str(counter)]=row
		counter = counter+1

# Parses male and female for remissed
for patient in REMISSED_PATIENTS:
	for ind, var in enumerate(REMISSED_PATIENTS[patient]):
		if var == 'M':
			M_Rem_Pat[patient] = REMISSED_PATIENTS[patient]
		if var == 'F':
			F_Rem_Pat[patient] = REMISSED_PATIENTS[patient]

# Parses male and female for resistant
for patient in RESISTANT_PATIENTS:
	for ind, var in enumerate(RESISTANT_PATIENTS[patient]):
		if var == 'M':
			M_Res_Pat[patient] = RESISTANT_PATIENTS[patient]
		if var == 'F':
			F_Res_Pat[patient] = RESISTANT_PATIENTS[patient]


print M_Res_Pat
print str(len(M_Rem_Pat)+len(F_Rem_Pat)+len(M_Res_Pat)+len(F_Res_Pat))
# # for patient in REMISSED_PATIENTS:
# # 	print REMISSED_PATIENTS[patient][266]
# for patient in RESISTANT_PATIENTS:
# 	print patient

for patient in REMISSED_PATIENTS:
	for ind, var in enumerate(REMISSED_PATIENTS[patient]):
		# Yes/No responses
				if var in ('YES', 'COMPLETE_REMISSION', 'POS', 'F'):
					var = '1'
					REMISSED_PATIENTS[patient][ind] = var 
				if var in ('No', 'RESISTANT', 'NEG', 'M') :
					var='-1'
					REMISSED_PATIENTS[patient][ind] = var 
				# No information
				if var == 'NA':
					var = '0'
					REMISSED_PATIENTS[patient][ind] = var  

				# Chemo type
				if var == 'Anthra-HDAC':
					var = '0'
					REMISSED_PATIENTS[patient][ind] = var  
				if var == 'HDAC-Plus':
					var = '1'
					REMISSED_PATIENTS[patient][ind] = var 
				if var == 'Flu-HDAC':
					var = '2'
					REMISSED_PATIENTS[patient][ind] = var 
				if var == 'StdAraC-Plus':
					var = '3'
					REMISSED_PATIENTS[patient][ind] = var 

for patient in RESISTANT_PATIENTS:
	for ind, var in enumerate(RESISTANT_PATIENTS[patient]):
				
		# Yes/No responses
				if var in ('YES','Yes', 'COMPLETE_REMISSION', 'POS', 'F'):
					var = '1'
					RESISTANT_PATIENTS[patient][ind] = var 
				if var in ('No', 'NO', 'RESISTANT', 'NEG', 'M') :
					var='-1'
					RESISTANT_PATIENTS[patient][ind] = var 
				# No information
				if var == 'NA':
					var = '0'
					RESISTANT_PATIENTS[patient][ind] = var  

				# Chemo type
				if var == 'Anthra-HDAC':
					var = '0'
					RESISTANT_PATIENTS[patient][ind] = var  
				if var == 'HDAC-Plus':
					var = '1'
					RESISTANT_PATIENTS[patient][ind] = var 
				if var == 'Flu-HDAC':
					var = '2'
					RESISTANT_PATIENTS[patient][ind] = var 
				if var == 'StdAraC-Plus':
					var = '3'
					RESISTANT_PATIENTS[patient][ind] = var 

# print REMISSED_PATIENTS["Patient166"]
# print "________________________________________________________"
# print RESISTANT_PATIENTS["Patient165"]	
# print str(len(REMISSED_PATIENTS)+len(RESISTANT_PATIENTS))			

