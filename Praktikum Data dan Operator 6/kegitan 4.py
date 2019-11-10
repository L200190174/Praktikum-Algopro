Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Nama = 'Labib Majid'
>>> NIM = 174
>>> Tinggi = 1.55
>>> Berat = 53
>>> Tahunlahir = 2001
>>> Aku = (Tahunlahir, Berat, Tinggi, NIM, Nama)
>>> Data = (Tahunlahir, Berat, Tinggi, NIM, Nama)
>>> 
>>> type(Aku)
<class 'tuple'>
>>> #perintah diatas menampilkan kelas yaitu tuple dderetan huruf atau objek
>>> 
>>> Aku(0)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    Aku(0)
TypeError: 'tuple' object is not callable
>>> aku[0]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    aku[0]
NameError: name 'aku' is not defined
>>> Aku[0]
2001
>>> 
>>> #perintah diatas menampilkan slicing dari tipe data aku menampilkan data tahunlahir
>>> 
>>> a = NIM % 4; Aku[a]
1.55
>>> #perintah diatas menampilkan sisa pembagian antara 174 dengan 4 maka hasilya Aku[a] yaitu 1.55
>>> 
>>> type(Aku[a])
<class 'float'>
>>> #perintah diatas menampilkan kelas dari data "aku[a]"
>>> 
>>> Aku[a:4]
(1.55, 174)
>>> #perintah diatas menampilkan data Aku yaitu Tinggi, dan NIM
>>> 
>>> type(Aku[4])
<class 'str'>
>>> #perintah diatas manampilkan data ke 4 dari aku yaitu nama bentuk dari sebuah string
>>> 
>>> Aku[0] = 'ok'
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    Aku[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> #perintah diatas eror karena kelas tuple tidak bisa dibuat untuk menyimpan data
>>> 
>>> type(Data)
<class 'tuple'>
>>> #perintah diatas menampilkan jenis dari onjek Data adalah tuple
>>> 
>>> type(Data[4])
<class 'str'>
>>> #perintah diatas menampilkan data ke 4 dari Data, yaitu nama bentuk dari string
>>> 
>>> Data[4][5]
' '
>>> #perintah diatas menampilkan di dalam list selanjutnya menambil lagi dialam Nama urutan ke 5
>>> 
>>> Data[4][a:6]
'bib '
>>> #perintah diatas menampilkan dari data Nama dan mengambil dari data 2-5
>>> 
>>> Data[0] = 'ok'; Data
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    Data[0] = 'ok'; Data
TypeError: 'tuple' object does not support item assignment
>>> #perintah diatas eror karena kelas tuple tidak bisa dibuat untuk menyimpan data
>>> 
>>> Data[-a]
174
>>> #perintah diatas menampilkan NIM yang tersimpan didalam list
>>> 
>>> range(a)
range(0, 2)
>>> #perintah menampilkan range dari a yaitu 0 dan 2
