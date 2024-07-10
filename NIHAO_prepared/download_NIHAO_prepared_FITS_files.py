import os

files = [
'NIHAO_g8.26e11_extensive_darkmatter.fits',
'NIHAO_g8.26e11_extensive_gas.fits',
'NIHAO_g8.26e11_extensive_stars.fits',
'NIHAO_g8.26e11_pilot_darkmatter.fits',
'NIHAO_g8.26e11_pilot_gas.fits',
'NIHAO_g8.26e11_pilot_stars.fits'
]

for file in files:
os.system('wget https://www.mso.anu.edu.au/~buder/NIHAO_prepared/'+file)
