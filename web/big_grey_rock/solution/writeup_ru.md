# Big Grey Rectangle writeup

На сайте виден большой серый прямоугольник. Посмотрим html-код страницы:

```html
<body>
    <svg width="40%" viewBox="0 0 1570 100" fill="none" class="center">
        <path d="A LOT OF SYMBOLS SKIPPED" fill="black"/>
    </svg>
    <svg width="90%" height="90%"" class="center">
        <rect width="100%" height="100%" style="fill:#C4C4C4;" />
    </svg> 
</body>
```

Видно, что прямугольник перекрывает какую-то svg. Удалим прямоугольник через рекдатор кода в брузере, и увидим флаг.

P.S. Изображение взято с https://wikiway.com/upload/hl-photo/38e/b78/dolina-bekaa_33.jpg

Флаг: `li2CTF{H7ML__3d1t3D_5ucc355fully!}`
