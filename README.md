# internship-tools
Python scripts to save time on your internship for fun stuff.

Mostly dutch output.



## Install dependencies
```
sudo apt update
sudo apt install pdflatex biber python -y
```

## Tools
### Generate daylog document
Specify period in days.py and generate the markdown. Use *mdtopdf.sh* to convert markdown to pdf.


```
python days.py > out.md
./mdtopdf.sh out.md out.pdf
```


### Build LaTeX document
Build latex document using pdflatex and biber.


```
cd latex-example
./BUILD
```
