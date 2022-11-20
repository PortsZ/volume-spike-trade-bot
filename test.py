
import os

os.system("""
    powershell.exe \"
        Add-Type -AssemblyName System.Windows.Forms
        [Windows.Forms.Sendkeys]::SendWait('+{Prtsc}')
        \$img = [Windows.Forms.Clipboard]::GetImage()
        \$img.Save(\\\"/home/portsz/Projects/volumeTradeBot/screenshots/screenshot.jpg\\\", [Drawing.Imaging.ImageFormat]::Jpeg)\"
""")