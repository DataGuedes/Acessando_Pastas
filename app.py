import os
import datetime
import shutil
import time

def compactar_arquivos():
    file_path = 'C:\\'+D1.strftime('20'+'%y%d')
    os.chdir(file_path)
    print('Acessando a pasta - ', file_path)
    shutil.make_archive('voice_File_'+D1.strftime('20'+'%y%m%d'), 'gztar', file_path)
    print('Arquivos compactados - voice_File'+D1.strftime('%d.%m.%y'))

def buscar_arquivo():
    file_path_onedrive = 'C:\\Users\\gabri\\OneDrive\\Arquivo de voz\\'+str(month)+' - '+str(meses[month])
    file_path = 'C:\\'+str(D1.strftime('20'+'%y%d'))    
    print('Movendo o arquivo para o OneDrive - ', file_path)
    os.chdir(file_path)
    file_name = 'voice_File_20'+str(D1.strftime('%y%m%d'))+'.tar.gz'
    for i in os.listdir():
        if i == file_name:
            os.rename(i,file_path_onedrive+'\\20'+D1.strftime('%y%m%d')+'\\'+i)
    print('Arquivo postado - ', time.strftime('%d/%m%y %H:%M:%S'))
            
if __name__ == "__main__":
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
    date_now = datetime.datetime.now()
    D1 = date_now - datetime.timedelta(days=0)
    month = D1.strftime('%m')
    print('Compactando arquivo de voz - TIM')
    print('Inicio - ', date_now.strftime('%d/%m/20/%y %H:%M:%S'))
    compactar_arquivos()
    buscar_arquivo()







    





