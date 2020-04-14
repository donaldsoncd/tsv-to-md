# tsv-to-md
A script to convert a tab-separated value (tsv) file to a markdown text file in a prose-like format.

It is the counterpart to [md-to-tsv](https://github.com/donaldsoncd/md-to-tsv), which converts in the opposite direction.

## Instructions

- Download the python script `to-md.py`

- Place it in the folder along with the TSV file that you would like to convert to a markdown file.

- Open your terminal and navigate to the folder where the script and your file are

- Run the script by typing in `python to-md.py` PLUS the name of your file.

  All together, this means you type something like this, for example:

  `python to_md.py manuscript.tsv`

### Formatting specifications

Input file notes:

- The input file must be a tab-separated value file
- The first row must be a series of headers
- The first column must be identifiers for the segments

Output file notes:

- Identifiers become level three markdown headers via three hashtag marks (`###`)
- Language segments become markdown paragraphs (that is, with an empty line between them)

## Ajami Lab Use

This script was designed in the context of the [Ajami Lab](https://ajami.hypotheses.org/) to facilitate the conversion of [Ajami annotation data extracted from a Tropy project](https://ajami.hypotheses.org/598) into a format conducive to prose-like publication (as a critical edition style chapter, appendix, etc).

Once a TSV is put into markdown format, it can easily be edited further using [pandoc](https://pandoc.org/) flavored markdown that allows for footnotes, etc., and then easily exported as a static html page or common word-processing file for Word, LibreOffice, etc.

From this perspective, the Tropy project is the single or master "source code" for export to other formats (tabular or text) designed for further analysis or publication.

## Screenshots

For from this:

<img width="598" alt="tabbed" src="https://user-images.githubusercontent.com/28364193/79261297-ea076e00-7e8f-11ea-9c36-1303c93b467b.png">

To this:

<img width="272" alt="prose" src="https://user-images.githubusercontent.com/28364193/79261247-d65c0780-7e8f-11ea-97bf-000339f0421a.png">