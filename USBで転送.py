# coding: shift-jis
import os
import shutil

# USB�h���C�u�̑I��
drive_path = input("USB�h���C�u�̃p�X����͂��Ă�������: ")

# ���M�������t�@�C���̃p�X
file_path = input("���M�������t�@�C���̃p�X����͂��Ă�������: ")

# USB�h���C�u�Ƀt�@�C�����R�s�[
shutil.copy2(file_path, drive_path)

# ��M���ł̉𓀏���
# �t�@�C���̊g���q�ɉ����ĉ𓀕��@��ς���
file_name, file_extension = os.path.splitext(file_path)
if file_extension == ".zip":
    import zipfile
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(drive_path)
elif file_extension == ".rar":
    import rarfile
    with rarfile.RarFile(file_path, 'r') as rar_ref:
        rar_ref.extractall(drive_path)
else:
    print("�Ή����Ă��Ȃ��g���q�ł�")
