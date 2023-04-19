import matplotlib.pyplot as plt
fig, ax= plt.subplots(2,2, figsize=(10, 12))

jpg=plt.imread('D:\File ITTS S1 CE\SEMESTER 8\CEC30C3 Digital Computer Vision\Pertemuan 2\TUGAS 1\zevalente.jpg')
print("dimensi gambar {}".format(jpg.shape))

jpg_red=jpg[:,:,0]
jpg_green=jpg[:,:,1]
jpg_blue=jpg[:,:,2]
cmap = 'gray'

#RGB
ax[0,0].imshow(jpg, cmap = 'gray')
ax[0,0].axis('off')
ax[0,0].set_title('Channel Warna RGB')

#Split Channel Merah
ax[0,1].imshow(jpg_red, cmap = 'gray')
ax[0,1].axis('off')
ax[0,1].set_title('Channel Warna Red')

#Split Channel Hijau
ax[1,0].imshow(jpg_green, cmap = 'gray')
ax[1,0].axis('off')
ax[1,0].set_title('Channel Warna Green')

#Split Channel Biru
ax[1,1].imshow(jpg_blue, cmap = 'gray')
ax[1,1].axis('off')
ax[1,1].set_title('Channel Warna Blue')

plt.show()