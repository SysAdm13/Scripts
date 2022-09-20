# Выполняем настройку скрипта.
$TargetFolder = "" # Путь к папке логов.
$TargetFolder2 = "" # Путь к папке логов.
$Period = "-10" # Количество хранимых дней.

# Вычисляем дату после которой будем удалять файлы.
$CurrentDay = Get-Date
$ChDaysDel = $CurrentDay.AddDays($Period)
 
# Удаление файлов, дата создания которых больше заданного количества дней
GCI -Path $TargetFolder -Recurse | Where-Object {$_.CreationTime -LT $ChDaysDel} | RI -Recurse -Force 
GCI -Path $TargetFolder2 -Recurse | Where-Object {$_.CreationTime -LT $ChDaysDel} | RI -Recurse -Force 
 
# Удаление пустых папок
#GCI -Path $TargetFolder -Recurse | Where-Object {$_.PSIsContainer -and @(Get-ChildItem -Path $_.Fullname -Recurse | Where { -not $_.PSIsContainer }).Count -eq 0 } | RI -Recurse