kolichestvo_chisel = 0
summa_chisel = 0
proizvedenie_chisel = 1
srednee_arifmetich = 1
poryadkoviy_nomer_max_chisla = 0
max_chislo = 0
kolichestvo_chetnih = 0
kolichestvo_nechetnih = 0
vtoroe_max_chislo = 0
poryadkoviy_nomer_vtorogo_max_chisla = 0
novoe_chislo = 1

while novoe_chislo != 0:
    novoe_chislo = int(input('Please input number: \n'))
    if novoe_chislo != 0:
        kolichestvo_chisel += 1
        summa_chisel += novoe_chislo
        proizvedenie_chisel *= novoe_chislo
        srednee_arifmetich = summa_chisel / kolichestvo_chisel
        if novoe_chislo > max_chislo:
            vtoroe_max_chislo = max_chislo
            poryadkoviy_nomer_vtorogo_max_chisla += 1
            max_chislo = novoe_chislo
            poryadkoviy_nomer_max_chisla += 1
        if novoe_chislo % 2 == 0:
            kolichestvo_chetnih += 1
        else:
            kolichestvo_nechetnih += 1
print(f'''kolichestvo_chisel = {kolichestvo_chisel= {max_chislo}
poryadkoviy_nomer_max_chisla = {poryadkoviy_nomer_max_chisla}
vtoroe_max_chislo = {vtoroe_max_chislo}
poryadkoviy_nomer_vtorogo_max_chisla = {poryadkoviy_nomer_vtorogo_max_chisla}
kolichestvo_ch             kolichestvo_nechetnih += 1
print(f'''kolichestvo_chisel = {kolichestvo_chisel= {max_chislo}
poryadkoviy_nomer_max_chisla = {poryadkoviy_nomer_max_chisla}
vtoroe_max_chislo = {vtoroe_max_chislo}
poryadkoviy_nomer_vtorogo_max_chisla = {poryadkoviy_nomer_vtorogo_max_chisla}
kolichestvo_chetnih = {kolichestvo_chetnih}
kolichestvo_nechetnih = {kolichestvo_nechetnih}'''
      )
