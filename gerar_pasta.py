import os
import datetime

meses = {'01':'Janeiro',
         '02':'Fevereiro',
         '03':'Março',
         '04':'Abril',
         '05':'Maio',
         '06':'Junho',
         '07':'Julho',
         '08':'Agosto',
         '09':'Setembro',
         '10':'Outubro',
         '11':'Novembro',
         '12':'Dezembro'}

today = datetime.datetime.now()
D1 = today - datetime.timedelta(days=0)
month = D1.strftime('%m')
#os.chdir('C:\\')
#os.mkdir(D1.strftime('20'+'%y%d'))
file_path_onedrive = 'C:\\Users\\gabri\\OneDrive\\Arquivo de voz\\'+str(month)+' - '+str(meses[month])
if not os.path.exists(file_path_onedrive):
    os.chdir('C:\\Users\\gabri\\OneDrive\\Arquivo de voz')
    os.mkdir(str(month)+' - '+str(meses[month]))
os.chdir(file_path_onedrive)
for i in os.listdir():
    pasta_d1 = '20'+D1.strftime('%y%m%d')
    if not os.path.exists(pasta_d1):
        os.mkdir(pasta_d1)
os.chdir('C:\\')
for i in os.listdir():
    pasta_d1 = '20'+D1.strftime('%y%d')
    if not os.path.exists(pasta_d1):
        os.mkdir(pasta_d1)
    



