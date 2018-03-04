import argparse
import glob
import os
import sys
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer

print """
 
 `\.      ./'
  |\\\____//|
  )/_ `' _\(
 ,'/-`__'-\`,
 /. (_><_) ,\\
 ` )/`--'\(`'
   `      '
   
    __    _____   ___  __      ____ 
   / /   /  _/ | / / |/ /     / __ \\
  / /    / //  |/ /|   /_____/ / / /
 / /____/ // /|  //   /_____/ /_/ / 
/_____/___/_/ |_//_/|_|     \____/  
                                    
 
 	Logic Identification of uNique eXploit (Kit)-Objects
 
 """

parser = argparse.ArgumentParser(description= "LINX-O - Logic Identification of uNique eXploit (Kit)-Objects")
parser.add_argument("-f","--file", required=True, help="File of Interest - Needs to be in Directory of Files")
parser.add_argument("-p","--path", required=True, help="Directory of Files to Compare Against")
args = vars(parser.parse_args())

#File of interest NEEDS to be in path_to_files directory
file_of_interest = args['file']

#Path to directory of files to compare against
path_to_files = args['path']

file_list  = glob.glob("%s*.*" % path_to_files)

index_pages = []

if not os.path.exists("%s" % file_of_interest):
    print "Your object was not %s is not found. Provide absolute path." % file_of_interest
    sys.exit(0)
else:
    print "The object %s found. Analyzing now." % file_of_interest


for f in file_list:	
	#reads HTML files, converts them to unicode
	try:
		soup = BeautifulSoup(open(f), "html.parser")

		try:
			html_file = unicode(soup)
		except:
			#Cannot convert HTML to unicode, prints problem files
			print f
		#puts HTML files in unicode into index_page list
		index_pages.append(html_file) 	
	except:
		#Text based files (not HTML files) read and turned into unicode and put into index_page list
		with open(f,'r') as ins:
			for line in ins:
				line = unicode(line, error='ignore')
				index_pages.append(line)
		
#Machine Learning section
tfidf = TfidfVectorizer().fit_transform(index_pages)
pairwise_similarity = tfidf * tfidf.T
page_similarity_matrix = pairwise_similarity.A[file_list.index(file_of_interest)]

#Search for clone based on detect_score
detect_score = 0.75
compare_counter = 0
for score in page_similarity_matrix:
	if score > detect_score:
		if file_list[compare_counter] != file_of_interest:
			if score == 1.0:
				print "Exact Clone: %s to %s (Score: %2.2f)" % (file_of_interest,file_list[compare_counter],score)
			else:
				print "Potential Clone: %s to %s (Score: %2.2f)" % (file_of_interest,file_list[compare_counter],score)
	compare_counter += 1

print "[!] Analysis Complete [!]"
