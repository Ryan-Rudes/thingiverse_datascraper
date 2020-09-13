# Thingiverse Datscraper
A Python Datascraper for the Thingiverse Website

Upon executing, this will create a directory to store .stl files. It will begin iterating through all possible things on thingiverse.com, scraping every .stl file from every .zip archive it can find, storing them in the aforementioned directory.

It will also continue to update a text file containing many unseparated 8-digit numbers between 1000000 and 99999999. These represent the thing ID of each item found. Note that thingiverse items can be found via their ID with the following URL format: https://www.thingiverse.com/thing:8DIGITID. Accordingly, the files associated with a particular item can be found by adding "/zip" to the path.

Run `python3 thingiverse.py` to get started.
