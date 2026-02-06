$content = Get-Content "PUBLICATION_READY_NOVEL.html" -Encoding UTF8
$cleanContent = $content[0..495] # Lines are 0-indexed. Line 496 is index 495.
$cleanContent += "</html>"
$cleanContent | Set-Content "PUBLICATION_READY_NOVEL.html" -Encoding UTF8
Write-Host "Template cleaned."
