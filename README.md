# Project1-analyzator
První projekt kurzu ENGETO

# Připomínky lektora
Co zlepšit:

1. Statistika pro titlecase: zde výpis slov: There are 12 titlecase words:
   ['Situated', 'Kemmerer,', 'Fossil', 'Butte', 'Twin', 'Creek', 'Valley', 'The', '30N', 'Union', 'Pacific', 'Railroad,']- 30N nezačíná na velké písmeno.
   Metoda isstitle funguje tak, že zjišťuje zda první ABECEDNÍ znak ve slově je velký písmeno a ostatní malá ,
   ale ignoruje NEABECEDNˇI znaky. Takže slovo 30N vidí jako N. Zde je potřeba k tomu přistoupit trochu jinak.
   
3. Univerzálnost: použil jsi proměnnou nr_of_texts, ale mohla být použita i na řádku 29
4. Řádek 85: je to ok pro ukázkové texty, ale když se ale změní text, nebo přidá a bude obsahovat i jiné nežádoucí znaky, tak ti to fungovat nebude.
