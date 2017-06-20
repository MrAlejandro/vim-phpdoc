if !has("python") && !has("python3")
    finish
endif

let s:plugindir = expand('<sfile>:p:h:h')

function! PhpDocPasteComment()
    if filereadable(s:plugindir . "/plugin/python/phpdoc.py")
        :write
        let $python_script = s:plugindir . "/plugin/python/phpdoc.py"
        execute (has('python3') ? 'py3file' : 'pyfile') $python_script
        :edit
    endif
endfunction
