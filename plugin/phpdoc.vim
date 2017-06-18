if !has("python")
    finish
endif

let s:plugindir = expand('<sfile>:p:h:h')

function! PhpDocPasteComment()
    if filereadable(s:plugindir . "/plugin/python/phpdoc.py")
        let $python_script = s:plugindir . "/plugin/python/phpdoc.py"
        pyfile $python_script
    endif
endfunction
