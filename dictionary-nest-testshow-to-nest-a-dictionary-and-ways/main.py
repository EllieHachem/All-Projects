#nesting ways

pro = {
    bro:"lebanon",
    pro:"united state"
    }


# each key can only have one value that is why we need list for
#example

pro = {bro:"lebanon"} and not pro = {bro:"lebanon", "united state"}

#fo fix this we change key into list like now 
pro = {bro:["lebanon", "united state"]}


#you can also nest a list inside a list an exaple

[a, b, c, [d, f]] #though not effeicent as storying list or dictonary
#inside a dictonary bcause of way data is structured 


#nest a dicontary in a dictonary 


pro = {
    bro:{"city_visted":["lebanon", "united state"]}"pro":{"my man"}
    }

#now nesting a dictonary inside a list just put squard bracket easy as that

pro =[
{
    bro:{"city_visted":["lebanon", "united state"]}"pro":{"my man"}
    } {
    bro:{"city_visted":["lebanon", "united state"]}"pro":{"my man"}
    }
]