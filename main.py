from functions import *

summarise = summary(extract('animal_welfare.pdf', pg_reduction=0), 
                    instructions="Provide a quick summary by condensing the chapters into bite sized paragraphs and explain it in layman terms.")
print(summarise)
