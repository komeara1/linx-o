# LINX-O (Logic Identification of uNique eXploit (Kit) - Objects) - A Tool to Find Commonalities in Exploit Kit Objects from Packet Captures.

* The tool uses TF-IDF short for term frequency–inverse document frequency, is a numerical statistic that is intended to reflect how important a word is to a document in a collection. 
* Search engines have been known to use TF-IDF.
* scikit-learn is the Python library that is used to do the TF-IDF analysis.

## Author
* Kyle O'Meara
* Created during [GeekWeek 2016](https://g33kw33k.ca/en/index.html)

## Dependencies
* scipy, numpy, scikit-learn. Use pip to install them in this order.

## Usage
```
$ python linx-o.py -f [file-of-interest] -p [path-to-files]
```

## Notes
* There is a little pre-work needed. You need to extract all text based objects from exploit kit packet captures. 
* Goal was to determine if there were or were not commonalities in exploit kit objects
* Just an FYI the Scikit-Learn machine learning Python library is processor intensive.

## References
* Justin Seitz and his [Automation OSINT Blog](http://www.automatingosint.com/blog/2016/09/dark-web-osint-part-four-using-scikit-learn-to-find-hidden-service-clones/)
* [Malware Traffic Analysis](http://www.malware-traffic-analysis.net/)