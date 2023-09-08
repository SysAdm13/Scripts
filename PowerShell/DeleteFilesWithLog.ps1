
$list = Get-ChildItem -path C:\123\* | fl Name
$data = Get-Date
Remove-Item -path C:\123\* -Exclude log
echo "This file was deleted" "$data" $list > c:\231\log.txt