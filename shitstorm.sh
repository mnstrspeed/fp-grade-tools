#! /bin/bash

# shitstorm.sh keeps throwing ungraded work at 
# you until you beg for mercy

EDITOR="vi -p"
for fulldir in "${1:+$1/}"[sez][0-9]*; do
    dir="${fulldir##*/}"
    file="${fulldir}/${dir}.txt"
    
    GRADE=`sed -n '/^Current Grade:[[:space:]]*/s///p' "$file"`
    if [ "$GRADE" = "Not Yet Graded" ] || ! grep -q "Feedback:" "$file"; then
        
        read -p "Next up: $dir. Beg for mercy [please stop|come at me bro] "
        if [[ $REPLY == *"please stop"* ]]; then
            echo "You're weak."
            exit 0
        fi

        ./log.sh $1/logged_time $EDITOR $(find $fulldir '*' | sed 's/ /\\ /g') $1/notes 
    fi
done
echo "Looks like you survived... this time"
