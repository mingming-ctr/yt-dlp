


cd "C:\myexe\《凡人修仙传》\《凡人修仙传》1501-1600集Mortal's Journey to Immortality 最新动漫解说"


$allFile = Get-ChildItem -Path "C:\myexe\《凡人修仙传》\《凡人修仙传》1501-1600集Mortal's Journey to Immortality 最新动漫解说"  -Filter *.m4a;
foreach ($file in $allFile)
{
 ffmpeg -i ''$file'' ''$file''".mp3";
} 




 ffmpeg -i "'$file'" "'$file.mp3'";

 ffmpeg -i "'$file'" "'$file.mp3'";
Write-Host
ffmpeg -i $file.name $file.name.mp3

for %i in( *.m4a ) do echo %i

