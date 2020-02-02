cd D:\dest
mp3cat -d . -o combined.mp3
for %%f in (./*.mp3) do (if NOT %%f == combined.mp3 del %%f )