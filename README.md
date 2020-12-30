
# GetBase
## 1. Introduction

The UCSC genome browser [1] is widely used in comparative genomics, but it does not provide a highly customized data download path. Researchers are usually only interested in specific genes or regions and expect to obtain corresponding alignment data. Manually downloading these data is disorderly and difficult to analyze. To automatically obtain the species alignment data from the UCSC genome browser, we developed a tool, GetBase, to obtain the base information of a specific location from the UCSC genome browser. This tool allows us to obtain base information at any position in the species of interest for comparative genomics analysis.

## 2. Running requirement

GetBase is based on Python-3.7; any operation system with Python can use it.

## 3. Input and output format

Input format:
(example.input)
Line 1: Species Name, which need to be same with UCSC recorded
Column 1: Genome position
Output format:
The results including a,t,c,g,-,=,N and blank. All the results are the same annotation with UCSC rule [1]. 


## Reference: 
[1] UCSC Genome Browser: Kent WJ, Sugnet CW, Furey TS, Roskin KM, Pringle TH, Zahler AM, Haussler D. The human genome browser at UCSC. Genome Res. 2002 Jun;12(6):996-1006.
