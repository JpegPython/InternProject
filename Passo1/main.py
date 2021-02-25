import os
import shutil


def compile_files_WMLS(path,path_exe):
    for root, dirs, files in os.walk(path):
        for file in files:
            original_path_file = os.path.join(root, file)
            if '.wmls' in file:
                os.system(fr'{path_exe} {original_path_file}')




def rename_compiled_file(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            original_path_file = os.path.join(root, file)
            file_name, file_exp = os.path.splitext(file)
            new_exp = file_name + '.wsc'
            new_path_file = os.path.join(root, new_exp)
            if file_exp == '.wmlsc' in file:
                print(f'Renomeando arquivo {file} para {file_name}.wsc')
                shutil.move(original_path_file, new_path_file)


def copy_files_POSWEB(path,path_f,path_i):
    for root, dirs, files in os.walk(path):
        for file in files:
            original_path_file = os.path.join(root, file)
            new_path_file_f = os.path.join(path_f, file)
            new_path_file_i = os.path.join(path_i, file)
            file_name, file_ext = os.path.splitext(file)


            if file_ext == '.wsc' in file:
                shutil.move(original_path_file, new_path_file_f)
                print(f'Arquivo {file} foi movido.')
            elif file_ext == '.wml' in file:
                shutil.copy(original_path_file, new_path_file_f)
                print(f'Arquivo {file} foi movido.')
            elif (file_name + file_ext == 'config.ini'):
                shutil.copy(original_path_file, new_path_file_i)
                print(f'Arquivo {file} foi movido.')
            else:
                pass


            if root == fr'{path}\db':
                shutil.copy(original_path_file, new_path_file_i)
                print(f'Arquivo {file} foi movido.')
            elif root == fr'{path}\images':
                shutil.copy(original_path_file, new_path_file_f)
                print(f'Arquivo {file} foi movido.')
            else:
                pass

def copy_files_src(path,path_f,path_i):
    for root, dirs, files in os.walk(path):
        for file in files:
            original_path_file = os.path.join(root, file)
            new_path_file_f = os.path.join(path_f, file)
            new_path_file_i = os.path.join(path_i, file)
            file_name, file_ext = os.path.splitext(file)


            if root == fr'{path}\_font':
                if (file_ext == '.pwf'):
                    shutil.copy(original_path_file, new_path_file_f)
                    print(f'Arquivo {file} foi movido.')
            elif root == fr'{path}\_theme':
                shutil.copy(original_path_file, new_path_file_f)
                print(f'Arquivo {file} foi movido.')
            elif root == fr'{path}\_minimal':
                shutil.copy(original_path_file, new_path_file_i)
                print(f'Arquivo {file} foi movido.')
            else:
                pass


def list_files(path_load,path_f,path_i):
    arqf=[]
    arqi=[]

    for root, dirs, files in os.walk(path_f):
        for file in files:
            arqf.append(file)


    for root, dirs, files in os.walk(path_i):
        for file in files:
            arqi.append(file)


    with open(fr'{path_load}\flist.web', 'w+') as file:
        for i in arqf:
            file.write(i)
            file.write('\n')

    with open(fr'{path_load}\ilist.web', 'w+') as file:
        for i in arqi:
            file.write(i)
            file.write('\n')




#declaraçao dos diretorios originais

exe_path=r'...\WMLSComp.exe'
original_path_src =r'...\src'
original_path_src_POSWEB=r'...\src\POSWEB'


#criaçao dos novos diretorios
try:
    os.mkdir(r'...\load')
    os.mkdir(r'...\load\POSWEB')
    os.mkdir(r'...\load\POSWEB\f')
    os.mkdir(r'...\load\POSWEB\i')
except FileExistsError as e:
    print("Arquivo ja existe.")


#declaraçao dos novos diretorios
new_path_load=r'...\load'
new_path_load_POSWEB=r'...\load\POSWEB'
new_path_load_POSWEB_f=r'...\load\POSWEB\f'
new_path_load_POSWEB_i=r'...\load\POSWEB\i'



#compilar arquivo WMLS
compile_files_WMLS(original_path_src_POSWEB,exe_path)
print("Compiled!")
print()


#renomear arquivo compilado (.wmlsc) para .wsc
rename_compiled_file(original_path_src_POSWEB)
print()



#movendo e copiando do diretorio original(POSWEB) para o novo diretorio POSWEB\f e POSWEB\i
copy_files_POSWEB(original_path_src_POSWEB,new_path_load_POSWEB_f,new_path_load_POSWEB_i)
print()


#copiando do diretorio original (src) para novo diretorio POSWEB\f e POSWEB\i
copy_files_src(original_path_src,new_path_load_POSWEB_f,new_path_load_POSWEB_i)
print()


#criar .web listando os arquivos de cada diretorio
list_files(new_path_load,new_path_load_POSWEB_f,new_path_load_POSWEB_i)
print("Arquivos listados.")