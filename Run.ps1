Invoke-WebRequest -Uri 'https://go.microsoft.com/fwlink/?linkid=2084706"&"Channel=Canary"&"language=en' -OutFile MicrosoftEdgeSetup.exe;
Start-Process .\MicrosoftEdgeSetup.exe -ArgumentList '/silent /install' -Wait;

py .\webdriver.py