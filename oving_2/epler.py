print("Dette er et program for å teste din sjenerøsitet.")
har_epler = int(input("Hvor mange epler har du? "))
if har_epler == 0:
   print("Æsj, det sier du bare for å slippe å gi noe!")
else:
    gir_epler = int(input("Hvor mange kan du gi til meg? "))
    
    if gir_epler < (har_epler / 2):
        print("Du beholder det meste for deg selv...")
    else:
        print("Takk, det var snilt!")
    
    print("Du har nå ", max(har_epler - gir_epler,0), " eple",''.join(['r' for s in range(int(bool((har_epler - gir_epler)!=1)))])," igjen.", sep='')
    if har_epler < gir_epler:
        print("Gi meg de {0} du skylder meg neste gang vi møtes.".format(gir_epler-har_epler))
  