# Simple PHPDoc Vim plugin
Creates simple PHPDoc comment for functions defined without line breaks, based on type hints and default values.

## Installation 
* ```cd ~/.vim/bundle/```
* ```git clone {current_repo_url}```
* ```vim ~/.vimrc```
* add line ```Plugin 'mralejandro/vim-phpdoc'```
* add line ```nmap <Leader>d :call PhpDocPasteComment()<CR>```

## Usage
* move cursor to the line with a function keyword
```php
function example($string = '', $integer = 0, $bool = true, DateTime $date, Array $array1, $array2 = array(), $array3 = [], $mixed1 = null, $mixed2)
{
    // function body
}
```
* press ```<Leader>d``` (```,d```)
* the script must insert a PHPDoc comment to the line above
```php
/**
 * @param string $string
 * @param integer $integer
 * @param boolean $bool
 * @param DateTime $date
 * @param array $array1
 * @param array $array2
 * @param array $array3
 * @param mixed $mixed1
 * @param mixed $mixed2
 * @return mixed
 */
```

# Limitations
* Function definition must occupy only one line, the following will not workout
```php
function example(
    $string = '', 
    $integer = 0,
    ...
```
* Line must end with closing bracket (curly bracket on the next line)
* File must have ```.php``` extension
* Some more?
