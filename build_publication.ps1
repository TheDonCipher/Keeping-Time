# Script to build complete publication HTML
$template = Get-Content "PUBLICATION_READY_NOVEL.html" -Raw

# 0. Prepare Sidebar Content
$sidebarFile = "REPOSITORY\SIDEBAR_LIBRARY.md"
$sidebarHTML = ""
if (Test-Path $sidebarFile) {
    $sidebarMD = Get-Content $sidebarFile -Raw -Encoding UTF8
    # Convert Markdown Headers to HTML
    $sidebarHTML = $sidebarMD -replace '(?m)^### (.+)$', '<h4>$1</h4>'
    $sidebarHTML = $sidebarHTML -replace '(?m)^#### (.+)$', '<h5>$1</h5>'
    # Remove MD horizontal rules
    $sidebarHTML = $sidebarHTML -replace '---', '<hr>'
    # Remove Quote blocks context
    $sidebarHTML = $sidebarHTML -replace '> \*\*Usage\*\*.*', ''
    $sidebarHTML = $sidebarHTML -replace '> \*\*Style\*\*.*', ''
    $sidebarHTML = $sidebarHTML -replace '# SIDEBAR LIBRARY: COMMON TERMS', ''
    # Strip <aside> tags as they are redundant inside the #sidebar container
    $sidebarHTML = $sidebarHTML -replace '<aside>', ''
    $sidebarHTML = $sidebarHTML -replace '</aside>', ''
}

# Load all chapters
$chapterHTML = ""
1..17 | ForEach-Object {
    $chFile = "MANUSCRIPT\chapter_{0:D2}.md" -f $_
    if (Test-Path $chFile) {
        $md = Get-Content $chFile -Raw -Encoding UTF8
        
        # 0. Tooltip Processing [[Term::Description]]
        $md = [Regex]::Replace($md, '\[\[(.*?)::(.*?)\]\]', {
            param($m)
            $term = $m.Groups[1].Value
            $tip = $m.Groups[2].Value -replace '&', '&amp;' -replace '"', '&quot;' -replace '<', '&lt;' -replace '>', '&gt;'
            return "<span class=`"tooltip`" data-tip=`"$tip`">$term</span>"
        })

        # 1. Headers
        $html = $md -replace '# KEEPING TIME', ''
        $html = $html -replace '(?m)^## (.+)$', '<h3>$1</h3>'
        $html = $html -replace '(?m)^### (.+)$', '<h4>$1</h4>'
        
        # 2. Bold/Italic
        $html = $html -replace '\*\*([^*]+)\*\*', '<strong>$1</strong>'
        $html = $html -replace '\*([^*]+)\*', '<em>$1</em>'

        # 3. System Blocks (**> TEXT)
        $html = $html -replace '(?m)^\*\*>\s*(.+)$', '<div class="system-block"><p>$1</p></div>'

        # 4. Paragraphs
        # Wrap lines that are NOT headers, NOT HTML tags, NOT empty in <p>
        $html = $html -replace '(?m)^(?![<])(.+)$', '<p>$1</p>'

        $chapterHTML += "`n<div class=`"chapter`" id=`"ch$_`">`n$html`n</div>`n"
    }
}

# Insert content into template
$output = $template -replace '<!-- NOTE: Full chapter content.*?-->', $chapterHTML
$output = $output -replace '<!-- NOTE: Sidebar content goes here -->', $sidebarHTML

$output | Out-File "PUBLICATION_COMPLETE.html" -Encoding UTF8

Write-Host "Complete publication HTML created: PUBLICATION_COMPLETE.html"
