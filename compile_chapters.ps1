# Compile all chapters into a single variable
$chapters = @()

1..17 | ForEach-Object {
    $chapterFile = "MANUSCRIPT\chapter_{0:D2}.md" -f $_
    if (Test-Path $chapterFile) {
        $content = Get-Content $chapterFile -Raw -Encoding UTF8
        $chapters += @{
            Number = $_
            Content = $content
        }
        Write-Host "Loaded Chapter $_"
    }
}

# Output chapter count
Write-Host "Total chapters loaded: $($chapters.Count)"

# Save a simple compilation test
$chapters | ForEach-Object {
    "Chapter $($_.Number): $($_.Content.Length) characters"
} | Out-File "chapter_manifest.txt"

Write-Host "Chapter manifest created"
