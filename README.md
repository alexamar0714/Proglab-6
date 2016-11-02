# Proglab-6
Proglab oppgave 6 
Dette er et sted hvor vi kan legge til felles koden til oppgaven, sånn at alle har tilgang til siste versjon av prosjektet. Vennligst ta en titt på dokumentasjon angående bruk av GitHub (det er enkelt). https://guides.github.com/activities/hello-world/ gir en ganske god forklaring om hvordan ting fungerer.

-----------------------------------------------------------------------------------------

UPDATE 1:      
i motor reccomendations så har meg og alex no blitt enige om at vi kjører [ (tuple), (tuple).... ] som betyr at om du har bare 1 recommendation så skal den være [(tuple)] dette slik at bbcon koden kan være generelt. ved å gjøre dette vil det være lettere å utføre flere ting i en omgang, som feks actions >> right -> left -> backwards
Tuplen skal ha 3 verdier,  

||| 1: en String som forteller hva retning man vil, hhv forward = "f", backwards = "b", right = "r", left = "l"         
||| 2: en float som definere speed ie hvor fort man vil at tuple(1) skal kjøre, float interval [-1,1]  
||| 3: en int som fortell hvor lenge en action skal vare i ms(millisekund). int interval [0, inf]

eksempel 1: [("f", 0.9, 2000)]         
eksempel 2: [("f", 0.9, 2000),("b", 0.9, 2000)]          
eksempel 2 vil foreksempel starte i posisjon A og kjøre til B, og rett etterpå gå fra B til A igjen.

Behaviour:      
Make a method with name "get_weight()" that returns the weight. this is mostly so that the ARBITRATOR can easily access all the weights of ea behaviour.         
Make another method with the name "get_motor_recc()" that returns the behaviours motor reccommendation. this is mostly for the BBCON

-----------------------------------------------------------------------------------------
NB: LES PDF AV OPPGAVEN, DETTE ER SERR VIKTIG
NB2: Sett dere inn i korleis de wrapper klassene funker

*******

FRIST:   9. Oktober

*******

Sigve:

-- Behaviours >> Line Following

use: IR reflective sensors.

Description:

We will make a line on the floor with tape. so when a line is detected, try to readjust
so that the line comes under the middle of the robot and follow it.


-- Object >> Arbitrator

input -> Array of "Behaviour Objects"

Description:

loop through ea behaviour object and use either weight or Stochastic weight to determine
the "winning" behaviour and return the WINNING behaviour Object

Output -> 1 Behaviour Object

----------------------------------------------------------------------------------------

Alex:

-- Behaviours >> Do shit if detected color

use: Camera

Description:

When a certain amount of a specific color is detected, do something random (360* turn?)

---------------------------------------------------------------------------------------

Duong:

-- Behaviours >> Avoid Obj

use: Ultra sensor and IR proximity sensor

Description:

If object is in range of either Ultra senor or IR sensor, avoid. If ultra then check ea
side first with IR-prox before turning that way.

*** IF TIME LEFT ***

Connect it to camera, so that if a certain colored obj is detected, follow its edge. ie
a box or something similar.


-- Object  >> BBCON

Description:

Make the "main" object to intertwine everything to get it to work as intended
