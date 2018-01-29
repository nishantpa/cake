<< DnD >>
@nishantpatel ; 12 Oct 2017

# Plan of Attack (Scrape and search):

The jenkPlug.fail file is the file that has errors when attempting to update 
all plugins at once. There are certain plugins that require a specific 
version of another plugin, and mismatches exist at this point. One possible
solution is to find those mismatches and correct them by hand after scraping
them with scrapy. 

Before we scrape, we need to get a list of URLs. Execute the following:
./getURL.sh jenkPlug.fail > URLsList.txt
	and move the file to the first jenkinsWork dir

In the top level jenkinsWork folder, to scrape those required dependencies from 
the sites, run it with the following:

scrapy crawl jenkTS -a filename=URLsList.txt -o plugDependents.json

This file will contain a list of each plugin ID's dependencies. The next job is
to find those mismatched dependencies and output that in a neat format. It would
be easier to grab those dependencies that are repeated within the plugDeps.json 
file and check their versions to see if there's a mismatch. Output that in a 
neat format.

Using a json parser called jq, I was able to narrow down those dependencies that 
match across the set of all plugins.

jq -r '.[] | select(.dependency[0]) | (.dependency|tostring|ltrimstr("[")|rtrimstr("]")) + ", \"plugID\": "+ (.plugID|tostring) | @text' plugDeps.json > mismatchedVers.txt
