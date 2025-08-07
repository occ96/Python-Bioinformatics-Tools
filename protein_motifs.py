import os #import operating system
# loop through protein id's to import from uniprot website
from urllib.request import urlopen  #import new module to use, will assist in opening direct URL                        
from Bio import SeqIO   #must use BioPython for assignment, import this module for use                       
import re #regex module to assist in N-glycosylation motif

mydir = "C:\\Users\\16186\\Downloads\\" #locate downloads filepath
infile = mydir + "rosmprt.txt" #designate input file location and dataset we will be using
outfile = open(os.getcwd() + "\\prob_15soln.txt", "w") #specify output file that we will write to
ID = [] #create empty list to contain access IDs found                 
with open(infile) as f:  #open our input file as f              
    for line in f:  #designate for each line existing in the file used                                
        ID.append(line.rstrip()) #add to list; for each line in file, strip() removes trailing and leading chars
                                                              
for i in range(len(ID)):                                      
    URL = 'http://www.uniprot.org/uniprot/' + ID[i] + '.fasta' #direct link to uniprot + access ID from dataset + retrieve fasta format
    #can include protein data in URL if we wanted
    dataset = urlopen(URL)  #using shortcut urlopen we can open the link to uniprot             
    fasta = dataset.read().decode(encoding= 'utf-8', errors = 'ignore')    #fasta file must be opened in text mode otherwise error occurs BioSeq cannot decode bytes
    #decode the string using the codec registered for encoding
    with open("fastafile.fasta", 'a') as txtmode: #open the file and this fasta file must be in text mode,
        #able to retrieve this information using urlopen and decoding our datset while appending to the file         
        txtmode.write(fasta)  #write the fasta seq to the file                               
                                              
handle = open("fastafile.fasta") #open our sequence fasta                         
motif = re.compile('(?=(N[^P][ST][^P]))') #regex compiles the N-glycos. motifs
                                        #N{any but P}[S or T]{any but P}, but we could have overlap
                                        #parentheses and use of '?=' allow for overlapping motifs

counter = 0 #initialize counter to begin at 0                                          
for record in SeqIO.parse(handle, 'fasta'):  #using BioPython, parse each record with SeqIO in dataset                
    location = []  #create empty list that will contain each motif's position
    seq1 = record.seq     #seq var will contain the record we parsed through                                                                         
    for pm in re.finditer(motif, str(seq1)): #pm = protein motifs; using regexfinditer can yield all non-overlapped motifs that match the pattern       
        location.append(pm.start() +1) #with append fxn, we can add matches to list of positions found for protein motifs                           
    if len(location) !=0:  #len will return location of position found if they do not equal to pos 0                                  
        print(ID[counter], file=outfile)#print the respective access ID when the motifs are found
        print(' '.join(map(str, location)), file=outfile) #map function executes str for each location found
        #joins these together and writes it to output file
    counter = counter + 1 #add to counter as more motifs pos are located

outfile.close() #close output file we wrote to
